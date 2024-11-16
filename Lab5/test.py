import numpy as np

data = np.load('mnist.npz')

print(data.files)

print(data['x_test'])
