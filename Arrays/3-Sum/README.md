# 3Sum

## Problem

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

nums[i] + nums[j] + nums[k] = 0

The solution should not contain duplicate triplets.

---

## Approach

This was the toughest problem I had solved so far because it combined multiple concepts into a single solution.

I initially approached the problem using brute force. The idea was to generate every possible triplet using three nested loops and check whether the sum of the triplet was equal to zero. Although this worked, the time complexity was O(n³), which is inefficient for larger inputs.

To optimize the solution, I first sorted the array. The key insight was that this problem can be reduced to a variation of the Two Sum II problem.

For every element in the array, I fixed that value and calculated the value needed from the remaining two elements:

needed = -nums[i]

I then used two pointers:

* left = i + 1
* right = len(nums) - 1

Using standard two-pointer logic:

* If the current sum is smaller than the needed value, move the left pointer forward.
* If the current sum is greater than the needed value, move the right pointer backward.
* If the current sum equals the needed value, a valid triplet has been found.

Since the problem requires unique triplets, duplicate checks were added for both the fixed element and the pointer values after a match is found.

---

## Complexity

Time Complexity: O(n²)

* Sorting takes O(n log n)
* The outer loop runs O(n) times
* The two-pointer search runs in O(n)

Overall complexity is O(n²)

Space Complexity: O(1) extra space

No additional data structures are created apart from a few variables and pointers. The output list is not counted toward auxiliary space complexity.

---

## Key Learning

This problem showed how a difficult problem can often be transformed into a simpler problem that has already been solved. By sorting the array and reducing 3Sum into multiple Two Sum searches, the time complexity was improved from O(n³) to O(n²).
