from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import joblib
import pandas as pd
from tkinter import *
from tkinter import ttk

class SVMClass:
    def __init__(self, case):
        self.data_frame = pd.read_csv('Data.csv')
        self.x = self.data_frame.drop('Churn', axis=1)
        self.y = self.data_frame['Churn']

        self.mainColor = "#191142"
        self.root = Toplevel()
        self.root.title("Service cancellation predictor")

        self.root.configure(background=self.mainColor, padx=30, pady=30)
        self.root.overrideredirect(True)

        global image
        image = PhotoImage(file="Photos/Buttons/closeButton.png")
        self.close_button = Button(self.root, image=image, background=self.mainColor, bd=0, cursor="hand2",
                                   activebackground=self.mainColor,
                                   command=self.root.destroy)

        global x_train, x_test, y_train, y_test, cls
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=0.20, random_state=200)
        cls = svm.SVC(kernel="linear")
        cls.fit(x_train, y_train)


        match case:
            case 'test':
                self.test()
                return
            case 'train':
                self.train()
                return
            case 'predict':
                self.predict()
                return


    def center(self, win, window_width, window_height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    def test(self):
        y_predict = cls.predict(x_test)
        joblib.dump(cls, 'SVM_model.sav')

        # Accuracy for testing
        score = metrics.accuracy_score(y_test, y_predict)
        print("Accuracy Of SVM Model(Test) :", score)
        # -------------------------------------------------adding gui---------------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)

        frame = Frame(self.root, background=self.mainColor, pady=20)

        global accuracyImage
        accuracyImage = PhotoImage(file="Photos/Labels/testAccuracy.png")
        accuracyLabel = Label(frame, text="Accuracy Model for Test: ",image=accuracyImage, background=self.mainColor)
        accuracyValue = Label(frame, text=score, background=self.mainColor, font=('arial', 16, 'bold'),
                              foreground="white")
        accuracyLabel.grid(row=0, column=0)
        accuracyValue.grid(row=0, column=1)
        frame.pack()

        self.close_button.pack()

    def train(self):
        cls = svm.SVC(kernel="linear")
        cls.fit(x_train, y_train)
        # -------------------------------------------------adding gui---------------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)

        frame = Frame(self.root, background=self.mainColor, pady=20)

        global successImage
        successImage = PhotoImage(file="Photos/Labels/CreatedSuccessfully.png")

        value = Label(frame, text="Model Created Successfully", image=successImage, background=self.mainColor,
                      font=('arial', 16, 'bold'),
                      foreground="white")
        value.grid(row=0, column=1)
        frame.pack()

        self.close_button.pack()

    def predict(self):
        newData = pd.read_csv('model.csv')
        newData = newData[['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                           'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
                           'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                           'PaymentMethod', 'MonthlyCharges', 'TotalCharges']]
        # load saved model

        loaded_model = joblib.load('SVM_model.sav')
        predictions = loaded_model.predict(newData)
        print(f"predictions = {predictions}")
        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)

        frame = Frame(self.root, background=self.mainColor, pady=20)

        global predictionsImage
        if predictions[0] == 1:
            predictionsImage = PhotoImage(file="Photos/Labels/customerCancelService.png")
            self.predictionsValue = Label(frame, image=predictionsImage, background=self.mainColor)
        elif predictions[0] == 0:
            predictionsImage = PhotoImage(file="Photos/Labels/customerWillKeepService.png")
            self.predictionsValue = Label(frame, image=predictionsImage, background=self.mainColor)
        self.predictionsValue.grid(row=0, column=1)
        frame.pack()

        self.close_button.pack()
