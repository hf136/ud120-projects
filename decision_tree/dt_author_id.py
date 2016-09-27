#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
## your code goes here ###
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
score = accuracy_score(labels_test, pred)
### accuracy_score: 0.990329920364  (min_samples_split=2)
### accuracy_score: 0.977246871445  (min_samples_split=40)
### 1%Ê±£¬accuracy_score: 0.967007963595
print "accuracy_score:",score

### features number
print "features number:",len(features_train[0])


#########################################################


