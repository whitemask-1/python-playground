#Conditional statements let you control the flow of your program based on whether certain condition are true or false.
#The basic building blocks of conditional statements are comparison operators and boolean values.
#Conditional statements often use boolean values (True or False) to determine which code block to execute.

#Comparison Operators
# == : Equal to
# != : Not equal to
# >  : Greater than
# <  : Less than
# >= : Greater than or equal to
# <= : Less than or equal to
a = 10
b = 20
print("a == b:", a == b)   # False
print("a != b:", a != b)   # True
print("a > b:", a > b)     # False
print("a < b:", a < b)     # True
print("a >= b:", a >= b)   # False
print("a <= b:", a <= b)   # True

#the most basic conditional statement is the if statement, code only runs if the condition is true
if a < b:
    print("a is less than b")
#You can also use else to provide an alternative code block if the condition is false
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")
#You can chain multiple conditions using elif (else if)
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")

#You can also combine multiple conditions using logical operators
# and : True if both conditions are true
# or  : True if at least one condition is true
# not : Inverts the boolean value
c = 15
if a < b and c < b:
    print("Both a and c are less than b")
if a < b or c > b:
    print("At least one of a or c is less than b")
if not a > b:
    print("a is not greater than b")
#Nested conditionals are also possible, in order to check multiple layers of conditions
if a < b:
    if c < b:
        print("Both a and c are less than b (nested)")
    else:
        print("a is less than b, but c is not (nested)")
#Conditional statements are essential for controlling the flow of your program and making decisions based on data.
#In Python, every value has an inherent boolean value, which can be used in conditionals.
#For example, non-zero numbers and non-empty strings/lists are considered True, while zero and empty strings/lists are considered False.
if 5:
    print("5 is considered True")
if 0:
    print("0 is considered True")
else:
    print("0 is considered False")

#Some generic truthy and falsy values in Python:
#Truthy values: Non-zero numbers (e.g., 1, -1, 3.14), Non-empty strings (e.g., "Hello"), Non-empty lists (e.g., [1, 2, 3])
#Falsy values: 0, 0.0, Empty strings (""), Empty lists ([]), None
#You can use these values directly in conditionals
my_list = [1, 2, 3]
if my_list:
    print("my_list is not empty")
empty_list = []
if not empty_list:
    print("empty_list is empty")
#Understanding booleans and conditionals is crucial for writing effective and dynamic programs in Python.
#They allow you to make decisions and control the flow of your code based on different conditions and data states.

print(bool(10))        # True
print(bool(0))         # False
print(bool(-5))        # True
print(bool(3.14))      # True
print(bool(0.0))       # False
print(bool("Hello"))   # True
print(bool(""))        # False
print(bool([1, 2, 3])) # True
print(bool([]))        # False
print(bool(None))      # False

#There are three boolean operators in Python: and, or, and not.
#The and operator returns True if both operands are true, otherwise it returns False.
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False
#Also known as a short-circuit operator, if the first operand is False, Python does not evaluate the second operand because the overall expression will be False regardless.
#Evaluation stops as soon as the result is determined.
print(False and (1 / 0 == 0))  # False, does not raise an error
print(bool(1 / 0 == 0))  # Raises ZeroDivisionError

#The or operator returns True if at least one of the operands is true, otherwise it returns False.
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

#The not operator inverts the boolean value of its operand.
print(not True)        # False
print(not False)       # True

