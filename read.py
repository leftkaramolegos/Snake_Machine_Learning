import numpy as np
import pandas as pd
import random
import time
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.externals import joblib

class Util():

    @staticmethod
    def sanitizeMapInstance(mapp):
        list =[]
        for i in mapp:
            if(i > 0 and i < 1):
                i = 1
            elif(i == 1):
                i = 2
            list.append(int(i))
        return list

class Instance():
    """docstring for Instance"""
mapInstance = []
action = 0


class TrainingData():
    """docstring for TrainingData"""
actionArray = []
instanceArray = []

for x in range(3):
    filePath = 'action' + str(x) + '.log'
    with open(filePath) as fp:
        linesList = list(fp)
        # if(x == 1):
        #     linesList = linesList[:len(linesList)//2]
        for line in linesList:
            results = [float(i) for i in line.split(',')]
            instanceArray.append(results)
            actionArray.append(x)
print('Data collected')
xTrain = instanceArray
yTrain = actionArray
kfold = model_selection.KFold(n_splits=10, random_state=20)
model = RandomForestClassifier(bootstrap=True, class_weight='balanced_subsample',
	        max_features='auto', max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_samples_split=3, n_estimators=100, n_jobs=4,
            oob_score=True, random_state=0, verbose=0, warm_start=False)
results = model_selection.cross_val_score(model, xTrain,yTrain, cv=kfold)
model.fit(xTrain,yTrain)
print('Model trained')

filename = 'snakeModel.sav'
joblib.dump(model, filename)
print('Model saved')
# print(xTrain[0])
# while True:#for i in range(1000):
#     # start_time = time.time()
#     n = None
#     n = input("Enter your value: ") 
#     print(n)
#     xTest = []
#     # index = random.randint(0,len(instanceArray) - 1)
#     a = None
#     a = [float(i) for i in n.split(',')]
#     print(a)
#     # a.append(n.strip())
#     xTest.append(a)
#     print(xTest)
#     predicted=model.predict(xTest)
#     score = model.predict_proba(xTest)
#     # elapsed_time = time.time() - start_time
#     # print(elapsed_time)
#     print(predicted[0])
#     print(score1)
#     print(score2)
