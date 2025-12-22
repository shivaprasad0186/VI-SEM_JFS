import numpy as np

def train(X, y, lr=0.1, epochs=10):
    w = np.zeros(X.shape[1])
    b = 0

    for _ in range(epochs):
        for xi, yi in zip(X, y):
            pred = 1 if np.dot(xi, w) + b >= 0 else 0
            error = yi - pred
            w += lr * error * xi
            b += lr * error
    return w, b

def predict(X, w, b):
    return [1 if np.dot(x, w) + b >= 0 else 0 for x in X]

# AND gate
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

w, b = train(X, y)
print("Predictions:", predict(X, w, b))
print("Weights:", w)
print("Bias:", b)
