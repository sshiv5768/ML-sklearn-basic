import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

# ['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename']
diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

diabetes_Y_train = diabetes.target[:-30]
diabetes_Y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_Y_train)

diabetes_Y_predict = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_Y_test, diabetes_Y_predict))
print("Weight: ", model.coef_)
print("Intercept: ", model.intercept_)

# Below Mean squared error, Weight, Intercept when there are only one feature.
# Mean squared error is:  3035.0601152912695
# Weight:  [941.43097333]
# Intercept:  153.39713623331698
