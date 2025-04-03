# %% MODULE BEGINS
module_name = 'Stats'

'''
Version: 1.2

Description:
    <***>

Authors:
    Brennan Kimbrell
    Trent Law 

Date Created     :  4/1/2025
Date Last Updated:  4/1/2025

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
import matplotlib.pyplot as plt
from sklearn import metrics
import pandas as pd
from sklearn.model_selection import train_test_split



# %% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Global declarations Start Here


# Class definitions Start Here
class Stats:

    @staticmethod
    def dataSplit(dataframe, pRatio=(0.6, 0.2, 0.2)):
        """ Splits the dataset into training, validation, and test sets. """
        try:
            dTrn, temp_df = train_test_split(dataframe, test_size=(1 - pRatio[0]))
            dVal, dTst = train_test_split(temp_df, test_size=pRatio[1] / (pRatio[1] + pRatio[2]))

            return dTrn, dVal, dTst

        except Exception as e:
            log.error(f"Error in dataSplit: {e}")
            return None, None, None  # Return None values if an error occurs

    @staticmethod
    def calculate_confusion_matrix(dataframe, predicted, actual='hidden_element',
                                   plot=True, output='Output/confusion_matrix.pdf', skip_to_pm=True, pm_output=None):
        """ Computes and optionally plots the confusion matrix. """
        try:
            log.info('calculate_confusion_matrix started')

            confusion_matrix = metrics.confusion_matrix(dataframe[actual], dataframe[predicted])

            if plot:
                cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0, 1])
                cm_display.plot()
                plt.savefig(output)
                plt.close()

            if skip_to_pm:
                return Stats.calculate_performance_measures(confusion_matrix, output= pm_output)  # Fixed call

            log.info('calculate_confusion_matrix finished')

        except Exception as e:
            log.error(f'calculate_confusion_matrix crashed: {e}')
            return None  # Return None if an error occurs

    @staticmethod
    def calculate_performance_measures(confusion_matrix, output = 'Output/performance_matrix/PM.csv'):
        """ Calculates sensitivity, specificity, accuracy, precision, and F1-score. """
        try:
            log.info('calculate_performance_measures started')

            tn, fp, fn, tp = confusion_matrix.ravel()

            sensitivity = tp / (tp + fn)
            specificity = tn / (tn + fp)
            accuracy = (tp + tn) / (tp + tn + fp + fn)
            precision = tp / (tp + fp)
            f1 = 2 * (precision * sensitivity) / (precision + sensitivity)

            log.info(f"Performance Metrics - Sensitivity: {sensitivity}, Specificity: {specificity}, "
                     f"Accuracy: {accuracy}, Precision: {precision}, F1-score: {f1}")

            results = pd.DataFrame([{
                "Sensitivity": sensitivity,
                "Specificity": specificity,
                "Accuracy": accuracy,
                "Precision": precision,
                "F1-Score": f1
            }])

            results.to_csv(output)

            return sensitivity, specificity, accuracy, precision, f1

        except Exception as e:
            log.error(f'calculate_performance_measures crashed: {e}')
            return None, None, None, None, None  # Return None values if an error occurs