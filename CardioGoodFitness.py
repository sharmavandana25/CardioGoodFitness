#!/usr/bin/env python
# coding: utf-8

# In[ ]:


CardioGoodFitness CaseStudy


# In[6]:


import numpy as np
import pandas as pd


# In[7]:


mydata = pd.read_csv("\\Users\Vandana Sharma\OneDrive\Desktop\python\CardioGoodFitness.csv")


# In[8]:


mydata.head()


# In[10]:


#Description of data
mydata.describe()  #it only considers numeric data
mydata.describe(include='all') #it considers all data including strings


# In[9]:


mydata.info()   #information of the data


# In[10]:


import matplotlib.pyplot as plt
 #plots to display inside the jupyter notbook
get_ipython().run_line_magic('matplotlib', 'inline')


# In[15]:


#creating histogram plots for data
mydata.hist(figsize=(20,30))


# In[12]:


#importing seaborn 
import seaborn as sns


# In[13]:


#Boxplots
sns.boxplot(x="Gender", y="Age", data=mydata)


# In[14]:


#crosstab
pd.crosstab(mydata['Product'],mydata['Gender'])


# In[15]:


pd.crosstab(mydata['Product'],mydata['MaritalStatus'])


# In[16]:


#Countplot
sns.countplot(x="Product", hue="Gender", data=mydata)


# In[17]:


#Pivottable
pd.pivot_table(mydata,index=['Product','Gender'], columns=['MaritalStatus'], aggfunc=len)


# In[18]:


pd.pivot_table(mydata,'Income',index=['Product','Gender'], columns=['MaritalStatus'])


# In[19]:


pd.pivot_table(mydata,'Miles',index=['Product','Gender'], columns=['MaritalStatus'])


# In[20]:


sns.pairplot(mydata)


# In[21]:


#Standard Deviation
Sd = mydata['Age'].std()
Sd


# In[22]:


#Mean
Mean = mydata['Age'].mean()
Mean


# In[24]:


#Histogram 
sns.displot(mydata['Age'])


# In[25]:


mydata.hist(by = 'Gender', column = 'Income')


# In[26]:


mydata.hist(by = 'Product', column = 'Miles')


# In[27]:


#Correlation with heat map
corr = mydata.corr()
corr


# In[28]:


sns.heatmap(corr,annot=True)


# In[ ]:





# In[ ]:




