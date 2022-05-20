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

        self.mainColor = "#522dbd"
        self.root = Tk()
        self.root.title("Service cancellation predictor")

        self.windowWidth = self.root.winfo_reqwidth()
        self.windowHeight = self.root.winfo_reqheight()
        # Gets both half the screen width/height and window width/height
        self.positionRight = int(self.root.winfo_screenwidth() / 2 - self.windowWidth / 2)
        self.positionDown = int(self.root.winfo_screenheight() / 2 - self.windowHeight / 2)

        self.root.configure(background=self.mainColor, padx=30, pady=30)
        self.root.overrideredirect(1)

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


    def test(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.20, random_state=200)
        self.cls = svm.SVC(kernel="linear")
        self.cls.fit(self.x_train, self.y_train)
        self.cls.predict(self.x_test)
        joblib.dump(self.cls, 'SVM_model.sav' )

        # Accuracy for testing
        self.score = self.cls.score(self.x_test, self.y_test)
        print("Accuracy Of SVM Model(Test) :", self.score)
        # -------------------------------------------------adding gui---------------------------------------------------
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(self.positionRight - 200, self.positionDown))
        frame = Frame(self.root, background=self.mainColor, pady=20)
        accuracyLabel = Label(frame, text="Accuracy Model for Test: ", background=self.mainColor,
                              font=('Comic Sans MS', 20, 'bold'), foreground="#57d7ff")
        accuracyValue = Label(frame, text=self.score, background=self.mainColor, font=('arial', 16, 'bold'),
                              foreground="white")
        accuracyLabel.grid(row=0, column=0)
        accuracyValue.grid(row=0, column=1)
        frame.pack()

        close_button = Button(self.root, text="Close", background="#251260", foreground="#a744ff", padx=100,
                              font=('Comic Sans MS', 20, 'bold'), cursor="hand2", command=self.root.destroy)
        close_button.pack()

    def train(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.20, random_state=200)

        self.cls = svm.SVC(kernel="linear")
        self.cls.fit(self.x_train, self.y_train)
        self.score = self.cls.score(self.x_train, self.y_train)
        print("Accuracy Of SVM Model(Train) :", self.score)
        # -------------------------------------------------adding gui---------------------------------------------------
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(self.positionRight - 200, self.positionDown))
        frame = Frame(self.root, background=self.mainColor, pady=20)
        accuracyLabel = Label(frame, text="Accuracy Model for Train: ", background=self.mainColor,
                              font=('Comic Sans MS', 20, 'bold'), foreground="#57d7ff")
        accuracyValue = Label(frame, text=self.score, background=self.mainColor, font=('arial', 16, 'bold'),
                              foreground="white")
        accuracyLabel.grid(row=0, column=0)
        accuracyValue.grid(row=0, column=1)
        frame.pack()

        close_button = Button(self.root, text="Close", background="#251260", foreground="#a744ff", padx=100,
                              font=('Comic Sans MS', 20, 'bold'), cursor="hand2", command=self.root.destroy)
        close_button.pack()

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
        self.root.geometry("+{}+{}".format(self.positionRight - 100, self.positionDown))
        frame = Frame(self.root, background=self.mainColor, pady=20)
        accuracyLabel = Label(frame, text="Predictions: ", background=self.mainColor,
                              font=('Comic Sans MS', 20, 'bold'), foreground="#57d7ff")
        if predictions[0] == 1:
            accuracyValue = Label(frame, text="Customer Will Left", background=self.mainColor,
                                  font=('arial', 16, 'bold'),
                                  foreground="white")
        elif predictions[0] == 0:
            accuracyValue = Label(frame, text="Customer Will Stay", background=self.mainColor,
                                  font=('arial', 16, 'bold'),
                                  foreground="white")
        accuracyLabel.grid(row=0, column=0)
        accuracyValue.grid(row=0, column=1)
        frame.pack()

        close_button = Button(self.root, text="Close", background="#251260", foreground="#a744ff", padx=100,
                              font=('Comic Sans MS', 20, 'bold'), cursor="hand2", command=self.root.destroy)
        close_button.pack()
