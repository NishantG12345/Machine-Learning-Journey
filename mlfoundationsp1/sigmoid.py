import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))
def binary_crossentropy(y,p):
    #use clipping to prevent np.log(0), keeps values within this range
    loss = 0
    y_pred = np.clip(p,1e-15,1-1e-15)
    loss = -(y*np.log(y_pred) + (1-y)*np.log(1-y_pred))
    return np.mean(loss)
def main():
    y = np.array([1.0,0.0])
    p = np.array([0.99,0.01])
    p_bad = np.array([0.01, 0.99])
    print(binary_crossentropy(y,p))
    print(binary_crossentropy(y,p_bad))
if __name__ == "__main__":
    main()