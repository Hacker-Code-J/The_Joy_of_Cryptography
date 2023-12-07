import matplotlib.pyplot as plt
import numpy as np

# Increasing the number of samples to 1000
num_samples = 100
input_space = range(num_samples)
key_space = range(1, 2**4)  # Two example keys for PRF
output_space = range(2**16)  # Let's assume the output space is 16-bit values

class RandomPerm:
    def __init__(self, y_space):
        self.y_space = list(y_space)  # Convert range to list for direct indexing
        self.T = {}  # to store input to output mappings
        self.Tinv = {}  # to store output to input mappings

    def lookup(self, x):
        if x not in self.T:
            # Choose an output y that has not been mapped yet
            available_ys = set(self.y_space) - set(self.T.values())
            y = np.random.choice(list(available_ys))
            self.T[x] = y
            self.Tinv[y] = x
        return self.T[x]

    def invlookup(self, y):
        if y not in self.Tinv:
            # Choose an input x that has not been mapped yet
            available_xs = set(range(len(self.y_space))) - set(self.Tinv.values())
            x = np.random.choice(list(available_xs))
            self.Tinv[y] = x
            self.T[x] = y
        return self.Tinv[y]

# Define the RandomFunction class
class RandomFunction:
    def __init__(self, y_space):
        self.y_space = y_space
        self.results = {}  # to store results

    def __call__(self, x):
        if x not in self.results:
            self.results[x] = np.random.choice(self.y_space)
        return self.results[x]

example_rf = RandomFunction(output_space)
example_rp = RandomPerm(output_space)
example_rp_inv = RandomPerm(output_space)

rp_outputs = [example_rp.lookup(x) for x in input_space]
rp_inv_outputs = [example_rp_inv.invlookup(x) for x in input_space]
rf_outputs = [example_rf(x) for x in input_space]

# To improve readability with a large number of samples, we'll use a scatter plot with lower opacity
plt.figure(figsize=(12, 7))

# Scatter plot for PRF with key 1
plt.scatter(input_space, rp_outputs, alpha=0.5, label='PP', s=10)

# Scatter plot for PRF with key 2
plt.scatter(input_space, rp_inv_outputs, alpha=0.5, color='green', label='PP_INV', s=10)

# Scatter plot for RF
plt.scatter(input_space, rf_outputs, alpha=0.2, color='red', label='RF', s=10)

# Title and labels
plt.title('Comparison of PRF (with two keys) and RF Outputs (1000 samples)')
plt.xlabel('Input Space')
plt.ylabel('Output Space')
plt.legend()

plt.show()