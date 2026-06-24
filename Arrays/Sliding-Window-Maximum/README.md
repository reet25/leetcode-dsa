# Sliding Window Maximum

## Problem

Given an array `nums` and an integer `k`, return an array containing the maximum value in every sliding window of size `k`.

## Approach

I initially solved this problem using a brute force approach. For each window of size `k`, I traversed all elements within that window and calculated the maximum value. Although this produced the correct result, the solution required scanning every window separately, resulting in a time complexity of O(n × k).

To optimize the solution, I used a monotonic deque.

Instead of storing values directly, the deque stores indices and maintains them in decreasing order based on their corresponding values in the array.

For every new element entering the window:

- Any smaller elements at the back of the deque are removed.
- These elements can never become the maximum while the larger element remains inside the window.

I also remove indices from the front of the deque whenever they move outside the current window.

Once the window reaches size `k`, the index at the front of the deque always corresponds to the maximum value of the current window, which is added to the answer.

## Complexity

**Time Complexity:** O(n)

Each index is added to the deque once and removed from the deque at most once.

**Space Complexity:** O(k)

The deque stores at most the indices belonging to the current window.

## Key Learning

This problem introduced the monotonic deque pattern. The key insight was that smaller elements become useless once a larger element enters the window because they can never become the maximum while that larger element remains present.

By maintaining only useful candidates for the maximum, the solution reduces the complexity from O(n × k) to O(n).