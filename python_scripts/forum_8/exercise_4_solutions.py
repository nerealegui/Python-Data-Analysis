# %% [markdown]
# ### Exercise 4
# 
# Using everything you have learned so far, try to get the best accuracy you can.
# 
# Save the best accuracy in a variable named `accuracy_ex4`. Post it in the forum discussion!

# %%
#data importing + selecting string columns

import pandas as pd

data = pd.read_csv("HR-Employee-Attrition.csv")

data.head()

# Create new features
data['JobSatisfaction_EnvironmentSatisfaction'] = data['JobSatisfaction'] + data['EnvironmentSatisfaction']
data['Education_StockOptionLevel'] = data['Education'] * data['StockOptionLevel']
data['YearsInCurrentRole_PerformanceRating'] = data['YearsInCurrentRole'] * data['PerformanceRating']
data['Age_MonthlyIncome'] = data['Age'] * data['MonthlyIncome']
data['YearsWithCurrManager_RelationshipSatisfaction'] = data['YearsWithCurrManager'] + data['RelationshipSatisfaction']
data['YearsInCurrentRole_YearsSinceLastPromotion'] = data['YearsInCurrentRole'] - data['YearsSinceLastPromotion']

new_features = ['JobSatisfaction_EnvironmentSatisfaction', 'Education_StockOptionLevel', 'YearsInCurrentRole_PerformanceRating', 'Age_MonthlyIncome', 'YearsWithCurrManager_RelationshipSatisfaction', 'YearsInCurrentRole_YearsSinceLastPromotion']

# %%
# separate the data into x and y
x = data.drop('Attrition', axis=1)
y = data['Attrition']

# check for columns that are strings in x
string_categorical_columns_x = x.select_dtypes(include=['object']).columns

string_categorical_columns_x

# check for columns that are strings
string_categorical_columns = data.select_dtypes(include=['object']).columns

# %%
# label encoding

from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()

x_le = x.copy()

for column in string_categorical_columns_x:
    x_le[f'{column}_le'] = label_encoder.fit_transform(data[column])

x_le = x_le.drop(string_categorical_columns_x, axis=1) #drop original categorical columns to keep only their encoded version

x_le.head()

# %%
# train test split, using 30% of the data for testing
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x_le, y, test_size=0.3, random_state=42)

print(x_train.shape)
print(y.shape)


# %%
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# %%
# instantiate the model DecisionTreeClassifier
tree = DecisionTreeClassifier(random_state=42)

# train the model
tree.fit(x_train, y_train)

# make predictions
y_pred = tree.predict(x_test)

# calculate the accuracy
baseline_ex4_accuracy_decisiontree = accuracy_score(y_test, y_pred)

print(f'Accuracy: {baseline_ex4_accuracy_decisiontree}')

# %%
# instantiate the model RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier


tree = RandomForestClassifier()

tree.fit(x_train, y_train)

# make predictions
y_pred = tree.predict(x_test)

# calculate the accuracy
baseline_ex4_accuracy_randomforest = accuracy_score(y_test, y_pred)


print(f'Accuracy: {baseline_ex4_accuracy_randomforest}')


# %%
# feature importance
importances = tree.feature_importances_

feature_importances = pd.DataFrame(importances, index=x_le.columns, columns=['importance'])

feature_importances = feature_importances.sort_values(by='importance', ascending=False)

import plotly.express as px

fig = px.bar(feature_importances, x=feature_importances.index, y='importance')
fig.show()
# %%
