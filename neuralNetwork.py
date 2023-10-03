import numpy as np


class NeuralNetwork:
    """
    A simple feedforward neural network.
    """

    def __init__(self, input_nodes, hidden_nodes, output_nodes):
        """
        Initialize the neural network with given nodes.
        """
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        self.weights_ih = np.random.rand(self.hidden_nodes, self.input_nodes)
        self.weights_ho = np.random.rand(self.output_nodes, self.hidden_nodes)
        self.bias_h = np.random.rand(self.hidden_nodes, 1)
        self.bias_o = np.random.rand(self.output_nodes, 1)
        self.learning_rate = 0.1

    @staticmethod
    def sigmoid(x):
        """
        Sigmoid activation function.
        """
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_derivative(x):
        """
        Derivative of the sigmoid function.
        """
        return x * (1 - x)

    def feedforward(self, input_array):
        """
        Perform a feedforward pass through the network.
        """
        inputs = np.array(input_array).reshape(-1, 1)

        self.hidden = np.dot(self.weights_ih, inputs)
        self.hidden += self.bias_h
        self.hidden = self.sigmoid(self.hidden)

        self.output = np.dot(self.weights_ho, self.hidden)
        self.output += self.bias_o
        self.output = self.sigmoid(self.output)

        return self.output

    def train(self, input_array, target_array):
        """
        Train the neural network.
        """
        inputs = np.array(input_array).reshape(-1, 1)
        targets = np.array(target_array).reshape(-1, 1)

        self.feedforward(input_array)

        output_errors = targets - self.output
        hidden_errors = np.dot(self.weights_ho.T, output_errors)

        output_gradients = self.sigmoid_derivative(self.output)
        output_deltas = output_errors * output_gradients * self.learning_rate
        self.weights_ho += np.dot(output_deltas, self.hidden.T)
        self.bias_o += output_deltas

        hidden_gradients = self.sigmoid_derivative(self.hidden)
        hidden_deltas = hidden_errors * hidden_gradients * self.learning_rate
        self.weights_ih += np.dot(hidden_deltas, inputs.T)
        self.bias_h += hidden_deltas


if __name__ == "__main__":
    """
    Test the neural network.
    """
    nn = NeuralNetwork(2, 2, 1)
    for i in range(1000):
        nn.train([1.0, 0.5], [1])
    output = nn.feedforward([1.0, 0.5])
    print("Output after training:", output)
