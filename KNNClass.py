import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from tkinter import *
from tkinter import ttk

class KNNClass:
    def __init__(self, case):
        self.data = pd.read_csv('Data.csv')
        self.X = self.data.drop('Churn', axis=1)
        self.y = self.data['Churn']

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
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.classifier = KNeighborsClassifier(n_neighbors=7)
        self.classifier.fit(self.X_train , self.y_train)
        self.y_pred = self.classifier.predict(self.X_test)
        joblib.dump(self.classifier, 'KNN_model.sav')

        # Accuracy for testing
        self.score = metrics.accuracy_score(self.y_test ,self.y_pred)
        print("Accuracy Of KNN Model(Test) :", self.score)
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
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size = 0.2, random_state=42)
        self.classifier = KNeighborsClassifier(n_neighbors=7)
        self.classifier.fit(self.X_train, self.y_train)
        self.score = self.classifier.score(self.X_train, self.y_train)
        print("Accuracy Of KNN Model(Train) :", self.score)
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
        loaded = joblib.load('KNN_model.sav')
        predictions = loaded.predict(newData)
        print(f"predictions = {predictions}")
        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(self.positionRight - 100, self.positionDown))
        frame = Frame(self.root, background=self.mainColor, pady=20)
        accuracyLabel = Label(frame, text="Predictions: ", background=self.mainColor,
                              font=('Comic Sans MS', 20, 'bold'), foreground="#57d7ff")
        if predictions[0] == 1:
            accuracyValue = Label(frame, text="Customer Cancel Service", background=self.mainColor,
                                  font=('arial', 16, 'bold'),
                                  foreground="white")
        elif predictions[0] == 0:
            accuracyValue = Label(frame, text="Customer will keep the service", background=self.mainColor,
                                  font=('arial', 16, 'bold'),
                                  foreground="white")
        accuracyLabel.grid(row=0, column=0)
        accuracyValue.grid(row=0, column=1)
        frame.pack()

        close_button = Button(self.root, text="Close", background="#251260", foreground="#a744ff", padx=100,
                              font=('Comic Sans MS', 20, 'bold'), cursor="hand2", command=self.root.destroy)
        close_button.pack()
