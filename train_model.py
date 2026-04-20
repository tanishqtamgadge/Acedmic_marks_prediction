import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Realistic synthetic data
data = {
    'Hours': [1, 2, 2.5, 3, 3.5, 4, 5, 5.5, 6, 7, 8, 8.5, 9, 10],
    'Marks': [15, 22, 28, 35, 40, 48, 55, 62, 70, 78, 88, 92, 95, 99]
}

df = pd.DataFrame(data)

# Train the model
X = df[['Hours']]
y = df['Marks']
model = LinearRegression()
model.fit(X, y)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model trained and saved as model.pkl")