#We use float and int as the primary numerical data types in Python
#With them we can perform various mathematical operations and store numerical data
my_integer = 10
my_float = 5.5
print(type(my_integer)) #Output: <class 'int'>
print(type(my_float))   #Output: <class 'float'>

#They can also be negative or zero
negative_integer = -3
zero_float = 0.0
print("Negative Integer:", negative_integer)
print("Zero Float:", zero_float)

#Basic Mathematical Operations
addition = my_integer + my_float
subtraction = my_integer - my_float
multiplication = my_integer * my_float
division = my_integer / my_float  #Note: Division always results in a float
floor_division = my_integer // my_float #Floor division discards the decimal part
modulus = my_integer % 3  #Gives the remainder of the division
exponentiation = my_integer ** 2  #Raises to the power
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

#If you mix integers and floats in operations, Python automatically converts integers to floats
mixed_operation = my_integer + 2.5  #my_integer is treated as 10.0
print("Mixed Operation (int + float):", mixed_operation)
#You can also use built-in functions to convert between data types
converted_to_float = float(my_integer)  #Converts integer to float
converted_to_int = int(my_float)        #Converts float to integer (truncates)
print("Converted to Float:", converted_to_float)
print("Converted to Int:", converted_to_int)

#You can also use the round() function to round floats to a specified number of decimal places
rounded_value = round(my_float, 1)  #Rounds to 1 decimal place
print("Rounded Value:", rounded_value)
#Mathematical functions like abs(), pow(), min(), max() are also available
absolute_value = abs(-my_integer)  #Gives the absolute value
power_value = pow(my_integer, 3)   #Raises to the power
minimum_value = min(my_integer, my_float, 3)  #Finds the minimum
maximum_value = max(my_integer, my_float, 3)  #Finds the maximum
#Syntax for pow() is pow(base, exponent)
#Syntax for min() and max() is min(value1, value2, ...)
print("Absolute Value:", absolute_value)
print("Power Value:", power_value)
print("Minimum Value:", minimum_value)
print("Maximum Value:", maximum_value)

#How about augmented assignment operators?
#They combine a binary operation with assignment in one step, it takes a variable, applies an operation, and then stores the result back into the same variable
counter = 5
print("Initial Counter:", counter)
counter += 3  #Equivalent to counter = counter + 3
print("After += 3:", counter)
counter -= 2  #Equivalent to counter = counter - 2
print("After -= 2:", counter)
counter *= 4  #Equivalent to counter = counter * 4
print("After *= 4:", counter) #useable for all operations like division, modulus, exponentiation etc.

#you can also use augmented assignment operators with strings
greeting = "Hello"
print("Initial Greeting:", greeting)
greeting += ", World!"  #Equivalent to greeting = greeting + ", World!"
print("After += ', World!':", greeting)

#Note that there are no increment (++) or decrement (--) operators in Python like in some other languages. You can achieve the same effect using += and -= operators.