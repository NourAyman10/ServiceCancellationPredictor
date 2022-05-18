#Import the required modules
import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn import metrics
from sklearn.metrics import classification_report


class LogisticRegressionClass:
    def __init__(self):
        self.data_frame = pd.read_csv('Data.csv')
        # Split the dataset

    # Visualize the data
    def Sctatter_plot(self):
        plt.scatter(self.data_frame.MonthlyCharges, self.data_frame.Churn, cmap="rainbow")
        plt.title("Scatter plot for Logistic Regression")
        plt.show()

    def train(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.data_frame.drop('Churn', axis=1),
                                                                                self.data_frame['Churn'],
                                                                                test_size=0.30,
                                                                                random_state=101)
        self.model = LogisticRegression(max_iter=1000000)
        self.model.fit(self.X_train, self.y_train)
        # Make prediction using the model and display the confusion_matrix
        # for test model
        self.Y_predictions = self.model.predict(self.X_test)
        print(self.Y_predictions[:10])
        self.cm = metrics.confusion_matrix(self.y_test, self.Y_predictions)
        print(classification_report(self.y_test, self.Y_predictions))
        # Accuracy
        self.score = self.model.score(self.X_test, self.y_test)
        self.cm = metrics.confusion_matrix(self.y_test, self.Y_predictions)
        plt.figure(figsize=(9, 9))
        sns.heatmap(self.cm, annot=True, fmt=".3f", linewidths=.5, square=True, cmap='Blues_r')
        plt.ylabel('Actual label')
        plt.xlabel('Predicted label')
        self.all_sample_title = 'Accuracy Score: {0}'.format(self.score)
        plt.title(self.all_sample_title, size=15)
        plt.show()







