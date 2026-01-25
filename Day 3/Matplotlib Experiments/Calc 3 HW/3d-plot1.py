import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of points
x = np.linspace(-6, 6, 200) # Generate 200 points from -6 to 6 along x-axis
y = np.linspace(-5, 5, 200) # Generate 200 points from -5 to 5 along y-axis
X, Y = np.meshgrid(x, y) # Create a meshgrid for 3D surface plotting

# Solve for z from x^2/36 + z^2 = 1
Zpos = np.sqrt(X**2 / 36) # Calculate positive z values
Zneg = -Zpos # Calculate negative z values

fig = plt.figure(figsize=(10, 7)) # Create a new figure for plotting, set size
ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot, 111 means 1x1 grid, first subplot

# Plot the positive and negative surfaces
ax.plot_surface(X, Y, Zpos, alpha=0.7, rstride=10, cstride=10, color='cyan', edgecolor='k') # Plot positive surface
ax.plot_surface(X, Y, Zneg, alpha=0.7, rstride=10, cstride=10, color='red', edgecolor='k') # Plot negative surface

# Make panes transparent
ax.xaxis.pane.set_edgecolor('w')
ax.yaxis.pane.set_edgecolor('w')
ax.zaxis.pane.set_edgecolor('w')

# Draw axis lines through origin
ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [0, 0], [0, 0], color='k', linewidth=1)  # x-axis
ax.plot([0, 0], [ax.get_ylim()[0], ax.get_ylim()[1]], [0, 0], color='k', linewidth=1)  # y-axis
ax.plot([0, 0], [0, 0], [ax.get_zlim()[0], ax.get_zlim()[1]], color='k', linewidth=1)  # z-axis

# Set labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_title('3D Surface Plot of x^2/36 + z^2 = 1')
plt.show() # Display the plot

