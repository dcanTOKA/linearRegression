import numpy as np
from tqdm import tqdm

def calculateCost(X, y, theta):
    m = X.shape[0]

    h = np.dot(X, theta) - y
    J = np.dot(h.T, h) / (2 * m)

    return J
