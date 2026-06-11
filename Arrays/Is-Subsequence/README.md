# Is Subsequence

## Problem

Given two strings s and t, determine whether s is a subsequence of t.

A subsequence is formed by deleting some (or no) characters from a string without changing the relative order of the remaining characters.

---

## Approach

In this problem, I learned another variation of the Two Pointers technique where both pointers start from the beginning of their respective strings.

The goal is to check whether all characters of string s appear in string t in the same order.

I used two pointers:

* One pointer traverses string s.
* Another pointer traverses string t.

If the characters at both pointers match, both pointers move forward because the current character of s has been successfully found.

If the characters do not match, only the pointer of t moves forward because we are still searching for the current character of s.

The process continues until either string t is fully traversed or all characters of s have been matched.

If the pointer of s reaches the end of the string, it means every character was found in the correct order and the subsequence exists.

---

## Complexity

Time Complexity: O(n)

where n is the length of string t.

Space Complexity: O(1)

No extra data structures are used.

---

## Key Learning

This problem introduced a forward-moving Two Pointers pattern. Instead of comparing values from opposite ends, both pointers move from left to right while maintaining the relative order requirement of a subsequence.
