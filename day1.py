import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
print(matplotlib.get_backend()) 

#used to populate a random number of integers/uniform

rng = np.random.default_rng(seed = 35)
x = rng.uniform(low = 0, high = 50, size = 100) 

#add normal noise
noise = rng.normal(loc = 0,scale = 1, size = 100)
y = 3 * x + 2 + noise

slope,intercept = np.polyfit(x, y, deg = 1)
y_new = slope * x + intercept
plt.xlabel(xlabel = "x")
plt.ylabel(ylabel = "y")
plt.title("Plotting noisy and fitted data")
plt.plot(x, slope*x+intercept, color = 'black')
plt.scatter(x,y, c = 'red', label = "points")
plt.scatter(x,y_new, c = 'blue', label = "fitted points")
plt.legend()
plt.show(block=True)
