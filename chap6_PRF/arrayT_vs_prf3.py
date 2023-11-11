import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming the example_prf and example_rf functions and the necessary imports are already defined above
# Also assuming the large_prf_outputs_key1, large_prf_outputs_key2, and large_rf_outputs are already generated

num_samples_large = 1000
input_space_large = range(num_samples_large)
output_space = range(2**8)

# Example PRF using a simple hash function (not cryptographically secure)
def example_prf(key, input_value):
    return (hash(f"{key}-{input_value}") % (2**8))

# Example RF that simply chooses a random value from the output space for every input
def example_rf(input_value):
    return np.random.choice(output_space)

# Generate outputs for PRFs with two different keys and RF with a larger sample size
large_prf_outputs_key1 = [example_prf(1, x) for x in input_space_large]
large_prf_outputs_key2 = [example_prf(2, x) for x in input_space_large]
large_rf_outputs = [example_rf(x) for x in input_space_large]

# Convert the input space from range to list for correct repetition
input_space_list = list(input_space_large)

# Corrected data dictionary
data = {
    'Input': input_space_list * 3,  # Repeat the input space for each label
    'Output': large_prf_outputs_key1 + large_prf_outputs_key2 + large_rf_outputs,
    'Label': ['PRF Key 1'] * num_samples_large + 
             ['PRF Key 2'] * num_samples_large + 
             ['RF'] * num_samples_large
}

# Convert the data to a DataFrame
df = pd.DataFrame(data)

# Prepare separate dataframes for each label for comparison
df_prf_key1 = df[df['Label'] == 'PRF Key 1']
df_prf_key2 = df[df['Label'] == 'PRF Key 2']
df_rf = df[df['Label'] == 'RF']

# Plot joint density for PRF with Key 1 vs RF
sns.jointplot(data=df_prf_key1, x="Input", y="Output", kind="kde", color="blue", fill=True, space=0)
sns.jointplot(data=df_rf, x="Input", y="Output", kind="kde", color="red", fill=True, space=0)
plt.show()

# Plot joint density for PRF with Key 2 vs RF
sns.jointplot(data=df_prf_key2, x="Input", y="Output", kind="kde", color="green", fill=True, space=0)
sns.jointplot(data=df_rf, x="Input", y="Output", kind="kde", color="red", fill=True, space=0)
plt.show()
