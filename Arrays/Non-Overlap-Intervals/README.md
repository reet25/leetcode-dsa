# Non-overlapping Intervals

## Problem

Given an array of intervals, return the minimum number of intervals that need to be removed so that the remaining intervals do not overlap.

## Approach

In this problem, the goal is to remove the minimum number of intervals. Instead of directly thinking about removals, I focused on keeping the maximum number of non-overlapping intervals, since both objectives are equivalent.

I first sorted the intervals according to their ending values. I then used a variable called `prev_end` to keep track of the ending value of the last interval that was accepted.

While traversing the remaining intervals, I checked whether the current interval overlapped with the previously accepted interval. If the starting value of the current interval was greater than or equal to `prev_end`, the interval could be kept and `prev_end` was updated. Otherwise, an overlap existed and the removal count was increased.

By sorting based on ending values, intervals that finish earlier are prioritized, leaving the maximum possible room for future intervals and minimizing the number of removals.

## Complexity

**Time Complexity:** O(n log n)

* Sorting the intervals takes O(n log n)
* Traversing the intervals takes O(n)

Overall complexity is O(n log n).

**Space Complexity:** O(1)

Only a few variables are used apart from the input array.

## Key Learning

This problem demonstrated a classic greedy strategy. Rather than deciding which intervals to remove directly, it is often easier to maximize the number of intervals that can be kept. Sorting by ending time and always keeping the interval that finishes earliest ensures the optimal solution.
