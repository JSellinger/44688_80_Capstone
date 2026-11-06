
#import stuff here

import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd
import numpy as np

#Setting my dataset as the default

def kaggle_data_pull(dataset_file: str, dataset_url: str = "shashwatwork/dataco-smart-supply-chain-for-big-data-analysis") -> pd.DataFrame:
    """
    Pulls a specific dataset file from Kaggle and loads it into a Pandas DataFrame.
    
    :param dataset_file: Filename within the Kaggle dataset (e.g., 'DataCoSupplyChainDataset.csv')
    :return: pd.DataFrame
    """

    #This is the url of twhere the kaggle data lives
    
    df = kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS, 
        dataset_url,
        #This is the actual dataset file that it loads in - in this case the DataCo CSV 
        dataset_file
    )
    print("Dataset pulled succesffully")
    return df


kaggle_data_pull()