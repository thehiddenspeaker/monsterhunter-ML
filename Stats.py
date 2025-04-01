# %% MODULE BEGINS
module_name = 'Stats'

'''
Version: 1

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
import numpy
from sklearn import metrics
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
class Stats:

    def calculate_confusion_matrix(self, dataframe, predicted, actual = 'hidden_element',
                                   plot = True, output = 'Output/scatter_plot.pdf', skip_to_pm = True ):
        try:
            log.info('calculate_confusion_matrix started')

            confusion_matrix = metrics.confusion_matrix(dataframe[actual], dataframe[predicted])

            if plot:
                cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=[0, 1])

                cm_display.plot()
                plt.savefig(output)
                plt.close()
            #

            if skip_to_pm:
                self.calculate_performance_measures(confusion_matrix)
            #
            log.info('calculate_confusion_matrix started finished')
        except:
            log.error('calculate_confusion_matrix crashed')




    def calculate_performance_measures(self, confusion_matrix):
        try:
            log.info('calculate_performance_measures started')
            tn, fp, fn, tp = confusion_matrix.ravel()

            sensitivity = tp / (tp + fn)
            specificity = tn / (tn + fp)
            accuracy = (tp + tn) / (tp + tn + fp + fn)
            precision = tp / (tp + fp)
            f1 = 2 * (precision * sensitivity) / (precision + sensitivity)

            return sensitivity, specificity, accuracy, f1
        except:
            log.error('calculate_performance_measures crashed')


