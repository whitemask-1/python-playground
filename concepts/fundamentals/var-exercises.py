#LEVEL 1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
country = input("Enter your country: ")
city = input("Enter your city: ")
age = int(input("Enter your age: "))
year = 2025
is_married = input("Are you married? (yes/no): ").strip().lower() == 'yes' #Here we convert the input to a boolean by checking if the input is 'yes'
#print("Married Status:", is_married)
is_true = True
is_light_on = False
a, s, d = 5, 10.5, "Python"

#LEVEL 2
print(type(first_name))  # Output: <class 'str'>
print(type(last_name))   # Output: <class 'str'>
print(type(full_name))   # Output: <class 'str'>
print(type(country))     # Output: <class 'str'>
print(type(city))        # Output: <class 'str'>
print(type(age))         # Output: <class 'int'>
print(type(year))        # Output: <class 'int'>
print(type(is_married))  # Output: <class 'bool'>
print(type(is_true))     # Output: <class 'bool'>
print(type(is_light_on)) # Output: <class 'bool'>
print(type(a))          # Output: <class 'int'>
print(type(s))          # Output: <class 'float'>
print(type(d))          # Output: <class 'str'>
print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_div = num_one // num_two

area_of_circle = 3.14 * (30 ** 2)  # Assuming radius is 30
circum_of_circle = 2 * 3.14 * 30  # Assuming radius is 30
#OR you could do it like
radius = int(input("Enter the radius of the circle: "))
pi = 3.14
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius
print("Area of the circle:", area_of_circle)