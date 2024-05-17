#!/usr/bin/env python
# coding: utf-8

# #  Mohamed Omran Part 
# 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r"C:\Users\1\Desktop\ds_salaries.csv")
df


# # Data Cleaning
# 

# In[3]:


df.isnull()


# In[4]:


df.isnull().sum()


# In[7]:


print("Current Number of Column", df.shape[1])  # Number of column (in advance)


# In[8]:


print("Current Number of rows", df.shape[0])  # Number of rows (in advance)


# In[9]:


df.duplicated()


# In[10]:


df.duplicated().sum()


# In[ ]:





# In[ ]:




