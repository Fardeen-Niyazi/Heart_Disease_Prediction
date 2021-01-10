
import numpy as np
import pandas as pd
import joblib
dataset = pd.read_csv(r'C:\Users\FARDEEN\Desktop\ML Model and Dataset\HealthData.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:, 13].values


#handling missing data

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer=imputer.fit(X[:,11:13])
X[:,11:13]=imputer.transform(X[:,11:13])



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15, random_state = 0)

from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dtree.fit(X_train, y_train)

# Predicting the Test set results
print(dtree.score(X_test,y_test))
filename = 'decision.sav'
joblib.dump(dtree,filename)
