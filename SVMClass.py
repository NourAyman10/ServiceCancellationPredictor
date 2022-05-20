from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
import joblib
import pandas as pd

class SVMClass:
    def __init__(self, case):
        self.data_frame = pd.read_csv('Data.csv')
        self.x = self.data_frame.drop('Churn', axis=1)
        self.y = self.data_frame['Churn']

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

    def train(self):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x, self.y, test_size=0.20, random_state=200)

        self.cls = svm.SVC(kernel="linear")
        self.cls.fit(self.x_train, self.y_train)
        self.score = self.cls.score(self.x_train, self.y_train)
        print("Accuracy Of SVM Model(Train) :", self.score)

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