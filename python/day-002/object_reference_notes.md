# python object and refernces

1. what is Python?
Python is a high level,intrepeted programming language which works on line by line execution.it is used in webdevelopment, datascience,ai etc.

2.What is an interpreter?
In Python, Interpreter works as  line by line execution. It reads Python code,translates it into corrections the computer can execute.

3. What is an Object?
An object is a piece of data in memory.Every value in python is an object.
#ex:
10
3.14
"Ramzan"

4. What is a variable?
A variable is a name that refers to the object.

5. What is reference?
A reference is the connection between a variable name and an object.

6. What id id()?
id() is a python built-in function that returns the identity  of an object. we use it to check whether two variables refer to the same object.

7. What is mutable objects?
Mutable objects are the objects where the modifications can be possible even after their creation.

#ex 
list
set
dict


8. What is an immutable object?
Immutable objects are nothing but objects which are once created cannot be changed.
# ex
String
tuple
int
float


9. Assignment(=)?
Assisgnment is an assignment operator makes a variable refer to an object.

10. Copy()?
Copy will create a new object and refer to it.
Shallow copy() will also create a  new object for outer most on which is first and in the inner objects are stil shared.

11. Deepcopy()?
Unlike Shallowcopy(), Deepcopy() will creare different objects and the objects will also refer to the different. no objects will be shared.

# Examples

x = 10 
# here x is  a varible name which refers to the object of integer value 10
# 10 is an object value which refereed for variable x
# = is an  assignment operator 
