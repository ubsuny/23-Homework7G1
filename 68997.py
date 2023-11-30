import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Assuming the 2D plot represents the top view of the configuration,
# and all ions lie in the same plane (z = 0).
# These positions are purely hypothetical and used for illustrative purposes.

# Assuming large circles are Na+ and small circles are Cl-
# The structure seems to be an octagon, we'll assume a regular octagon for simplicity
# Let's set the radius of this regular octagon where ions lie
radius = 1  # arbitrary units

# The angles for a regular octagon
angles = np.linspace(0, 2 * np.pi, 8, endpoint=False)

# Assuming alternating ions (Na+, Cl-, Na+, Cl-, ...)
# Calculating positions for Na+ ions (even indices)
na_angles = angles[0::2]
r_na = np.array([radius * np.cos(na_angles), radius * np.sin(na_angles), np.zeros_like(na_angles)]).T

# Calculating positions for Cl- ions (odd indices)
cl_angles = angles[1::2]
r_cl = np.array([radius * np.cos(cl_angles), radius * np.sin(cl_angles), np.zeros_like(cl_angles)]).T

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Na+ ions
ax.scatter(r_na[:, 0], r_na[:, 1], r_na[:, 2], c='blue', label='Na+', s=100)

# Plot Cl- ions
ax.scatter(r_cl[:, 0], r_cl[:, 1], r_cl[:, 2], c='red', label='Cl-', s=50)

# Draw lines between ions to represent bonds or interactions
for i in range(4):
    ax.plot([r_na[i, 0], r_cl[i, 0]], [r_na[i, 1], r_cl[i, 1]], [r_na[i, 2], r_cl[i, 2]], 'k-')

# Labeling and visualization settings
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
ax.set_title('Hypothetical Equilibrium Configuration at -6.8997 eV')

# Setting equal aspect ratio for all axes
ax.set_box_aspect([1,1,1])  # Equal aspect ratio

plt.show()
