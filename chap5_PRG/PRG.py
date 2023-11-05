from prg_rand_1024 import query_random
from prg_real import query_G

import matplotlib.pyplot as plt
import seaborn as sns

# To visually check the output values as a distribution, we'll plot histograms of multiple outputs.

# Define the number of experiments to run
num_experiments = 100

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
norm_sums_G = [s / 1024 for s in sums_G]
norm_sums_random = [s / 2048 for s in sums_random]

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

# # Generate a Kernel Density Estimate plot for each distribution
# sns.set(style="whitegrid")

# # Set up the matplotlib figure
# plt.figure(figsize=(10, 6))

# # Plot KDE for sums_G
# sns.kdeplot(sums_G, bw_adjust=0.5, label='query_G() Distribution', color='blue')

# # Plot KDE for sums_random
# sns.kdeplot(sums_random, bw_adjust=0.5, label='query_random() Distribution', color='green')

# # Add a legend and titles
# plt.legend()
# plt.title('Comparison of Distributions')
# plt.xlabel('Sum of 1s')
# plt.ylabel('Density')

# plt.show()

# # Create histograms
# fig, axes = plt.subplots(1, 2, figsize=(14, 7))

# # Histogram for query_G() outputs
# axes[0].hist(sums_G, bins=range(min(sums_G), max(sums_G) + 1), color='blue', alpha=0.7)
# axes[0].set_title('Distribution of Sum of 1s in query_G() outputs')
# axes[0].set_xlabel('Sum of 1s')
# axes[0].set_ylabel('Frequency')

# # Histogram for query_random() outputs
# axes[1].hist(sums_random, bins=range(min(sums_random), max(sums_random) + 1), color='green', alpha=0.7)
# axes[1].set_title('Distribution of Sum of 1s in query_random() outputs')
# axes[1].set_xlabel('Sum of 1s')
# axes[1].set_ylabel('Frequency')

# plt.tight_layout()
# plt.show()