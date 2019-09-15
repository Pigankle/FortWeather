#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:39:42 2019

@author: ami
"""


    # Load the Pandas libraries with alias 'pd' 
import pandas as pd
from dateutil.parser import parse 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})


    # Read data from file 'filename.csv' 
    # (in the same directory that your python process is based)
    # Control delimiters, rows, column names with read_csv (see later) 
df_all = pd.read_csv("output/All_Parsed_Data-multi.csv",  parse_dates=['dt'])
#df_all['dt'] = pd.to_datetime(df_all['dt'])
df_all.columns = df_all.columns.str.replace("[-]", "_")
df_all = df_all[['dt']+[c for c in df_all if c not in ['dt']]]
    # Preview the first 5 lines of the loaded data
#%%
start_date = '1861-10-01'
end_date = '1862-07-30'
mask = (df_all['dt'] > start_date) & (df_all['dt'] <= end_date)
df = df_all.loc[mask]


dataWalla       = df[df.stationName =='WA_Fort_Walla_Walla']
dataSacr        = df[df.stationName =='CA_Sacramento']
dataSanFran     = df[df.stationName =='CA_San_Francisco']
dataSanDiego    = df[df.stationName =='CA_San_Diego']
dataFtVanc      = df[df.stationName =='WA_Fort_Vancouver']
dataSteilacoom  = df[df.stationName =='WA_Fort_Steilacoom']

smalldf = dataFtVanc.head(100)
#%%
