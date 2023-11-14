import matplotlib.pyplot as plt
import numpy as np

# Assume some arbitrary values for demonstration purposes
# Let's say we have 2 observations and 2 features (D=2, N=2)
D = 2
N = 2
theta = np.array([0.5, -0.3])  # an example theta
Phi = np.array([[1, 0.5], [0.2, 1]])  # an example Phi matrix
y = np.array([1.5, 0.7])  # an example y vector

# Define the epsilon function
def epsilon(theta, Phi, y):
    return y - Phi.dot(theta)

# Define the loss function L
def loss_function(epsilon):
    return epsilon.T.dot(epsilon)

# Create a grid of theta values for visualization
theta1_range = np.linspace(-1, 1, 100)
theta2_range = np.linspace(-1, 1, 100)
Theta1, Theta2 = np.meshgrid(theta1_range, theta2_range)

# Compute the loss over the grid
Loss = np.array([[loss_function(epsilon(np.array([theta1, theta2]), Phi, y))
                  for theta1 in theta1_range] for theta2 in theta2_range])

# Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(Theta1, Theta2, Loss, cmap='viridis', edgecolor='none')

# Labels and title
ax.set_xlabel('Theta1')
ax.set_ylabel('Theta2')
ax.set_zlabel('Loss')
ax.set_title('Least-Squares Loss Surface')

# Color bar to indicate the loss values
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
