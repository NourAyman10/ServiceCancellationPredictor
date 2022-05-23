# Import the required modules
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import metrics
from tkinter import *
from tkinter import ttk


class LogisticRegressionClass:
    def __init__(self, case):
        self.data_frame = pd.read_csv('Data.csv')

        self.mainColor = "#191142"
        self.root = Toplevel()
        self.root.title("Service cancellation predictor")

        self.root.configure(background=self.mainColor, padx=30, pady=30)
        self.root.overrideredirect(True)

        global X_train, X_test, y_train, y_test, model
        X_train, X_test, y_train, y_test = train_test_split(self.data_frame.drop('Churn', axis=1),
                                                            self.data_frame['Churn'],
                                                            test_size=0.30,
                                                            random_state=101)
        model = LogisticRegression()
        model.fit(X_train, y_train)

        global image
        image = PhotoImage(file="Photos/Buttons/closeButton.png")
        self.close_button = Button(self.root, image=image, background=self.mainColor, bd=0, cursor="hand2",
                                   activebackground=self.mainColor,
                                   command=self.root.destroy)

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

    def center(self, win, window_width, window_height):
        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (window_width / 2))
        y_coordinate = int((screen_height / 2) - (window_height / 2))
        win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Visualize the data
    def scatter_plot(self):
        plt.scatter(self.data_frame.MonthlyCharges, self.data_frame.Churn, cmap="rainbow")
        plt.title("Scatter plot for Logistic Regression")

    def test(self):
        Y_prediction = model.predict(X_test)
        joblib.dump(model, 'Logistic_Regression_Model.joblib')
        # checking coeffiecent
        print('coef:', model.coef_, end='\n\n')
        # checking intercept
        print('intercept:', model.intercept_)

        # Accuracy for testing
        score = metrics.accuracy_score(y_test, Y_prediction)
        # calculate confusion_matrix
        print("Accuracy Of Logistic Regression Model(Test) :", score)
        cm = metrics.confusion_matrix(y_test, Y_prediction)
        plt.figure(figsize=(9, 9))
        sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        all_sample_title = 'Accuracy Score: {0}'.format(score)
        plt.title(all_sample_title, size=15)

        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 800, 600)

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview.Heading", font=('Comic Sans MS', 20, 'bold'), background='#251260', borderwidth=0)
        style.configure("Treeview", background="#150941", font=('arial', 16), fieldbackground="#150941", rowheight=40,
                        foreground='white', highlightthickness=0)
        style.map("Treeview", background=[('selected', '#251260')])

        tree_frame = Frame(self.root)
        tree_frame.pack(pady=20, padx=40)

        tree_scrollbar = Scrollbar(tree_frame)
        tree_scrollbar.pack(side=RIGHT, fill=Y)

        tv = ttk.Treeview(tree_frame, height=5, yscrollcommand=tree_scrollbar.set)
        global imageHeading
        imageHeading = PhotoImage(file="Photos/Labels/coefficient.png")
        tv.heading("#0", image=imageHeading)
        tv.column('#0', width=290, anchor='center', stretch=NO)
        tv.pack()

        tree_scrollbar.config(command=tv.yview)

        index = 0
        for item in model.coef_[0]:
            tv.insert('', 'end', f"item{index}", text=item)
            index += 1

        frame2 = Frame(self.root, background=self.mainColor)

        global interceptImage
        interceptImage = PhotoImage(file="Photos/Labels/intercept.png")
        interceptLabel = Label(frame2, text="Intercept: ", image=interceptImage, background=self.mainColor)
        interceptValue = Label(frame2, text=model.intercept_[0], background=self.mainColor,
                               font=('arial', 16, 'bold'), foreground="white")

        global accuracyImage
        accuracyImage = PhotoImage(file="Photos/Labels/testAccuracy.png")
        accuracyLabel = Label(frame2, image=accuracyImage, background=self.mainColor)
        accuracyValue = Label(frame2, text=score, background=self.mainColor, font=('arial', 16, 'bold'),
                              foreground="white")

        interceptLabel.grid(row=0, column=0)
        interceptValue.grid(row=0, column=1)
        accuracyLabel.grid(row=1, column=0)
        accuracyValue.grid(row=1, column=1)
        frame2.pack()

        global showGraphImage
        showGraphImage = PhotoImage(file="Photos/Buttons/showGraph.png")
        showGraphBtn = Button(self.root, text="Show Graph", image=showGraphImage, background=self.mainColor, bd=0,
                              activebackground=self.mainColor,
                              cursor="hand2", command=plt.show)
        showGraphBtn.pack()

        self.close_button.pack()

    def train(self):
        model = LogisticRegression()
        model.fit(X_train, y_train)
        # -----------------------------------------------------adding gui-----------------------------------------------
        # Positions the window in the center of the page.
        self.center(self.root, 700, 200)

        frame = Frame(self.root, background=self.mainColor, pady=20)

        global successImage
        successImage = PhotoImage(file="Photos/Labels/CreatedSuccessfully.png")
        value = Label(frame, image=successImage, background=self.mainColor,
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
        model = joblib.load('Logistic_Regression_Model.joblib')
        predictions = model.predict(newData)
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
