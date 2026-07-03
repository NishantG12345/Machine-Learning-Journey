import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# create random dataset and add noise using default_rng and normal
rng = np.random.default_rng(seed = 10)
x = rng.uniform(0,15,5)
noise = rng.normal(loc = 0,scale = 1, size = 5)
y = np.sin(x) + noise

poly = PolynomialFeatures(degree = 15)
x = x.reshape(-1,1)
x_pred = poly.fit_transform(x)
lin = LinearRegression()
lin.fit(x_pred, y)
y_pred = lin.predict(x_pred)

plt.scatter(x,y, c = 'red', label = '5 Points')
plt.plot(x_pred,y_pred,c='blue', label = 'Polynomial Fit') 
plt.title('x vs y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

if __name__ == "__main__":
    main()







