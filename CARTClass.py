from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
import joblib
import pandas as pd
from tkinter import *

class CARTClass:
    def __init__(self, case):
        self.treeData = pd.read_csv('Data.csv')
        global treeX
        treeX = self.treeData.drop('Churn', axis=1)
        global treeY
        treeY = self.treeData['Churn']

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

        global DTx_train, DTx_test, DTy_train, DTy_test, clf, DTclf
        DTx_train, DTx_test, DTy_train, DTy_test = train_test_split(treeX, treeY, test_size=0.50, random_state=101)

        clf = tree.DecisionTreeClassifier(criterion="entropy")
        DTclf = clf.fit(DTx_train, DTy_train)


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
        pred = DTclf.predict(DTx_test)
        joblib.dump(DTclf, "cart_model.dt")

        score = metrics.accuracy_score(DTy_test, y_pred=pred)
        print("Accuracy Of CART Model(Test) :", score)
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
        clf = tree.DecisionTreeClassifier(criterion="entropy")
        clf.fit(DTx_train, DTy_train)
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
        model = joblib.load('cart_model.dt')
        predictions = model.predict(newData)
        print(f"predictions = {predictions}")
        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)
        frame = Frame(self.root, background=self.mainColor, pady=20)

        global predictionsImage
        if predictions < 0.5:
            predictionsImage = PhotoImage(file="Photos/Labels/customerWillKeepService.png")
            self.accuracyValue = Label(frame, image=predictionsImage, background=self.mainColor)
        elif predictions >= 0.5:
            predictionsImage = PhotoImage(file="Photos/Labels/customerCancelService.png")
            self.accuracyValue = Label(frame, image=predictionsImage, background=self.mainColor)
        self.accuracyValue.grid(row=0, column=1)
        frame.pack()

        self.close_button.pack()
