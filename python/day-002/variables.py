# experiment 1 variable assignment

x = 20
print("x  =",x)
print("id(x) = ",id(x))


#Experiment 2 – Dynamic Typing

a = 10
print(type(a))

a=10.5
print(type(a))

a = "R"
print(type(a))

#Experiment 3 – Multiple Assignment
a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

#Experiment 4 – Single Object, Multiple References

a = b = c = 100

print(a, b, c)

print(id(a))
print(id(b))
print(id(c))

#Experiment 5 – Variable Swapping
x = 10
y = 20

print("Before Swap:", x, y)

x, y = y, x

print("After Swap:", x, y)

#Experiment 6 – type()
x = 10

print(type(x))
# Experiment 7 – isinstance()
x = 3.14

print(isinstance(x, float))
print(isinstance(x, int))


#Experiment 8 – Immutable Integer Reassignment
x = 10
y = x

print(id(x))
print(id(y))

x += 5

print(x)
print(y)

print(id(x))
print(id(y))