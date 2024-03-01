import pandas as pd
import numpy as np

# Load the data
data = pd.read_csv('heart_disease_data.csv')

# Drop missing values
data.dropna(inplace=True)

# Encode categorical variables
data = pd.get_dummies(data, columns=['gender', 'smoker', 'heart_disease'])

# Scale numerical variables
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
data[['age', 'blood_pressure', 'cholesterol']] = scaler.fit_transform(data[['age', 'blood_pressure', 'cholesterol']])
