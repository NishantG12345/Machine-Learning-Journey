import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
def f(x):
        return x ** 4 -  3 * x**3 + 2
def d_f(x):
        return 4 * x ** 3 - 9 * x ** 2
def gradient_descent(x,learning_rate, epochs = 10):
        #it's more efficient to use a regular array since numpy creates a new array everytime
        try:
            arr = [x]
            for _ in range(epochs):
                x -= (d_f(x) * learning_rate)
                arr.append(x)
                if(abs(x) > 1e5):
                      break
        except OverflowError:
              print("too large")
        return np.array(arr)
def main():
    x = 3
    lr1 = 0.001
    lr2 = 0.1
    #lr3 = 2.0
    x1 = gradient_descent(x,lr1)
    x2 = gradient_descent(x,lr2)
    #x3 = gradient_descent(x,lr3)
    f_x1 = f(x1)
    f_x2 = f(x2)
   # f_x3 = f(x3)
    plt.scatter(x1,f_x1, c = 'red', label = '0.001')
    plt.scatter(x2,f_x2, c = 'blue', label = '0.1')
   # plt.scatter(x3,f_x3, c = 'black', label = '2.0')
    plt.title('x vs f(x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    main()

