# Loops are used to repeat a block of code multiple times.
# The two main types of loops in Python are 'for' loops and 'while' loops.

# For Loop
# A 'for' loop is used to iterate over a sequence (like a list, tuple, string, or range).
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
# You can also use the 'range()' function to generate a sequence of numbers.
for i in range(5):  # This will iterate from 0 to 4
    print("Number:", i)

#You can also nest loops, meaning you can have a loop inside another loop.
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# While Loop
# A 'while' loop continues to execute as long as a specified condition is true.
count = 0
while count < 5:
    print("Count is:", count)
    count += 1  # Increment the count to avoid infinite loop

# Be cautious with 'while' loops to ensure the condition will eventually become false.
# You can also use 'break' and 'continue' statements within loops.
# 'break' exits the loop entirely, while 'continue' skips to the next iteration.
for i in range(10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue  # Skip even numbers
    print("Odd number:", i)

# Loops are powerful tools for automating repetitive tasks and iterating over data structures in Python.
# Both for and while loops can be used with else clauses as well.
for i in range(3):
    print("Looping i =", i)
else:
    print("For loop completed without break.")

count = 0
while count < 3:
    print("While looping count =", count)
    count += 1
else:
    print("While loop completed without break.")