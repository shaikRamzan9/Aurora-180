# Python Data Types
## what is a data type?
A data type refers to the which type of object it is dealing with.Every object created in Python belongs to a specific data type.

Ex :- int,float,string, bool,list,etc

## Integer
Defnition: An integer is a data type used to represent whole numbers without a decimal point.
Example x=10
here 10 is an object which is integer  object

## Flaot 
Defnition: A float is a data type used to represent numbers with a decimal point.
    
example x =10.0
here 10.0 is an object which is floating decimal

## Complex
Def :A complex data type represents numbers with a real part and an imaginary part.
ex : 10+2j
here j is an imaginary part


## Boolean
Def : Boolean will have two type of object types
    1. True
    2. False


A Boolean data type represents logical values.

It has only two possible objects:

## None
None is object which dont hold any value it is intentionally not assigned.
ex:x =None

`None` is a special object that represents the absence of a value. It is intentionally assigned when no value is available.


## Type Conversion
int() - converts compatible object type to integer object type.
float() - converts compatible object type to float object type.
str() - converts compaible object type to string object type.
bool() -  coverts any object to bool object type. 


#  Conversion rules 
Numbers:
0       → False
Non-zero → True

Strings:
""      → False
"0"   -> True
Anything else → True

Lists:
[]      → False
[Any elements] → True

Tuples:
()      → False

Sets:
set()   → False

Dictionaries:
{}      → False

None:
None    → False

# 7. type()

Definition:

`type()` returns the data type of an object.

Example:

```python
x = 25

print(type(x))
```

Output:

```python
<class 'int'>
```

---

# 8. isinstance()

Definition:

`isinstance()` checks whether an object belongs to a particular data type.

Example:

```python
x = 25

print(isinstance(x, int))
```

Output:

```python
True
```

---

# 9. Explicit Type Conversion

Definition:

Explicit type conversion is the process of intentionally converting one object into another data type using conversion functions.

Python creates a new object during explicit type conversion.

The original object is never modified.

Example:

```python
x = "25"

y = int(x)
```

Memory:

```
x ─────► "25" (str)

y ─────► 25 (int)
```

---

# 10. int()

Converts a compatible object into an integer object.

Examples:

```python
int("25")
int(10.99)
int(True)
```

Important:

`int()` removes the decimal part.

It does NOT round the number.

Example:

```python
int(10.99)
```

Output

```python
10
```

---

# 11. float()

Converts a compatible object into a float object.

Examples:

```python
float(25)

float("25")
```

Output

```python
25.0
```

---

# 12. str()

Converts an object into a string object.

Examples:

```python
str(25)

str(False)
```

Outputs

```python
"25"

"False"
```

---

# 13. bool()

Converts an object into a Boolean object.

Rules:

Numbers

```python
0 → False

Non-zero → True
```

Strings

```python
"" → False

Any non-empty string → True
```

Lists

```python
[] → False

[1] → True
```

Tuples

```python
() → False

(1,) → True
```

Dictionaries

```python
{} → False

{"a":1} → True
```

Sets

```python
set() → False

{1} → True
```

None

```python
None → False
```

---

# 14. Truthy and Falsy Objects

Falsy Objects

```python
0
0.0
False
None
""
[]
()
{}
set()
```

Everything else is Truthy.

---

# 15. ValueError

Definition:

A ValueError occurs when the object type is acceptable, but its value is not valid for the requested operation.

Example:

```python
int("hello")
```

Output

```
ValueError:
invalid literal for int() with base 10: 'hello'
```

Reason:

The object is a string, but its value cannot be interpreted as an integer.

---

# 16. Reading a Python Error

Example:

```
Traceback (most recent call last):

File "errors.py", line 3

print(int(x))

ValueError: invalid literal for int() with base 10: 'hello'
```

How to read it:

1. Traceback tells where Python found the error.

2. File and line number show the exact location.

3. Python displays the statement causing the error.

4. The last line tells the exception type and the reason.