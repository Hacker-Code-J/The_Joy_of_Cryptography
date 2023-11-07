from prg_rand_8 import query_random
from prg_real_4 import query_G
import matplotlib.pyplot as plt
import seaborn as sns

# To visually check the output values as a distribution, we'll plot histograms of multiple outputs.

# Define the number of experiments to run
num_experiments = 10000

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
norm_sums_G = [s / 8 for s in sums_G]
norm_sums_random = [s / 8 for s in sums_random]

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