import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier


# Disease model
X_disease = np.array([
[1,1,1],
[1,0,1],
[0,1,0],
[1,1,0]
])

y_disease = ["Flu","Cold","Healthy","Viral Fever"]

disease_model = DecisionTreeClassifier()
disease_model.fit(X_disease,y_disease)

pickle.dump(disease_model, open("disease_model.pkl","wb"))

print("Models created successfully")