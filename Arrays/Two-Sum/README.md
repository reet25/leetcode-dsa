# Two Sum

## Problem

Given an array of integers and a target integer, return indices of two numbers such that they add up to the target.

---

## Approach

Use a hashmap to store previously seen elements and their indices.

For every element:

1. Compute required complement
2. Check if complement exists in hashmap
3. If yes, return indices
4. Otherwise store current element

---

## Complexity Analysis

Time Complexity: O(n)

Space Complexity: O(n)

---

## Key Learning

Hashmaps allow pair-search problems to be optimized from O(n²) to O(n) by enabling constant time lookups.