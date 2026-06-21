# Palindrome Number (LeetCode 9)

## Solution

```python
class Solution(object):
    def isPalindrome(self, x):
        a = str(x)
        return a == a[::-1]
```

## Key Idea

A palindrome reads the same forward and backward.

Examples:

* 121 → Palindrome
* 1331 → Palindrome
* 123 → Not a palindrome

The number is first converted into a string. Then Python's slicing syntax is used to create a reversed version of the string and compare it with the original.

## Time Complexity

* Converting integer to string: O(n)
* Reversing the string: O(n)
* Comparison: O(n)

Overall: O(n)

where n is the number of digits.

## What I Learned

### 1. Reverse Indexing (String Slicing)

```python
a[::-1]
```

This creates a reversed copy of the string.

Example:

```python
a = "12321"
a[::-1]
```

Output:

```python
"12321"
```

Another example:

```python
a = "hello"
a[::-1]
```

Output:

```python
"olleh"
```

This problem helped me understand a practical use of reverse indexing in Python.

### 2. Returning a Boolean Expression Directly

```python
return a == a[::-1]
```

The expression:

```python
a == a[::-1]
```

already evaluates to either `True` or `False`.

Therefore, there is no need to write:

```python
if a == a[::-1]:
    return True
else:
    return False
```

This problem taught me that comparison operators return Boolean values and can be returned directly.

### 3. Converting Data Types

```python
a = str(x)
```

This problem showed how converting an integer into a string can simplify certain operations, such as reversing and comparing digits.

## Personal Notes

This was a simple but useful problem. It helped me practice Python string slicing, reverse indexing, type conversion, and returning Boolean expressions directly without using extra if-else statements.
