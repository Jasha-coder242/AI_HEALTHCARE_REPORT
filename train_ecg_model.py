import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Sample ECG dataset
X = np.array([
    [0.85],
    [0.92],
    [0.76],
    [0.65],
    [1.02],
    [0.70],
    [0.88]
])

y = [
    "Normal",
    "Normal",
    "Abnormal",
    "Abnormal",
    "Normal",
    "Abnormal",
    "Normal"
]

model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("ecg_model.pkl", "wb"))

print("ECG model created successfully")