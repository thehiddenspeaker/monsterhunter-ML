# %% MODULE BEGINS
module_name = 'DT'

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
from config import log

# other imports
from copy import deepcopy as dpcpy
from   matplotlib import pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC
import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import numpy as np
# %% USER INTERFACE              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONSTANTS                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% CONFIGURATION               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% INITIALIZATIONS             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# %% DECLARATIONS                ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Global declarations Start Here


# Class definitions Start Here
class decision_trees():

    def dt_model(self, dataframe):

        try:

            log.info('dt model started')
            #filling NaN
            dataframe = dataframe.fillna(0)

            #convert strings into numbers
            elderseal_map = {0 : 0,'low' : 1, 'average': 2, 'high':3}
            dataframe['elderseal'] = dataframe['elderseal'].map(elderseal_map)

            damageType_map = {'sever' : 1, 'blunt' : 2, 'projectile': 3}
            dataframe['damageType'] = dataframe['damageType'].map(damageType_map)

            element_type_map = { 0:0, 'fire':1 , 'water': 2, 'thunder':3,
                                'ice':4, 'dragon':5, 'poison': 6,
                                'paralysis':7, 'sleep':8, 'blast':9}
            dataframe['element_type'] = dataframe['element_type'].map(element_type_map)

            element_hidden_map = {True : 1, False: 0}
            dataframe['element_hidden'] = dataframe['element_hidden'].map(element_hidden_map)


            #splits the data
            dTrn, dVal, dTst = Stats.dataSplit(dataframe)

            features = ['elderseal', 'rarity', 'damageType', 'attack_display',
                        'attack_raw', 'element_type', 'element_damage']
            x1 = dTrn[features]
            y1 = dTrn['element_hidden']


            # Train Decision Tree
            dtree = DecisionTreeClassifier(class_weight=None, random_state=42)
            dtree = dtree.fit(x1, y1)

            plt.figure(figsize=(50, 25), dpi=400)  # Even larger image
            tree.plot_tree(dtree, feature_names=features, class_names=True, filled=True, rounded=True)
            plt.savefig("Output/decision_tree.png", dpi=400, bbox_inches="tight")  # Save for better readability
            plt.close()

        except Exception as e:
            log.error(f'Error in dt model: {str(e)}')
        pass
