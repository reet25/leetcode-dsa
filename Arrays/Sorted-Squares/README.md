# Squares of a Sorted Array

## Problem

Given a sorted integer array nums, return an array of the squares of each number sorted in non-decreasing order.

---

## Approach

Initially, I found this problem difficult to visualize because squaring the elements destroys the original ordering of the array. A straightforward solution would be to square every element and then sort the resulting array.

After understanding the pattern, I used the Two Pointers approach.

The key observation is that the largest square must come from one of the two ends of the array because the largest absolute value will always be present at either the leftmost or rightmost position.

I maintain two pointers, one at the beginning and one at the end of the array. At each step, I compare their absolute values. The larger absolute value produces the larger square, which is placed at the current position from the end of the result array.

A third pointer is used to track the position where the next largest square should be inserted. Depending on which side produced the larger square, the corresponding pointer is moved inward.

---

## Complexity

Time Complexity: O(n)

Space Complexity: O(n)

---

## Key Learning

This problem introduced the Two Pointers pattern where two ends of a sorted array compete to produce the next optimal value. Instead of sorting after squaring, we leverage the existing ordering of the input array to build the answer directly.