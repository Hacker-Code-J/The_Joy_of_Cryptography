import matplotlib.pyplot as plt
import numpy as np

# Using the previously defined RandomFunction class to replace the rf function
class RandomFunction:
    def __init__(self, y_space):
        self.y_space = y_space
        self.results = {}  # to store results

    def __call__(self, x):
        if x not in self.results:
            self.results[x] = np.random.choice(self.y_space)
        return self.results[x]

# Generate a random key
key = np.random.randint(0, 2**10, size=1)

def prf(x, k):
    x_k = np.bitwise_xor(x, k)
    return x_k

input_space = np.arange(2**10)

prf_output = np.array([prf(x, key) for x in input_space])



output_space = np.arange(2**10)
rf_instance = RandomFunction(output_space)
rf_output = np.array([rf_instance(x) for x in input_space])

plt.figure(figsize=(7, 7))

plt.plot(input_space, rf_output, 'x', color='dodgerblue', label='RF', markersize=4)
plt.plot(input_space, prf_output, 'o', color='mediumvioletred', label='RF', markersize=4)
plt.title(f'PRF vs. RF (KEY: {key})', fontsize=14)
# plt.title(f'Random Table T', fontsize=14)
plt.xlabel('Index Space X', fontsize=12)
plt.ylabel('Output Space Y', fontsize=12)
plt.legend()
plt.grid(True)

# Adjust layout to prevent overlap and show the plot
plt.tight_layout()
plt.show()