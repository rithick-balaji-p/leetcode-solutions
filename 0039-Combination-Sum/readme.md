LeetCodeProblem: Combination Sum (Medium)

Problem Statement

Given an array of distinct integers candidates and a target integer target, return all unique combinations of candidates where the chosen numbers sum to target.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one chosen number differs.

Approach

This solution uses the Backtracking technique.

Key Idea
Build combinations incrementally using a temporary list (path).
If the current sum equals the target, store the combination.
If the current sum exceeds the target, stop exploring that path.
Use a start index to avoid generating duplicate combinations.
Pass the current index i during recursion to allow reuse of the same element multiple times.
