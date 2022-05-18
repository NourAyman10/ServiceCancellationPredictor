from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

mainColor = '#191142'
foregroundColor = '#8AD7FF'

root = Tk()
root.title("Service cancellation predictor")

#setting tkinter window size
width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry("%dx%d" % (width, height))
root.attributes('-fullscreen', True)

image = Image.open("Photos/background.png")
backgroundImage = ImageTk.PhotoImage(image)
backgroundLabel = Label(root, image=backgroundImage)
backgroundLabel.place(x=0, y=0)

# general styles
style = ttk.Style(root)
style.configure("TLabel", font=('arial', 12), background=mainColor)

frame = Frame(root, background=mainColor, padx=30, pady=30)

# value of variables
methodology = StringVar(value="none")
customerIDValue = StringVar()
genderValue = StringVar()
seniorCitizenValue = StringVar()

partnerValue = StringVar()
dependentsValue = StringVar()
tenureValue = StringVar()

phoneServiceValue = StringVar()
multipleLinesValue = StringVar()
internetServiceValue = StringVar()

onlineSecurityValue = StringVar()
onlineBackupValue = StringVar()
deviceProtectionValue = StringVar()

techSupportValue = StringVar()
streamingTVValue = StringVar()
streamingMoviesValue = StringVar()

contractValue = StringVar()
paperlessBillingValue = StringVar()
paymentMethodValue = StringVar()

monthlyChargesValue = StringVar()
totalChargesValue = StringVar()

# labels
customerID = PhotoImage(file="Photos/Labels/customerID.png")
customerIDLabel = ttk.Label(frame, image=customerID)

gender = PhotoImage(file="Photos/Labels/gender.png")
genderLabel = ttk.Label(frame, image=gender)

seniorCitizen = PhotoImage(file="Photos/Labels/Senior Citizen.png")
seniorCitizenLabel = ttk.Label(frame, image=seniorCitizen)


partner = PhotoImage(file="Photos/Labels/Partner.png")
partnerLabel = ttk.Label(frame, image=partner)

dependents = PhotoImage(file="Photos/Labels/Dependents.png")
dependentsLabel = ttk.Label(frame, image=dependents)

tenure = PhotoImage(file="Photos/Labels/Tenure.png")
tenureLabel = ttk.Label(frame, image=tenure)


phoneService = PhotoImage(file="Photos/Labels/Phone Service.png")
phoneServiceLabel = ttk.Label(frame, image=phoneService)

multipleLines = PhotoImage(file="Photos/Labels/Multiple Lines.png")
multipleLinesLabel = ttk.Label(frame, image=multipleLines)

internetService = PhotoImage(file="Photos/Labels/Internet Service.png")
internetServiceLabel = ttk.Label(frame, image=internetService)


onlineSecurity = PhotoImage(file="Photos/Labels/Online Security.png")
onlineSecurityLabel = ttk.Label(frame, image=onlineSecurity)

onlineBackup = PhotoImage(file="Photos/Labels/Online Backup.png")
onlineBackupLabel = ttk.Label(frame, image=onlineBackup)

deviceProtection = PhotoImage(file="Photos/Labels/Device Protection.png")
deviceProtectionLabel = ttk.Label(frame, image=deviceProtection)


techSupport = PhotoImage(file="Photos/Labels/Tech Support.png")
techSupportLabel = ttk.Label(frame, image=techSupport)

streamingTV = PhotoImage(file="Photos/Labels/Streaming TV.png")
streamingTVLabel = ttk.Label(frame, image=streamingTV)

streamingMovies = PhotoImage(file="Photos/Labels/Streaming Movies.png")
streamingMoviesLabel = ttk.Label(frame, image=streamingMovies)


contract = PhotoImage(file="Photos/Labels/Contract.png")
contractLabel = ttk.Label(frame, image=contract)

paperlessBilling = PhotoImage(file="Photos/Labels/Paperless Billing.png")
paperlessBillingLabel = ttk.Label(frame, image=paperlessBilling)

paymentMethod = PhotoImage(file="Photos/Labels/Payment Method.png")
paymentMethodLabel = ttk.Label(frame, image=paymentMethod)


