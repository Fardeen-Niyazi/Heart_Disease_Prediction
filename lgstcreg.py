# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 12:12:25 2020

@author: FARDEEN
"""
# Basic
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

import joblib
df = pd.read_csv(r'C:\Users\FARDEEN\Desktop\ML Model and Dataset\HealthData.csv')
X = df.iloc[:,:-1].values
y = df.iloc[:, 13].values


from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer=imputer.fit(X[:,11:13])
X[:,11:13]=imputer.transform(X[:,11:13])



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

lr = LogisticRegression()
lr.fit(X_train,y_train)
acc = lr.score(X_test,y_test)*100
print(acc)

x= sc.transform([[63,1,3,145,233,1,0,150,0,2.3,0,0,1]])#1
ynew = lr.predict(x)
print(ynew)


x= [[51,0,0,130,305,0,1,142,1,1.2,1,0,3]]#0
x = sc.transform(x)
ynew = lr.predict(x)
print(ynew)

x =sc.transform([[44,1,0,110,197,0,0,177,0,0,2,1,2]])#0
print(lr.predict_proba(x))

x = [[63,0,0,150,407,0,0,154,0,4.0,1,3,3]]#0
print(lr.predict_proba(x))

w = sc.transform([[67,1,4,120,229,0,2,129,1,2.6,2,2,7]])#1
print(lr.predict(w))


z = sc.transform([[60,1,4,130,206,0,2,132,1,2.4,2,2,7]])#1
print(lr.predict(z))
filename = 'scaler.sav'
joblib.dump(sc,filename)