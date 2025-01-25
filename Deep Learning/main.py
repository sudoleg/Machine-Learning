import numpy as np
from perceptron import RegressionPercepton

rp = RegressionPercepton(2)

a1 = np.array([1, 2])
y_hat = rp.forward(a1)
print(y_hat)