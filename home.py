from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image
import csv
from tkinter import messagebox
from CARTClass import CARTClass
from DecisionTreeClass import DecisionTreeClass
from KNNClass import KNNClass
from SVMClass import SVMClass
from logisticRegressionClass import LogisticRegressionClass


class Home:
    def __init__(self):
        self.mainColor = '#191142'
        self.secondColor = '#251260'
        self.foregroundColor = '#8AD7FF'
        self.font = "Comic Sans MS"
        self.data_frame = pd.read_csv('Data.csv')

        self.root = Tk()
        self.root.title("Service cancellation predictor")
        self.root.attributes('-fullscreen', True)

        # general style for all labels
        self.style = ttk.Style(self.root)
        self.style.configure("TLabel", font=('arial', 12), background=self.mainColor)

        # setting background image
        self.image = Image.open("Photos/background.png")
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)
        self.backgroundLabel.place(x=0, y=0)

        self.frame = Frame(self.root, background=self.mainColor, padx=30, pady=30)

        # variables to get data from user
        self.user_data_values()

        # labels
        self.generate_labels()

        # Radio buttons
        self.generate_radio_buttons()

        # set background to Entries and place it
        self.entries_gui()

        # Entries
        self.generate_inputs()

        # buttons
        self.generate_buttons(self.check_inputs_validation, self.test_data, self.train_data)

        # positions
        self.components_positions()

        self.root.mainloop()

    def generate_labels(self):
        self.gender = PhotoImage(file="Photos/Labels/gender.png")
        self.genderLabel = ttk.Label(self.frame, image=self.gender, background=self.mainColor)
        self.seniorCitizen = PhotoImage(file="Photos/Labels/Senior Citizen.png")
        self.seniorCitizenLabel = ttk.Label(self.frame, image=self.seniorCitizen, background=self.mainColor)
        self.partner = PhotoImage(file="Photos/Labels/Partner.png")
        self.partnerLabel = ttk.Label(self.frame, image=self.partner, background=self.mainColor)
        self.dependents = PhotoImage(file="Photos/Labels/Dependents.png")
        self.dependentsLabel = ttk.Label(self.frame, image=self.dependents, background=self.mainColor)
        self.tenure = PhotoImage(file="Photos/Labels/Tenure.png")
        self.tenureLabel = ttk.Label(self.frame, image=self.tenure, background=self.mainColor)
        self.phoneService = PhotoImage(file="Photos/Labels/Phone Service.png")
        self.phoneServiceLabel = ttk.Label(self.frame, image=self.phoneService, background=self.mainColor)
        self.multipleLines = PhotoImage(file="Photos/Labels/Multiple Lines.png")
        self.multipleLinesLabel = ttk.Label(self.frame, image=self.multipleLines, background=self.mainColor)
        self.internetService = PhotoImage(file="Photos/Labels/Internet Service.png")
        self.internetServiceLabel = ttk.Label(self.frame, image=self.internetService, background=self.mainColor)
        self.onlineSecurity = PhotoImage(file="Photos/Labels/Online Security.png")
        self.onlineSecurityLabel = ttk.Label(self.frame, image=self.onlineSecurity, background=self.mainColor)
        self.onlineBackup = PhotoImage(file="Photos/Labels/Online Backup.png")
        self.onlineBackupLabel = ttk.Label(self.frame, image=self.onlineBackup, background=self.mainColor)
        self.deviceProtection = PhotoImage(file="Photos/Labels/Device Protection.png")
        self.deviceProtectionLabel = ttk.Label(self.frame, image=self.deviceProtection, background=self.mainColor)
        self.techSupport = PhotoImage(file="Photos/Labels/Tech Support.png")
        self.techSupportLabel = ttk.Label(self.frame, image=self.techSupport, background=self.mainColor)
        self.streamingTV = PhotoImage(file="Photos/Labels/Streaming TV.png")
        self.streamingTVLabel = ttk.Label(self.frame, image=self.streamingTV, background=self.mainColor)
        self.streamingMovies = PhotoImage(file="Photos/Labels/Streaming Movies.png")
        self.streamingMoviesLabel = ttk.Label(self.frame, image=self.streamingMovies, background=self.mainColor)
        self.contract = PhotoImage(file="Photos/Labels/Contract.png")
        self.contractLabel = ttk.Label(self.frame, image=self.contract, background=self.mainColor)
        self.paperlessBilling = PhotoImage(file="Photos/Labels/Paperless Billing.png")
        self.paperlessBillingLabel = ttk.Label(self.frame, image=self.paperlessBilling, background=self.mainColor)
        self.paymentMethod = PhotoImage(file="Photos/Labels/Payment Method.png")
        self.paymentMethodLabel = ttk.Label(self.frame, image=self.paymentMethod, background=self.mainColor)
        self.monthlyCharges = PhotoImage(file="Photos/Labels/Monthly Charges.png")
        self.monthlyChargesLabel = ttk.Label(self.frame, image=self.monthlyCharges, background=self.mainColor)
        self.totalCharges = PhotoImage(file="Photos/Labels/Total Charges.png")
        self.totalChargesLabel = ttk.Label(self.frame, image=self.totalCharges, background=self.mainColor)

    def generate_radio_buttons(self):
        self.logisticRegressionImage = PhotoImage(file="Photos/Labels/Logistic Regression.png")
        self.logisticRegressionRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                                         value="Logistic Regression", background=self.mainColor,
                                                         image=self.logisticRegressionImage,
                                                         activebackground=self.mainColor)
        self.SVMImage = PhotoImage(file="Photos/Labels/SVM.png")
        self.SVMRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                          value="SVM", background=self.mainColor, image=self.SVMImage,
                                          activebackground=self.mainColor)
        self.CARTImage = PhotoImage(file="Photos/Labels/CART.png")
        self.CARTRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                           value="CART", background=self.mainColor, image=self.CARTImage,
                                           activebackground=self.mainColor)
        self.ID3Image = PhotoImage(file="Photos/Labels/ID3.png")
        self.ID3RadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                          value="ID3", background=self.mainColor, image=self.ID3Image,
                                          activebackground=self.mainColor)
        self.KNNImage = PhotoImage(file="Photos/Labels/KNN.png")
        self.KNNRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                          value="KNN", background=self.mainColor, image=self.KNNImage,
                                          activebackground=self.mainColor)

    def user_data_values(self):
        self.methodologyValue = StringVar(value="none")
        self.genderStringValue = StringVar()
        self.seniorCitizenStringValue = StringVar()
        self.partnerStringValue = StringVar()
        self.dependentsStringValue = StringVar()
        self.tenureValue = IntVar()
        self.phoneServiceStringValue = StringVar()
        self.multipleLinesStringValue = StringVar()
        self.internetServiceStringValue = StringVar()
        self.onlineSecurityStringValue = StringVar()
        self.onlineBackupStringValue = StringVar()
        self.deviceProtectionStringValue = StringVar()
        self.techSupportStringValue = StringVar()
        self.streamingTVStringValue = StringVar()
        self.streamingMoviesStringValue = StringVar()
        self.contractStringValue = StringVar()
        self.paperlessBillingStringValue = StringVar()
        self.paymentMethodStringValue = StringVar()
        self.monthlyChargesValue = DoubleVar()
        self.totalChargesValue = DoubleVar()

    def generate_buttons(self, check_inputs_validation, test_data, train_data):
        self.train_button_back = PhotoImage(file="Photos/Buttons/trainButton.png")
        self.trainButton = Button(self.frame, image=self.train_button_back, borderwidth=0, cursor="hand2", bd=0,
                                  background=self.mainColor, activebackground=self.mainColor, command=train_data)
        self.test_button_back = PhotoImage(file="Photos/Buttons/testButton.png")
        self.testButton = Button(self.frame, image=self.test_button_back, borderwidth=0, cursor="hand2", bd=0,
                                 background=self.mainColor, activebackground=self.mainColor, command=test_data)
        self.predict_button_back = PhotoImage(file="Photos/Buttons/predictButton.png")
        self.predictButton = Button(self.frame, image=self.predict_button_back, borderwidth=0, cursor="hand2", bd=0,
                                    background=self.mainColor, anchor='center', activebackground=self.mainColor,
                                    command=check_inputs_validation)
        self.close_button_back = PhotoImage(file="Photos/Buttons/closeWindowButton.png")
        self.closeButton = Button(self.frame, image=self.close_button_back, borderwidth=0, cursor="hand2", bd=0,
                                  background=self.mainColor, activebackground=self.mainColor,
                                  command=self.root.destroy)

    def components_positions(self):
        self.logisticRegressionRadioButton.grid(row=1, column=0)
        self.SVMRadioButton.grid(row=1, column=1)
        self.CARTRadioButton.grid(row=1, column=2)
        self.ID3RadioButton.grid(row=1, column=3)
        self.KNNRadioButton.grid(row=1, column=4)
        self.closeButton.grid(row=1, column=6)
        self.trainButton.grid(row=2, column=2)
        self.testButton.grid(row=2, column=3)

        self.genderLabel.grid(row=4, column=0)
        self.seniorCitizenLabel.grid(row=4, column=2)

        self.partnerLabel.grid(row=5, column=0)
        self.dependentsLabel.grid(row=5, column=2)
        self.tenureLabel.grid(row=4, column=4)
        self.phoneServiceLabel.grid(row=6, column=0)
        self.multipleLinesLabel.grid(row=6, column=2)
        self.internetServiceLabel.grid(row=5, column=4)
        self.onlineSecurityLabel.grid(row=7, column=0)
        self.onlineBackupLabel.grid(row=7, column=2)
        self.deviceProtectionLabel.grid(row=6, column=4)
        self.techSupportLabel.grid(row=8, column=0)
        self.streamingTVLabel.grid(row=8, column=2)
        self.streamingMoviesLabel.grid(row=7, column=4)
        self.contractLabel.grid(row=9, column=0)
        self.paperlessBillingLabel.grid(row=9, column=2)
        self.paymentMethodLabel.grid(row=8, column=4)
        self.monthlyChargesLabel.grid(row=10, column=0)
        self.totalChargesLabel.grid(row=10, column=2)
        #############################################
        self.genderEntry.grid(row=4, column=1)
        self.seniorCitizenEntry.grid(row=4, column=3)

        self.partnerEntry.grid(row=5, column=1)
        self.dependentsEntry.grid(row=5, column=3)
        self.tenureEntry.grid(row=4, column=5)
        self.phoneServiceEntry.grid(row=6, column=1)
        self.multipleLinesEntry.grid(row=6, column=3)
        self.internetServiceEntry.grid(row=5, column=5)
        self.onlineSecurityEntry.grid(row=7, column=1)
        self.onlineBackupEntry.grid(row=7, column=3)
        self.deviceProtectionEntry.grid(row=6, column=5)
        self.techSupportEntry.grid(row=8, column=1)
        self.streamingTVEntry.grid(row=8, column=3)
        self.streamingMoviesEntry.grid(row=7, column=5)
        self.contractEntry.grid(row=9, column=1)
        self.paperlessBillingEntry.grid(row=9, column=3)
        self.paymentMethodEntry.grid(row=8, column=5)
        self.monthlyChargesEntry.grid(row=10, column=1)
        self.totalChargesEntry.grid(row=10, column=3)
        self.predictButton.grid(row=12, columnspan=6)
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

    def generate_inputs(self):

        self.genderEntry = OptionMenu(self.frame, self.genderStringValue, "Male", "Female")
        self.genderEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                activebackground=self.mainColor, foreground=self.foregroundColor,
                                font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor, cursor="hand2")
        self.genderEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                        font=(self.font, 14))

        self.seniorCitizenEntry = OptionMenu(self.frame, self.seniorCitizenStringValue, "Yes", "No")
        self.seniorCitizenEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                       activebackground=self.mainColor, foreground=self.foregroundColor,
                                       font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                       cursor="hand2")
        self.seniorCitizenEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                               font=(self.font, 14))

        self.partnerEntry = OptionMenu(self.frame, self.partnerStringValue, "Yes", "No")
        self.partnerEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                 activebackground=self.mainColor, foreground=self.foregroundColor,
                                 font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor, cursor="hand2")
        self.partnerEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                         font=(self.font, 14))

        self.dependentsEntry = OptionMenu(self.frame, self.dependentsStringValue, "Yes", "No")
        self.dependentsEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                    activebackground=self.mainColor, foreground=self.foregroundColor,
                                    font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor, cursor="hand2")
        self.dependentsEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                            font=(self.font, 14))

        self.tenureEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.tenureValue,
                                 background=self.mainColor,
                                 foreground=self.foregroundColor)

        self.phoneServiceEntry = OptionMenu(self.frame, self.phoneServiceStringValue, "Yes", "No")
        self.phoneServiceEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                      activebackground=self.mainColor, foreground=self.foregroundColor,
                                      font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                      cursor="hand2")
        self.phoneServiceEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                              font=(self.font, 14))

        self.multipleLinesEntry = OptionMenu(self.frame, self.multipleLinesStringValue, "Yes", "No")
        self.multipleLinesEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                       activebackground=self.mainColor, foreground=self.foregroundColor,
                                       font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                       cursor="hand2")
        self.multipleLinesEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                               font=(self.font, 14))

        self.internetServiceEntry = OptionMenu(self.frame, self.internetServiceStringValue, "DSL", "Fiber Optic", "No")
        self.internetServiceEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                         activebackground=self.mainColor, foreground=self.foregroundColor,
                                         font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                         cursor="hand2")
        self.internetServiceEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor,
                                                 foreground="white",
                                                 font=(self.font, 14))

        self.onlineSecurityEntry = OptionMenu(self.frame, self.onlineSecurityStringValue, "Yes", "No")
        self.onlineSecurityEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                        activebackground=self.mainColor, foreground=self.foregroundColor,
                                        font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                        cursor="hand2")
        self.onlineSecurityEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor,
                                                foreground="white",
                                                font=(self.font, 14))

        self.onlineBackupEntry = OptionMenu(self.frame, self.onlineBackupStringValue, "Yes", "No")
        self.onlineBackupEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                      activebackground=self.mainColor, foreground=self.foregroundColor,
                                      font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                      cursor="hand2")
        self.onlineBackupEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                              font=(self.font, 14))

        self.deviceProtectionEntry = OptionMenu(self.frame, self.deviceProtectionStringValue, "Yes", "No")
        self.deviceProtectionEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                          activebackground=self.mainColor, foreground=self.foregroundColor,
                                          font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                          cursor="hand2")
        self.deviceProtectionEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor,
                                                  foreground="white",
                                                  font=(self.font, 14))

        self.techSupportEntry = OptionMenu(self.frame, self.techSupportStringValue, "Yes", "No")
        self.techSupportEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                     activebackground=self.mainColor, foreground=self.foregroundColor,
                                     font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                     cursor="hand2")
        self.techSupportEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                             font=(self.font, 14))

        self.streamingTVEntry = OptionMenu(self.frame, self.streamingTVStringValue, "Yes", "No")
        self.streamingTVEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                     activebackground=self.mainColor, foreground=self.foregroundColor,
                                     font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                     cursor="hand2")
        self.streamingTVEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                             font=(self.font, 14))

        self.streamingMoviesEntry = OptionMenu(self.frame, self.streamingMoviesStringValue, "Yes", "No")
        self.streamingMoviesEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                         activebackground=self.mainColor, foreground=self.foregroundColor,
                                         font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                         cursor="hand2")
        self.streamingMoviesEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor,
                                                 foreground="white",
                                                 font=(self.font, 14))

        self.contractEntry = OptionMenu(self.frame, self.contractStringValue, "Month to Month", "One Year", "Two Years")
        self.contractEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                  activebackground=self.mainColor, foreground=self.foregroundColor,
                                  font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor, cursor="hand2")
        self.contractEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                          font=(self.font, 14))

        self.paperlessBillingEntry = OptionMenu(self.frame, self.paperlessBillingStringValue, "Yes", "No")
        self.paperlessBillingEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                          activebackground=self.mainColor, foreground=self.foregroundColor,
                                          font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                          cursor="hand2")
        self.paperlessBillingEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor,
                                                  foreground="white",
                                                  font=(self.font, 14))

        self.paymentMethodEntry = OptionMenu(self.frame, self.paymentMethodStringValue, "Electronic Check",
                                             "Mailed Check",
                                             "Bank Transfer(automatic)", "Credit Card(automatic)")
        self.paymentMethodEntry.config(background=self.mainColor, borderwidth=0, width=10, highlightthickness=0,
                                       activebackground=self.mainColor, foreground=self.foregroundColor,
                                       font=(self.font, 11, 'bold'), activeforeground=self.foregroundColor,
                                       cursor="hand2")
        self.paymentMethodEntry["menu"].config(bg=self.mainColor, activebackground=self.secondColor, foreground="white",
                                               font=(self.font, 14))

        self.monthlyChargesEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                         textvariable=self.monthlyChargesValue,
                                         background=self.mainColor, foreground=self.foregroundColor)
        self.totalChargesEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                       textvariable=self.totalChargesValue,
                                       background=self.mainColor, foreground=self.foregroundColor)

    def entries_gui(self):
        self.Entry_back = PhotoImage(file="Photos/RectangleEntry.png")
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=4, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=4, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=5, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=5, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=4, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=6, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=6, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=5, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=7, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=7, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=6, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=8, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=8, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=7, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=9, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=9, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=8, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=10, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=10, column=3)

    def clean_input_data(self):
        data_frame_model = pd.read_csv('model.csv')

        # categorical data
        data_frame_model['Contract'] = pd.Categorical(data_frame_model['Contract'],
                                                      ["Month to Month", "One Year", "Two Years"], ordered=True)
        data_frame_model['Contract'] = data_frame_model['Contract'].cat.codes

        data_frame_model['gender'] = pd.Categorical(data_frame_model['gender'], ['Male', 'Female'], ordered=True)
        data_frame_model['gender'] = data_frame_model['gender'].cat.codes

        data_frame_model['PaymentMethod'] = pd.Categorical(data_frame_model['PaymentMethod'],
                                                           ["Electronic Check", "Mailed Check",
                                                            "Bank Transfer(automatic)", "Credit Card(automatic)"],
                                                           ordered=True)
        data_frame_model['PaymentMethod'] = data_frame_model['PaymentMethod'].cat.codes

        data_frame_model['InternetService'] = pd.Categorical(data_frame_model['InternetService'],
                                                             ["DSL", "Fiber Optic", "No"], ordered=True)
        data_frame_model['InternetService'] = data_frame_model['InternetService'].cat.codes

        # Convert all columns have Yes or No to 0 and 1
        data_frame_model = data_frame_model.replace(to_replace=['Yes', 'No'], value=['1', '0'])

        # 1- convert data type of columns to suitable datatypes
        self.data_frame['TotalCharges'] = pd.to_numeric(self.data_frame.TotalCharges, errors='coerce')
        # set all non numeric values to numeric
        self.data_frame['TotalCharges'] = self.data_frame['TotalCharges'].astype(float)
        # convert data type of TotalCharges column to float

        columns = ["tenure", "MonthlyCharges", "TotalCharges"]
        # apply normalization techniques
        for column in columns:
            data_frame_model.at[0, column] = (data_frame_model.at[0, column] -
                                              self.data_frame[column].mean()) / self.data_frame[column].std()

        data_frame_model.to_csv("model.csv")

    def save_data_in_file(self):
        row = {
            "gender": self.genderStringValue.get(),
            'SeniorCitizen': self.seniorCitizenStringValue.get(),
            'Partner': self.partnerStringValue.get(),
            'Dependents': self.dependentsStringValue.get(),
            'tenure': self.tenureValue.get(),
            'PhoneService': self.phoneServiceStringValue.get(),
            'MultipleLines': self.multipleLinesStringValue.get(),
            'InternetService': self.internetServiceStringValue.get(),
            'OnlineSecurity': self.onlineSecurityStringValue.get(),
            'OnlineBackup': self.onlineBackupStringValue.get(),
            'DeviceProtection': self.deviceProtectionStringValue.get(),
            'TechSupport': self.techSupportStringValue.get(),
            'StreamingTV': self.streamingTVStringValue.get(),
            'StreamingMovies': self.streamingMoviesStringValue.get(),
            'Contract': self.contractStringValue.get(),
            'PaperlessBilling': self.paperlessBillingStringValue.get(),
            'PaymentMethod': self.paymentMethodStringValue.get(),
            'MonthlyCharges': self.monthlyChargesValue.get(),
            'TotalCharges': self.totalChargesValue.get()}
        # Save in new csv file
        with open('model.csv', 'w') as csvfile:
            fieldnames = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                          'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                          'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                          'PaymentMethod', 'MonthlyCharges', 'TotalCharges']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(row)
        csvfile.close()
        self.predict_data()

    def test_data(self):
        if self.methodologyValue.get() == 'none':
            messagebox.showerror("Validation", "You Should Choose Methodology")
        if self.methodologyValue.get() == "Logistic Regression":
            LogisticRegressionClass('test')
        if self.methodologyValue.get() == "SVM":
            SVMClass("test")
        if self.methodologyValue.get() == "ID3":
            DecisionTreeClass('test')
        if self.methodologyValue.get() == "CART":
            CARTClass('test')
        if self.methodologyValue.get() == "KNN":
            KNNClass('test')

    def train_data(self):
        if self.methodologyValue.get() == 'none':
            messagebox.showerror("Validation", "You Should Choose Methodology")
        if self.methodologyValue.get() == "Logistic Regression":
            LogisticRegressionClass('train')
        if self.methodologyValue.get() == "SVM":
            SVMClass("train")
        if self.methodologyValue.get() == "CART":
            CARTClass('train')
        if self.methodologyValue.get() == "ID3":
            DecisionTreeClass('train')
        if self.methodologyValue.get() == "KNN":
            KNNClass('train')

    def predict_data(self):
        # to clean user data input
        self.clean_input_data()

        if self.methodologyValue.get() == "Logistic Regression":
            LogisticRegressionClass('predict')
        if self.methodologyValue.get() == "SVM":
            SVMClass("predict")
        if self.methodologyValue.get() == "CART":
            CARTClass('predict')
        if self.methodologyValue.get() == "ID3":
            DecisionTreeClass('predict')
        if self.methodologyValue.get() == "KNN":
            KNNClass('predict')

    def center(self, win, window_width, window_height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))

        win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    def check_inputs_validation(self):
        if self.methodologyValue.get() == 'none':
            messagebox.showerror("Validation", "You Should Choose Methodology")
        if self.genderStringValue.get() == "" or self.seniorCitizenStringValue.get() == "" or self.partnerStringValue.get() == "" or self.dependentsStringValue.get() == "" or self.phoneServiceStringValue.get() == "" or self.multipleLinesStringValue.get() == "" or self.internetServiceStringValue.get() == "" or self.onlineSecurityStringValue.get() == "" or self.onlineBackupStringValue.get() == "" or self.deviceProtectionStringValue.get() == "" or self.techSupportStringValue.get() == "" or self.streamingTVStringValue.get() == "" or self.streamingMoviesStringValue.get() == "" or self.contractStringValue.get() == "" or self.paperlessBillingStringValue.get() == "" or self.paymentMethodStringValue.get() == "":
            messagebox.showerror("Validation", "All data must be filled")

        else:
            # to save data in file
            self.save_data_in_file()
