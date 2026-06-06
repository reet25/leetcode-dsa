# Maximum Subarray (Kadane’s Algorithm)

## Problem
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

---

## Approach

I started with a brute force approach where I calculated the sum of all possible subarrays using nested loops. This approach works but has high time complexity.

After that, I optimized the solution using Kadane’s Algorithm.

The key idea is to maintain a running sum of the subarray. At each element, we decide whether to:
- continue the previous subarray
- or start a new subarray from the current element

If the running sum becomes negative, it is reset because a negative sum will only reduce future contributions.

We continuously track the maximum sum seen so far.

---

## Algorithm Idea

For each element:
- current_sum = max(current element, current_sum + current element)
- max_sum = max(max_sum, current_sum)

---

## Complexity

Time Complexity: O(n)  
Space Complexity: O(1)

---

## Key Learning

This problem introduces the greedy "running sum with reset" pattern. Instead of checking all subarrays, we make a local optimal decision at each step to build the global optimal answer.