#!/usr/bin/env python
# coding: utf-8

# # Challenge
# 
# Another approach to identifying fraudulent transactions is to look for outliers in the data. Standard deviation or quartiles are often used to detect outliers. Using this starter notebook, code two Python functions:
# 
# * One that uses standard deviation to identify anomalies for any cardholder.
# 
# * Another that uses interquartile range to identify anomalies for any cardholder.
# 
# ## Identifying Outliers using Standard Deviation

# In[1]:


# Initial imports
import pandas as pd
import numpy as np
import random
from sqlalchemy import create_engine


# In[2]:


# Create a connection to the database
engine = create_engine("postgresql://postgres:FinTechSQL@localhost:5432/fraud_detection")


# In[22]:


# Write function that locates outliers using standard deviation
def calc_anomalies_using_standard_deviation(cardholders):
    query = "SELECT cardholder_id as cardholder, date as hour,amount FROM \"transaction\" t INNER JOIN credit_card c ON c.card = t.card ORDER BY amount"
    df = pd.read_sql(query,engine)
    data = df.loc[df['cardholder'].isin(cardholders)]
    mean = np.mean(data['amount'], axis=0)
    sd = np.std(data['amount'], axis=0)
    return data[(data['amount'] < (mean - 2 * sd)) | (data['amount'] > (mean + 2 * sd))]


# In[23]:


# Find anomalous transactions for 3 random card holders
anamalous_transactions = calc_anomalies_using_standard_deviation([2,18,25])
anamalous_transactions


# ## Identifying Outliers Using Interquartile Range

# In[20]:


# Write a function that locates outliers using interquartile range
def calc_median(df):
    median = 0
    if len(df) % 2 == 0:
        amount_1 = df[:int(len(df)/2)].iloc[[-1]]['amount'].values[0]
        amount_2 = df[int(len(df)/2) + 1 :].iloc[[0]]['amount'].values[0]
        median = (amount_1 + amount_2) / 2
    else:
        median = df[:int(len(df)/2)].iloc[[-1]]['amount'].values[0]
    return median

def calc_anomalies_using_interquartile(cardholders):
    query = "SELECT cardholder_id as cardholder, date as hour,amount FROM \"transaction\" t INNER JOIN credit_card c ON c.card = t.card ORDER BY amount"
    df = pd.read_sql(query,engine)
    data = df.loc[df['cardholder'].isin(cardholders)]
    data_q1 = data[:int(len(data)/2)]
    data_q3 = data[int(len(data)/2) + 1 :] 
    q1 = calc_median(data_q1)
    q2 = calc_median(data)
    q3 = calc_median(data_q3)
    interquartile_inner = (q3 - q1) * 1.5
    interquartile_outer = (q3 - q1) * 3
    innerfence = [q1 - interquartile_inner, q3 + interquartile_inner]
    outerfence = [q1 - interquartile_outer, q3 + interquartile_outer]
    return data[(data['amount'] < outerfence[0]) | (data['amount'] > outerfence[1])]


# In[21]:


# Find anomalous transactions for 3 random card holders
data = calc_anomalies_using_interquartile([2,18,25])
    
data

