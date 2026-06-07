# Best Time to Buy and Sell Stock

## Problem

Given an array where prices[i] represents the price of a stock on day i, determine the maximum profit that can be achieved by buying once and selling once.

---

## Approach

Initially, I thought about solving this problem using a brute force approach with nested loops where I compare every possible buying day with every possible selling day and calculate profit.

While implementing it, I realized that instead of checking all pairs, we only need to continuously track two things:

- minimum buying price seen so far
- maximum profit obtained so far

For every price in the array:

- update the minimum buying price if a lower price is found
- calculate profit if current price is used as selling price
- update maximum profit accordingly

This removes the need for checking every pair explicitly.

---

## Algorithm Idea

For every element:

- minimum_price = minimum(previous minimum, current price)
- profit = current price - minimum_price
- maximum_profit = maximum(previous maximum profit, profit)

---

## Complexity

Time Complexity: O(n)

Space Complexity: O(1)

---

## Key Learning

This problem introduces the running minimum tracking pattern where previous information is continuously maintained to avoid recomputation.