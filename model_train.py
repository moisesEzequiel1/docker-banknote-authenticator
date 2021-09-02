"""
Bank Note Authentication
Data were extracted from images that were taken from genuine and forged banknote
like specimens. For digitization, an industrial camera usually used for print 
inspection was used. The final images have 400x 400 pixels. Due to the object 
lens and distance to the investigated object gray-scale pictures with a 
resolution of about 660 dpi were gained. Wavelet Transform tool were used to 
extract features from images.
"""

import numpy as np
import pandas as pd

dataset = pd.read_csv('BankNote_Authentication.csv')

print(dataset.head())


#Adjusting the dataset

X = dataset.iloc[:, :-1]
y = dataset.iloc[:,-1]

#print('\n', X.head())
#print('\n', y.head())

###Tranform  the dataset in X_train, X_test, y_train, y_test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=0)
print(X_train)
#Implement RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier()
classifier.fit(X_train, y_train)


#Predicition
y_pred = classifier.predict(X_test)

#Check Accuaracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_test, y_pred)

print('\n',score)
#Create a pickle file using serialization
import pickle
pickle_out = open("classifier.pkl", "wb")
pickle.dump(classifier, pickle_out)
pickle_out.close()



