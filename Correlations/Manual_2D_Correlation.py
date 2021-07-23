#!/usr/bin/env python
# coding: utf-8

# In[6]:


from numpy import mean
from numpy import std
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from pandas import DataFrame
import pandas as pd
from sklearn.linear_model import LinearRegression


# In[7]:


data1 = pd.read_csv('/home/schnablelab/Downloads/Manual_DataMedian60.csv')
data2 = pd.read_csv('/home/schnablelab/Downloads/PlantCV_DataMedian60.csv')
print(data1)
print(data2)


# In[18]:


r2 = []

#correlation between the median
correlation_matrix = np.corrcoef(data1['Median'], data2['Median'])

correlation_xy = correlation_matrix[0, 1]
r_squared = correlation_xy**2

r2.append(r_squared)

######################################################################################################################

r = []

#correlation between median
correlation_matrix = np.corrcoef(data1['Median'], data2['Median'])

correlation_xy = correlation_matrix[0, 1]
r_median = correlation_xy

r.append(r_median)

######################################################################################################################

r2 = round(r2[0],4)


# In[30]:


import seaborn as sns

df = plt.scatter(data1['Median'], data2['Median'])
plt.title('Correlation of Median Leaf Values', size = 19)
plt.text(16, 56, r2, fontsize=20)
plt.plot(data1['Median'], data2['Median'], 'o', color = 'blue')
plt.style.use('ggplot')
m, b = np.polyfit(data1['Median'], data2['Median'], 1)
plt.plot(data1['Median'], m*data1['Median'] + b)

sns.regplot(data1['Median'], data2['Median'], ci = 80, truncate=False)
plt.xlabel('2D Images', size = 18)
plt.ylabel('Manual', size = 18)


# In[5]:


r2


# In[6]:


r

