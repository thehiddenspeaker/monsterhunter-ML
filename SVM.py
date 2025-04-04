# %% MODULE BEGINS
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
from   matplotlib import pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC
from Stats import Stats
import pandas as pd


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

    def svm_model(self, dataframe, column1, column2, output='Output/svm_graph.pdf'):
        log.info('svm_model started')

        try:

            dTrn, dVal, dTst = Stats.dataSplit(dataframe)

            # x needs to be 2 values, y is the truth values
            x = dTrn[[column1, column2]].values
            y = dTrn['element_hidden']  # Ensure column name is correct

            # Build the model
            svm_model = SVC(kernel="rbf", gamma=0.5, C=1.0, class_weight="balanced")

            # Train the model
            svm_model.fit(x, y)

            # Plot Decision Boundary
            DecisionBoundaryDisplay.from_estimator(
                svm_model,
                x,
                response_method="predict",
                cmap=plt.cm.Spectral,
                alpha=0.8
            )

            # Scatter plot
            plt.scatter(dTrn[column1], dTrn[column2], c=y, s=20, edgecolors="k")
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.savefig(output)
            plt.close()

            # Test the model
            dTst = dTst.reset_index(drop=True)

            temp = svm_model.predict(dTst[[column1, column2]].values)

            # Create a DataFrame for predictions
            prediction = pd.DataFrame(temp, columns=['Predicted'])

            # Add the actual truth values from dTst (make sure element_hidden exists in dTst)
            prediction['Truth'] = dTst['element_hidden'].copy()

            #caluclate stats
            Stats.calculate_confusion_matrix(prediction, 'Predicted', 'Truth',
                                             output= 'Output/SVM_confusion_matrix.pdf',
                                             pm_output='Output/performance_matrix/SVM_PM.csv')


        except Exception as e:
            log.error(f"Error in svm_model: {e}")

        log.info('svm_model finished')
