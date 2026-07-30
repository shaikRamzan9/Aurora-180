#Experiment 1 – Integer Assignment
x = 10
y = x

print(x, y)
print(id(x))
print(id(y))

#Experiment 2 – List Assignment
x = [1,2,3]
y = x

print(id(x))
print(id(y))

y.append(4)

print(x)
print(y)

#Experiment 3 – Shallow Copy
x = [1,2,3]
y = x.copy()

print(id(x))
print(id(y))

y.append(4)

print(x)
print(y)

#Experiment 4 – Deep Copy
import copy

x = [[1,2],[3,4]]
y = copy.deepcopy(x)

print(id(x))
print(id(y))

y[0].append(99)

print(x)
print(y)

#Experiment 5 – Tuple
x = (1,2,3)
y = x

print(id(x))
print(id(y))

x = x + (4,)

print(x)
print(y)

#Experiment 6 – Integer Immutability
x = 10
y = x

x += 5

print(x)
print(y)