import numpy as np #Numerical operations
import matplotlib.pyplot as plt #Plotting library
from mpl_toolkits.mplot3d import Axes3D #3D plotting toolkit

#visit matplotlib docs for more info: https://matplotlib.org/stable/users/index.html

#Coordinate finder function
def find_coordinates(X, Y, Z, equation, safe_dict):
    """Find coordinates on the surface based on user input"""
    while True:
        print('\n' + '='*50)
        print('Coordinate Finder')
        print('='*50)
        print('1. Given x and y, find z')
        print('2. Given x and z, find y')
        print('3. Given y and z, find x')
        print('4. Exit coordinate finder')

        choice = input('Enter choice (1-4): ').strip()

        if choice == '4':
            print("Exiting coordinate finder.")
            break

        tolerance = 0.1  # Tolerance for finding close matches

        if choice == '1':
            x_val = float(input("Enter x value: "))
            y_val = float(input("Enter y value: "))
            
            # Find indices where x and y match
            x_match = np.abs(X - x_val) < tolerance
            y_match = np.abs(Y - y_val) < tolerance
            both_match = x_match & y_match
            
            indices = np.where(both_match)
            
            if len(indices[0]) == 0:
                print(f"No points found for x ≈ {x_val}, y ≈ {y_val}")
                continue
            
            print(f"\nPoints where x ≈ {x_val} and y ≈ {y_val}:")
            for i, j in zip(indices[0], indices[1]):
                if not np.ma.is_masked(Z[i, j]):
                    print(f"  ({X[i, j]:.3f}, {Y[i, j]:.3f}, {Z[i, j]:.3f})")

        elif choice == '2':
            x_val = float(input("Enter x value: "))
            z_val = float(input("Enter z value: "))
            
            # Find indices where x and z match
            x_match = np.abs(X - x_val) < tolerance
            z_match = np.abs(Z - z_val) < tolerance
            both_match = x_match & z_match
            
            indices = np.where(both_match)
            
            if len(indices[0]) == 0:
                print(f"No points found for x ≈ {x_val}, z ≈ {z_val}")
                continue
            
            print(f"\nPoints where x ≈ {x_val} and z ≈ {z_val}:")
            for i, j in zip(indices[0], indices[1]):
                if not np.ma.is_masked(Z[i, j]):
                    print(f"  ({X[i, j]:.3f}, {Y[i, j]:.3f}, {Z[i, j]:.3f})")

        elif choice == '3':
            y_val = float(input("Enter y value: "))
            z_val = float(input("Enter z value: "))
            
            # Find indices where y and z match
            y_match = np.abs(Y - y_val) < tolerance
            z_match = np.abs(Z - z_val) < tolerance
            both_match = y_match & z_match
            
            indices = np.where(both_match)
            
            if len(indices[0]) == 0:
                print(f"No points found for y ≈ {y_val}, z ≈ {z_val}")
                continue
            
            print(f"\nPoints where y ≈ {y_val} and z ≈ {z_val}:")
            for i, j in zip(indices[0], indices[1]):
                if not np.ma.is_masked(Z[i, j]):
                    print(f"  ({X[i, j]:.3f}, {Y[i, j]:.3f}, {Z[i, j]:.3f})")

        else:
            print("Invalid choice. Please select 1-4.")
            return

