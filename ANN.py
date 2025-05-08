# %% MODULE BEGINS
from sklearn.metrics import roc_curve

module_name = 'ANN'

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
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# other imports
from Stats import Stats
from copy import deepcopy as dpcpy

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
class ANN():
    def model(self, data):
        st = Stats()
        train, val, test = st.dataSplit(data)
        X_train = train.iloc[:,[2,5,6,8]]
        Y_train = train.iloc[:,-1].values
        X_val = val.iloc[:,[2,5,6,8]]
        X_test = test.iloc[:,[2,5,6,8]]
        Y_val = val.iloc[:,-1].values
        Y_test = test.iloc[:,-1].values
        LE1 = LabelEncoder()
        Y_train = np.array(LE1.fit_transform(Y_train))
        ann = tf.keras.models.Sequential()
        ann.add(tf.keras.layers.Dense(units=6, activation="relu"))
        ann.add(tf.keras.layers.Dense(units=6, activation="relu"))
        ann.add(tf.keras.layers.Dense(units=1, activation="sigmoid"))
        ann.compile(optimizer="adam", loss="binary_crossentropy", metrics=['accuracy'])
        history = ann.fit(X_train, Y_train, batch_size=32, epochs=50)
        pred_value = ann.predict(X_val)
        return(history)
# Function definitions Start Here