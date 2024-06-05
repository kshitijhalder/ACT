"""
KNN - K Nearest Neighbors Algorithm
        - It is a simple, easy-to-implement supervised machine learning algorithm that can be 
        used to solve both classification and regression problems. 
        - It is a non-parametric method used for classification and regression.
        
Date : 25-05-2024
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
import seaborn as sns
import matplotlib.pyplot as plt

# import data set: iris 

# data set: iris
# Call excel file
os.system('clear')
df = pd.read_excel('/Users/kshitijhalder/Desktop/ACT/Python/May/StudentInfo.xlsx')
#print(df)

# Extract input
x = df.iloc[:, 1:4]
#print(x)

# Extract output
y = df.iloc[:, 4]
#print(y)

z = df.iloc[:, 1:2]
#print(z)

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=0)

# Print the training and testing sets
#print("X train: \n",x_train)
#print("Y train: \n",y_train)
#print("X test: \n",x_test)
print("Y test: \n",y_test)

# Create a random forest classifier
clf = RandomForestClassifier(n_estimators=100)

# Train the classifier
clf.fit(x_train, y_train)

# Predict the output
y_pred = clf.predict(x_test)
#print(y_pred)

# Print the accuracy
accuracy = clf.score(x_test, y_test)
#print(f'Accuracy: {accuracy}')

# Create a KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn.fit(x_train, y_train)

# Predict the output
y_pred = knn.predict(x_test)
print("Y Pred: ",y_pred)

# Print the accuracy
accuracy = knn.score(x_test, y_test)
print(f'Accuracy: {accuracy}')

# Print the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Matrix\n",conf_matrix)

# Print the confusion matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(conf_matrix, annot=True, cmap='Blues', xticklabels=knn.classes_, yticklabels=knn.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
#plt.show()

# Print the classification report
class_report = classification_report(y_test, y_pred)
print("Class report: \n",class_report)

# Save the model
import joblib                # type: ignore
import pickle
joblib.dump(knn, '/Users/kshitijhalder/Desktop/ACT/Python/May/StudentInfo.pkl')
with open('/Users/kshitijhalder/Desktop/ACT/Python/May/StudentInfo.pkl', 'rb') as file:
    object = pickle.load(file)
    print(object)
