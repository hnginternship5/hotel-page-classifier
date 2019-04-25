from sklearn.trees import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
dtr = DecisionTreeRegressor()
def validate(x_test):
	y_pred = dtr.predict(x_test)
	print('*' * 20)
	print("Mean Squared Error: ")
	mse = mean_squared_error(y_test, y_pred)

	return y_pred, mse

print(validate(x_test))
