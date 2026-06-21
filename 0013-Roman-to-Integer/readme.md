# Roman to Integer (LeetCode 13)

## Solution

```python
class Solution(object):
    def romanToInt(self, s):
        a = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                result -= a[s[i]]
            else:
                result += a[s[i]]

        return result
```

## Key Idea

Most Roman numerals are formed by adding values:

* III = 1 + 1 + 1 = 3
* VIII = 5 + 1 + 1 + 1 = 8

However, some Roman numerals use subtraction:

* IV = 4
* IX = 9
* XL = 40
* XC = 90
* CD = 400
* CM = 900

The solution checks whether the current Roman numeral is smaller than the next one.

If it is smaller, subtract its value.

Otherwise, add its value.


```

## Time Complexity

* Traversing the string once: O(n)
* Dictionary lookup: O(1)

Overall:

```text
O(n)
```

## What I Learned

### 1. Dictionaries in Python

```python
a = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
```

This problem helped me understand how dictionaries can be used to map symbols to values and retrieve them efficiently.

Example:

```python
a["X"]
```

Output:

```text
10
```

### 2. Looking Ahead to the Next Character

```python
a[s[i]] < a[s[i + 1]]
```

This was one of the first problems where I needed to compare the current element with the next element to make a decision.

### 3. Multiple Conditions in an If Statement

```python
if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
```

This taught me how to combine conditions safely.

The first condition ensures that `i + 1` exists before accessing it.

### 4. Applying Problem-Specific Logic

Instead of memorizing Roman numeral combinations such as IV, IX, XL, XC, CD, and CM, I learned to derive the answer using a general rule:

* Smaller value before a larger value → subtract.
* Otherwise → add.

### 5. Iterating Through Strings

This problem improved my understanding of traversing strings using indices and accessing characters one by one.

## Personal Notes

This was one of my first LeetCode problems where the solution was not immediately obvious. It required understanding the Roman numeral rules and converting them into code using dictionaries, indexing, and conditional logic.

The most valuable lesson was learning how to transform a real-world rule into a simple algorithm.
