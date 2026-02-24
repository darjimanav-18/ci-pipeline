import sys
from sklearn.linear_model import LinearRegression
import pickle


model=LinearRegression()

x=[[1], [2], [3]]
y=[2, 4,6]

model.fit(x, y)

predict=model.predict([[4.0]])
print(predict)
if abs(predict-8.0)<.1:
    print("Prediction sucessfully done")
    sys.exit(1)
else:
    print("Prediction Failed")
    sys.exit(1)