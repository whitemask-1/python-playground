#Mandelbrot set asks: 'Does this complex number explode to infinity or stay bounded?'
#The formula is: z = z^2 + c, starting with z = 0, where c is the complex number being tested.
#If the magnitude of z exceeds a certain threshold (usually 2), we say it escapes
#We color points based on how quickly they escape (number of iterations before exceeding threshold)

#Other Fractals:
#Burning Ship Fractal: Similar to Mandelbrot but uses absolute values in the iteration formula.
#So instead of z = z^2 + c, it uses z = (|Re(z)| + i|Im(z)|)^2 + c
#This means we take the absolute values of the real and imaginary parts of z before squaring it.

#Example
#z = -0.5 + 0.3j  # A complex number
#Normal Mandelbrot iteration: z = z**2 + c
#z_mandelbrot = z**2 + c
#Burning Ship iteration: z = (|Re(z)| + i|Im(z)|)^2 + c
#z_burning_ship = (abs(z.real) + 1j * abs(z.imag))**2 + c
#Tricorn(or Mandelbar) iteration uses the complex conjugate: z = conjugate(z)**2 + c
#z_tricorn = (z.conjugate())**2 + z

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ========================================
# STEP 1: Define Fractal Formulas
# ========================================

# Lambda function: anonymous function defined inline
# Syntax: lambda arguments: expression

# Mandelbrot: z² + c
# Takes current z value and c value, returns new z
mandelbrot = lambda z, c: z**2 + c

# Burning Ship: (|real| + i|imag|)² + c
# abs() on complex number gives magnitude, but we want abs of parts
burning_ship = lambda z, c: (abs(z.real) + 1j*abs(z.imag))**2 + c
# Breakdown:
# z.real extracts real part of z
# z.imag extracts imaginary part of z
# abs(z.real) makes real part positive
# 1j*abs(z.imag) creates imaginary part that's positive
# Then we square the whole thing and add c

# Tricorn: conjugate(z)² + c
tricorn = lambda z, c: np.conj(z)**2 + c
# np.conj(z) flips sign of imaginary part
# If z = 3 + 4j, then np.conj(z) = 3 - 4j

# ========================================
# STEP 2: Create the Iteration Function
# ========================================

def iterate_fractal(c_values, fractal_func, max_iter=50):
    """
    Apply fractal iteration to determine escape time
    
    Args:
        c_values: List/array of complex numbers to test
        fractal_func: Which fractal formula to use (lambda function)
        max_iter: Maximum iterations before giving up
    
    Returns:
        List of integers: how many iterations until escape (or max_iter)
    """
    
    # Define inner function to check ONE complex number
    def check_escape(c):
        z = 0  # Always start at origin
        
        # Iterate up to max_iter times
        for i in range(max_iter):
            # Apply the fractal formula
            # This calls our lambda function: mandelbrot(z, c) or burning_ship(z, c)
            z = fractal_func(z, c)
            
            # Check if z has escaped
            # If |z| > 2, it will go to infinity
            if abs(z) > 2:
                return i  # Return iteration count (for coloring)
        
        # If we got here, z never escaped
        return max_iter  # Return max value (will be darkest color)
    
    # ========================================
    # KEY FUNCTIONAL PROGRAMMING CONCEPT: map()
    # ========================================
    # map(function, iterable) applies function to every item in iterable
    # Instead of a for loop like:
    #   results = []
    #   for c in c_values:
    #       results.append(check_escape(c))
    # We use map for a more functional style:
    
    return list(map(check_escape, c_values))
    # This applies check_escape to EVERY c in c_values
    # Returns an iterator, so we convert to list

# ========================================
# STEP 3: Generate the Complex Grid
# ========================================

width, height = 800, 800  # Resolution of our image

# Create arrays of x and y coordinates
# linspace creates evenly spaced values
x = np.linspace(-2, 1, width)    # Real axis: from -2 to 1
y = np.linspace(-1.5, 1.5, height)  # Imaginary axis: from -1.5 to 1.5

# meshgrid creates 2D grids from 1D arrays
# Think of it as creating a checkerboard of coordinates
X, Y = np.meshgrid(x, y)
# Now X[i,j] contains the x-coordinate at position (i,j)
# And Y[i,j] contains the y-coordinate at position (i,j)

# Combine X and Y to create complex numbers
C = X + 1j*Y
# Now C[i,j] = X[i,j] + 1j*Y[i,j]
# This is a 2D array where each element is a complex number
# For example: C[400,400] might be 0 + 0j (the origin)

# Example of what C looks like:
# C[0,0] = -2 - 1.5j      (bottom-left corner)
# C[0,799] = 1 - 1.5j     (bottom-right corner)
# C[799,0] = -2 + 1.5j    (top-left corner)
# C[799,799] = 1 + 1.5j   (top-right corner)

# ========================================
# STEP 4: Flatten for map() Operation
# ========================================

# C is 2D (800x800), but map() works on 1D sequences
# flatten() converts 2D array to 1D
c_flat = C.flatten()
# Now c_flat is a 1D array of 640,000 complex numbers
# c_flat[0] = C[0,0], c_flat[1] = C[0,1], etc.

# ========================================
# STEP 5: Generate Each Fractal
# ========================================

print("Generating Mandelbrot...")
# Call our function with the mandelbrot lambda
mandelbrot_data = np.array(iterate_fractal(c_flat, mandelbrot))
# This applies mandelbrot formula to all 640,000 points
# Returns array of integers (escape times)
mandelbrot_data = mandelbrot_data.reshape(height, width)
# Reshape back to 2D for image display

# Same process for other fractals:
print("Generating Burning Ship...")
burning_ship_data = np.array(iterate_fractal(c_flat, burning_ship)).reshape(height, width)

print("Generating Tricorn...")
tricorn_data = np.array(iterate_fractal(c_flat, tricorn)).reshape(height, width)

# ========================================
# STEP 6: Visualize with Animation
# ========================================

# Create figure with black background
fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')

# Store fractals in a list of tuples (data, name)
fractals = [
    (mandelbrot_data, 'Mandelbrot Set'),
    (burning_ship_data, 'Burning Ship Fractal'),
    (tricorn_data, 'Tricorn (Mandelbar) Fractal')
]

def update(frame):
    """
    Called for each frame of animation
    
    Args:
        frame: Current frame number (0, 1, 2, 3, ...)
    """
    ax.clear()  # Clear previous image
    
    # Cycle through fractals every 60 frames
    # frame % len(fractals) gives: 0, 1, 2, 0, 1, 2, ...
    fractal_idx = (frame // 60) % len(fractals)
    data, title = fractals[fractal_idx]
    
    # Display the fractal as an image
    ax.imshow(
        data,  # 2D array of escape times
        extent=[-2, 1, -1.5, 1.5],  # Coordinate bounds [left, right, bottom, top]
        cmap='hot',  # Color map: black -> red -> yellow -> white
        interpolation='bilinear',  # Smooth pixels
        origin='lower'  # (0,0) at bottom-left
    )
    
    # Styling
    ax.set_title(title, color='white', fontsize=16)
    ax.axis('off')  # Hide axes
    
    return ax,  # Return as tuple (required by FuncAnimation)

# Create animation
anim = FuncAnimation(
    fig,  # Figure to animate
    update,  # Function to call each frame
    frames=range(len(fractals) * 60),  # Total frames (3 fractals × 60 frames each)
    interval=1000,  # Milliseconds between frames (1 second per frame)
    blit=False  # Don't use blitting (simpler but slower)
)

plt.show()