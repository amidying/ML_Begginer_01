

import numpy as np

x =np.array([2600,3000,3200,3600,4000])

y = np.array([550000,565000,610000,680000,725000])
def gradient_descent2(x,y,iteration):
    mcurr=bcurr = 0
    n = len(x)
    learningRate = .0001
    for i in range(iteration):
        ypredicted = mcurr*x+bcurr
        mse = (1/n) * sum([i**2 for i in (y-ypredicted)])
        md = -(1/n)*sum(x*(y-ypredicted))
        bd = -(1/n) * sum(y-ypredicted)
        mcurr -= learningRate*md
        bcurr -= learningRate*bd
        print(f"m {mcurr}, b {bcurr}, i {i}")
        print("cost:",mse)    
    
gradient_descent2(x,y,100)
'''
import numpy as np
def gradient_descent(x,y):
    # start with some initial value of the slope and coeff
    m_curr = b_curr = 0
    iterations = 100000
    n = len(x) # if len of x and y are same you can raise error
    learning_rate = 0.01 # if you learning rate is too big you might miss the global minima. our goal is to find the minima
    for i in range(iterations):
        y_predicted = m_curr*x+b_curr # just starting with a step
        cost = (1/n)*sum([val**2 for val in (y-y_predicted)])
        md = -(1/n)*sum(x*(y-y_predicted))# B1 in regression
        bd = -(1/n)*sum(y-y_predicted) # B0 "    "
        m_curr = m_curr-learning_rate*md
        b_curr = b_curr-learning_rate*bd
        print(f"m {m_curr} b {b_curr} iteration {i}")# print MSE to see how you are doing
        print("Cost is: ",cost)
                        
x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
gradient_descent(x,y)
'''