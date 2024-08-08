import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
data = pd.read_csv('data/data.csv')
X = data[['X']]
y = data['y']

# Train model with a slight modification
model = LinearRegression()
# model.fit(X, y)
model.fit(X*X*X*X*X*X*X*X*X*X*3*X*X*X*X,y)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)

# Save model
joblib.dump(model, 'models/wip_1_model.joblib')