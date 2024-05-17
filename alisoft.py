#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(r'ds_salaries.csv')
df


# Data Wrangling

# Some Properties of dataset
# 

# In[3]:


print("Dimensions of DF: ", df.shape)


# In[4]:


print("\nInformation about DF: ")# print Information of DF
df.info()


# In[5]:


print("Head of DF: ") # First fifth rows of DF
df.head(5)


# information about the salary_in_usd of the work_your?
# 

# In[6]:


sns.kdeplot(df.salary_in_usd, color='red', shade='True');

plt.xlabel('salary_in_usd', fontsize = 13)

plt.ylabel('work_your', fontsize=13)



plt.show()


# Relationship between employee_residence and company_locatoin?
# 

# In[7]:


df.plot(x= 'salary_in_usd', y= 'remote_ratio' , kind='scatter', color = 'blue');


# Relationship between salry_in_usd and vote_salary_in_usd?
# 

# In[8]:


df.plot(x= 'salary', y= 'remote_ratio' , kind='scatter', color = 'red');


# information about the salary of the work_year?
# 

# In[9]:


plt.bar(df['work_year'],df['salary'])
plt.xlabel('work_your', fontsize=13)

plt.ylabel('salary', fontsize=13)
plt.show()


# In[ ]:




