# %% MODULE BEGINS
from sklearn.neighbors import KNeighborsClassifier

module_name = 'KNN'

'''
Version: 1

Description:
    <***>

Authors:
    Brennan Kimbrell
    Trent Law

Date Created     :  3/31/2025
Date Last Updated:  3/31/2025

Doc:
    <***>

Notes:
    <***>
'''

# %% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    import os
    # os.chdir("./../..")
#

# custom imports
from Stats import Stats

# other imports
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from copy import deepcopy as dpcpy
import numpy as np

'''
from   matplotlib import pyplot as plt
import mne
import numpy  as np 
import os
import pandas as pd
import seaborn as sns
'''


# %% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Global declarations Start Here


# Class definitions Start Here
class knn:
    def __innit__(self):
        pass
    def knnClassifier(self, dataframe, col1, col2, target,  output = 'Output/knn_graph.pdf'):
        k = 1
        accuracies = []
        splitter = Stats()
        train, val, test = splitter.dataSplit(dataframe)
        while k < len(train):
            model = KNeighborsClassifier(n_neighbors=k)
            X_train = train[[col1,col2]]
            Y_train = train[target]
            model.fit(X_train,Y_train)
            X_val = val[[col1,col2]]
            Y_val = val[target]
            val_preds = model.predict(X_val)
            tn, fp, fn, tp = confusion_matrix(Y_val, val_preds).ravel()
            accuracy = accuracy_score(Y_val, val_preds)
            accuracies.append(accuracy)
            k +=1
        best_k = np.argmax(accuracies) + 1  # add 1 k starts 1 so index will be off otherwise
        best_model = KNeighborsClassifier(n_neighbors=best_k)
        best_model.fit(train[[col1,col2]], train[target])
        X_test = test[[col1, col2]]
        Y_test = test[target]
        test_preds = best_model.predict(X_test)
        tn, fp, fn, tp = confusion_matrix(Y_test, test_preds).ravel()

        accuracy = accuracy_score(Y_test, test_preds)
        sensitivity = tp / (tp + fn)
        specificity = tn / (tn + fp)
        f1 = f1_score(Y_test, test_preds)

        performance_measures = {
            'accuracy': accuracy,
            'sensitivity': sensitivity,
            'specificity': specificity,
            'f1_score': f1
        }

        confusionmatrix = {'tn': tn, 'fp': fp, 'fn': fn, 'tp': tp}


        return performance_measures, confusionmatrix
        pass


