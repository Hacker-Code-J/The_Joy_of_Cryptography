import matplotlib.pyplot as plt
import numpy as np

# Define the GGM_PRF function as previously implemented
def GL(v):
    return ((v << 1) | (v >> (len(bin(v)) - 3))) & 0xFFFFFFFF

def GR(v):
    return (v >> 1) | ((v & 1) << (len(bin(v)) - 3))

def GGM_PRF(k, x_in):
    v = k
    for xi in x_in:
        if xi == '0':
            v = GL(v)
        elif xi == '1':
            v = GR(v)
    return v

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
key = np.random.randint(0, 2**10)

# Generate input space
input_space = np.arange(2**10)

# We will convert the inputs to binary strings for the GGM_PRF
binary_input_space = ['{0:010b}'.format(x) for x in input_space]

# Compute the GGM_PRF output for all inputs in the space
ggm_prf_output = np.array([GGM_PRF(key, x) for x in binary_input_space])

output_space = np.arange(2**10)
rf_instance = RandomFunction(output_space)
rf_output = np.array([rf_instance(x) for x in input_space])

# Plotting the outputs of RF and GGM_PRF
plt.figure(figsize=(7, 7))
plt.plot(input_space, rf_output, 'x', color='dodgerblue', label='RF', markersize=4)
plt.plot(input_space, ggm_prf_output, 'o', color='mediumvioletred', label='GGM_PRF', markersize=4)
plt.title(f'GGM_PRF vs. RF (KEY: {key})', fontsize=14)
plt.xlabel('Index Space X', fontsize=12)
plt.ylabel('Output Space Y', fontsize=12)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()