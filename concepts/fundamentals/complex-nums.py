import cmath

z = 1 + 2j  # Define a complex number
angle = cmath.pi / 4  # 45 degrees in radians

rotated_z = z * cmath.exp(1j * angle)  # Rotate the complex number by 45 degrees
print(rotated_z)  # Output the rotated complex number

position = 3 + 4j
velocity = 1 + 1j

position += velocity  # Update position by adding velocity
print(position)  # Output the new position

# Calculate the magnitude and phase of a complex number
magnitude = abs(z)
phase = cmath.phase(z) # Phase is the angle in radians
print("Magnitude:", magnitude)
print("Phase (radians):", phase)

# We can use these in physics simulations, graphics transformations, and signal processing.
conjugate_z = z.conjugate()  # Get the complex conjugate
print("Conjugate:", conjugate_z)

# Convert polar to rectangular form
r = 5  # magnitude
theta = cmath.pi / 3  # angle in radians (60 degrees)
rectangular_form = cmath.rect(r, theta)
print("Rectangular form:", rectangular_form)