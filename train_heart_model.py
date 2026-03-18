import numpy as np
import pickle
from sklearn.tree import DecisionTreeClassifier

# Training dataset
X = np.array([
[25,110,170,70],
[30,120,180,75],
[35,125,190,80],
[45,140,220,120],
[50,150,240,150],
[60,160,260,170]
])

# 0 = Low Risk
# 1 = High Risk
y = [0,0,0,1,1,1]

model = DecisionTreeClassifier()

model.fit(X,y)

with open("heart_model.pkl","wb") as f:
    pickle.dump(model,f)

print("Heart model saved successfully")