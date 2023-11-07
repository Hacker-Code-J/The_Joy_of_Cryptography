import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Parameters for the distributions
otp_mean = 0
otp_std = 1
pseudo_otp_mean = 0
pseudo_otp_std = 2

# Create a range of values
x = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 1000)

# Generate the OTP distribution
otp_dist = norm.pdf(x, otp_mean, otp_std)

# Generate the Pseudo-OTP distribution
pseudo_otp_dist = norm.pdf(x, pseudo_otp_mean, pseudo_otp_std)

# Hexadecimal color code for emerald
emerald_hex = '#50C878'

# Plot both distributions to visualize the difference with the emerald color
plt.figure(figsize=(10, 5))
plt.plot(x, otp_dist, label='OTP (One-Time Pad)', linewidth=2, color=emerald_hex)
plt.plot(x, pseudo_otp_dist, label='Pseudo-OTP', linestyle='dashed', linewidth=2, color=emerald_hex)
plt.title('Comparison of OTP vs Pseudo-OTP Distributions')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
