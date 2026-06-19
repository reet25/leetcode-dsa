# Merge Intervals

## Problem

Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Approach

I initially approached this problem using a brute force mindset by comparing neighboring intervals and merging them whenever an overlap was found. While this worked for simple cases, I eventually realized that it failed when multiple intervals formed a chain of overlaps because I was comparing intervals directly instead of tracking previously merged results.

To optimize the solution, I first sorted the intervals and created a new list called `merged`. Instead of comparing intervals among themselves, every new interval was compared with the last interval already present in the `merged` list.

If the starting point of the current interval was less than or equal to the ending point of the last merged interval, an overlap existed. In that case, I updated the ending value of the last merged interval using the maximum of the two ending values. Otherwise, the current interval was added as a new interval in the result.

This approach correctly handles chains of overlapping intervals while processing the intervals in a single pass after sorting.

## Complexity

**Time Complexity:** O(n log n)

* Sorting takes O(n log n)
* Traversing the intervals takes O(n)

Overall complexity is O(n log n).

**Space Complexity:** O(n)

The merged result list can contain up to n intervals in the worst case.

## Key Learning

This problem showed that after sorting intervals, it is often better to maintain a running merged result rather than repeatedly comparing neighboring intervals. Comparing each interval with the most recently merged interval ensures that overlapping chains are handled correctly and efficiently.
