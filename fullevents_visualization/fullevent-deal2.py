#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


data = pd.read_csv('fullevents.csv',index_col='EventTime')
data = data.dropna(subset=['EventOrigin_x','EventOrigin_y','EventDestination_x','EventDestination_y'])
data1=data[data['MatchID']==1]

data1_hu=data1[data1['TeamID']=='Huskies']
data1_opp=data1[data1['TeamID']!='Huskies']


# In[6]:


shadow=5
shals_hu=[]
shals_opp=[]
for i in data1.index:
    if i in data1_hu.index:
        plt.clf()
        shals_hu.append(i)
        if len(shals_hu) >= shadow:
            shals_hu = shals_hu[1:]
        for j in shals_hu:
            plt.plot([data1_hu['EventOrigin_x'][j],data1_hu['EventDestination_x'][j]],[data1_hu['EventOrigin_y'][j],data1_hu['EventDestination_y'][j]],c='b')
        print(shals_hu)
    # if i in data1_opp.index:
    plt.pause(0.01)


# In[ ]:




