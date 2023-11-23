import matplotlib.pyplot as plt
import numpy as np

# Create a visual representation of the concept with matplotlib for the array T and pseudorandom function F

# Define parameters for the drawing
array_length = 16  # Just for illustrative purposes, not 2^in
in_bit_length = 4  # Number of bits to represent the index
out_bit_length = 8  # Number of bits in the output string

# Create figure and axes
fig, ax = plt.subplots(1, 2, figsize=(14, 5))

# Draw the array T
ax[0].table(cellText=np.random.randint(0, 2, (array_length, out_bit_length)),
            colWidths=[0.05] * out_bit_length,
            cellLoc='center', rowLoc='center',
            loc='center')
ax[0].set_title("Array T")
ax[0].axis('tight')
ax[0].axis('off')

# Draw the function F with seed
ax[1].table(cellText=np.random.randint(0, 2, (array_length, out_bit_length)),
            colWidths=[0.05] * out_bit_length,
            cellLoc='center', rowLoc='center',
            loc='center')
ax[1].set_title("Pseudorandom Function F with Seed")
ax[1].axis('tight')
ax[1].axis('off')

# Add text annotations
ax[0].text(-0.1, 0.5, "T[i]:", transform=ax[0].transAxes, fontsize=12, verticalalignment='center')
ax[1].text(-0.1, 0.5, "F(seed, i):", transform=ax[1].transAxes, fontsize=12, verticalalignment='center')

plt.tight_layout()
plt.show()
