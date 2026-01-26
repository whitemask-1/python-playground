#The range() function is used to generate a sequence of numbers within a specified range.
#Basic Syntax:
# range(start, stop, step)
# start: The starting value of the sequence (inclusive). Default is 0.
# stop: The ending value of the sequence (exclusive).
# step: The difference between each number in the sequence. Default is 1.

#Examples of using range():
# Generate numbers from 0 to 4
for num in range(5):
    print(num)  # Outputs: 0, 1, 2, 3, 4
# Generate numbers from 2 to 6
for num in range(2, 7):
    print(num)  # Outputs: 2, 3, 4, 5, 6
# Generate even numbers from 0 to 10
for num in range(0, 11, 2):
    print(num)  # Outputs: 0, 2, 4, 6, 8, 10

# Note that the range function only accepts integer values for start, stop, and step.

# The generated range object can be converted to a list or tuple if needed:
range_list = list(range(5))  # [0, 1, 2, 3, 4]
range_tuple = tuple(range(2, 7))  # (2, 3, 4, 5, 6)
print("Range as List:", range_list)
print("Range as Tuple:", range_tuple)

#You can also use negative step values to generate sequences in reverse order.
for num in range(10, 0, -2):
    print(num)  # Outputs: 10, 8, 6, 4, 2

#The range function is commonly used in for-loops to iterate a specific number of times.