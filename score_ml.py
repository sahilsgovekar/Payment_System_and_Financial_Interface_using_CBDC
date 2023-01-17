import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

class Generate_Score :
    def __init__(self, c_debt, c_credit, c_score):
        self.c_debt = c_debt
        self.c_credit = c_credit
        self.c_score = c_score

    def loadDataset(self):
        self.dataset = pd.read_csv('scores.csv')
        self.X = self.dataset.iloc[:, 1:-1].values
        self.y = self.dataset.iloc[:, -1].values
    
    def getScore(self):
        regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
        regressor.fit(self.X, self.y)
        regressor.predict([[6.5]])