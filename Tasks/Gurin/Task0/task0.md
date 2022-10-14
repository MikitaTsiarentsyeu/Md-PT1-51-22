
# Task example
## List Comprehensions:

Let’s say I give you a list saved in a variable: __a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]__. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

## Solution:

```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("A list containing only even elements: ", [b for b in a if b%2 == 0])