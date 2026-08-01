# int 

x = 10
print("type : ",type(x))
print("isInstance: ",isinstance(x,int))

# Dynamic Typing
x = 10
print("type:",type(x))
x = 10.0
print("type :",type(x))


#Integer,Float,Complex
x = 10
y = 12.5
z = 10 +2j

print("type :",type(x))
print("type: ",type(y))
print("type: ",type(z))


#Boolean Type

x = True
y = False
print("type:",type(x))
print("type: ",type(y))


# Boolean Arithmetic
print(True+True)
print(True+False)
print(False+True)
print(True+ True +False)

#Integer Conversion
print(int(True))
print(int(False))

# Float Conversion
print(float(True))
print(float(False))

#String Conversion
print(str(True))
print(str(False))

#None
x =None
print("x =",x)
print("type :",type(x))
print(x is None)
print(x == None)


# bool numbers
print(bool(0))
print(bool(1))
print(bool(-5))
print(bool(0.0))
print(bool(0.0))
print(bool(0.00001))


#bool Strings
print(bool(""))
print(bool(" "))
print(bool("Aurora "))
print(bool("0"))
print(bool("False"))


# bool lists
print(bool([]))
print(bool([1]))
print(bool([0]))
print(bool([False]))
print(bool([True]))


#bool tuples
print(bool(()))
print(bool((1)))
print(bool((1,)))


#bool dictionaries

print(bool({}))
print(bool({"name":"honda"}))


#bool sets
print(bool(set()))
print(bool({1}))
print(bool({0}))


# Explicit Type Conversion
x = "25"
print(type(x))
y = int(x)
print(type(y))
print(y)

# Float to Integer
x = 10.99
y = int(x)
print(type(x))
print(type(y))

#Integer to Float

x = 25
print(float(x))
print(type(float(x)))

# Number to String
x = 500
y= str(x)
print(y)
print(type(y))

#String to Boolean
print(bool(""))
print(bool("Python"))
print(bool("0"))
print(bool("False"))
print(bool("True"))


# ============================================
# Experiment 21 - Explicit Type Conversion
# ============================================

x = "25"

print("Experiment 21")

print("Before Conversion")
print("Value:", x)
print("Type:", type(x))

y = int(x)

print("\nAfter Conversion")
print("Value:", y)
print("Type:", type(y))

print(id(x))
print(id(y))

print("-" * 40)

# Experiment 22
x = 10.99

y = int(x)

print(x)
print(y)
print(type(x))
print(type(y))
print("-" * 40)

# ============================================
# Experiment 24 - Integer to String
# ============================================

x = 500

print("Experiment 24")

print("Before Conversion")
print("Value:", x)
print("Type:", type(x))
print("ID:", id(x))

y = str(x)

print("\nAfter Conversion")
print("Value:", y)
print("Type:", type(y))
print("ID:", id(y))

print("-" * 40)

#🧪 Experiment 25 – Boolean Conversion from Strings

print(bool(""))

print(bool("Python"))

print(bool("0"))

print(bool("False"))

print(bool(" "))

print(bool("None"))

print("-" * 40)
