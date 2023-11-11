import matplotlib.pyplot as plt
import numpy as np

# Increase the bits to a larger but reasonable number for visualization
input_bits = 16  # 'in' parameter for a larger comparison
output_bits = 4  # 'out' parameter for a larger comparison
array_size = 2 ** input_bits

# The seed for the pseudorandom function, given the larger number of input bits
seed_example = '1101011101101011'  # Example 16-bit seed

# Create a pseudorandom function
# This function now returns a random integer hashed from the input and seed
def pseudorandom_function(input_value, seed, output_bits):
    np.random.seed(int(input_value + seed, 2))  # Seed with input and seed combined
    return np.random.randint(0, 2**output_bits)

# Since we're dealing with a large number of samples, we'll visualize the data using a line plot
# Generate a smaller output space for visualization purposes
T = np.random.randint(0, 2**output_bits, array_size)
F = np.array([pseudorandom_function(bin(i)[2:].zfill(input_bits), seed_example, output_bits) for i in range(array_size)])

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(T, label='Array T', alpha=0.75)
plt.plot(F, label='Function F', alpha=0.75)

# Add some text for labels, title and axes ticks
plt.ylabel('Output Values')
plt.xlabel('Input Values')
plt.title('Full Scale Comparison between Array T and Pseudorandom Function F')
plt.legend()

plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # Increase the bits for a larger comparison, keeping in mind the bounds of visualization
# input_bits = 10  # 'in' parameter for a larger comparison
# output_bits = 10  # 'out' parameter for a larger comparison
# array_size = 2 ** input_bits
# seed_example = '11010'  # Example seed for a larger comparison

# # Create a pseudorandom function
# # For illustration, this is a simple hash of the input and seed
# def pseudorandom_function(input_value, seed, output_bits):
#     np.random.seed(int(seed, 10))  # Seed the random number genera tor for reproducibility
#     return np.random.randint(0, 2**output_bits)

# # Generate data for the array T and pseudorandom function F at a larger scale
# T = np.random.randint(0, 2**output_bits, array_size)
# F = np.array([pseudorandom_function(bin(i)[2:].zfill(input_bits), seed_example, output_bits) for i in range(array_size)])

# # Due to the large number of bits, we'll only show a sample of the data
# sample_size = 70  # Number of samples to display for visualization
# indices = np.random.choice(array_size, sample_size, replace=False)
# sampled_T = T[indices]
# sampled_F = F[indices]
# sampled_labels = [bin(i)[2:].zfill(input_bits) for i in indices]

# x = np.arange(sample_size)  # the label locations

# width = 0.35  # the width of the bars

# fig, ax = plt.subplots(figsize=(15, 5))  # Larger figure size for readability
# rects1 = ax.bar(x - width/2, sampled_T, width, label='Array T (Sampled)')
# rects2 = ax.bar(x + width/2, sampled_F, width, label='Function F (Sampled)')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Output Values')
# ax.set_title('Sampled Comparison between Array T and Pseudorandom Function F')
# ax.set_xticks(x)
# # ax.set_xticklabels(sampled_labels, rotation='vertical')
# ax.legend()

# fig.tight_layout()

# plt.show()