import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os
print(os.listdir())

# Sample dataset
data = pd.read_csv("dataset.csv")

X = data[['PM2.5', 'PM10', 'NO2','co1']]
y = data['AQI']

model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)