# Kth Largest Element in an Array

## Problem

Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

Note that it is the kth largest element in sorted order, not the kth distinct element.

## Approach

My first thought was to sort the entire array and return the element at the appropriate position. Although this works, sorting processes every element even though the problem only requires the kth largest value.

To optimize the solution, I used a min heap.

The key observation is that we only need to keep track of the k largest elements seen so far. While traversing the array:

- Each element is pushed into the min heap.
- If the heap size exceeds `k`, the smallest element is removed.

By continuously removing the smallest element whenever the heap grows beyond size `k`, the heap always contains the k largest elements encountered so far.

After processing all elements, the root of the min heap represents the smallest element among those k largest elements, which is exactly the kth largest element in the array.

## Complexity

**Time Complexity:** O(n log k)

Each insertion and removal operation on the heap takes O(log k), and all `n` elements are processed once.

**Space Complexity:** O(k)

The heap stores at most `k` elements at any time.

## Key Learning

This problem demonstrated that it is often unnecessary to sort an entire dataset when only a subset of information is needed. By maintaining only the k largest elements using a min heap, the solution becomes significantly more efficient than sorting the complete array.