# ⚡ Two Pointers — Memory Card

> **Pattern:** Start at edges → converge toward center → guaranteed O(n)

---

## What is it?

Two Pointers uses **two integer indices** — typically `left` & `right` — that traverse an array or string from **opposite ends toward each other**.

Because the gap closes by at least one step per iteration, the while-loop runs at most **O(n)** times. If each step is O(1), the whole algorithm is **linear**.

---

## Pseudocode Template

```
function twoPointers(arr):
    left  = 0
    right = arr.length - 1

    while left < right:
        // logic depends on the problem
        if condition_A:
            left++
        else if condition_B:
            right--
        else:
            left++; right--   // both converge
```

---

## Step-by-Step Setup

1. Set `left = 0` (first index) and `right = input.length - 1` (last index)
2. Run a `while left < right` loop
3. Each iteration: move one or both pointers **inward** based on your condition

---

## Example — Palindrome Check

**Input:** `"racecar"`

```
Step 0:  [r] a c e c a [r]   →  'r' == 'r' ✓  →  left++, right--
Step 1:   r [a] c e c [a] r  →  'a' == 'a' ✓  →  left++, right--
Step 2:   r  a [c] e [c] a r →  'c' == 'c' ✓  →  left++, right--
Step 3:   r  a  c [e] c  a r →  left == right  →  stop ✓
```

**Result:** Palindrome ✅

---

## Key Facts

| | |
|---|---|
| ⚡ **Why it's fast** | Pointers start `n` apart and close each step → at most O(n) iterations |
| 🧠 **When to use** | Sorted arrays, palindromes, pair-sum targets, symmetric comparisons |
| 🔄 **Loop condition** | `while left < right` — stops when pointers meet or cross |
| 💾 **Space** | O(1) — no extra data structures needed |

---

## Complexity

| Time | Space |
|------|-------|
| **O(n)** | **O(1)** |

---

## Common Use-Cases

- ✅ Palindrome check
- ✅ Two-sum on a sorted array
- ✅ Reverse array in-place
- ✅ Remove duplicates
- ✅ Container with most water
- ✅ Squaring a sorted array
- ✅ Trapping rain water

---

## Quick Tip

> If work inside each loop iteration is **O(1)** and you use two pointers, your overall runtime is **O(n)** — usually the best possible for array problems.

