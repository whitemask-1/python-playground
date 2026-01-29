#Getters and Setters are methods that allow you to control how attributes of a class are accessed and modifies
#With getters you retrieve the value of an attribute
#With setters you set or update the value of an attribute
#These actions are done through properties that act as intermediaries between the attribute and the outside world
#This allows you to add validation logic when setting values or perform additional actions when getting values

#Why use properties instead of methods?
#Using properties allows you to access attributes like regular variables while still having the benefits of methods
#This makes the code cleaner and easier to read while still providing control over how attributes are accessed

class Person:
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age

    @property #Getter for name
    def name(self):
        return self.__name
    
    @name.setter #Setter for name
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            print("Invalid name. Please provide a non-empty string.")
    
    @property #Getter for age
    def age(self):
        return self.__age
    
    @age.setter #Setter for age
    def age(self, new_age):
        if isinstance(new_age, int) and 0 <= new_age <= 120:
            self.__age = new_age
        else:
            print("Invalid age. Please provide an integer between 0 and 120.")

#To make getter properties: use @property decorator above the method
#To make setter properties: use @<property_name>.setter decorator above the method


#Creating an instance of Person
person = Person("Alice", 30)
print(person.name)  # Accessing name using getter
print(person.age)   # Accessing age using getter
person.name = "Bob"  # Setting name using setter
person.age = 35     # Setting age using setter
print(person.name)  # Output: Bob
print(person.age)   # Output: 35

#Invalid values are caught immediately by the setters
person.name = ""    # Output: Invalid name. Please provide a non-empty string.
person.age = -5     # Output: Invalid age. Please provide an integer between 0 and 120.
person.age = 150    # Output: Invalid age. Please provide an integer between 0 and 120.

#The name and age remain unchanged
print(person.name)  # Output: Bob
print(person.age)   # Output: 35

#Basically when the call to set the attribute is made, the setter runs first to check it and then if valid it updates the private attribute
#When the call to access the attribute is made, the getter runs to retrieve the value of the private attribute

person.name = "Charlie" #Calls setter
print(person.name)      #Calls getter, Output: Charlie

#The same way you can control access and modification with getters and setters
#You can also control deletion of attributes using deleter properties with the @<property_name>.deleter decorator
#However, deleters are less commonly used compared to getters and setters

class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def grade(self):
        return self.__grade

    @grade.deleter
    def grade(self):
        print(f"Deleting grade for {self.__name}")
        del self.__grade

#Creating an instance of Student
student = Student("David", "A")
print(student.grade)  # Accessing grade using getter, Output: A
del student.grade    # Deleting grade using deleter, Output: Deleting grade for David

#Trying to access grade after deletion will raise an AttributeError
# print(student.grade)  # Uncommenting this line will raise an error

