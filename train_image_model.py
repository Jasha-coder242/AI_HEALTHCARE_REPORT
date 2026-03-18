import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier

# Simple training data (brightness feature)
X = np.array([
    [50],
    [80],
    [120],
    [150],
    [200],
    [230]
])

y = [
    "Disease",
    "Disease",
    "Normal",
    "Normal",
    "Normal",
    "Normal"
]

model = DecisionTreeClassifier()
model.fit(X,y)

pickle.dump(model,open("image_model.pkl","wb"))

print("Model created successfully")