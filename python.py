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


# # Data Wrangling

# Some Properties of dataset

# In[3]:


print("Dimensions of DF: ", df.shape)


# In[4]:


print("\nInformation about DF: ")# print Information of DF
df.info()


# In[5]:


print("Head of DF: ") # First fifth rows of DF
df.head(5)


# # Exploratory Data Analysis
# 
what was the max of all employees salary_in_usd ?(2020-2023)?

# In[7]:


df.groupby('salary_in_usd').max()


# Relationship between salary and experience level
# 

# In[10]:


sns.boxplot(x='experience_level', y='salary_in_usd', data=df)
plt.title('Salary Distribution by Experience Level')
plt.xlabel('Experience Level')
plt.ylabel('Salary (USD)')
plt.xticks(rotation=45)
plt.show()


# Relationship between salary and company size
# 

# In[11]:


sns.scatterplot(x='company_size', y='salary_in_usd', data=df)
plt.title('Salary vs Company Size')
plt.xlabel('Company Size')
plt.ylabel('Salary (USD)')
plt.xticks(rotation=45)
plt.show()


# information about the salary of the work_your?
# 

# In[14]:


sns.kdeplot(df.salary,color='green',shade=True) 
plt.xlabel('salary', fontsize=13)
plt.ylabel('work_your', fontsize=13)
plt.show()


# Information about the salary currency and average of the salary?
# 

# In[16]:


fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2);

# Plot violin plot on axes 1
ax1.violinplot(df.salary_in_usd, showmedians=True)
ax1.set_title('salary_in_usd')
ax1.set_xticks([1])

# Plot violin plot on axes 2
ax2.violinplot(df.salary, showmedians=True)
ax2.set_title('salary')
ax2.set_xticks([1])


plt.show()


# In[ ]:




