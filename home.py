from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class Home:
    def __init__(self):
        self.mainColor = '#191142'
        self.foregroundColor = '#8AD7FF'

        self.root = Tk()
        self.root.title("Service cancellation predictor")
        self.root.attributes('-fullscreen', True)
        self.width = self.root.winfo_screenwidth()

        # setting background image
        self.image = Image.open("Photos/background.png")
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)
        self.backgroundLabel.place(x=0, y=0)

        # general styles
        self.style = ttk.Style(self.root)
        self.style.configure("TLabel", font=('arial', 12), background=self.mainColor)

        self.frame = Frame(self.root, background=self.mainColor, padx=30, pady=30)

        # variables to get data from user
        self.methodology = StringVar(value="none")

        self.customerIDValue = StringVar()
        self.genderValue = StringVar()
        self.seniorCitizenValue = StringVar()

        self.partnerValue = StringVar()
        self.dependentsValue = StringVar()
        self.tenureValue = StringVar()

        self.phoneServiceValue = StringVar()
        self.multipleLinesValue = StringVar()
        self.internetServiceValue = StringVar()

        self.onlineSecurityValue = StringVar()
        self.onlineBackupValue = StringVar()
        self.deviceProtectionValue = StringVar()

        self.techSupportValue = StringVar()
        self.streamingTVValue = StringVar()
        self.streamingMoviesValue = StringVar()

        self.contractValue = StringVar()
        self.paperlessBillingValue = StringVar()
        self.paymentMethodValue = StringVar()

        self.monthlyChargesValue = StringVar()
        self.totalChargesValue = StringVar()

        # labels
        self.customerID = PhotoImage(file="Photos/Labels/customerID.png")
        self.customerIDLabel = ttk.Label(self.frame, image=self.customerID)

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

        # Radio buttons
        self.logisticRegressionImage = PhotoImage(file="Photos/Labels/Logistic Regression.png")
        self.logisticRegressionRadioButton = Radiobutton(self.frame, variable=self.methodology,
                                                         value="logistic Regression", background=self.mainColor,
                                                         image=self.logisticRegressionImage)

        self.SVMImage = PhotoImage(file="Photos/Labels/SVM.png")
        self.SVMRadioButton = Radiobutton(self.frame, variable=self.methodology,
                                          value="SVM", background=self.mainColor, image=self.SVMImage)

        self.ID3Image = PhotoImage(file="Photos/Labels/ID3.png")
        self.ID3RadioButton = Radiobutton(self.frame, variable=self.methodology,
                                          value="ID3", background=self.mainColor, image=self.ID3Image)

        self.KNNImage = PhotoImage(file="Photos/Labels/KNN.png")
        self.KNNRadioButton = Radiobutton(self.frame, variable=self.methodology,
                                          value="KNN", background=self.mainColor, image=self.KNNImage)

        # set background to Entries and place it
        self.Entry_back = PhotoImage(file="Photos/RectangleEntry.png")

        Label(self.frame, image=self.Entry_back, bg=self.mainColor).grid(row=4, column=1)
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

        # Entries
        self.customerIDEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.customerIDValue,
                                     background=self.mainColor, foreground=self.foregroundColor)
        self.genderEntry = Entry(self.frame, width=14, font=("arial", 14), bd=0, textvariable=self.genderValue,
                                 background=self.mainColor,
                                 foreground=self.foregroundColor)
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

        # buttons
        self.train_button_back = PhotoImage(file="Photos/Buttons/trainButton.png")
        self.trainButton = Button(self.frame, image=self.train_button_back, borderwidth=0, cursor="hand2", bd=0,
                                  background=self.mainColor)

        self.test_button_back = PhotoImage(file="Photos/Buttons/testButton.png")
        self.testButton = Button(self.frame, image=self.test_button_back, borderwidth=0, cursor="hand2", bd=0,
                                 background=self.mainColor)

        self.predict_button_back = PhotoImage(file="Photos/Buttons/predictButton.png")
        self.predictButton = Button(self.frame, image=self.predict_button_back, borderwidth=0, cursor="hand2", bd=0,
                                    background=self.mainColor, anchor='center')

        self.close_button_back = PhotoImage(file="Photos/Buttons/closeButton.png")
        self.closeButton = Button(self.frame, image=self.close_button_back, borderwidth=0, cursor="hand2", bd=0,
                                  background=self.mainColor,
                                  command=self.root.destroy)

        # margin photo
        self.marginPhoto = PhotoImage(file="Photos/RectangleMargin.png")
        self.margin = Label(self.frame, image=self.marginPhoto, borderwidth=0)

        # positions
        # methodologyLabel.grid(row=0, column=0)

        self.logisticRegressionRadioButton.grid(row=1, column=0)
        self.SVMRadioButton.grid(row=1, column=1)
        self.ID3RadioButton.grid(row=1, column=2)
        self.KNNRadioButton.grid(row=1, column=3)
        self.closeButton.grid(row=1, column=6)

        self.trainButton.grid(row=2, column=2)
        self.testButton.grid(row=2, column=3)

        self.margin.grid(row=3, columnspan=6)

        self.customerIDLabel.grid(row=4, column=0)
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
        self.customerIDEntry.grid(row=4, column=1)
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

        self.margin.grid(row=11, columnspan=6)

        self.predictButton.grid(row=12, columnspan=6)

        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        self.root.mainloop()
