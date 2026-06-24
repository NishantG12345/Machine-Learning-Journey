import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self, epochs=100, learning_rate = 0.0001):
        self.w = 0 
        self.b = 0
        self.allcost = []
        self.epoch = epochs
        self.learning_rate = learning_rate

    def computeCost(self, x, y):
        n = len(x)
        sum = 0
        for i in range(n):
            y_pred = self.w * x[i] + self.b
            sum += (y[i] - y_pred) ** 2
        cost = sum / n
        self.allcost.append(cost)
        return cost
    def numOfEpochs(self):
        return self.epoch

    def gradientDescent(self, x,y):
        n = len(x)
        sum_b = 0
        sum_w = 0
        for i in range(n):
            y_pred = self.w * x[i] + self.b
            sum_b += (y[i] - y_pred)
            sum_w += x[i]*(y[i] - y_pred)
        dj_db = (-2/n)* sum_b
        dj_dw = (-2/n)* sum_w
        self.b = self.b - self.learning_rate * dj_db
        self.w = self.w - self.learning_rate * dj_dw
        return dj_db, dj_dw
        
    def fit(self, x, y):
        for i in range(self.epoch):
            self.computeCost(x,y)
            self.gradientDescent(x,y)
        
    def predict(self,x):
        return self.w * x + self.b
       
def main():
    rng = np.random.default_rng(seed = 35)
    x = rng.uniform(low = 0, high = 50, size = 100) 
    sortedx = np.argsort(x)
    noise = rng.normal(loc = 0,scale = 1, size = 100)
    y = 3 * x + 2 + noise
    model = LinearRegression()
    epochs = model.numOfEpochs()
    model.fit(x,y)
    y_pred = model.predict(x)
    print(model.w)
    print(model.b)
    epoch_arr = np.arange(1,epochs+1)
    plt.plot(epoch_arr,model.allcost)
    plt.xlabel('epochs')
    plt.ylabel('cost history')
    plt.title('Cost Decay Over Time')
    plt.show()

if __name__ == "__main__":
    main()

