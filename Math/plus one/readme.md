# Plus One (LeetCode 66)

## Solution

```python
class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        digits.insert(0, 1)
        return digits
```

## Key Idea

The array represents a number where each element is a digit.

Examples:

* [1,2,3] → 123
* [4,3,2,1] → 4321
* [9,9,9] → 999

The task is to add one to the number and return the result as an array.

Instead of converting the entire array into a number, adding one, and converting it back, we can simulate how addition is performed manually.

## Example 1

Input:

```text
[1,2,3]
```

Process:

```text
123 + 1 = 124
```

Output:

```text
[1,2,4]
```

## Example 2

Input:

```text
[1,2,9]
```

Process:

```text
129 + 1 = 130
```

Output:

```text
[1,3,0]
```

## Example 3

Input:

```text
[9,9,9]
```

Process:

```text
999 + 1 = 1000
```

Output:

```text
[1,0,0,0]
```

## Time Complexity

Worst Case:

```text
O(n)
```

because we may need to traverse all digits.

## What I Learned

### 1. Simulating Real Addition

This problem taught me how addition actually works digit by digit.

When adding 1:

* If the digit is less than 9, increase it and stop.
* If the digit is 9, it becomes 0 and a carry moves to the previous digit.

### 2. Traversing a List Backwards

```python
for i in range(len(digits)-1, -1, -1):
```

This loop starts from the last digit and moves toward the first digit.

Example:

```python
digits = [1, 2, 9]
```

Indices visited:

```text
2 → 1 → 0
```

### 3. Early Return Optimization

```python
if digits[i] < 9:
    digits[i] += 1
    return digits
```

If a digit is less than 9, we can finish immediately without checking the remaining digits.

This avoids unnecessary work.

### 4. Carry Propagation

```python
digits[i] = 0
```

When a digit is 9, adding one causes it to become 0 and generates a carry.

Example:

```text
129 + 1
```

```text
9 → 0
carry → 2 becomes 3
```

Result:

```text
130
```

### 5. Handling Edge Cases

```python
digits.insert(0, 1)
```

If every digit is 9:

```text
999 + 1 = 1000
```

All digits become 0, and a new leading 1 must be inserted.

## Personal Notes

My first idea was to convert the array into a number, add one, and then convert it back into an array.

After thinking about how addition works manually, I found a better solution that modifies only the necessary digits.

This problem helped me understand carry propagation, reverse traversal, and how to optimize a straightforward solution into a more efficient one.
