''' 
3x3 기반 forward propagation, backpropagation 구현이다
'''

import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# inputs
I = np.array([0.9, 0.1, 0.8])
# [Weights] inputs -> hidden layer
W1 = np.array([[0.9, 0.3, 0.4], [0.2, 0.8, 0.2], [0.1, 0.5, 0.6]])
# [Weights] hidden layer -> outputs
W2 = np.array([[0.3, 0.7, 0.5], [0.6, 0.5, 0.2], [0.8, 0.1, 0.9]])

'''Forwardpropagation'''
X_hidden = np.dot(W1, I)
array_a = sigmoid(X_hidden)
X_output = np.dot(W2, array_a)
output = np.around(sigmoid(X_output), 3)

print("forward propagation output: {}".format(output))

'''Backpropagation'''
answer = np.array([0.8, 0.9, 0.9])
print("answer : {}".format(answer))
output_error = np.round((answer - output),3)
print(output_error)

W1_T = W1.transpose()
print("tranpose W1: \n{}".format(W1_T))
W2_T = W2.transpose()
print("tranpose W2: \n{}".format(W2_T))

# Error_Hidden layer
E_h = np.array([])

# Calculation error
for  i in range(3):
    w = 0
    for j in range(3):
        w_sum = np.sum(W2[j])
        w += output_error[j]*(W2_T[i][j]/w_sum)
    E_h = np.append(E_h, np.round(w, 3))

print("Hidden layer's errors: \n{}".format(E_h))

# Error_Input layer
E_i = np.array([])

# Calculation error
for  i in range(3):
    w = 0
    for j in range(3):
        w_sum = np.sum(W1[j])
        w += E_h[j]*(W1_T[i][j]/w_sum)
    E_i = np.append(E_i, np.round(w, 3))

print("Input layer's errors: {}".format(E_i))

