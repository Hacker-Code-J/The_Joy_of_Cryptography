import matplotlib.pyplot as plt
import numpy as np

# Let's visualize the concept of a Pseudo-Random Function (PRF) using a simple example.
# We'll generate a random key and use a simple hash function as an example PRF.

# Generate a random key
key1 = np.random.randint(0, 2**10, size=1)  # A 1-byte key
key2 = np.random.randint(0, 2**10, size=1)  # A 8-byte key

# Define a simple PRF using a hash function
# For visualization purposes, we'll just use a hash of the input x XORed with the key
def prf(x, k):
    # XOR the input with the key
    x_k = np.bitwise_xor(x, k)
    # Hash the result to get the PRF output
    return x_k # % (2**10)
    # return np.mod(np.sum(x_k), 256)  # Output space is Y = {0, 1, ..., 255}

# Define a truly random function (RF)
def rf(x, y_space):
    # Choose a random output from the output space for each input
    return np.random.choice(y_space)

# Let's apply different sizes for the input and output space to both the PRF and RF and visualize the results.

# Define new input and output spaces of different sizes
input_space1 = np.arange(2**10)
output_space = np.arange(2**10)

# Compute the PRF and RF outputs for the smaller input/output space
prf_output1 = np.array([prf(x, key1) for x in input_space1])
rf_output1 = np.array([rf(x, output_space) for x in input_space1])

prf_output2 = np.array([prf(x, key2) for x in input_space1])
rf_output2 = np.array([rf(x, output_space) for x in input_space1])

# Create a figure with specified figure size
plt.figure(figsize=(14, 7))

# Subplot 1 for PRF vs RF comparison in the first scenario
plt.subplot(1, 2, 1)
plt.plot(input_space1, prf_output1, 'o', color='mediumvioletred', label='PRF', markersize=4)
plt.plot(input_space1, rf_output1, 'x', color='dodgerblue', label='RF', markersize=4)
plt.title('PRF vs. RF (kEY 1)', fontsize=14)
plt.xlabel('Index Space X', fontsize=12)
plt.ylabel('Output Space Y', fontsize=12)
plt.legend()
plt.grid(True)

# Subplot 2 for PRF vs RF comparison in the second scenario
plt.subplot(1, 2, 2)
plt.plot(input_space1, prf_output2, 'o', color='mediumvioletred', label='PRF', markersize=4)
plt.plot(input_space1, rf_output2, 'x', color='dodgerblue', label='RF', markersize=4)
plt.title('PRF vs. RF (KEY 2)', fontsize=14)
plt.xlabel('Index Space X', fontsize=12)
plt.ylabel('Output Space Y', fontsize=12)
plt.legend()
plt.grid(True)

# Adjust layout to prevent overlap and show the plot
plt.tight_layout()
plt.show()


# # Input space X = {0, 1, ..., 255}
# input_space = np.arange(256)

# # Compute the PRF output for each input in the input space
# prf_output = np.array([prf(x, key) for x in input_space])

# # Output space Y for the RF is the same as the PRF for comparison
# y_space = np.arange(256)

# # Compute the RF output for each input in the input space
# rf_output = np.array([rf(x, y_space) for x in input_space])

# # Plot the PRF and RF together for comparison
# plt.figure(figsize=(12, 6))

# # PRF plot
# plt.plot(input_space, prf_output, 'o', label='PRF')

# # RF plot
# plt.plot(input_space, rf_output, 'x', label='RF')

# plt.title('Pseudo-Random Function (PRF) vs. Truly Random Function (RF) Visualization')
# plt.xlabel('Input Space X')
# plt.ylabel('Output Space Y')
# plt.legend()
# plt.grid(True)
# plt.show()