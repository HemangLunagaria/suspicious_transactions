#!/usr/bin/env python
# coding: utf-8

# # Visual Data Analysis of Fraudulent Transactions
# 
# Your CFO has also requested detailed trends data on specific card holders. Use the starter notebook to query your database and generate visualizations that supply the requested information as follows, then add your visualizations and observations to your markdown report.

# In[1]:


# Initial imports
import pandas as pd
import calendar
import plotly.express as px
import hvplot.pandas
from sqlalchemy import create_engine


# In[4]:


# Create a connection to the database
engine = create_engine("postgresql://postgres:FinTechSQL@localhost:5432/fraud_detection")


# ## Data Analysis Question 1
# 
# The two most important customers of the firm may have been hacked. Verify if there are any fraudulent transactions in their history. For privacy reasons, you only know that their cardholder IDs are 2 and 18.
# 
# * Using hvPlot, create a line plot representing the time series of transactions over the course of the year for each cardholder separately. 
# 
# * Next, to better compare their patterns, create a single line plot that containins both card holders' trend data.  
# 
# * What difference do you observe between the consumption patterns? Does the difference suggest a fraudulent transaction? Explain your rationale in the markdown report.

# In[26]:


# loading data for card holder 2 and 18 from the database
# Write the query
query = "SELECT cardholder_id as cardholder, date as hour,amount FROM \"transaction\" t INNER JOIN credit_card c ON c.card = t.card WHERE c.cardholder_id IN (2,18)"
# Create a DataFrame from the query result. HINT: Use pd.read_sql(query, engine)

data = pd.read_sql(query, engine)
data.head()


# In[29]:


# Plot for cardholder 2
data.loc[data['cardholder'] == 2].hvplot.line(x="hour",y="amount")


# In[31]:


# Plot for cardholder 18
data.loc[data['cardholder'] == 18].hvplot.line(x="hour",y="amount", color="red")


# In[33]:


# Combined plot for card holders 2 and 18
data.hvplot.line(x="hour",y="amount", by="cardholder")


# ## Data Analysis Question 2
# 
# The CEO of the biggest customer of the firm suspects that someone has used her corporate credit card without authorization in the first quarter of 2018 to pay quite expensive restaurant bills. Again, for privacy reasons, you know only that the cardholder ID in question is 25.
# 
# * Using Plotly Express, create a box plot, representing the expenditure data from January 2018 to June 2018 for cardholder ID 25.
# 
# * Are there any outliers for cardholder ID 25? How many outliers are there per month?
# 
# * Do you notice any anomalies? Describe your observations and conclusions in your markdown report.

# In[56]:


# loading data of daily transactions from jan to jun 2018 for card holder 25
# Write the query
query_2 = """
SELECT EXTRACT(MONTH from date) as month,EXTRACT(DAY FROM date) as day, amount
FROM "transaction" t
INNER JOIN credit_card c
ON c.card = t.card
WHERE c.cardholder_id IN (25)
ORDER BY c.cardholder_id,t.date"""
# Create a DataFrame from the query result. HINT: Use pd.read_sql(query, engine)
data_2 = pd.read_sql(query_2, engine)
data_2.head()


# In[57]:


# loop to change the numeric month to month names
data_2 = data_2.astype({'month': 'int32'})
data_2['month_name'] = data_2['month'].apply(lambda x: calendar.month_name[x])
data_2 = data_2.drop(['month'], axis=1)
data_2 = data_2.rename(columns={'month_name' : 'month'})
data_2


# In[65]:


# Creating the six box plots using plotly express
px.box(data_2.loc[data_2['month'].isin(['January', 'February', 'March', 'April', 'May', 'June'])],x='month',y="amount",color="month")


# In[ ]:




