from module import *
# Define side lengths 'a' and 'b'
a = 0.2 # length
b = 0.3 # width
h = a # height

# Define rectangle configuration for Na+ and Cl- ions
r_na = np.array([[0, 0, 0], [a, 0, a], [0, b, a], [a, b, 0]])
r_cl = np.array([[0, 0, a], [a, 0, 0], [0, b, 0], [a, b, a]])

# Create Cluster instance
cluster = Cluster(r_na, r_cl)
vals_init = cluster.get_vals()
print('initial Na positions:\n', r_na)
print('initial Cl positions:\n', r_cl)
print('initial positions flattened shape:\n', vals_init )
print('initial V  :', cluster.V() )

# Optimization using scipy.optimize.minimize
res = scipy.optimize.minimize(fun=cluster, x0=vals_init, tol=1e-3, method="BFGS", callback=cluster.callback)
cluster.set_vals(res.x)  # Update cluster with optimized positions
print("Final optimized cluster positions")
print(cluster.positions)
print("Final potential:", res.fun)
print("Number of iterations:", res.nit)

# Plotting
# Combine Na+ and Cl- positions
positions = np.vstack((r_na, r_cl))

# Define connections between ions for line plotting
lines = [
    [0, 5],
    [0, 4],
    [0, 6],
    [4, 1],
    [4, 2],
    [1, 7],
    [7, 2],
    [7, 3],
    [6, 2],
    [5, 3],
    [6, 3],
    [1, 5]
]

# Prepare the points for line plotting
# Each line segment is defined by a pair of points.
points = np.array([positions[idx] for idx_pair in lines for idx in idx_pair])
      # The 'points' array is reshaped to form a series of line segments.
      # Each segment is represented by two points (start and end),
      # and each point has three coordinates (x, y, z). The resulting shape is (-1, 2, 3),
      # where -1 allows numpy to automatically
      # determine the necessary size based on the length of 'lines'.
lines = points.reshape(-1, 2, 3)


# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', facecolor='white', alpha=1 )
#plt.figure(figsize=(8, 10))
# Plot initial positions for Na+ and Cl-
ax.scatter(r_na[:,0], r_na[:,1], r_na[:,2], c='blue', label='Initial Na+', s=50, alpha=1)
ax.scatter(r_cl[:,0], r_cl[:,1], r_cl[:,2], c='red', label='Initial Cl-', s=50, alpha=1)

# Plot optimized positions for Na+ and Cl-
ax.scatter(optimized_r_na[:,0], optimized_r_na[:,1], optimized_r_na[:,2], c='indigo', label='Optimized Na+', s=50, alpha=1)
ax.scatter(optimized_r_cl[:,0], optimized_r_cl[:,1], optimized_r_cl[:,2], c='darkgreen', label='Optimized Cl-', s=50, alpha=1)

# Add the lines for initial positions
line_collection = Line3DCollection(lines, colors='black', linewidths=1, alpha=1)
ax.add_collection3d(line_collection)

# Set labels and legend
ax.set_xlabel('a (nm)')
ax.set_ylabel('b (nm)')
ax.set_zlabel('h (nm)')
ax.text2D(0.05, 0.95, "Optimized potential for rectangle configuration: -28.69 eV", transform=ax.transAxes, color='blue', weight='bold')
ax.legend(loc='center left', bbox_to_anchor=(1.1, 0.75))
plt.show()

# Plotting the potential energy vs. optimization steps
plt.figure()
plt.rcParams['font.size'] = 12
# Plotting the potential energy vs. optimization steps
plt.figure(figsize=(6, 4))
plt.plot(cluster.potentials_per_step, marker='o', linestyle='-', color='blue', linewidth=1.5, markersize=6)
plt.xlabel('Optimization Steps', fontsize=14, fontweight='bold')
plt.ylabel('Potential Energy (eV)', fontsize=14, fontweight='bold')
plt.title('Rectangle: Potential Energy vs. Optimization Steps (Using BFGS)', fontsize=10, fontweight='bold')
plt.show()
