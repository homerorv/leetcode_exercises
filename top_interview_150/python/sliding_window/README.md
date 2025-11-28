# Sliding Window — Summary

This note summarizes the Sliding Window technique for array / string problems.
https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4502/

## What it is
- The sliding window is a way to examine contiguous subarrays (or substrings) by maintaining a window defined by two indices (usually `left` and `right`).
- Instead of recomputing values from scratch for each candidate subarray, you update the window incrementally as it moves across the input.

## When to use
- Problems that ask about contiguous ranges: sums, maxima/minima over windows, counts of distinct elements, longest/shortest subarray that satisfies a condition, etc.

## Two main patterns
- Fixed-size window: the window length is constant (e.g., find all windows of size `k`). Move `right` and drop the leftmost element when the window grows beyond `k`.
- Variable-size (dynamic) window: expand `right` to include elements until a condition is met, then shrink `left` to try to restore or re-evaluate the condition (e.g., minimum-length subarray with sum >= target, longest substring with at most K distinct characters).

## Typical implementation steps (variable-size)
1. Initialize `left = 0` and iterate `right` from `0` to `n-1`.
2. Add `nums[right]` (or the new character) to your running state (sum, counts, deque, etc.).
3. While the window satisfies (or fails) the target condition, update the answer and move `left` forward to shrink the window, updating your running state as you remove elements.
4. Continue until `right` reaches the end.

## Common data maintained inside a window
- Running sum or running count.
- Frequency map (for counting distinct elements or checking requirements).
- Monotonic deque (for sliding-window maximum/minimum problems) that allows amortized O(1) retrieval of extreme values.

## Complexity
- Each element is typically visited at most twice (once by `right`, once by `left`), so time complexity is usually O(n).
- Space complexity depends on the auxiliary data structure: O(1) for simple sums, O(k) or O(n) for maps/deques.

## Tips and pitfalls
- Carefully maintain state when moving `left` (e.g., decrement counts, remove from deque).
- Use a monotonic deque for max/min queries to avoid O(k) scans inside the window.
- Translate problem constraints into a boolean condition that describes when to expand or shrink the window.

## Example problems
- Minimum-size subarray with sum >= target (variable-size window and running sum).
- Sliding window maximum (fixed window with monotonic deque).
- Longest substring with at most K distinct characters (variable window with frequency map).

## Pseudocode

        function fn(arr):
            left = 0
            for (int right = 0; right < arr.length; right++):
                Do some logic to "add" element at arr[right] to window

                while WINDOW_IS_INVALID:
                    Do some logic to "remove" element at arr[left] from window
                    left++

                Do some logic to update the answer

Puts all together:

        function fn(nums, k):
            left = 0
            curr = 0
            answer = 0
            for (int right = 0; right < nums.length; right++):
                curr += nums[right]
                while (curr > k):
                    curr -= nums[left]
                    left++

                answer = max(answer, right - left + 1)

            return answer

---
Reference: inspired by the LeetCode Interview Crash Course: Sliding Window (array/strings) overview.