#Plotting function
def plot_3d_equation():
    """Main function to plot 3D equations based on user input."""
    print("3D Plot Generator")
    print('=' * 20)
    print('Please enter an equation in terms of x and y to plot z.')
    print('For example: z = sqrt(9 - x**2 - y**2) for a hemisphere.')
    
    equation = input("Enter the equation for z (use 'x' and 'y'): ")

    if not equation:
        print("No equation provided. Exiting.")
        return
    
    print(f"Plotting the equation: z = {equation}")

    #Get ranges for x and y axes
    print("\n Enter plotting ranges (press Enter for default values):")

    x_min_input = input("x min (default -5): ").strip() #Get x min
    x_min = float(x_min_input) if x_min_input else -5.0 #Default -5

    x_max_input = input("x max (default 5): ").strip() #Get x max
    x_max = float(x_max_input) if x_max_input else 5.0 #Default 5

    y_min_input = input("y min (default -5): ").strip() #Get y min
    y_min = float(y_min_input) if y_min_input else -5.0 #Default -5

    y_max_input = input("y max (default 5): ").strip() #Get y max
    y_max = float(y_max_input) if y_max_input else 5.0 #Default 5

    resolution_input = input("Number of points per axis (default 100): ").strip() #Get resolution
    resolution = int(resolution_input) if resolution_input else 100 #Default 100

    print(f"\nX range: [{x_min}, {x_max}]")
    print(f"Y range: [{y_min}, {y_max}]")
    print(f"Resolution: {resolution} points per axis")

    #Create mesh grid
    print("\nGenerating grid...")
    x = np.linspace(x_min, x_max, resolution) #X values
    y = np.linspace(y_min, y_max, resolution) #Y values
    X, Y = np.meshgrid(x, y) #Meshgrid for 3D

    #Create a safe namespace with numpy functions
    safe_dict = {
        'x' : X,
        'y' : Y,
        'X' : X,
        'Y' : Y,
        'sin' : np.sin,
        'cos' : np.cos,
        'tan' : np.tan,
        'arcsin' : np.arcsin,
        'arccos' : np.arccos,
        'arctan' : np.arctan,
        'sqrt' : np.sqrt,
        'exp' : np.exp,
        'log' : np.log,
        'pi' : np.pi,
        'e' : np.e,
        'log10' : np.log10,
        'abs' : np.abs,
        '__builtins__': {} #Disable built-in functions for safety
    }

    try:
        print("Evaluating equation...")
        Z = eval(equation, safe_dict) #Evaluate user equation
        print("Equation evaluated successfully.")
    except Exception as e:
        print(f"Error evaluating equation: {e}")
        return
    
    #Handle invalid values (like sqrt of negative numbers)
    Z = np.ma.masked_invalid(Z) #Mask NaN and inf values

    #Plotting
    print('\nCreating 3D plot...')
    plt.ion
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')

    #Plot the surface with colormap
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none', antialiased=True)

    #add color bar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    #Labels and title
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.set_zlabel('Z-axis', fontsize=12)
    ax.set_title(f'3D Plot of z = {equation}', fontsize=14, fontweight='bold')

    print("Displaying plot... \n" + "=" * 20 +"\nCoordinate finder now available.")
    plt.show(block = False) #Show plot
    plt.pause(0.1) #Pause to ensure plot renders

    use_finder = input("\nWould you like to find specific coordinates? (y/n): ").strip().lower()
    if use_finder == 'y':
        find_coordinates(X, Y, Z, equation, safe_dict)
    
    input("\nPress Enter to close plot and exit...")
    plt.close()


if __name__ == "__main__":
    plot_3d_equation()

# FEATURE IDEA: Continuity Checker for 3D Surfaces
# ================================================
# Concept: Analyze 3D surfaces for continuity and discontinuities
# - Detect jumps/breaks in surface (undefined regions, asymptotes)
# - Identify points where function is discontinuous
# - Highlight discontinuous regions with different colors
# - Calculate gradient magnitude to find sharp changes
# - Visual indicators: color discontinuities red, continuous regions green
# - Add menu option "Check Continuity" alongside coordinate finder
# - Report statistics: % of surface continuous, number of breaks
# - Useful for calculus homework - verify continuity at specific points
# - Could extend to differentiability checking (check partial derivatives)
#
# Technical approach:
# - Use np.gradient() to compute rate of change
# - Set threshold for "too steep" = discontinuity
# - Mask regions where Z has NaN or large jumps
# - Create separate scatter plots for continuous/discontinuous points
# - Add toggle to show/hide discontinuity overlay
#
# Future enhancement: Integrate with coordinate finder to check continuity at specific (x,y) points
# This would combine matplotlib visualization with mathematical analysis for calculus applications