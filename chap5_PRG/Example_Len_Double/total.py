import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# def G(s):
#     """
#     This function takes a list of bits (s), and returns a new list where each 8-bit unit is doubled.
#     """
#     # Initialize an empty list to store the result
#     result = []
#     # Process each 8-bit segment of the input list
#     for i in range(0, len(s), 8):
#         # Extract the 8-bit segment
#         segment = s[i:i+8]
#         # Double the segment and add it to the result list
#         result.extend(segment * 2)
#     return result

def G(s):
    # This function takes 4 bits and returns a list with those 4 bits repeated twice to make 4 bits.
    return s * 2

def query_G():
    lambda_length = 2048
    s = np.random.randint(0, 2, lambda_length).tolist()
    return G(s)

# def G(s):
#     """
#     This function takes a list of bits (s), and returns a new list where each 8-bit unit is doubled.
#     """
#      # Double the list
#     return s * 2

# def query_G():
#     """
#     This function generates a random binary list of length lambda (512 bits),
#     then doubles each 8-bit unit using the G function.
#     """
#     lambda_length = 32
#     s = np.random.randint(0, 2, lambda_length).tolist()
#     return G(s)

def query_random():
    # Generate a random binary string of length lambda + l
    lambda_length = 2048  # Example length of lambda, can be any positive integer
    l_length = 2048  # Example length of l, can be any positive integer
    r = np.random.randint(0, 2, lambda_length + l_length).tolist()  # Generates a list of 0s and 1s
    return r

# res1 = query_G()
# res2 = query_random() 
# print(res1)
# print(res2)

# Define the number of experiments to run
num_experiments = 100000

# Record the outputs
outputs_G = [query_G() for _ in range(num_experiments)]
outputs_random = [query_random() for _ in range(num_experiments)]

# Convert outputs to the sum of their elements to see the distribution of the number of 1s
sums_G = [sum(output) for output in outputs_G]
sums_random = [sum(output) for output in outputs_random]

# To adjust for the length difference between the outputs of query_G() and query_random(),
# we will normalize the sums by dividing by the length of the binary string they were summed from.
# This will give us a proportion of 1s in each string, making the distributions comparable.

# Normalizing the sums by the length of the binary string (10 for query_G() and 15 for query_random())
norm_sums_G = [s / 4096 for s in sums_G]
norm_sums_random = [s / 4096 for s in sums_random]

# Generate a Kernel Density Estimate plot for each normalized distribution
plt.figure(figsize=(10, 6))

# Plot KDE for normalized sums_G
sns.kdeplot(norm_sums_G, bw_adjust=0.5, label='Normalized query_G() Distribution', color='blue')

# Plot KDE for normalized sums_random
sns.kdeplot(norm_sums_random, bw_adjust=0.5, label='Normalized query_random() Distribution', color='green')

# Add a legend and titles
plt.legend()
plt.title('Comparison of Normalized Distributions')
plt.xlabel('Proportion of 1s')
plt.ylabel('Density')

plt.show()