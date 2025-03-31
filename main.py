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
import pandas as pd

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

# %% MAIN CODE                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main code start here


# %% SELF-RUN                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main Self-run block
if __name__ == "__main__":
    print(f"\"{module_name}\" module begins.")

    # TEST Code
    main()