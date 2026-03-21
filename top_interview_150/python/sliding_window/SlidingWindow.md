# 🪟 Sliding Window — Memory Card

> **Pattern:** Expand right → shrink left when invalid → always slides rightward → O(n)

---

## What is it?

Sliding Window is a technique to efficiently find **valid subarrays** (contiguous sections of an array or string). It uses **two pointers** — `left` and `right` — to define the bounds of a "window" that grows and shrinks as it slides across the input.

- **Add** an element → increment `right`
- **Remove** an element → increment `left`
- The window always moves **rightward**, never backward

---

## Key Concept: "Valid" Subarrays

Every sliding window problem defines validity using two things:

| Term | Meaning | Example |
|---|---|---|
| **Constraint metric** | An attribute of the subarray | sum, product, count of zeros |
| **Numeric restriction** | The limit on that metric | `<= k`, `at most 1`, `< 100` |

A subarray is **valid** when its constraint metric satisfies the restriction.

---

## Pseudocode — Dynamic Window (most common)

```
function fn(arr, k):
    left = 0
    curr = 0        // tracks the constraint metric
    answer = 0

    for right in range(len(arr)):
        curr += arr[right]          // expand window

        while WINDOW_IS_INVALID:    // e.g. curr > k
            curr -= arr[left]       // shrink window
            left++

        answer = max(answer, right - left + 1)

    return answer
```

---

## Pseudocode — Fixed Window Size k

```
function fn(arr, k):
    curr = 0

    // build first window
    for i in range(k):
        curr += arr[i]

    answer = curr
    for i in range(k, len(arr)):
        curr += arr[i]        // add new right element
        curr -= arr[i - k]    // remove old left element
        answer = max(answer, curr)

    return answer
```

---

## Visual — Dynamic Window

```
nums = [3, 2, 1, 3, 1, 1],  k = 5

[3]           sum=3 ✓  expand →
[3, 2]        sum=5 ✓  expand →
[3, 2, 1]     sum=6 ✗  shrink ←
[2, 1]        sum=3 ✓  expand →
[2, 1, 3]     sum=6 ✗  shrink ←
[1, 3]        sum=4 ✓  expand →
[1, 3, 1]     sum=5 ✓  expand →
[1, 3, 1, 1]  sum=6 ✗  shrink ←
[3, 1, 1]     sum=5 ✓  ← longest valid = 3
```

---

## Counting Valid Subarrays

When a problem asks **how many** valid subarrays exist, use this trick:

> After each iteration (once the window is valid), **add `right - left + 1`** to the answer.

This works because fixing `right` and choosing any `left` value from `left` to `right` gives exactly `right - left + 1` valid subarrays ending at `right`.

---

## Key Facts

| | |
|---|---|
| ⚡ **Why it's fast** | `right` moves n times, `left` moves at most n times → max 2n iterations |
| 🔄 **Amortized O(1)** | The inner `while` loop averages out — left never resets |
| 💾 **Space** | O(1) — only need `left`, `right`, `curr`, and `answer` |
| 📐 **Window length formula** | `right - left + 1` |
| 🚫 **Brute force cost** | O(n²) subarrays exist — sliding window avoids checking all of them |

---

## Complexity

| Time | Space |
|------|-------|
| **O(n)** | **O(1)** |

---

## Two Window Types at a Glance

| Type | When to use | Left moves when... |
|---|---|---|
| **Dynamic** | "longest/shortest valid subarray" | constraint is violated |
| **Fixed (size k)** | "subarray of length exactly k" | every step (`i - k`) |

---

## Common Use-Cases

- ✅ Longest subarray with sum ≤ k
- ✅ Longest substring with at most one "0"
- ✅ Number of subarrays with product < k
- ✅ Max sum of subarray of length k
- ✅ Longest substring without repeating characters
- ✅ Minimum window substring

---

## When to Reach for Sliding Window

> 👀 If a problem mentions **subarrays or substrings** and asks for the **best** (longest, shortest, max sum) or **count** of valid ones — think **Sliding Window** immediately.

---

## Quick Tip

> The `while` loop inside the `for` loop does **not** make this O(n²). `left` only ever increases and can move at most `n` times total across the entire run — this is **amortized O(1)** per iteration.
