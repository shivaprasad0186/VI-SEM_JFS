import numpy as np
def initialize_weights(strategy="zeros"):
    if strategy == "zeros":
        weights = np.zeros(2)
        bias = 0.0

    elif strategy == "random":
        weights = np.random.randn(2) * 0.01
        bias = np.random.randn() * 0.01

    elif strategy == "uniform":
        weights = np.random.uniform(-1, 1, 2)
        bias = np.random.uniform(-1, 1)

    else:
        raise ValueError("Unknown initialization strategy")

    return weights, bias

def train_perceptron(X, y, learning_rate=0.1, epochs=10, init="zeros"):
    weights, bias = initialize_weights(init)

    print(f"Initial weights: {weights}, bias: {bias}")

    for epoch in range(epochs):
        for i in range(len(X)):
            z = np.dot(X[i], weights) + bias
            pred = 1 if z >= 0 else 0
            error = y[i] - pred

            weights += learning_rate * error * X[i]
            bias += learning_rate * error
        print(f"Epoch {epoch+1}: weights={weights}, bias={bias}")

    return weights, bias

def predict(X, weights, bias):
    predictions = []
    for x in X:
        z = np.dot(x, weights) + bias
        pred = 1 if z >= 0 else 0
        predictions.append(pred)
    return predictions
if __name__ == "__main__":
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    y = np.array([0, 0, 0, 1])
    weights, bias = train_perceptron(X, y, learning_rate=0.1, epochs=10, init="random")
    preds = predict(X, weights, bias)
    print("\nFinal Predictions:", preds)
    print("Final Weights:", weights)
    print("Final Bias:", bias)
