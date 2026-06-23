# Minimum Window Substring

## Problem

Given two strings `s` and `t`, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window.

If no such substring exists, return an empty string.

## Approach

This was one of the most challenging sliding window problems I had solved so far.

My initial thought was to use a hashmap for the target string and another hashmap for the current window, then directly compare the two hashmaps to determine whether a valid window had been found. However, I realized that this approach would not work because a valid window can contain additional characters that are not present in the target string.

To solve this, I created:

- A hashmap called `need` to store the required frequency of each character in `t`.
- A hashmap called `window` to store the frequency of characters inside the current window.

I then introduced two variables:

- `required` = number of unique characters that must be satisfied.
- `formed` = number of character requirements currently satisfied.

As the right pointer expands the window, character frequencies are added to the window hashmap. Whenever a character's frequency reaches its required frequency, `formed` is incremented.

Once `formed == required`, the current window contains all required characters. At this point, I attempt to shrink the window from the left while maintaining validity. During shrinking, I continuously update the smallest valid window found so far.

If removing a character causes its frequency in the window to fall below the required frequency, the window becomes invalid, `formed` is decremented, and expansion resumes.

## Complexity

**Time Complexity:** O(n)

Both the left and right pointers move through the string at most once.

**Space Complexity:** O(m)

Where `m` is the number of unique characters stored in the hashmaps.

## Key Learning

The most important lesson from this problem was that a valid window does not necessarily mean the current window hashmap is equal to the target hashmap. A window may contain extra characters and still be valid.

The `formed` and `required` technique provides an efficient way to determine whether all required character frequencies have been satisfied, making it possible to solve the problem in linear time.