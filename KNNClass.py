import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from tkinter import *

class KNNClass:
    def __init__(self, case):
        self.data = pd.read_csv('Data.csv')

        global X, y
        X = self.data.drop('Churn', axis=1)
        y = self.data['Churn']

        self.mainColor = "#191142"
        self.root = Toplevel()
        self.root.title("Service cancellation predictor")

        self.root.configure(background=self.mainColor, padx=30, pady=30)
        self.root.overrideredirect(True)

        global X_train, X_test, y_train, y_test, classifier
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        global image
        image = PhotoImage(file="Photos/Buttons/closeButton.png")
        self.close_button = Button(self.root, image=image, background=self.mainColor, bd=0, cursor="hand2",
                                   activebackground=self.mainColor,
                                   command=self.root.destroy)
        classifier = KNeighborsClassifier(n_neighbors=7)
        classifier.fit(X_train, y_train)

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
        y_pred = classifier.predict(X_test)
        joblib.dump(classifier, 'KNN_model.sav')

        # Accuracy for testing
        score = metrics.accuracy_score(y_test, y_pred)
        print("Accuracy Of KNN Model(Test) :", score)
        # -------------------------------------------------adding gui---------------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)

        frame = Frame(self.root, background=self.mainColor, pady=20)

        global accuracyImage
        accuracyImage = PhotoImage(file="Photos/Labels/testAccuracy.png")
        accuracyLabel = Label(frame, image=accuracyImage, background=self.mainColor)
        accuracyValue = Label(frame, text=score, background=self.mainColor, font=('arial', 16, 'bold'),
                              foreground="white")
        accuracyLabel.grid(row=0, column=0)
        accuracyValue.grid(row=0, column=1)
        frame.pack()

        self.close_button.pack()

    def train(self):
        classifier = KNeighborsClassifier(n_neighbors=7)
        classifier.fit(X_train, y_train)
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
        loaded = joblib.load('KNN_model.sav')
        predictions = loaded.predict(newData)
        print(f"predictions = {predictions}")
        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)

        frame = Frame(self.root, background=self.mainColor, pady=20)
        global predictionsImage
        if predictions[0] == 1:
            predictionsImage = PhotoImage(file="Photos/Labels/customerCancelService.png")
            self.accuracyValue = Label(frame, image=predictionsImage, background=self.mainColor)
        elif predictions[0] == 0:
            predictionsImage = PhotoImage(file="Photos/Labels/customerWillKeepService.png")
            self.accuracyValue = Label(frame, image=predictionsImage, background=self.mainColor)
        self.accuracyValue.grid(row=0, column=1)
        frame.pack()

        self.close_button.pack()
