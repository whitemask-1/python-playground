#Prefixing an attribute with double underscores in Python triggers the name mangling process
#In which Python internally renames the attribute by adding an underscore and the class name as a prefix
#_ClassName__attributeName

#This makes it harder to accidentally access or modify the attribute from outside the class, providing a layer of protection
class SecretAgent:
    def __init__(self, codename, real_name):
        self.codename = codename  # Public attribute
        self.__real_name = real_name  # Private attribute

    def reveal_identity(self):
        return f"The agent's real name is {self.__real_name}"
    
agent = SecretAgent("Shadow", "John Doe")
print(agent.codename)  # Accessible
# print(agent.__real_name)  # This will raise an AttributeError

#To see this in action, you can create an instance and use __dict__ to view its attributes
print(agent.__dict__)  # Shows the mangled name for __real_name

#However, you can still access the private attribute using its mangled name
print(agent._SecretAgent__real_name)  # Accessing the private attribute using name mangling

#But this is discouraged as it breaks the encapsulation principle
print(agent.reveal_identity())  # Proper way to access the private attribute via a public method
#Output: The agent's real name is John Doe

#Name mangling is primarily used to avoid naming conflicts in subclasses
#It is not meant to be a robust security feature, as determined users can still access the mangled attributes if they know the class name
#It's more about preventing accidental access and modification rather than providing true privacy

#Heres an example of why name mangling is useful in inheritance scenarios
class Base:
    def __init__(self):
        self.__value = "Base Value"

    def get_value(self):
        return self.__value
    
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.__value = "Derived Value"  # This creates a new private attribute in Derived

    def get_derived_value(self):
        return self.__value
    
base_instance = Base()
derived_instance = Derived()    
print(base_instance.get_value())          # Output: Base Value
print(derived_instance.get_derived_value())  # Output: Derived Value
print(derived_instance.get_value())       # Output: Base Value

#In this example, both Base and Derived have their own __value attributes
#Due to name mangling, they do not conflict with each other
#This allows Derived to have its own private attribute without interfering with Base's attribute
#Without name mangling, the __value in Derived would override the one in Base, leading to potential bugs and confusion

#The difference between single underscore (_) and double underscore (__) is that single underscore is a convention indicating that an attribute is intended for internal use (protected)
#But it can still be accessed from outside the class
#Double underscore triggers name mangling, making it harder to access the attribute from outside the class
#This provides a stronger level of encapsulation and helps prevent accidental access or modification of private attributes, especially in inheritance scenarios