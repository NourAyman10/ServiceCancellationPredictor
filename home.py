from tkinter import *
from tkinter import ttk
import pandas as pd
from PIL import ImageTk, Image
import csv

from CARTClass import CARTClass
from DecisionTreeClass import DecisionTreeClass
from SVMClass import SVMClass
from logisticRegressionClass import LogisticRegressionClass


class Home:
    def __init__(self):
        self.mainColor = '#191142'
        self.foregroundColor = '#8AD7FF'
        self.data_frame = pd.read_csv('Data.csv')

        self.root = Tk()
        self.root.title("Service cancellation predictor")
        self.root.attributes('-fullscreen', True)

        # general style for all labels
        self.style = ttk.Style(self.root)
        self.style.configure("TLabel", font=('arial', 12), background=self.mainColor)
        # self.style.theme_use('clam')
        # self.style.configure("TCombobox", fieldbackground="orange", background="red", foreground='blue',
        #                      selectbackground='black')

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
        self.generate_buttons(self.predict_data, self.test_data, self.train_data)

        # positions
        self.components_positions()

        self.root.mainloop()

    def generate_labels(self):
        self.gender = PhotoImage(file="Photos/Labels/gender.png")
        self.genderLabel = ttk.Label(self.frame, image=self.gender)
        self.seniorCitizen = PhotoImage(file="Photos/Labels/Senior Citizen.png")
        self.seniorCitizenLabel = ttk.Label(self.frame, image=self.seniorCitizen)
        self.partner = PhotoImage(file="Photos/Labels/Partner.png")
        self.partnerLabel = ttk.Label(self.frame, image=self.partner)
        self.dependents = PhotoImage(file="Photos/Labels/Dependents.png")
        self.dependentsLabel = ttk.Label(self.frame, image=self.dependents)
        self.tenure = PhotoImage(file="Photos/Labels/Tenure.png")
        self.tenureLabel = ttk.Label(self.frame, image=self.tenure)
        self.phoneService = PhotoImage(file="Photos/Labels/Phone Service.png")
        self.phoneServiceLabel = ttk.Label(self.frame, image=self.phoneService)
        self.multipleLines = PhotoImage(file="Photos/Labels/Multiple Lines.png")
        self.multipleLinesLabel = ttk.Label(self.frame, image=self.multipleLines)
        self.internetService = PhotoImage(file="Photos/Labels/Internet Service.png")
        self.internetServiceLabel = ttk.Label(self.frame, image=self.internetService)
        self.onlineSecurity = PhotoImage(file="Photos/Labels/Online Security.png")
        self.onlineSecurityLabel = ttk.Label(self.frame, image=self.onlineSecurity)
        self.onlineBackup = PhotoImage(file="Photos/Labels/Online Backup.png")
        self.onlineBackupLabel = ttk.Label(self.frame, image=self.onlineBackup)
        self.deviceProtection = PhotoImage(file="Photos/Labels/Device Protection.png")
        self.deviceProtectionLabel = ttk.Label(self.frame, image=self.deviceProtection)
        self.techSupport = PhotoImage(file="Photos/Labels/Tech Support.png")
        self.techSupportLabel = ttk.Label(self.frame, image=self.techSupport)
        self.streamingTV = PhotoImage(file="Photos/Labels/Streaming TV.png")
        self.streamingTVLabel = ttk.Label(self.frame, image=self.streamingTV)
        self.streamingMovies = PhotoImage(file="Photos/Labels/Streaming Movies.png")
        self.streamingMoviesLabel = ttk.Label(self.frame, image=self.streamingMovies)
        self.contract = PhotoImage(file="Photos/Labels/Contract.png")
        self.contractLabel = ttk.Label(self.frame, image=self.contract)
        self.paperlessBilling = PhotoImage(file="Photos/Labels/Paperless Billing.png")
        self.paperlessBillingLabel = ttk.Label(self.frame, image=self.paperlessBilling)
        self.paymentMethod = PhotoImage(file="Photos/Labels/Payment Method.png")
        self.paymentMethodLabel = ttk.Label(self.frame, image=self.paymentMethod)
        self.monthlyCharges = PhotoImage(file="Photos/Labels/Monthly Charges.png")
        self.monthlyChargesLabel = ttk.Label(self.frame, image=self.monthlyCharges)
        self.totalCharges = PhotoImage(file="Photos/Labels/Total Charges.png")
        self.totalChargesLabel = ttk.Label(self.frame, image=self.totalCharges)

    def generate_radio_buttons(self):
        self.logisticRegressionImage = PhotoImage(file="Photos/Labels/Logistic Regression.png")
        self.logisticRegressionRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                                         value="Logistic Regression", background=self.mainColor,
                                                         image=self.logisticRegressionImage)
        self.SVMImage = PhotoImage(file="Photos/Labels/SVM.png")
        self.SVMRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                          value="SVM", background=self.mainColor, image=self.SVMImage)
        self.CARTImage = PhotoImage(file="Photos/Labels/CART.png")
        self.CARTRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                           value="CART", background=self.mainColor, image=self.CARTImage)
        self.ID3Image = PhotoImage(file="Photos/Labels/ID3.png")
        self.ID3RadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                          value="ID3", background=self.mainColor, image=self.ID3Image)
        self.KNNImage = PhotoImage(file="Photos/Labels/KNN.png")
        self.KNNRadioButton = Radiobutton(self.frame, variable=self.methodologyValue,
                                          value="KNN", background=self.mainColor, image=self.KNNImage)

    def user_data_values(self):
        self.methodologyValue = StringVar(value="none")
        self.genderValue = IntVar()
        # Button(self.root, text="get text", command=lambda : print(self.genderValue.get())).pack()
        self.seniorCitizenValue = IntVar()
        self.partnerValue = IntVar()
        self.dependentsValue = IntVar()
        self.tenureValue = DoubleVar()
        self.phoneServiceValue = IntVar()
        self.multipleLinesValue = IntVar()
        self.internetServiceValue = IntVar()
        self.onlineSecurityValue = IntVar()
        self.onlineBackupValue = IntVar()
        self.deviceProtectionValue = IntVar()
        self.techSupportValue = IntVar()
        self.streamingTVValue = IntVar()
        self.streamingMoviesValue = IntVar()
        self.contractValue = IntVar()
        self.paperlessBillingValue = IntVar()
        self.paymentMethodValue = IntVar()
        self.monthlyChargesValue = DoubleVar()
        self.totalChargesValue = DoubleVar()

    def generate_buttons(self, predict_data, test_data, train_data):
        self.train_button_back = PhotoImage(file="Photos/Buttons/trainButton.png")
        self.trainButton = Button(self.frame, image=self.train_button_back, borderwidth=0, cursor="hand2", bd=0,
                                  background=self.mainColor, command=train_data)
        self.test_button_back = PhotoImage(file="Photos/Buttons/testButton.png")
        self.testButton = Button(self.frame, image=self.test_button_back, borderwidth=0, cursor="hand2", bd=0,
                                 background=self.mainColor, command=test_data)
        self.predict_button_back = PhotoImage(file="Photos/Buttons/predictButton.png")
        self.predictButton = Button(self.frame, image=self.predict_button_back, borderwidth=0, cursor="hand2", bd=0,
                                    background=self.mainColor, anchor='center', command=predict_data)
        self.close_button_back = PhotoImage(file="Photos/Buttons/closeButton.png")
        self.closeButton = Button(self.frame, image=self.close_button_back, borderwidth=0, cursor="hand2", bd=0,
                                  background=self.mainColor,
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
        self.genderLabel.grid(row=4, column=2)
        self.seniorCitizenLabel.grid(row=4, column=4)
        self.partnerLabel.grid(row=5, column=0)
        self.dependentsLabel.grid(row=5, column=2)
        self.tenureLabel.grid(row=5, column=4)
        self.phoneServiceLabel.grid(row=6, column=0)
        self.multipleLinesLabel.grid(row=6, column=2)
        self.internetServiceLabel.grid(row=6, column=4)
        self.onlineSecurityLabel.grid(row=7, column=0)
        self.onlineBackupLabel.grid(row=7, column=2)
        self.deviceProtectionLabel.grid(row=7, column=4)
        self.techSupportLabel.grid(row=8, column=0)
        self.streamingTVLabel.grid(row=8, column=2)
        self.streamingMoviesLabel.grid(row=8, column=4)
        self.contractLabel.grid(row=9, column=0)
        self.paperlessBillingLabel.grid(row=9, column=2)
        self.paymentMethodLabel.grid(row=9, column=4)
        self.monthlyChargesLabel.grid(row=10, column=0)
        self.totalChargesLabel.grid(row=10, column=2)
        #############################################
        self.genderEntry.grid(row=4, column=3)
        self.seniorCitizenEntry.grid(row=4, column=5)
        self.partnerEntry.grid(row=5, column=1)
        self.dependentsEntry.grid(row=5, column=3)
        self.tenureEntry.grid(row=5, column=5)
        self.phoneServiceEntry.grid(row=6, column=1)
        self.multipleLinesEntry.grid(row=6, column=3)
        self.internetServiceEntry.grid(row=6, column=5)
        self.onlineSecurityEntry.grid(row=7, column=1)
        self.onlineBackupEntry.grid(row=7, column=3)
        self.deviceProtectionEntry.grid(row=7, column=5)
        self.techSupportEntry.grid(row=8, column=1)
        self.streamingTVEntry.grid(row=8, column=3)
        self.streamingMoviesEntry.grid(row=8, column=5)
        self.contractEntry.grid(row=9, column=1)
        self.paperlessBillingEntry.grid(row=9, column=3)
        self.paymentMethodEntry.grid(row=9, column=5)
        self.monthlyChargesEntry.grid(row=10, column=1)
        self.totalChargesEntry.grid(row=10, column=3)
        self.predictButton.grid(row=12, columnspan=6)
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

    def action(self, event):
        if self.genderEntry.get() == "Male":
            self.genderValue.set(0)
        elif self.genderEntry.get() == "Female":
            self.genderValue.set(1)

    def generate_inputs(self):
        self.genderEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.genderValue,
                                 background=self.mainColor,
                                 foreground=self.foregroundColor)
        # self.genderEntry = ttk.Combobox(self.frame, values=["Male", "Female"])
        # self.genderEntry.current(0)
        # self.genderEntry.bind("<<ComboboxSelected>>", self.action)
        # self.genderEntry.pack()

        self.seniorCitizenEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                        textvariable=self.seniorCitizenValue,
                                        background=self.mainColor, foreground=self.foregroundColor)
        self.partnerEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.partnerValue,
                                  background=self.mainColor,
                                  foreground=self.foregroundColor)
        self.dependentsEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.dependentsValue,
                                     background=self.mainColor, foreground=self.foregroundColor)
        self.tenureEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.tenureValue,
                                 background=self.mainColor,
                                 foreground=self.foregroundColor)
        self.phoneServiceEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                       textvariable=self.phoneServiceValue,
                                       background=self.mainColor, foreground=self.foregroundColor)
        self.multipleLinesEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                        textvariable=self.multipleLinesValue,
                                        background=self.mainColor, foreground=self.foregroundColor)
        self.internetServiceEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                          textvariable=self.internetServiceValue,
                                          background=self.mainColor, foreground=self.foregroundColor)
        self.onlineSecurityEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                         textvariable=self.onlineSecurityValue,
                                         background=self.mainColor, foreground=self.foregroundColor)
        self.onlineBackupEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                       textvariable=self.onlineBackupValue,
                                       background=self.mainColor, foreground=self.foregroundColor)
        self.deviceProtectionEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                           textvariable=self.deviceProtectionValue,
                                           background=self.mainColor, foreground=self.foregroundColor)
        self.techSupportEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                      textvariable=self.techSupportValue,
                                      background=self.mainColor, foreground=self.foregroundColor)
        self.streamingTVEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                      textvariable=self.streamingTVValue,
                                      background=self.mainColor, foreground=self.foregroundColor)
        self.streamingMoviesEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                          textvariable=self.streamingMoviesValue,
                                          background=self.mainColor, foreground=self.foregroundColor)
        self.contractEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.contractValue,
                                   background=self.mainColor, foreground=self.foregroundColor)
        self.paperlessBillingEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                           textvariable=self.paperlessBillingValue,
                                           background=self.mainColor, foreground=self.foregroundColor)
        self.paymentMethodEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                        textvariable=self.paymentMethodValue,
                                        background=self.mainColor, foreground=self.foregroundColor)
        self.monthlyChargesEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                         textvariable=self.monthlyChargesValue,
                                         background=self.mainColor, foreground=self.foregroundColor)
        self.totalChargesEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0,
                                       textvariable=self.totalChargesValue,
                                       background=self.mainColor, foreground=self.foregroundColor)

    def entries_gui(self):
        self.Entry_back = PhotoImage(file="Photos/RectangleEntry.png")
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=4, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=4, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=5, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=5, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=5, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=6, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=6, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=6, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=7, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=7, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=7, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=8, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=8, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=8, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=9, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=9, column=3)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=9, column=5)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=10, column=1)
        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=10, column=3)

    def save_data_in_file(self):
        row = {
            "gender": self.genderValue.get(),
            'SeniorCitizen': self.seniorCitizenValue.get(),
            'Partner': self.partnerValue.get(),
            'Dependents': self.dependentsValue.get(),
            'tenure': self.tenureValue.get(),
            'PhoneService': self.phoneServiceValue.get(),
            'MultipleLines': self.multipleLinesValue.get(),
            'InternetService': self.internetServiceValue.get(),
            'OnlineSecurity': self.onlineSecurityValue.get(),
            'OnlineBackup': self.onlineBackupValue.get(),
            'DeviceProtection': self.deviceProtectionValue.get(),
            'TechSupport': self.techSupportValue.get(),
            'StreamingTV': self.streamingTVValue.get(),
            'StreamingMovies': self.streamingMoviesValue.get(),
            'Contract': self.contractValue.get(),
            'PaperlessBilling': self.paperlessBillingValue.get(),
            'PaymentMethod': self.paymentMethodValue.get(),
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

    def test_data(self):
        if self.methodologyValue.get() == "Logistic Regression":
            LogisticRegressionClass('test')
        if self.methodologyValue.get() == "SVM":
            SVMClass("test")
        if self.methodologyValue.get() == "ID3":
            DecisionTreeClass('test')
        if self.methodologyValue.get() == "CART":
            CARTClass('test')

    def train_data(self):
        if self.methodologyValue.get() == "Logistic Regression":
            LogisticRegressionClass('train')
        if self.methodologyValue.get() == "SVM":
            SVMClass("train")
        if self.methodologyValue.get() == "CART":
            CARTClass('train')
        if self.methodologyValue.get() == "ID3":
            DecisionTreeClass('train')

    def predict_data(self):
        self.save_data_in_file()
        if self.methodologyValue.get() == "Logistic Regression":
            LogisticRegressionClass('predict')
        if self.methodologyValue.get() == "SVM":
            SVMClass("predict")
        if self.methodologyValue.get() == "CART":
            CARTClass('predict')
        if self.methodologyValue.get() == "ID3":
            DecisionTreeClass('predict')


Home()
