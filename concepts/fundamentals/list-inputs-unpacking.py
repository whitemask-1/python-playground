# Experiment started with question: can i collect inputs with a list and then distribute those inputs by unpacking to different variables

#Direct unpacking
inputs = [input('Enter name: '), input('Enter age: '), input('Enter city: ')]
name, age, city = inputs
print(f"{name} is {age} years old and lives in {city}")

#Collect multiple inputs at once in a simpler input variable using a variable to hold the prompts
prompts = ["Enter name: ", "Enter age: ", "Enter city: "]
inputs = [input(prompt) for prompt in prompts]
name, age, city = inputs

#Split a single input into three items in a list and then unpack the list to corresponding variables
inputs = input("Enter name, age, and city (separated by spaces): ").split() #Note that leaving split empty is better for handling tabs, multiple spaces, leading/trailing whitespace, and newlines all at once
name, age, city = inputs

#Use Type Conversion with unpacking
raw_inputs = [input("Name: "), input('Age: '), input('Height (m): ')]
name, age, height = raw_inputs[0], int(raw_inputs[1]), float(raw_inputs[2])

words = ['tree', 'house', 'apple', 'fly', 'kick']
long_words = list(filter(lambda word: len(word) > 4, words))
print(long_words)