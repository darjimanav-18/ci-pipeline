import sys
from sklearn.linear_model import LinearRegression
import pickle


model=LinearRegression()

x=[[1], [2], [3]]
y=[2, 4,6]

model.fit(x, y)

predict=model.predict([[4.0]])
print(predict)
