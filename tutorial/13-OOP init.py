 #AI Overview
#"init" can refer to several things, but most commonly it refers to the initialization process in computing, particularly in the context of operating systems. In Unix-based systems, init (short for initialization) is the first process started during boot-up. It is responsible for starting all other system processes and daemons, and it manages system services and the overall boot process. In Python, __init__ is a special method used in classes to initialize the attributes of an object when it is created. 
#Here's a more detailed breakdown:
#1. init in Unix/Linux Systems:
#First Process:
#init is the very first process that runs when a Unix-like operating system starts up. 
#Daemon Process:
#It's a daemon process, meaning it runs in the background and performs essential system tasks. 
#Process Management:
#init is responsible for starting, stopping, and managing other processes and services. 
#Configuration Files:
#init relies on configuration files (like /etc/inittab in older systems) to determine which processes to start and how the system should be configured. 
#Runlevels:
#i#nit also manages runlevels, which define different system states (e.g., single-user mode, multi-user mode, graphical mode). 
#Example:
##In modern systems, systemd is often used instead of init, but the core function of starting and managing system processes remains the same. 
#2. __init__ in Python:
#Constructor:
#__init__ is a special method in Python classes, commonly known as the constructor.
#Object Initialization:
#It's automatically called when a new object is created from a class.
#Attribute Initialization:
#__init__ is used to initialize the attributes (variables) of the object, giving them their initial values.
#Example:
#I##f you have a class Dog with attributes like name and breed, the __init__ method would be used to set the initial name and breed for each individual dog object created from the class. 
#3. Other Contexts:
##nit as a verb: In some contexts, "init" can be a verb meaning "to initialize" or prepare something for use. 
#init in C#: In C#, the init keyword is used in property declarations to create init-only setters, which allow setting a property's value only during object initialization. 
#init as an abbreviation: It can also be a simple abbreviation for "initial". 





#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

#To understand the meaning of classes we have to understand the built-in __init__() function.

#All classes have a function called __init__(), which is always executed when the class is being initiated.

#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)