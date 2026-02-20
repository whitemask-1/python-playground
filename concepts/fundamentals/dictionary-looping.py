#Some common techniques for looping through dictionaries are as follows:
#Defining a sample dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer"
}  

#Looping through keys
print("Looping through keys:")
for key in person:
    print(f"Key: {key}, Value: {person[key]}")

#Alternatively, you can use the keys() method
print("\nUsing keys() method:")
for key in person.keys():
    print(f"Key: {key}, Value: {person[key]}")

#Looping through values
print("\nLooping through values:")
for value in person.values():
    print(f"Value: {value}")


#Looping through key-value pairs
print("\nLooping through key-value pairs:")
for key, value in person.items():
    print(f"Key: {key}, Value: {value}")

#Using dictionary comprehension to create a new dictionary with modified values
print("\nUsing dictionary comprehension to create a new dictionary with modified values:")
squared_ages = {key: (value ** 2 if isinstance(value, int) else value) for key, value in person.items()}
print("Original Dictionary:", person)
print("Modified Dictionary:", squared_ages)

#Using enumerate to get index along with key-value pairs
print("\nUsing enumerate to get index along with key-value pairs:")
for index, (key, value) in enumerate(person.items()):
    print(f"Index: {index}, Key: {key}, Value: {value}")

#Using items() method with unpacking
print("\nUsing items() method with unpacking:")
for item in person.items():
    key, value = item
    print(f"Key: {key}, Value: {value}")

