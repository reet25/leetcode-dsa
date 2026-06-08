# Ransom Note

## Problem

Given two strings `ransomNote` and `magazine`, determine whether the ransom note can be constructed using the characters from magazine.

Each character in magazine can only be used once.

---

## Approach

Initially, I recognized that this problem was similar to Valid Anagram since both problems are based on frequency counting.

At first, I considered storing the frequency of characters from the ransom note inside a dictionary and reducing frequencies using magazine characters. Although this works, it requires an additional validation step at the end.

After thinking further, I realized that storing frequencies of magazine characters is more efficient because it allows early termination.

The approach is:

* Store frequencies of all characters from magazine in a dictionary
* Traverse ransomNote character by character
* If a required character is unavailable or its frequency becomes zero, immediately return False
* Otherwise reduce its frequency and continue

This eliminates the need for an extra validation loop.

---

## Algorithm Idea

For every character:

* Store magazine frequencies
* Traverse ransom note
* If character unavailable → return False
* Otherwise decrease frequency
* If traversal completes → return True

---

## Complexity

Time Complexity: O(n + m)

* n = length of ransomNote
* m = length of magazine

Space Complexity: O(k)

* k = number of unique characters stored in dictionary

---

## Key Learning

This problem reinforced the frequency map pattern while introducing the idea of resource consumption, where available frequencies are gradually consumed instead of only comparing counts.