monthlyCharges = PhotoImage(file="Photos/Labels/Monthly Charges.png")
monthlyChargesLabel = ttk.Label(frame, image=monthlyCharges)

totalCharges = PhotoImage(file="Photos/Labels/Total Charges.png")
totalChargesLabel = ttk.Label(frame, image=totalCharges)

# Radio buttons
logisticRegressionImage = PhotoImage(file="Photos/Labels/Logistic Regression.png")
logisticRegressionRadioButton = Radiobutton(frame, variable=methodology,
                                            value="logistic Regression", background=mainColor, image=logisticRegressionImage)

SVMImage = PhotoImage(file="Photos/Labels/SVM.png")
SVMRadioButton = Radiobutton(frame, variable=methodology,
                             value="SVM", background=mainColor, image=SVMImage)

ID3Image = PhotoImage(file="Photos/Labels/ID3.png")
ID3RadioButton = Radiobutton(frame, variable=methodology,
                             value="ID3", background=mainColor, image=ID3Image)

KNNImage = PhotoImage(file="Photos/Labels/KNN.png")
KNNRadioButton = Radiobutton(frame, variable=methodology,
                             value="KNN", background=mainColor, image=KNNImage)
# set background to Entries
Entry_back = PhotoImage(file="Photos/RectangleEntry.png")

Label(frame, image=Entry_back, bg=mainColor).grid(row=4, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=4, column=3)
Label(frame, image=Entry_back, bg=mainColor).grid(row=4, column=5)

Label(frame, image=Entry_back, bg=mainColor).grid(row=5, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=5, column=3)
Label(frame, image=Entry_back, bg=mainColor).grid(row=5, column=5)

Label(frame, image=Entry_back, bg=mainColor).grid(row=6, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=6, column=3)
Label(frame, image=Entry_back, bg=mainColor).grid(row=6, column=5)

Label(frame, image=Entry_back, bg=mainColor).grid(row=7, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=7, column=3)
Label(frame, image=Entry_back, bg=mainColor).grid(row=7, column=5)

Label(frame, image=Entry_back, bg=mainColor).grid(row=8, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=8, column=3)
Label(frame, image=Entry_back, bg=mainColor).grid(row=8, column=5)

Label(frame, image=Entry_back, bg=mainColor).grid(row=9, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=9, column=3)
Label(frame, image=Entry_back, bg=mainColor).grid(row=9, column=5)

Label(frame, image=Entry_back, bg=mainColor).grid(row=10, column=1)
Label(frame, image=Entry_back, bg=mainColor).grid(row=10, column=3)

# Entries
customerIDEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=customerIDValue, background=mainColor, foreground=foregroundColor)
genderEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=genderValue, background=mainColor, foreground=foregroundColor)
seniorCitizenEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=seniorCitizenValue, background=mainColor, foreground=foregroundColor)

partnerEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=partnerValue, background=mainColor, foreground=foregroundColor)
dependentsEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=dependentsValue, background=mainColor, foreground=foregroundColor)
tenureEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=tenureValue, background=mainColor, foreground=foregroundColor)

phoneServiceEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=phoneServiceValue, background=mainColor, foreground=foregroundColor)
multipleLinesEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=multipleLinesValue, background=mainColor, foreground=foregroundColor)
internetServiceEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=internetServiceValue, background=mainColor, foreground=foregroundColor)

onlineSecurityEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=onlineSecurityValue, background=mainColor, foreground=foregroundColor)
onlineBackupEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=onlineBackupValue, background=mainColor, foreground=foregroundColor)
deviceProtectionEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=deviceProtectionValue, background=mainColor, foreground=foregroundColor)

techSupportEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=techSupportValue, background=mainColor, foreground=foregroundColor)
streamingTVEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=streamingTVValue, background=mainColor, foreground=foregroundColor)
streamingMoviesEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=streamingMoviesValue, background=mainColor, foreground=foregroundColor)

contractEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=contractValue, background=mainColor, foreground=foregroundColor)
paperlessBillingEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=paperlessBillingValue, background=mainColor, foreground=foregroundColor)
paymentMethodEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=paymentMethodValue, background=mainColor, foreground=foregroundColor)

monthlyChargesEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=monthlyChargesValue, background=mainColor, foreground=foregroundColor)
totalChargesEntry = Entry(frame, width=14, font=("arial", 14), bd=0, textvariable=totalChargesValue, background=mainColor, foreground=foregroundColor)

# buttons
train_button_back = PhotoImage(file="Photos/Buttons/trainButton.png")
trainButton = Button(frame, image=train_button_back, borderwidth=0, cursor="hand2", bd=0, background=mainColor)

test_button_back = PhotoImage(file="Photos/Buttons/testButton.png")
testButton = Button(frame, image=test_button_back, borderwidth=0, cursor="hand2", bd=0, background=mainColor)

predict_button_back = PhotoImage(file="Photos/Buttons/predictButton.png")
predictButton = Button(frame, image=predict_button_back, borderwidth=0, cursor="hand2", bd=0, background=mainColor, anchor='center')

close_button_back = PhotoImage(file="Photos/Buttons/closeButton.png")
closeButton = Button(frame, image=close_button_back, borderwidth=0, cursor="hand2", bd=0, background=mainColor, command=root.destroy)

# margin photo
marginPhoto = PhotoImage(file="Photos/RectangleMargin.png")
margin = Label(frame, image=marginPhoto, borderwidth=0)

# positions
# methodologyLabel.grid(row=0, column=0)

logisticRegressionRadioButton.grid(row=1, column=0)
SVMRadioButton.grid(row=1, column=1)
ID3RadioButton.grid(row=1, column=2)
KNNRadioButton.grid(row=1, column=3)
closeButton.grid(row=1, column=6)

trainButton.grid(row=2, column=2)
testButton.grid(row=2, column=3)

margin.grid(row=3, columnspan=6)

customerIDLabel.grid(row=4, column=0)
genderLabel.grid(row=4, column=2)
seniorCitizenLabel.grid(row=4, column=4)

partnerLabel.grid(row=5, column=0)
dependentsLabel.grid(row=5, column=2)
tenureLabel.grid(row=5, column=4)

phoneServiceLabel.grid(row=6, column=0)
multipleLinesLabel.grid(row=6, column=2)
internetServiceLabel.grid(row=6, column=4)

onlineSecurityLabel.grid(row=7, column=0)
onlineBackupLabel.grid(row=7, column=2)
deviceProtectionLabel.grid(row=7, column=4)

techSupportLabel.grid(row=8, column=0)
streamingTVLabel.grid(row=8, column=2)
streamingMoviesLabel.grid(row=8, column=4)

contractLabel.grid(row=9, column=0)
paperlessBillingLabel.grid(row=9, column=2)
paymentMethodLabel.grid(row=9, column=4)

monthlyChargesLabel.grid(row=10, column=0)
totalChargesLabel.grid(row=10, column=2)
#############################################
customerIDEntry.grid(row=4, column=1)
genderEntry.grid(row=4, column=3)
seniorCitizenEntry.grid(row=4, column=5)

partnerEntry.grid(row=5, column=1)
dependentsEntry.grid(row=5, column=3)
tenureEntry.grid(row=5, column=5)

phoneServiceEntry.grid(row=6, column=1)
multipleLinesEntry.grid(row=6, column=3)
internetServiceEntry.grid(row=6, column=5)

onlineSecurityEntry.grid(row=7, column=1)
onlineBackupEntry.grid(row=7, column=3)
deviceProtectionEntry.grid(row=7, column=5)

techSupportEntry.grid(row=8, column=1)
streamingTVEntry.grid(row=8, column=3)
streamingMoviesEntry.grid(row=8, column=5)

contractEntry.grid(row=9, column=1)
paperlessBillingEntry.grid(row=9, column=3)
paymentMethodEntry.grid(row=9, column=5)

monthlyChargesEntry.grid(row=10, column=1)
totalChargesEntry.grid(row=10, column=3)

margin.grid(row=11, columnspan=6)
predictButton.grid(row=12, columnspan=6)
# closeButton.place(x=width-170, y=65)
frame.place(anchor='center', relx=0.5, rely=0.5)


root.mainloop()
