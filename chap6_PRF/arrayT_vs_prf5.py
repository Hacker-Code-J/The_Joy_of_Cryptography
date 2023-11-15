import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Generate random keys
key1 = np.random.randint(0, 2**10, size=1)
key2 = np.random.randint(0, 2**10, size=1)

# Define a simple PRF using an XOR operation
def prf(x, k):
    # XOR the input with the key
    return np.bitwise_xor(x, k)

# Define a truly random function (RF)
def rf(x, y_space):
    # Choose a random output from the output space for each input
    return np.random.choice(y_space, size=x.shape)

# Define input and output spaces
input_space1 = np.arange(2**10)
output_space = np.arange(2**10)

# Compute the PRF and RF outputs
prf_output1 = prf(input_space1, key1)
rf_output1 = rf(input_space1, output_space)

prf_output2 = prf(input_space1, key2)
rf_output2 = rf(input_space1, output_space)

# prf_output1 = np.array([prf(x, key1) for x in input_space1])
# rf_output1 = np.array([rf(x, output_space) for x in input_space1])

# prf_output2 = np.array([prf(x, key2) for x in input_space1])
# rf_output2 = np.array([rf(x, output_space) for x in input_space1])


# Convert the data to a long-form DataFrame for Seaborn
df1 = pd.DataFrame({'Input Space': input_space1, 'PRF Output': prf_output1, 'RF Output': rf_output1})
df1_melted = df1.melt('Input Space', var_name='Method', value_name='Output')

df2 = pd.DataFrame({'Input Space': input_space1, 'PRF Output': prf_output2, 'RF Output': rf_output2})
df2_melted = df2.melt('Input Space', var_name='Method', value_name='Output')

# Create a figure with specified figure size
plt.figure(figsize=(14, 7))

# Boxplot and violin plot for the first set of data using key1
plt.subplot(1, 2, 1)
sns.boxplot(x='Method', y='Output', data=df1_melted, palette=["#D35E60", "#84BA5B"], showfliers=False)
sns.violinplot(x='Method', y='Output', data=df1_melted, palette=["#E87A90", "#ABDDA4"], inner='point', alpha=0.5)
plt.title('Distribution of Outputs using Key 1', fontsize=15)
plt.ylabel('Output Values', fontsize=13)

# Boxplot and violin plot for the second set of data using key2
plt.subplot(1, 2, 2)
sns.boxplot(x='Method', y='Output', data=df2_melted, palette=["#D35E60", "#84BA5B"], showfliers=False)
sns.violinplot(x='Method', y='Output', data=df2_melted, palette=["#E87A90", "#ABDDA4"], inner='point', alpha=0.5)
plt.title('Distribution of Outputs using Key 2', fontsize=15)
plt.ylabel('Output Values', fontsize=13)

# Adjust layout and show plot
plt.tight_layout()
plt.show()