import numpy as np
import pandas as pd


X = np.array([
        [3, 3],
        [7,3],
        [-5,2],
        [-1,-1],
        [-1,1],
        [0,-2],
        [-1,-2]
    ])
Y = np.array([1,1,-1,-1, -1, 1, 1])

theta = np.array([0,0]).astype(np.float32)

k = 0
eta = 0.5
deltaTheta = 10
while (k < 1000 and np.linalg.norm(deltaTheta) > 0.1):
    shuffler = np.random.permutation(len(X)) 
    Y = Y[shuffler]
    X = X[shuffler]
    for x in range(len(X)):
        if (np.dot(Y[x], np.dot(X[x], theta)) < 1):
            oldTheta = theta.astype(np.float32)
            theta += np.dot(eta, np.multiply(Y[x], X[x]))
            deltaTheta = np.linalg.norm(np.subtract(oldTheta, theta))
            print()
            print("k=" + str(k))
            print("theta: " + str(np.around(theta, decimals=2)))
            print("deltaTheta: " + str(np.around(deltaTheta, decimals=2)))
            k += 1
            eta = 0.5 / (k+1)

print()
print("ANSWER:")
print(theta)
print("k=" + str(k))
