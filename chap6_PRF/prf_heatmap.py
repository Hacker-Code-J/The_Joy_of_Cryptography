import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Increase the number of samples
num_samples_large = 10000
input_space_large = range(num_samples_large)
key_space = range(1, 2**4)  # Two example keys for PRF
output_space = range(2**8)  # Let's assume the output space is 8-bit values

# Example PRF using a simple hash function (not cryptographically secure)
def example_prf(key, input_value):
    return (hash(f"{key}^{input_value}") % (2**8))

# Example RF that simply chooses a random value from the output space for every input
def example_rf(input_value):
    return np.random.choice(output_space)

# Generate outputs for PRFs with two different keys and RF with a larger sample size
key1 = np.random.choice(key_space)
key2 = np.random.choice(key_space)

large_prf_outputs_key1 = [example_prf(key1, x) for x in input_space_large]
large_prf_outputs_key2 = [example_prf(key2, x) for x in input_space_large]
large_rf_outputs = [example_rf(x) for x in input_space_large]

# Convert the input space from range to list for correct repetition
input_space_list = list(input_space_large)

# Corrected data dictionary
data = {
    'Index': input_space_list * 3,  # Repeat the input space for each label
    'Output': large_prf_outputs_key1 + large_prf_outputs_key2 + large_rf_outputs,
    'Label': (['PRF Key 1'] * num_samples_large) + 
             (['PRF Key 2'] * num_samples_large) + 
             (['RF'] * num_samples_large)
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Create a grid of plots for each label
g = sns.FacetGrid(df, col="Label", col_wrap=3, height=4, sharex=True, sharey=True)

# Map a density plot to each subset
g.map(sns.kdeplot, "Index", "Output", cmap="viridis", shade=True, bw_adjust=0.5)

# Show the plot
plt.show()
