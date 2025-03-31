# %% MODULE BEGINS
from matplotlib.pyplot import ylabel

module_name = 'SVM'

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
from config import log

# other imports
from copy import deepcopy as dpcpy
from   matplotlib import pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC


'''
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
class svm:

    def svm_model(self, dataframe, column1, column2, output ='Output/svm_graph.pdf'):
        log.info('svm_model started')
        try:
            #x needs to be 2 values. y is the Truth values
            x = dataframe[[column1, column2]].values
            y = dataframe['element_hidden']

            # Build the model
            svm_model = SVC(kernel="rbf", gamma=0.5, C=1.0, class_weight="balanced")

            # Trained the model
            svm_model.fit(x, y)

            # Plot Decision Boundary
            DecisionBoundaryDisplay.from_estimator(
                svm_model,
                x,
                response_method="predict",
                cmap=plt.cm.Spectral,
                alpha=0.8,
                xlabel= column1,
                ylabel= column2,
            )


            # Scatter plot
            X,Y = dataframe[column1], dataframe[column2]
            plt.scatter(X, Y,
                        c=y,
                        s=20, edgecolors="k")
            plt.savefig(output, format='pdf')
            plt.close()

        except:
            log.info('Error in svm_model')

        log.info('svm_model finished')