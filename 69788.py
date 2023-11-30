import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Hypothetical positions for Na and Cl ions
r_na = np.array([[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]])  # Na positions
r_cl = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]])  # Cl positions

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Na ions
ax.scatter(r_na[:, 0], r_na[:, 1], r_na[:, 2], c='blue', label='Na', s=50)

# Plot Cl ions
ax.scatter(r_cl[:, 0], r_cl[:, 1], r_cl[:, 2], c='red', label='Cl', s=50)

# Labeling and visualization settings
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
ax.set_title('Hypothetical Equilibrium Configuration at -6.9788 eV')

plt.show()
