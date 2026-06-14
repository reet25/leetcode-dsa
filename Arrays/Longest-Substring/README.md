# Longest Substring Without Repeating Characters

## Problem

Given a string `s`, find the length of the longest substring without repeating characters.

---

## Approach

When I first approached this problem, I recognized that it was a sliding window problem, but I was initially stuck on the implementation details.

The solution uses two pointers representing the boundaries of the current window. Both pointers start from the beginning of the string. A hashmap is used to store the frequency count of characters currently present inside the window.

As the right pointer moves forward, every character is added to the hashmap and its frequency is increased. If adding a character causes its frequency to become greater than 1, the window becomes invalid because it contains a duplicate character.

To restore validity, the left pointer is moved forward while decreasing the frequency of characters being removed from the window. This process continues until the duplicate is eliminated and all characters in the current window are unique again.

For every valid window, the current length is calculated using:

current_length = right - left + 1

The `+1` is required because the pointers represent indices in a zero-indexed string.

The maximum valid window length encountered throughout the traversal is stored as the answer.

---

## Complexity

Time Complexity: O(n)

Each character enters the sliding window at most once and leaves it at most once.

Space Complexity: O(k)

A hashmap is used to store character frequencies, where `k` is the number of unique characters present in the string.

---

## Key Learning

This problem introduced the sliding window pattern. Instead of restarting whenever a duplicate character is found, the existing window is adjusted by moving the left pointer forward until the window becomes valid again. This allows the solution to run in linear time.
