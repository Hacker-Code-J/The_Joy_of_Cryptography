from prg_adversary import adversary_G
from prg_adversary import adversary_rand
import matplotlib.pyplot as plt

# Run each function multiple times and collect the results.
def compare_distributions(num_trials=1000):
    results_G = [adversary_G() for _ in range(num_trials)]
    results_rand = [adversary_rand() for _ in range(num_trials)]
    
    # Calculate True/False ratios, handling the case where the denominator might be zero.
    ratio_G = (results_G.count(True) / results_G.count(False)) if results_G.count(False) > 0 else float('inf')
    ratio_rand = (results_rand.count(True) / results_rand.count(False)) if results_rand.count(False) > 0 else float('inf')

    return {
        'adversary_G_True_False_Ratio': ratio_G,
        'adversary_rand_True_False_Ratio': ratio_rand,
        'results_G': results_G,
        'results_rand': results_rand
    }


# Compare the distributions
compare_distributions_result = compare_distributions()
    
# Extract the results from the previous run for both functions
results_G = compare_distributions_result['results_G']
results_rand = compare_distributions_result['results_rand']

# Count the True and False occurrences for both functions
true_false_counts_G = [results_G.count(True), results_G.count(False)]
true_false_counts_rand = [results_rand.count(True), results_rand.count(False)]

# Set up the figure and axes for the bar plot
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Titles for subplots
axes[0].set_title('Adversary G Distribution')
axes[1].set_title('Adversary Random Distribution')

# Labels for bars
labels = ['True', 'False']

# Plotting the True/False distribution for adversary_G
axes[0].bar(labels, true_false_counts_G, color=['blue', 'orange'])
axes[0].set_ylim(0, max(true_false_counts_G + true_false_counts_rand) * 1.1)

# Plotting the True/False distribution for adversary_rand
axes[1].bar(labels, true_false_counts_rand, color=['blue', 'orange'])
axes[1].set_ylim(0, max(true_false_counts_G + true_false_counts_rand) * 1.1)

# Display the plot
plt.tight_layout()
plt.show()