# %% MODULE BEGINS
module_name = 'graphs'

'''
Version: 1

Description:
    Used to make simple graphs of out data 

Authors:
    Brennan Kimbrell
    Trent Law 

Date Created     :  3/26/2025
Date Last Updated:  3/26/2025

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
import seaborn as sns
import pandas as pd
'''
from copy import deepcopy as dpcpy
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

class Graphs:
    def scatter_plot(self, dataframe, column1, column2, user_title, output ='Output/scatter_plot.pdf'):
        log.info("scatter plot start")
        try:
            dataframe.plot.scatter(column1, column2, title= user_title)
            plt.savefig(output)
        #
        except:
            print('error, make sure the column you gave only have number values.')
            log.error("scatter plot code crashed")
        #
        log.info("scatter plot finished")
    # end of scatter plot method

    def counter_plot(self, dataframe, column1, user_title, output ='Output/counter_plot.pdf'):
        log.info('counter plot started')
        try:
            dataframe = dataframe.dropna(subset=[column1])
            ax = sns.countplot(x = column1, data= dataframe)

            for p in ax.patches:
                ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x() + 0.25, p.get_height() + 0.01))

            plt.title(user_title)

            # turns graph into pdf
            plt.savefig(output)
            plt.close()
            log.info("counter plot ended")
        except:
            log.error("counter code crashed")
