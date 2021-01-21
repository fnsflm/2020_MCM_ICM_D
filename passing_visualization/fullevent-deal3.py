#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

# In[2]:


data = pd.read_csv('fullevents.csv')
data = data.dropna(subset=['EventOrigin_x', 'EventOrigin_y', 'EventDestination_x', 'EventDestination_y'])
data_pass0 = pd.read_csv('passingevents.csv')


# In[3]:


# def get_pass_fill(data1, data_pass):
#     data_pass_fill = {}
#     j = 0
#     for i in range(len(data_pass) - 1):
#         t1 = data_pass.index[i]
#         t2 = data_pass.index[i + 1]
#         t = data1.index[j]
#         while t < t1:
#             j += 1
#             t = data1.index[j]
#         while t1 <= t < t2:
#             xx1 = data1['EventOrigin_x'][t1]
#             yy1 = data1['EventOrigin_y'][t1]
#             xx2 = data1['EventOrigin_x'][t2]
#             yy2 = data1['EventOrigin_y'][t2]
#             # if t == t1:
#             #     data_pass_fill['from_x']=xx1
#             #     data_pass_fill['from_y']=yy1
#             #     # data_pass_fill['to_x']=xx2
#             #     # data_pass_fill['to_y']=yy2
#             # else:
#             data_pass_fill[t] = [0, 0]
#             data_pass_fill[t][0] = xx1 + (xx2 - xx1) * (t - t1) / (t2 - t1)
#             data_pass_fill[t][1] = yy1 + (yy2 - yy1) * (t - t1) / (t2 - t1)
#             j += 1
#             t = data1.index[j]
#     return data_pass_fill
def get_pass_fill(data_pass):
    data_pass_fill = {}
    for i in range(len(data_pass)-1):
        t1 = data_pass.index[i]
        t2 = data_pass.index[i+1]
        xx11 = data_pass['EventOrigin_x'][t1]
        xx12 = data_pass['EventDestination_x'][t1]
        yy11 = data_pass['EventOrigin_y'][t1]
        yy12 = data_pass['EventDestination_y'][t1]
        xx21 = data_pass['EventOrigin_x'][t2]
        # xx22 = data_pass['EventDestination_x'][t2]
        yy21 = data_pass['EventOrigin_y'][t2]
        # yy22 = data_pass['EventDestination_y'][t2]
        data_pass_fill[t1]=[xx11,yy11]
        if xx12!=xx21 or yy12!=yy21:
            data_pass_fill[(t1+t2)/2]=[xx12,yy12]
    xx22 = data_pass['EventDestination_x'][t2]
    yy22 = data_pass['EventDestination_y'][t2]
    data_pass_fill[t2]=[xx22,yy22]
    return data_pass_fill
# In[4]:


shadow = 5
colordic = dict(zip(data['EventType'].unique(), sns.color_palette(n_colors=len(data['EventType'].unique())).as_hex()))
patches = [mpatches.Patch(label=i, color=colordic[i]) for i in colordic.keys()]


