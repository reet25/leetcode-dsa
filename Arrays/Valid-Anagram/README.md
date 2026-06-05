# Valid Anagram

## Problem
Check whether two strings are anagrams of each other.

---

## Approach

I started with a sorting-based approach, but later moved to frequency counting since anagram problems depend on character frequency rather than order.

Initial attempt used two dictionaries to store frequencies separately, but this increased space usage unnecessarily.

Final optimized approach uses a single dictionary:
- Store frequency of characters from first string
- Reduce counts using second string
- If any mismatch or negative count occurs, return False
- Finally ensure all counts are zero

Also added a length check as an early optimization.

---

## Complexity

Time Complexity: O(n + m)  
Space Complexity: O(k), where k is number of unique characters

---

## Key Learning

Frequency maps are a powerful pattern for problems where order does not matter.