#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[34]:


df = pd.read_csv('箱ひげ図.csv')
df.head()


# In[46]:


points = df.values
# points = df['なし'].values
# points = df[df['なし'] > 4]['なし'].values
# points = df.loc[:,'38':].values

fig, ax = plt.subplots()
bp = ax.boxplot(points)
plt.ylim([0,60])
plt.grid()
plt.show()


# In[ ]:




