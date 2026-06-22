# Maximum Number of Balloons

## Problem

Given a string `text`, return the maximum number of instances of the word `"balloon"` that can be formed using the characters in the string.

## Approach

* Count the occurrences of each character required to form the word `"balloon"`.
* Since the letters `'l'` and `'o'` appear twice in `"balloon"`, divide their counts by 2.
* The maximum number of times `"balloon"` can be formed is determined by the minimum available count among the required characters.

## Time Complexity

* **O(n)**, where `n` is the length of the string.

## Space Complexity

* **O(1)**

## What I Learned

* Learned how to use the `count()` function on strings to count the occurrences of specific characters.
* Practiced solving string problems using character frequency counting.
