# Subarray Sum Equals K

## Problem

Given an integer array `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals `k`.

---

## Approach

I initially approached this problem using brute force.

My first idea was to generate all possible subarrays and store their sums in an array. After thinking further, I realized storing every sum was unnecessary and switched to maintaining a running sum while expanding each subarray. This reduced space usage, but every possible subarray still needed to be examined, resulting in O(n²) time complexity.

To optimize the solution, I used a Prefix Sum + HashMap approach.

The key observation is that if:

```text
current_sum - previous_sum = k
```

then:

```text
previous_sum = current_sum - k
```

This means that for every prefix sum encountered, we only need to know whether a previous prefix sum equal to `current_sum - k` has already been seen.

A hashmap is used to store:

```text
prefix_sum → frequency
```

The hashmap is initialized with:

```python
{0:1}
```

This accounts for subarrays that begin at index 0.

For every element in the array:

1. Update the running prefix sum.
2. Calculate the required previous prefix sum:

```python
needed = current_sum - k
```

3. If `needed` exists in the hashmap, add its frequency to the answer.
4. Store the current prefix sum in the hashmap.

By reusing previously computed prefix sums, the solution avoids generating and checking every possible subarray.

---

## Complexity

### Time Complexity: O(n)

The array is traversed once, and all hashmap operations take O(1) on average.

### Space Complexity: O(n)

The hashmap can store up to O(n) distinct prefix sums.

---

## Key Learning

This problem demonstrated how prefix sums can transform an O(n²) subarray problem into an O(n) solution. Instead of explicitly checking every subarray, previously seen prefix sums can be stored and reused to instantly determine whether a valid subarray ending at the current position exists.

It also reinforced the importance of storing frequencies rather than just values, since the same prefix sum can occur multiple times and each occurrence may contribute to a valid answer.
