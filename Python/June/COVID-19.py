
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import sklearn.metrics
import joblib
import matplotlib.pyplot as plt

# Load the data

def readDataMulti():
#add the csv file to the current directory before proceeding
# read the CSV file
  global scaler
  global dictionary
  global colnames
   #path to the file in the current directory
  features = pd.read_csv('/kaggle/input/covid-flu-cold-symptoms/large_data.csv')                            #reading the file
  features = features.rename(columns={'TYPE' : 'class'})  #renaming the result column
  colnames=features.columns
  # Label Encoding refers to converting the labels into numeric form so as to convert it 
  # into the machine-readable form. 
  # Machine learning algorithms can then decide in a better way on how those labels must be operated
  label_encoder = LabelEncoder()                               
  features['class']= label_encoder.fit_transform(features['class']) #performing label encoding in the given column
  labels = features.pop('class')  #removing the class column from the features table
  keys = label_encoder.classes_  
  values = label_encoder.transform(label_encoder.classes_)
  dictionary = dict(zip(keys, values)) #storing the converted column entries as (key,value) pairs
  print(dictionary)
  X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.20,random_state=5)  #splitting the dataset into train and test set
  scaler = StandardScaler()
  scaler.fit(X_train)
  X_train = scaler.transform(X_train) 
  X_test = scaler.transform(X_test)
  return X_train,y_train, X_test, y_test
  