def gen_pic(data1, matchid, matchperiod, shadow=5):
    shals_hu = []
    shals_opp = []
    # passls = []     # 五个点
    data1_hu = data1[data1['TeamID'] == 'Huskies']
    data1_opp = data1[data1['TeamID'] != 'Huskies']
    data_pass = data_pass0[data_pass0['MatchID'] == matchid]
    data_pass = data_pass[data_pass['MatchPeriod'] == matchperiod].set_index('EventTime')
    data_pass_fill = get_pass_fill( data_pass)
    print(data_pass_fill)
    pass_wnd = []
    pas_idx = iter(data_pass_fill.keys())
    for i in data1.index:
        plt.clf()
        plt.figure(figsize=(9, 6))
        if i in data1_hu.index:
            shals_hu.append(i)
            if len(shals_hu) >= shadow:
                shals_hu = shals_hu[1:]
        for j in shals_hu:
            xx1 = data1_hu['EventOrigin_x'][j]
            xx2 = data1_hu['EventDestination_x'][j]
            yy1 = data1_hu['EventOrigin_y'][j]
            yy2 = data1_hu['EventDestination_y'][j]
            plt.scatter([xx1, xx2], [yy1, yy2], c='black')
            # plt.plot([data1_hu['EventOrigin_x'][j],data1_hu['EventDestination_x'][j]],[data1_hu['EventOrigin_y'][j],data1_hu['EventDestination_y'][j]],
            #          c=colordic[data1_hu['EventType'][j]])
            plt.arrow(xx1, yy1, xx2 - xx1, yy2 - yy1, fc=colordic[data1_hu['EventType'][j]], width=1.2,
                      length_includes_head=True)
            # print(shals_hu)
        if i in data1_opp.index:
            shals_opp.append(i)
            if len(shals_opp) >= shadow:
                shals_opp = shals_opp[1:]
        for j in shals_opp:
            xx1 = data1_opp['EventOrigin_x'][j]
            xx2 = data1_opp['EventDestination_x'][j]
            yy1 = data1_opp['EventOrigin_y'][j]
            yy2 = data1_opp['EventDestination_y'][j]
            plt.scatter([xx1, xx2], [yy1, yy2],
                        c='w', edgecolors='black')
            # plt.plot([data1_opp['EventOrigin_x'][j],data1_opp['EventDestination_x'][j]],[data1_opp['EventOrigin_y'][j],data1_opp['EventDestination_y'][j]],
            #          c=colordic[data1_opp['EventType'][j]])
            plt.arrow(xx1, yy1, xx2 - xx1, yy2 - yy1,
                      fc=colordic[data1_opp['EventType'][j]],
                      width=1.2,length_includes_head=True)
        # if data1['EventType'][i]=='Pass':
        #     xx1=data1['EventOrigin_x'][i]
        #     xx2=data1['EventDestination_x'][i]
        #     yy1=data1['EventOrigin_y'][i]
        #     yy2=data1['EventDestination_y'][i]
        #     flag=False
        #     for j in passls:
        #         if xx1==j[0] and yy1==j[1]:
        #             flag=True
        #             break
        #     if flag:
        #         passls.append((xx2,yy2))
        #     else:
        #         passls.append((xx1,yy1))
        #         passls.append((xx2,yy2))
        #     if len(passls)>5:
        #         passls=passls[-5:]
        # for j in range(len(passls)-1):
        #     plt.arrow(passls[j][0],passls[j][1],passls[j+1][0]-passls[j][0],passls[j+1][1]-passls[j][1],
        #               fc=colordic['Pass'],width=3,length_includes_head=True,alpha=0.3)
        # if i in data_pass.keys():
        #     pass_wnd.append(i)
        #     if len(pass_wnd) > shadow:
        #         pass_wnd = pass_wnd[1:]
        if len(pass_wnd) == 0:
            pass_wnd.append(next(pas_idx))
            # pass_wnd.append(next(pas_idx))
        if i >= max(pass_wnd):
            try:
                pass_wnd.append(next(pas_idx))
            except StopIteration:
                print("end_pass")
            if len(pass_wnd) > shadow:
                pass_wnd = pass_wnd[-shadow:]
        for j in range(len(pass_wnd) - 1):
            p1 = data_pass_fill[pass_wnd[j]]
            p2 = data_pass_fill[pass_wnd[j + 1]]
            # p1 = [data_pass['EventOrigin_x'][pass_wnd[j]], data_pass['EventOrigin_y'][pass_wnd[j]]]
            # p2 = [data_pass['EventOrigin_x'][pass_wnd[j + 1]], data_pass['EventOrigin_y'][pass_wnd[j + 1]]]
            plt.arrow(p1[0], p1[1], p2[0] - p1[0], p2[1] - p1[1],
                      fc=colordic['Pass'], width=3, length_includes_head=True, alpha=0.3)
        print(i,pass_wnd)
        plt.xlim(0, 110)
        plt.ylim(0, 110)
        plt.title("time=%.2f" % i)
        plt.subplots_adjust(right=0.6)
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 0), loc=3)
        plt.savefig('imgs/%d_%s/%d_%s_%07.2f.jpg' % (matchid, matchperiod, matchid, matchperiod, i))
    print(matchperiod)


# In[5]:


for i in data['MatchID'].unique():
    data1=data[data['MatchID']==i]
    gen_pic(data1[data1['MatchPeriod']=='1H'].set_index('EventTime'),i,'1H',shadow)
    gen_pic(data1[data1['MatchPeriod']=='2H'].set_index('EventTime'),i,'2H',shadow)
# data1 = data[data['MatchID'] == 1]
# gen_pic(data1[data1['MatchPeriod'] == '1H'].set_index('EventTime'), 1, '1H', shadow)

# In[ ]:


import cv2
import os


# fourcc=cv2.VideoWriter_fourcc(*"mp4v")
def img_to_video(matchid, matchperiod):
    fps = 2
    perfix = '%d_%s' % (matchid, matchperiod)
    video = cv2.VideoWriter('videos/' + perfix + '.mp4', cv2.VideoWriter_fourcc(*"mp4v"), fps, (900, 600))
    for i in sorted(os.listdir('imgs/' + perfix)):
        if i.find('jpg') == -1:
            continue
        image = cv2.imread('imgs/' + perfix + '/' + i)
        # print(image)
        video.write(image)
        # print("ok")
    video.release()


# cv2.waitKey()


# In[ ]:


for i in data['MatchID'].unique():
    img_to_video(i,'1H')
    img_to_video(i,'2H')
# img_to_video(1, '1H')

# In[ ]:


# f = plt.figure()
# f.get_size_inches()

# In[ ]:

