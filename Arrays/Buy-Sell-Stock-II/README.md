# Best Time to Buy and Sell Stock II

## Problem

Given an array `prices` where `prices[i]` is the price of a stock on the ith day, return the maximum profit that can be achieved. Multiple transactions are allowed, but you must sell the stock before buying again.

## Approach

This problem is a variation of the Buy and Sell Stock problem solved earlier. The major difference is that multiple transactions are allowed instead of only one.

Rather than searching for a single best buying and selling point, the goal is to maximize the total profit obtained from all valid transactions.

The key observation is that every positive price increase can contribute to the final answer. While traversing the array, I compare the current day's price with the previous day's price. If the current price is higher, the profit from that increase is added to the total profit. If the price decreases, that transaction is ignored since it would result in a loss.

By adding all positive differences, the solution effectively captures every profitable transaction and guarantees the maximum possible profit.

## Complexity

**Time Complexity:** O(n)

The array is traversed once.

**Space Complexity:** O(1)

Only a few variables are used regardless of input size.

## Key Learning

This problem demonstrated how a change in constraints can lead to a completely different solution. Instead of finding a single optimal transaction, the greedy approach works by taking every profitable opportunity. The sum of all positive gains naturally produces the maximum achievable profit when multiple transactions are allowed.
