# %% MODULE BEGINS
module_name = 'main'

'''
Version: 1

Description:
    <***>

Authors:
    Brennan Kimbrell
    Trent Law 

Date Created     :  3/27/2025
Date Last Updated:  3/27/2025

Doc:
    <***>

Notes:
    <***>
'''

# %% IMPORTS                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    pass
    # os.chdir("./../..")
#

# custom imports
from config import log
from graphs import Graphs
from SVM import svm


# other imports
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
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


# Function definitions Start Here
def main():
    log.info('Main started')

    #object creation
    graphs = Graphs()
    svm_model = svm()

    # make the dataframe
    df = pd.read_csv('Input/dict.csv')
    # makesure mumerical data is a number
    df[['id', 'rarity', 'attack_display', 'attack_raw', 'element_damage']] = \
        df[['id', 'rarity', 'attack_display', 'attack_raw', 'element_damage']].apply(pd.to_numeric,
                                                                                     errors='coerce')
    # runs the counter plot
    graphs.counter_plot(df, 'elderseal', 'elder seal', 'Output/counter_plot_elderseal.pdf')
    graphs.counter_plot(df, 'rarity', 'rarity', 'Output/counter_plot_rarity.pdf')
    graphs.counter_plot(df, 'damageType', 'Damage Type', 'Output/counter_plot_damageType.pdf')
    graphs.counter_plot(df, 'element_type', 'element type', 'Output/counter_plot_element_type.pdf')
    graphs.counter_plot(df, 'element_hidden', 'element hidden', 'Output/counter_plot_element_hidden.pdf')

    # runs the scatter plot
    graphs.scatter_plot(df, 'attack_raw', 'attack_display', 'damage', 'Output/scatter_plot_damage.pdf')

    #runs the SVM method
    svm_model.svm_model(df,'attack_display', 'attack_raw')

    log.info('Main done')

    pass


#
#dataSplit requires input file destination, with editable ratios, and returns 3 dataframes with split data
def dataSplit(file, pRatio = (0.6,0.2,0.2)):
    df = pd.read_csv(file)
    dTrn = pd.DataFrame()
    dVal = pd.DataFrame()
    dTst = pd.DataFrame()

    dTrn, temp_df = train_test_split(df, test_size=(1 - pRatio[0]))
    dVal, dTst = train_test_split(temp_df, test_size=pRatio[1] / (pRatio[1] + pRatio[2]))


    # Combine all classes back together

    return dTrn, dVal, dTst
    pass
# %% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code start here


# %% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")

    # TEST Code
    main()