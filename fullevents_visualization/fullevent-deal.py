#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# In[2]:


data = pd.read_csv('fullevents.csv',index_col='EventTime')
data = data.dropna(subset=['EventOrigin_x','EventOrigin_y','EventDestination_x','EventDestination_y'])
data1=data[data['MatchID']==1]


# In[3]:


data1_hu=data1[data1['TeamID']=='Huskies']
data1_opp=data1[data1['TeamID']!='Huskies']


# In[4]:


shadow=5
shals_hu=[]
shals_opp=[]
# 
# fig, ax = plt.subplots()
# fig.xlim(0,max(max(data1['EventDestination_x']),max(data1['EventOrigin_x'])))
# fig.ylim(0,max(max(data1['EventDestination_y']),max(data1['EventOrigin_y'])))
# # ax.scatter(data1_hu['EventOrigin_x'].iloc[0],data1_hu['EventOrigin_y'].iloc[0],c='b')
# # ax.scatter(data1_opp['EventOrigin_x'].iloc[0],data1_opp['EventOrigin_y'].iloc[0],c='r')
# pre_index=data1.index[0]
# for i in data1.index:
#     if i in data1_hu.index:
#         if len(shals_hu)<5:
#             shals_hu.append(i)
#         else:
#             shals_hu.append(i)
#             shals_hu = shals_hu[1:]
#         print(shals_hu)
#         for j in shals_hu:
#             ax.arrow(data1_hu['EventOrigin_x'][j],data1_hu['EventOrigin_y'][j],
#                      data1_hu['EventDestination_x'][j]-data1_hu['EventOrigin_x'][j],
#                      data1_hu['EventDestination_y'][j]-data1_hu['EventOrigin_y'][j],fc='b')
#     if i in data1_opp.index:
#         if i in data1_hu.index:
#             if len(shals_opp)<5:
#                 shals_opp.append(i)
#             else:
#                 shals_opp.append(i)
#                 shals_opp = shals_opp[1:]
#             for j in shals_hu:
#                 ax.arrow(data1_opp['EventOrigin_x'][j],data1_opp['EventOrigin_y'][j],
#                          data1_opp['EventDestination_x'][j]-data1_opp['EventOrigin_x'][j],
#                          data1_opp['EventDestination_y'][j]-data1_opp['EventOrigin_y'][j],fc='r')
#     print(i-pre_index + 0.0001)
#     plt.pause((i-pre_index+ 0.0001)/10)
#     pre_index=i


# In[5]:


# fig=plt.subplots()
# # line1 = ax.plot([],[],c='b')
# # line2 = ax.plot([],[],c='r')
# def update(i):
#     global shals_hu,shals_opp,pre_index
#     if i in data1_hu.index:
#         if len(shals_hu)<5:
#             shals_hu.append(i)
#         else:
#             shals_hu.append(i)
#             shals_hu = shals_hu[1:]
#         print("shals_hu",shals_hu)
#         # line1.set_xdata(data1_hu[''])
#         for j in shals_hu:
#             ax.arrow(data1_hu['EventOrigin_x'][j],data1_hu['EventOrigin_y'][j],
#                      data1_hu['EventDestination_x'][j]-data1_hu['EventOrigin_x'][j],
#                      data1_hu['EventDestination_y'][j]-data1_hu['EventOrigin_y'][j],fc='b')
#     if i in data1_opp.index:
#         if len(shals_opp)<5:
#             shals_opp.append(i)
#         else:
#             shals_opp.append(i)
#             shals_opp = shals_opp[1:]
#         print("shals_opp",shals_opp)
#         for j in shals_opp:
#             ax.arrow(data1_opp['EventOrigin_x'][j],data1_opp['EventOrigin_y'][j],
#                      data1_opp['EventDestination_x'][j]-data1_opp['EventOrigin_x'][j],
#                      data1_opp['EventDestination_y'][j]-data1_opp['EventOrigin_y'][j],fc='r')
    # print(i-pre_index + 0.0001)
    # plt.pause((i-pre_index+ 0.0001)/10)
    # pre_index=i
    # return fig,ax


# In[6]:


fig = plt.figure()
# fig,ax = plt.subplots()
def update(i):
    global shals_hu,shals_opp
    if i in data1_hu.index:
        # arr1 = plt.arrow(
        #         data1_hu['EventOrigin_x'][i],data1_hu['EventOrigin_y'][i],
        #              data1_hu['EventDestination_x'][i]-data1_hu['EventOrigin_x'][i],
        #              data1_hu['EventDestination_y'][i]-data1_hu['EventOrigin_y'][i],fc='b')
        arr1,=plt.plot([data1_hu['EventOrigin_x'][i],data1_hu['EventDestination_x'][i]],[data1_hu['EventOrigin_y'][i],data1_hu['EventDestination_y'][i]],c='b')
        shals_hu.append(arr1)
        if len(shals_hu) >= shadow:
            shals_hu = shals_hu[1:]
        print(shals_hu)
    if i in data1_opp.index:
        # arr2=plt.arrow(data1_opp['EventOrigin_x'][i],data1_opp['EventOrigin_y'][i],
        #              data1_opp['EventDestination_x'][i]-data1_opp['EventOrigin_x'][i],
        #              data1_opp['EventDestination_y'][i]-data1_opp['EventOrigin_y'][i],fc='r')
        arr2,= plt.plot([data1_opp['EventOrigin_x'][i],data1_opp['EventDestination_x'][i]],[data1_opp['EventOrigin_y'][i],data1_opp['EventDestination_y'][i]],c='r')
        shals_opp.append(arr2)
        if len(shals_opp) >= shadow:
            shals_opp = shals_opp[1:]
        print(shals_opp)
    return tuple(set(shals_opp).union(set(shals_hu)))
anim = FuncAnimation(fig, update, frames=data1.index, interval=200)
anim.save('./1.mp4')


# In[7]:


plt.show()


# In[8]:


# for i in data1.index:
#     if i not in data1_hu.index and i not in data1_opp.index:
#         print(False)

