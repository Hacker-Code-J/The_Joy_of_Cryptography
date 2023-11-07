import random
import secrets
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Let's define a function for OTP and Pseudo-OTP.

# OTP function - uses secrets module for generating a truly random key
def otp(length):
    # Generate a truly random byte sequence
    return secrets.token_bytes(length)

# Pseudo-OTP function - uses random module which is not suitable for cryptographic purposes
def pseudo_otp(length):
    # Set a seed for reproducibility in this example
    random.seed(0)
    # Generate a pseudo-random byte sequence
    return bytes([random.randint(0, 255) for _ in range(length)])

# To visualize the transformation of the distribution graph according to byte size changes,
# we can create a plot for several different byte sizes.


# Define byte sizes to analyze
byte_sizes = [4, 8, 64, 128]

# Create a figure and axes with subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

for i, byte_size in enumerate(byte_sizes):
    # Generate byte sequences for OTP and Pseudo-OTP
    otp_bytes = otp(byte_size)
    pseudo_otp_bytes = pseudo_otp(byte_size)

    # Convert byte sequences to integer lists for statistical analysis
    otp_values = [byte for byte in otp_bytes]
    pseudo_otp_values = [byte for byte in pseudo_otp_bytes]

    # Calculate mean and standard deviation for both sets of values
    otp_mean = np.mean(otp_values)
    otp_std = np.std(otp_values)

    pseudo_otp_mean = np.mean(pseudo_otp_values)
    pseudo_otp_std = np.std(pseudo_otp_values)

    # Generate x values for the normal distributions
    x_range = np.linspace(0, 255, 1000)  # byte values range from 0 to 255

    # Generate the normal distribution for OTP
    otp_normal_dist = norm.pdf(x_range, otp_mean, otp_std)

    # Generate the normal distribution for Pseudo-OTP
    pseudo_otp_normal_dist = norm.pdf(x_range, pseudo_otp_mean, pseudo_otp_std)

    # Plot the normal distributions for OTP and Pseudo-OTP
    axes[i].plot(x_range, otp_normal_dist, label=f'OTP (size={byte_size})', linewidth=2, color='green')
    axes[i].plot(x_range, pseudo_otp_normal_dist, label=f'Pseudo-OTP (size={byte_size})', linestyle='dashed', linewidth=2, color='blue')
    axes[i].set_title(f'Normal Distributions for Byte Size {byte_size}')
    axes[i].set_xlabel('Byte Values')
    axes[i].set_ylabel('Probability Density')
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()
plt.show()





# # Generating byte sequences
# otp_bytes = otp(8)
# pseudo_otp_bytes = pseudo_otp(8)

# # Convert byte sequences to integer lists for statistical analysis
# otp_values = [byte for byte in otp_bytes]
# pseudo_otp_values = [byte for byte in pseudo_otp_bytes]

# # Calculate mean and standard deviation for both sets of values
# otp_mean = np.mean(otp_values)
# otp_std = np.std(otp_values)

# pseudo_otp_mean = np.mean(pseudo_otp_values)
# pseudo_otp_std = np.std(pseudo_otp_values)

# # Generate x values for the normal distributions
# x_range = np.linspace(0, 255, 1000)  # byte values range from 0 to 255

# # Generate the normal distribution for OTP
# otp_normal_dist = norm.pdf(x_range, otp_mean, otp_std)

# # Generate the normal distribution for Pseudo-OTP
# pseudo_otp_normal_dist = norm.pdf(x_range, pseudo_otp_mean, pseudo_otp_std)

# # Plotting the normal distributions for OTP and Pseudo-OTP
# plt.figure(figsize=(10, 5))
# plt.plot(x_range, otp_normal_dist, label='OTP Normal Distribution', linewidth=2, color='green')
# plt.plot(x_range, pseudo_otp_normal_dist, label='Pseudo-OTP Normal Distribution', linestyle='dashed', linewidth=2, color='blue')
# plt.title('Normal Distributions of OTP and Pseudo-OTP')
# plt.xlabel('Byte Values')
# plt.ylabel('Probability Density')
# plt.legend()
# plt.grid(True)
# plt.show()





























# # Now let's generate some data and visualize the randomness.

# # We will create a simple frequency distribution of byte values to visualize
# # how uniformly the random and pseudo-random bytes are distributed.

# def frequency_distribution(byte_sequence):
#     # Count the frequency of each byte value (0-255)
#     frequency = [0] * 256
#     for byte in byte_sequence:
#         frequency[byte] += 1
#     return frequency

# # Generate random data using both functions
# otp_data = otp(10000)
# pseudo_otp_data = pseudo_otp(10000)

# # Get the frequency distribution of the generated data
# otp_freq_dist = frequency_distribution(otp_data)
# pseudo_otp_freq_dist = frequency_distribution(pseudo_otp_data)

# # Plotting the results
# plt.figure(figsize=(14, 7))

# # OTP frequency distribution plot
# plt.subplot(1, 2, 1)
# plt.bar(range(256), otp_freq_dist, color='green')
# plt.title('OTP Frequency Distribution')
# plt.xlabel('Byte Value')
# plt.ylabel('Frequency')
# plt.ylim(0, max(otp_freq_dist) * 1.1)  # Set y-axis limit a bit higher for better visualization

# # Pseudo-OTP frequency distribution plot
# plt.subplot(1, 2, 2)
# plt.bar(range(256), pseudo_otp_freq_dist, color='blue')
# plt.title('Pseudo-OTP Frequency Distribution')
# plt.xlabel('Byte Value')
# plt.ylabel('Frequency')
# plt.ylim(0, max(pseudo_otp_freq_dist) * 1.1)  # Set y-axis limit a bit higher for better visualization

# plt.tight_layout()
# plt.show()