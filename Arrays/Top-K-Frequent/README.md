# Top K Frequent Elements

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements.

The answer may be returned in any order.

---

## Approach

I initially solved this problem by counting the frequency of every element using a dictionary and then sorting the elements based on their frequencies. While this approach works correctly, sorting introduces an O(n log n) time complexity in the worst case.

The problem includes a follow-up asking for a solution better than O(n log n), which motivated a different approach.

The key observation is that the frequency of any element cannot exceed the length of the input array. Using this fact, I created a bucket array where:

* The index represents a frequency.
* Each bucket stores all numbers that occur with that frequency.

For example:

```text
Frequency 1 → [3]
Frequency 2 → [2]
Frequency 3 → [1]
```

After building the buckets, I traversed them from highest frequency to lowest frequency. Since higher frequencies appear at larger indices, traversing in reverse order automatically gives the most frequent elements first.

Elements are collected until `k` answers have been found.

---

## Complexity

### Time Complexity: O(n)

* Building the frequency dictionary takes O(n).
* Filling the buckets takes O(n).
* Traversing all buckets takes O(n).

Overall complexity is O(n).

### Space Complexity: O(n)

* The frequency dictionary stores up to n distinct elements.
* The bucket structure stores all elements grouped by frequency.

Overall auxiliary space is O(n).

---

## Key Learning

This problem demonstrated how constraints can be used to avoid sorting entirely. Since frequencies are bounded by the size of the input array, bucket sort can be used to group elements by frequency and retrieve the most frequent elements in linear time.

Another important takeaway was understanding that nested loops do not automatically imply O(n²). In this solution, each element is placed into exactly one bucket and visited only once during traversal, keeping the overall complexity linear.
