import matplotlib.pyplot as plt
import numpy as np

# Let's visualize the concept of the One-Time Pad and Pseudorandom Function (PRF)

# For the One-Time Pad, we can show an example of key space.
# Assume each key is a single byte for simplicity, the key space is then 256 (2^8).
key_space = np.arange(256)

# For the PRF, we can visualize it as a function mapping from inputs to outputs.
# We'll generate a random example of a PRF where the domain and co-domain are both [0, 255].
prf_domain = np.arange(256)
prf_codomain = np.random.permutation(prf_domain)

# Plotting the one-time pad key space
plt.figure(figsize=(14, 7))

# Plot 1: One-Time Pad Key Space
plt.subplot(1, 2, 1)
plt.title("One-Time Pad Key Space")
plt.bar(key_space, np.ones_like(key_space))
plt.xlabel('Key Number')
plt.ylabel('Existence of Key')
plt.xticks([0, 64, 128, 192, 255])
plt.yticks([0, 1])
plt.ylim(0, 1.5)
plt.grid(True)

# Plot 2: Pseudorandom Function (PRF)
plt.subplot(1, 2, 2)
plt.title("Pseudorandom Function (PRF)")
plt.plot(prf_domain, prf_codomain, 'o', markersize=3)
plt.xlabel('Input')
plt.ylabel('Output')
plt.xticks([0, 64, 128, 192, 255])
plt.yticks([0, 64, 128, 192, 255])
plt.grid(True)

# Show both plots
plt.tight_layout()
plt.show()
