import numpy as np
import matplotlib.pyplot as plt

# Create x-y grid
x = np.linspace(-np.sqrt(3), np.sqrt(3), 200) # Generate 200 points from -sqrt(3) to sqrt(3)
y = np.linspace(-np.sqrt(3), np.sqrt(3), 200) # Generate 200 points from -sqrt(3) to sqrt(3)
X, Y = np.meshgrid(x, y) # Create a meshgrid for 3D surface plotting

# Mask invalid values (outside the ellipsoid)
inside = 3 - X**2 - Y**2 # Calculate the inside of the ellipsoid equation
inside[inside < 0] = np.nan # Mask values outside the ellipsoid

# Bottom half of ellipsoid
Z = -np.sqrt(2 * inside) # Calculate negative z values
Z_top = np.sqrt(2 * inside) # Calculate positive z values


# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, alpha=0.8)
ax.plot_surface(X, Y, Z_top, alpha=0.4)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Ellipsoid')

plt.show()