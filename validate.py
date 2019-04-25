from sklearn.trees import DecisionTreeRegressor

dtr = DecisionTreeRegressor()
def validate(x_test):
	y_pred = dtr.predict(x_test)
	return y_pred

print(validate(x_test))