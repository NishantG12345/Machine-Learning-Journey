import numpy as np 

def train_val_test_split(X,y):
    #return a numpy array of indices
    indices = np.random.permutation(X.shape[0])
    #shuffle x and y because data could be ordered and make sure the x indices match with the y
    X_shuffled = X[indices]
    Y_shuffled = y[indices]
#splicing [:] for rows [:, : ] columns if you put just a : it will do all 
#remember to slice from 0 - 70, 70-85, 85- 100
    X_train = X_shuffled[:int(0.7 * len(X_shuffled))] 
    Y_train = Y_shuffled[:int(0.7 * len(Y_shuffled))]

    X_val = X_shuffled[int(0.7 * len(X_shuffled)): int(0.85 * len(X_shuffled))] 
    Y_val = Y_shuffled[int(0.7 * len(X_shuffled)): int(0.85 * len(X_shuffled))]

    X_test = X_shuffled[int(0.85 * len(X_shuffled)):] 
    Y_test = Y_shuffled[int(0.85 * len(X_shuffled)):]

    assert (len(np.intersect1d(X_train, X_val))) == 0
    assert (len(np.intersect1d(X_train, X_test))) == 0
    assert (len(np.intersect1d(X_test, X_val))) == 0

    return X_train, X_val, X_test, Y_train, Y_val, Y_test

def main():
    rng = np.random.default_rng(seed = 22)
    X = rng.uniform(low = 1, high = 100, size = (100,3))
    y = rng.uniform(low = 10, high = 1000, size = (100,) )
    X_train, X_val, X_test, Y_train, Y_val, Y_test = train_val_test_split(X,y)
    print(X_train.shape)
    print(X_val.shape)
    print(X_test.shape)
    print(Y_train.shape)
    print(Y_val.shape)
    print(Y_test.shape)

if __name__ == "__main__":
    main()
