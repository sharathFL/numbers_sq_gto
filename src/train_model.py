import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Load data
data = pd.read_csv('/code/data/data.csv')
X = data[['X']]
y = data['y']

# Train model
model = LinearRegression()
model.fit(X*3, y)

# Save model
joblib.dump(model, 'model.joblib')
