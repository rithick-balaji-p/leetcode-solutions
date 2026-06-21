# Maximum Ice Cream Bars (LeetCode 1833)

## Approaches Learned

### 1. Greedy + Sorting Approach

```python
costs.sort()

total = 0
count = 0

for cost in costs:
    total += cost

    if total > coins:
        break

    count += 1

return count
```

#### Key Idea

To maximize the number of ice cream bars, always buy the cheapest ice creams first. Sorting the array helps us process costs in increasing order.

#### Time Complexity

* Sorting: O(n log n)
* Traversal: O(n)
* Overall: O(n log n)

#### What I Learned

* Greedy algorithms.
* Why sorting can help maximize the number of items purchased.
* Using `break` to stop unnecessary iterations once the budget is exceeded.

---

### 2. Counting Sort + Greedy Approach

```python
class Solution(object):
    def maxIceCream(self, costs, coins):
        max_cost = max(costs)

        count = [0] * (max_cost + 1)

        for i in costs:
            count[i] += 1

        bar = 0

        for i in range(1, max_cost + 1):
            if count[i] == 0:
                continue

            if i > coins:
                break

            can_buy = min(count[i], coins // i)

            coins -= can_buy * i
            bar += can_buy

        return bar
```

#### Key Idea

Instead of sorting, count the frequency of each cost and buy ice creams starting from the cheapest cost.

#### Time Complexity

* Frequency counting: O(n)
* Traversing cost range: O(k)
* Overall: O(n + k)

where k is the maximum cost value.

#### What I Learned

* Frequency counting arrays.
* Counting Sort concept.
* How counting sort can improve performance over regular sorting when the value range is limited.
* The importance of `continue` for skipping unnecessary work.
* The importance of `break` for ending loops early and avoiding extra iterations.
* Using `coins // price` to determine how many items can be afforded at a particular price.
* Combining Greedy and Counting Sort techniques to achieve a more efficient solution.

---

## Personal Notes

This problem helped me understand that finding a correct solution is the first step, and then optimizing it is the next step.

I first solved the problem using a sorting-based greedy approach. Later, I learned how to optimize it using frequency counting and counting sort, which reduced the time complexity from O(n log n) to O(n + k).

This problem also reinforced the importance of small optimizations such as using `break` and `continue` effectively.
