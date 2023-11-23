import matplotlib.pyplot as plt
import numpy as np

# Increasing the number of samples to 1000
num_samples_large = 1000
input_space_large = range(num_samples_large)
key_space = range(1, 2**4)  # Two example keys for PRF
output_space = range(2**16)  # Let's assume the output space is 8-bit values

# Example PRF using a simple hash function (not cryptographically secure)
def example_prf(key, input_value):
    return (hash(f"{key}-{input_value}") % (2**16))

# Example RF that simply chooses a random value from the output space for every input
def example_rf(input_value):
    return np.random.choice(output_space)

#  Generate outputs for PRFs with two different keys and RF with a larger sample size
large_prf_outputs_key1 = [example_prf(1, x) for x in input_space_large]
large_prf_outputs_key2 = [example_prf(2, x) for x in input_space_large]
large_rf_outputs = [example_rf(x) for x in input_space_large]

# To improve readability with a large number of samples, we'll use a scatter plot with lower opacity
plt.figure(figsize=(12, 7))

# Scatter plot for PRF with key 1
plt.scatter(input_space_large, large_prf_outputs_key1, alpha=0.5, label='PRF with key 1', s=10)

# Scatter plot for PRF with key 2
plt.scatter(input_space_large, large_prf_outputs_key2, alpha=0.5, color='green', label='PRF with key 2', s=10)

# Scatter plot for RF
# plt.scatter(input_space_large, large_rf_outputs, alpha=0.2, color='red', label='RF', s=10)
plt.plot(input_space_large, large_rf_outputs, 'x', color='red', label='RF', alpha=0.2)


# Title and labels
plt.title('Comparison of PRF (with two keys) and RF Outputs (1000 samples)')
plt.xlabel('Input Space')
plt.ylabel('Output Space')
plt.legend()

plt.show()

# import matplotlib.pyplot as plt
# import numpy as np

# # Parameters for the visualization
# in_bits = 4  # This would be the 'in' in the description
# out_bits = 2  # This would be the 'out' in the description
# lambda_bits = 3  # This would be the 'λ' in the description
# num_accesses = 10  # Number of times the calling program will access the table

# # Simulate the lazy/on-demand population of the table T
# # We'll represent the table as a dictionary for simplicity
# T = {}
# accessed_indices = np.random.choice(2**in_bits, num_accesses, replace=False)

# # Populate the table on-demand
# for idx in accessed_indices:
#     if idx not in T:
#         T[idx] = np.random.randint(2**out_bits)

# # Now we can visualize the accessed part of the table
# # We'll create a binary matrix representation for visualization
# max_entries = 2**in_bits
# matrix = np.zeros((max_entries, out_bits))  # Initialize with zeros
# for idx in T:
#     binary_representation = [int(x) for x in bin(T[idx])[2:].zfill(out_bits)]
#     matrix[idx] = binary_representation

# # Plotting
# plt.figure(figsize=(10, 6))
# plt.imshow(matrix, cmap='Greys', interpolation='nearest')
# plt.title('Visualization of the Lazy Populated Table T')
# plt.xlabel('Output Bits')
# plt.ylabel('Input Entries')
# plt.yticks(range(max_entries), [bin(i)[2:].zfill(in_bits) for i in range(max_entries)])
# plt.colorbar(label='Bit Value')
# plt.grid(True, which='both', color='black', linewidth=0.5)
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm

# # Define parameters
# lambda_bits = 4 # Lambda bits for the second library
# num_samples = 1000 # Number of samples we want to generate

# # Generate random outputs for the first library: Each output is a random binary string of 'out_bits' length
# out_bits = 8 # Output bits for the first library
# first_library_outputs = np.random.randint(2, size=(num_samples, out_bits))

# # Define a function to simulate a simple pseudo-random function (PRF)
# def simple_prf(k, x, output_bits):
#     np.random.seed(hash(k + str(x)) % (2**32 - 1))
#     return np.random.randint(0, 2**output_bits)

# # Define a function to generate a random key of a given bit length
# def generate_random_key(bit_length):
#     return bin(np.random.randint(0, 2**bit_length))[2:].zfill(bit_length)

# # Generate a random key for the PRF from the lambda bits
# random_key = generate_random_key(lambda_bits)

# # Use the new random key to generate outputs for the second library using the simple PRF
# second_library_prf_outputs_with_random_key = [simple_prf(random_key, i, lambda_bits) for i in range(num_samples)]

# # Convert the outputs to integers
# first_library_int_outputs = [int(''.join(map(str, bits)), 2) for bits in first_library_outputs]
# second_library_prf_int_outputs_with_random_key = [int(''.join(np.binary_repr(output, width=lambda_bits)), 2) 
#                                                   for output in second_library_prf_outputs_with_random_key]

# # Calculate mean and standard deviation for both libraries
# mean_first_library = np.mean(first_library_int_outputs)
# std_dev_first_library = np.std(first_library_int_outputs)
# mean_second_library = np.mean(second_library_prf_int_outputs_with_random_key)
# std_dev_second_library = np.std(second_library_prf_int_outputs_with_random_key)

# # Calculate the normal distribution values for both libraries
# x_range = np.linspace(min(mean_first_library, mean_second_library) - 4*max(std_dev_first_library, std_dev_second_library), 
#                       max(mean_first_library, mean_second_library) + 4*max(std_dev_first_library, std_dev_second_library), 
#                       1000)
# first_library_normal_dist = norm.pdf(x_range, mean_first_library, std_dev_first_library)
# second_library_prf_normal_dist_with_random_key = norm.pdf(x_range, mean_second_library, std_dev_second_library)

# # Plot the smooth normal distributions for both libraries
# plt.figure(figsize=(10, 6))
# plt.plot(x_range, first_library_normal_dist, label='First Library (Random Table)')
# plt.plot(x_range, second_library_prf_normal_dist_with_random_key, label='Second Library (PRF with Random Key)', linestyle='--')
# plt.title('Smooth Normal Distribution Comparison with Random Key')
# plt.xlabel('Value')
# plt.ylabel('Probability Density')
# plt.legend()
# plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np

# # Parameters
# input_bits = 16
# output_bits = 4
# array_size = 2 ** input_bits
# seed_example = '1101011101101011'

# # Pseudorandom function definition
# def pseudorandom_function(input_value, seed, output_bits):
#     np.random.seed(int(seed, 2))  # Seed with seed only for reproducibility
#     np.random.seed(np.random.randint(0, 2**output_bits) + input_value)  # Add input value for more variation
#     return np.random.randint(0, 2**output_bits)

# # Generate data for array T and pseudorandom function F
# T = np.random.randint(0, 2**output_bits, array_size)
# F = np.array([pseudorandom_function(i, seed_example, output_bits) for i in range(array_size)])

# # Normalize the outputs for normal distribution plot
# T_normalized = (T - np.mean(T)) / np.std(T)
# F_normalized = (F - np.mean(F)) / np.std(F)

# # Create the normal distribution plots without color fill
# plt.figure(figsize=(12, 6))

# sns.kdeplot(T_normalized, shade=False, color="red", label="Array T")
# sns.kdeplot(F_normalized, shade=False, color="blue", label="Function F")

# plt.title('Normal Distribution Plot of Array T and Pseudorandom Function F')
# plt.xlabel('Normalized Output Value')
# plt.ylabel('Density')
# plt.legend()

# plt.show()


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