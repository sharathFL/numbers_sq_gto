import numpy as np
import pandas as pd

# Generate synthetic data
X = np.linspace(0, 10, 100)
y = 2 * X + 1 + np.random.normal(0, 1, 100)

# Save to CSV
data = pd.DataFrame({'X': X, 'y': y})
data.to_csv('/code/data/data.csv', index=False)
