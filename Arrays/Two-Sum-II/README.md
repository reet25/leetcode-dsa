# Two Sum II - Input Array Is Sorted

## Problem

Given a 1-indexed sorted array of integers and a target value, return the indices of the two numbers such that they add up to the target.

---

## Approach

This problem felt like an advanced version of the original Two Sum problem that I had solved earlier.

In the original problem, a HashMap was required because the array was unsorted. However, in this version the array is already sorted, which eliminates the need for an extra data structure.

I used the Two Pointers approach by placing one pointer at the beginning of the array and another at the end.

At each step:

* If the current sum is greater than the target, the right pointer is moved left because we need a smaller value.
* If the current sum is less than the target, the left pointer is moved right because we need a larger value.
* If the current sum equals the target, the required indices have been found.

Because the array is sorted, every pointer movement helps eliminate impossible pairs, allowing the solution to be found efficiently.

---

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Key Learning

This problem showed how a sorted array can completely change the solution strategy. Instead of using a HashMap, the ordering of the array itself can be exploited using the Two Pointers pattern to achieve O(1) extra space.
