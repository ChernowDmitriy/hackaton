#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

from predict_model import predict

# In[2]:


d1 = pd.read_csv('data/1_houses.csv')
incidents, capitals = predict(d1[:1000])

# In[3]:


# получаем список PredictedEvents
incidents = incidents.rename(
    columns={'event': 'name', 'unom': 'unom_id', 'date': 'expected_date', 'length': 'expected_duration',
             'sys': 'organization'})[['unom_id', 'name', 'expected_date', 'expected_duration', 'organization']]
incidents.expected_duration = incidents.expected_duration.astype(int)
predicted_events = list(incidents.T.to_dict().values())
# получаем список PredictedMajorRepairs
capitals = \
    capitals.rename(
        columns={'event': 'name', 'unom': 'unom_id', 'date': 'expected_date', 'length': 'expected_duration'})[
        ['unom_id', 'name', 'expected_date', 'expected_duration']]
capitals.expected_duration = capitals.expected_duration.astype(int)
predicted_major_repairs = list(incidents.T.to_dict().values())


# # тебе нужны predicted_events & predicted_major_repairs
# print(predicted_major_repairs)
# print(predicted_events)


