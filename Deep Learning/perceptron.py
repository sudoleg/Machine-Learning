from abc import ABC, abstractmethod
import numpy as np

class Perceptron(ABC):

    def __init__(self, num_inputs):
        self.num_inputs = num_inputs
        self.weights = np.random.rand(num_inputs)
        self.bias = np.random.rand()

    @abstractmethod
    def forward(self, inputs: np.array) -> np.array:
        pass

class RegressionPercepton(Perceptron):

    def __str__(self):
        return f"Regression Percepton with {self.num_inputs} inputs"

    def forward(self, inputs: np.array) -> np.array:
        return np.dot(inputs, self.weights) + self.bias