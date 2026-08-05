# Python Input

## What is input()?

`input()` is a built-in Python function that pauses program execution, accepts input from the user through the keyboard, and returns the input as a string object.

Example:

```python
name = input("Enter your name: ")
```

---

## Important Rule

`input()` always returns a string object, regardless of what the user types.

Examples:

```
25      -> "25"
3.14    -> "3.14"
True    -> "True"
Ramzan  -> "Ramzan"
```

---

## Why Type Casting is Needed

To perform numerical operations, convert the input to the required data type.

Example:

```python
age = int(input("Enter your age: "))
```

---

## Common Error

```python
age = input()

print(age + 5)
```

Raises:

```
TypeError
```

Reason:

A string object cannot be added to an integer object.

---

## Solution

```python
age = int(input())

print(age + 5)
```

---

## Key Takeaways

- Variables refer to objects.
- `input()` always creates a string object.
- Explicit type conversion creates a new object.
- The original object is not modified.