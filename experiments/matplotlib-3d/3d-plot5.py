import numpy as np
import matplotlib.pyplot as plt

#Choose z-range from -4π to 4π
z = np.linspace(-4*np.pi, 4*np.pi, 300) #Generate 400 points from -4π to 4π
theta = np.linspace(0, 2*np.pi, 300) #Generate 400 points from 0 to 2π
Z, Theta = np.meshgrid(z, theta) #Create a meshgrid for 3D surface plotting

# Calculate radius R as a function of z
# def f(z):
#     return 1 + 0.3*np.cos(2*z)

# R = f(Z) 

R = 2 + np.sin(Z)
X = R * np.cos(Theta) #Calculate x values
Y = R * np.sin(Theta) #Calculate y values

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.85)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title(r'Surface: $x^2 + y^2 = (2 + \sin(z))^2$')
plt.show()

#General version for x^2 + y^2 = (f(z))^2