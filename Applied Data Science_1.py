# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:22:26 2023

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:20:30 2023

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data= pd.read_csv('financials.csv')
data
data.isnull().sum()
data= data.drop(['Symbol','SEC Filings'], axis="columns")
data= data.sort_values(by=['Price'], ascending=False)
data
data.columns
data.head()
def line():
    plt.figure()
    plt.plot(data['Name'][:20],data['52 Week Low'][:20],color= 'red',label='Low')
    plt.plot(data['Name'][:20],data['52 Week High'][:20], color='blue',label='High')
    plt.xlabel(' Company Name' )
    plt.ylabel('Price in GBP')
    plt.legend()
    plt.title('Highest and Lowest price in last 52 weeks of top 20 companies')
    plt.xticks(rotation=90)
    plt.show()         
def barplot():
    plt.figure()
    plt.bar(data['Name'][:10], data['Price/Earnings'][:10])
    plt.xlabel('Company Name' )
    plt.ylabel('Price in GBP')
    plt.title('Price/Earnings of top 10 companies')
    plt.xticks(rotation=90)
    plt.show()  
def hist():
    plt.figure()
    plt.hist(data['Price'],bins=30)
    plt.title("Distribution of price")
    plt.xlabel('Companies Share Price' )
    plt.ylabel('Number of Companies')
    plt.show()    
line()
barplot()   
hist()
