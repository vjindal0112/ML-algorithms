import numpy as np
import pandas as pd


X = np.array([
        [3, 3],
        [7,3],
        [-5,2],
        [-1,-1],
        [-1,1]
    ])
Y = np.array([1,1,-1,-1, -1])

theta = [0,0]

misclassified = True
k = 0
while (misclassified):
    misclassified = False
    #shuffler = np.random.permutation(len(X)) # you do not need shuffling for perceptron
    #Y = Y[shuffler]
    #X = X[shuffler]
    for x in range(len(X)):
        if ((Y[x] * np.dot(X[x], theta)) <= 0):
            theta += np.multiply(Y[x], X[x])
            print(k)
            print(theta)
            k += 1
            misclassified = True

print()
print("ANSWER:")
print(theta)
print("k=" + str(k))
