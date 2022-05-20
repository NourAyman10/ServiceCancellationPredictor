# Import the required modules
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import metrics
from tkinter import *
from tkinter import ttk


class LogisticRegressionClass:
    def __init__(self, case):
        self.data_frame = pd.read_csv('Data.csv')

        # **********************************************************************************************************************
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
                self.scatter_plot()
                self.test()
                return
            case 'train':
                self.train()
                return
            case 'predict':
                self.predict()
                return

        self.root.mainloop()

    # Visualize the data
    def scatter_plot(self):
        plt.scatter(self.data_frame.MonthlyCharges, self.data_frame.Churn, cmap="rainbow")
        plt.title("Scatter plot for Logistic Regression")

    def test(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data_frame.drop('Churn', axis=1),
                                                                                self.data_frame['Churn'],
                                                                                test_size=0.30,
                                                                                random_state=101)
        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)
        self.Y_prediction = self.model.predict(self.X_test)
        joblib.dump(self.model, 'Logistic_Regression_Model.joblib')
        # checking coeffiecent
        print('coef:', self.model.coef_, end='\n\n')
        # checking intercept
        print('intercept:', self.model.intercept_)
        # save the model to disk

        # Accuracy for testing
        self.score = self.model.score(self.X_test, self.y_test)
        # calculate confusion_matrix
        print("Accuracy Of Logistic Regression Model(Test) :", self.score)
        self.cm = metrics.confusion_matrix(self.y_test, self.Y_prediction)
        plt.figure(figsize=(9, 9))
        sns.heatmap(self.cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        self.all_sample_title = 'Accuracy Score: {0}'.format(self.score)
        plt.title(self.all_sample_title, size=15)

        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.root.geometry("+{}+{}".format(self.positionRight - 200, self.positionDown - 200))

        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure("Treeview.Heading", foreground='#a744ff', font=('Comic Sans MS', 20, 'bold'),
                        background='#251260', borderwidth=0)
        style.configure("Treeview", background="#150941", font=('arial', 16), fieldbackground="#150941", rowheight=40,
                        foreground='white')
        style.map("Treeview", background=[('selected', '#251260')])

        tree_frame = Frame(self.root)
        tree_frame.pack(pady=20, padx=40)

        tree_scrollbar = Scrollbar(tree_frame)
        tree_scrollbar.pack(side=RIGHT, fill=Y)

        tv = ttk.Treeview(tree_frame, height=5, yscrollcommand=tree_scrollbar.set)
        tv.heading("#0", text="Coefficients")
        tv.column('#0', width=300, anchor='center', stretch=NO)
        tv.pack()

        tree_scrollbar.config(command=tv.yview)

        index = 0
        for item in self.model.coef_[0]:
            tv.insert('', 'end', f"item{index}", text=item)
            index += 1

        frame2 = Frame(self.root, background=self.mainColor)
        interceptLabel = Label(frame2, text="Intercept: ", background=self.mainColor,
                               font=('Comic Sans MS', 20, 'bold'), foreground="#57d7ff")
        interceptValue = Label(frame2, text=self.model.intercept_[0], background=self.mainColor,
                               font=('arial', 16, 'bold'), foreground="white")

        accuracyLabel = Label(frame2, text="Accuracy Model for Test: ", background=self.mainColor,
                              font=('Comic Sans MS', 20, 'bold'), foreground="#57d7ff")
        accuracyValue = Label(frame2, text=self.score, background=self.mainColor, font=('arial', 16, 'bold'),
                              foreground="white")

        interceptLabel.grid(row=0, column=0)
        interceptValue.grid(row=0, column=1)
        accuracyLabel.grid(row=1, column=0)
        accuracyValue.grid(row=1, column=1)
        frame2.pack()

        Label(self.root, text=" ", pady=2, background=self.mainColor).pack()

        showGraphBtn = Button(self.root, text="Show Graph", background="#251260", foreground="#a744ff", padx=80,
                              font=('Comic Sans MS', 20, 'bold'), cursor="hand2", command=plt.show)
        showGraphBtn.pack()

        Label(self.root, text=" ", pady=2, background=self.mainColor).pack()

        close_button = Button(self.root, text="Close", background="#251260", foreground="#a744ff", padx=100,
                              font=('Comic Sans MS', 20, 'bold'), cursor="hand2", command=self.root.destroy)
        close_button.pack()

    def train(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data_frame.drop('Churn', axis=1),
                                                                                self.data_frame['Churn'],
                                                                                test_size=0.30,
                                                                                random_state=101)
        self.model = LogisticRegression()
        self.model.fit(self.X_train, self.y_train)
        self.score = self.model.score(self.X_train, self.y_train)
        print("Accuracy Of Logistic Regression Model(Train) :", self.score)
        # -----------------------------------------------------adding gui-----------------------------------------------
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
        model = joblib.load('Logistic_Regression_Model.joblib')
        predictions = model.predict(newData)
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
