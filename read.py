import numpy as np
import pandas as pd
import random
from datetime import datetime
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

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
        print(len(list(fp)))
        for cnt, line in enumerate(fp):
            strResults = [x.strip() for x in line.split(',')]
            results = [float(x) for x in line.split(',')]
            instanceArray.append(results)
            actionArray.append(x)
print(len(actionArray))

 xTrain = instanceArray
 yTrain = actionArray
 kfold = model_selection.KFold(n_splits=15, random_state=10)
 model = RandomForestClassifier(n_estimators=100, max_features=5)
 results = model_selection.cross_val_score(model, xTrain,yTrain, cv=kfold)
 model.fit(xTrain,yTrain)
 xTest = []
 for x in range(1000):
     xTest = []
     index = random.randint(0,len(instanceArray) - 1)
     xTest.append(instanceArray[index])#[[0,0.98,0.99,1.00, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
     print(yTrain[index])
     predicted=model.predict(xTest)
     print(predicted[0])
     if(predicted[0] != yTrain[index]):
         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
