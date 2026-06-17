# Container With Most Water

## Problem

Given an array `height` where each element represents the height of a vertical line, find two lines that together with the x-axis form a container capable of holding the maximum amount of water.

The amount of water that can be stored is:

area = width × min(height[left], height[right])

Return the maximum area possible.

---

## Approach

I initially thought about checking different pairs of lines and calculating the area formed by each pair. This naturally leads to a brute force solution where every possible pair is examined.

Although this guarantees the correct answer, it requires checking O(n²) pairs.

To optimize the solution, I used the Two Pointer technique.

The important observation is that the shorter wall always determines the water level. Even if the taller wall is moved inward, the container height cannot increase because it is still limited by the shorter wall, while the width decreases.

Therefore:

* If `height[left] < height[right]`, move the left pointer.
* If `height[left] > height[right]`, move the right pointer.
* If both heights are equal, either pointer can be moved.

At each step, the area for the current pair is calculated and the maximum area is updated.

---

## Complexity

### Time Complexity: O(n)

Each pointer moves at most `n` times.

### Space Complexity: O(1)

Only a few variables and pointers are used.

---

## Key Learning

This problem demonstrated how eliminating impossible choices can drastically reduce the search space. Instead of checking every pair, the two-pointer strategy intelligently discards configurations that cannot lead to a better answer, reducing the complexity from O(n²) to O(n).
