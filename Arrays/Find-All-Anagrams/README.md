# Find All Anagrams in a String

## Problem

Given two strings `s` and `p`, return all starting indices of substrings in `s` that are anagrams of `p`.

An anagram contains exactly the same characters with the same frequencies, but possibly in a different order.

---

## Approach

I first created a frequency dictionary for the pattern string `p`.

Then I used a sliding window of fixed size equal to the length of `p`.

As the window moves through the string:

* Add the new character entering the window.
* Remove the character leaving the window when the size exceeds the required length.
* Compare the frequency dictionary of the current window with the pattern dictionary.

Whenever the two dictionaries match, the current starting index is added to the answer.

One important detail was ensuring that after shrinking an oversized window, the newly formed valid window is still checked. Missing this step can cause valid anagrams to be skipped.

---

## Complexity

### Time Complexity: O(n)

The sliding window moves through the string once.

### Space Complexity: O(k)

Where `k` is the number of distinct characters stored in the frequency dictionaries.

---

## Key Learning

This problem strengthened my understanding of fixed-size sliding windows. The main idea is to maintain information about the current window incrementally instead of recomputing it from scratch for every substring. This reduces the complexity from O(n × m) to O(n).
