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
from DT import decision_trees


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
    dt_model = decision_trees()

    # make the dataframe
    df = pd.read_csv('Input/dict.csv')
    # makesure numerical data is a number
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

    #runs the DT method
    dt_model.dt_model(df)

    log.info('Main done')

    pass
#

# %% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")

    # TEST Code
    main()