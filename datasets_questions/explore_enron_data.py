#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# 数据集中有多少数据点（人）？
people_number = len(enron_data)

# 对于每个人，有多少个特征可用？
featrues = len(enron_data['GLISAN JR BEN F'])

# E+F 数据集中有多少 POI？
cnt = 0
for key, value in enron_data.items():
	if value['poi']:
		cnt = cnt + 1

poi = cnt
