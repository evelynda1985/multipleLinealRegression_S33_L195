#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn
seaborn.set()


# In[4]:


data = pd.read_csv('L195MultipleLinearRegression.csv')


# In[5]:


data


# In[6]:


data.describe()


# In[7]:


y = data['GPA']
x1 = data[['SAT', 'Rand 1,2,3']]


# In[8]:


x = smd.add_constant(x1)
results = sm.OLS(y,x).fit()


# In[9]:


x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()


# In[10]:


results.summary()


# In[ ]:




