# 👉👈 Two Pointers — Memory Card

> **Pattern:** Use two index variables moving along an iterable (toward each other, or in parallel) to reduce O(n²) brute force down to O(n) time with O(1) space.

---

## What is it?

**Two pointers** is a technique where two integer variables track positions in an array or string, moving strategically so you avoid nested loops.

```
arr = [1, 2, 4, 6, 8, 9, 14, 15]
       ↑                       ↑
      left                   right
      moves →             ← moves
```

Instead of checking every pair (O(n²)), you exploit structure (sorted order, symmetry, merge logic) to advance pointers intelligently — each step eliminates candidates permanently.

---

## The Core Formula

**Method 1 — Converging (single iterable):**
```
left = 0
right = len(arr) - 1

while left < right:
    if condition met:
        return result
    elif need bigger value:
        left++
    else:
        right--
```

**Method 2 — Parallel (two iterables):**
```
i = 0, j = 0

while i < len(arr1) AND j < len(arr2):
    process arr1[i] and arr2[j]
    advance i, j, or both

while i < len(arr1): process arr1[i]; i++
while j < len(arr2): process arr2[j]; j++
```

**Why it works:** Each pointer can only move forward (or inward) — it never backtracks. So the total number of steps across all iterations is bounded by the length of the input(s). The key insight is that moving a pointer *permanently* rules out one direction of search.

---

## Visual

**Palindrome check on `"racecar"`:**
```
r  a  c  e  c  a  r
↑                 ↑
left            right   → 'r' == 'r' ✅  →  both move inward

r  a  c  e  c  a  r
   ↑           ↑
   left       right     → 'a' == 'a' ✅  →  both move inward

r  a  c  e  c  a  r
      ↑     ↑
      left right        → 'c' == 'c' ✅  →  both move inward

r  a  c  e  c  a  r
         ↑
      left==right       → pointers met → return true ✅
```

**Two Sum on sorted `[1, 2, 4, 6, 8, 9, 14, 15]`, target = 13:**
```
1 + 15 = 16 > 13  →  right--
1 + 14 = 15 > 13  →  right--
1 +  9 = 10 < 13  →  left++
2 +  9 = 11 < 13  →  left++
4 +  9 = 13 = 13  →  ✅ found!
```

---

## Building the Solution

**Converging two pointers (palindrome):**
```
function isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return false
        left++
        right--
    return true
```
Cost: O(n) time, O(1) space

**Parallel two pointers (merge sorted arrays):**
```
function mergeSorted(arr1, arr2):
    ans = []
    i = 0, j = 0
    while i < len(arr1) AND j < len(arr2):
        if arr1[i] <= arr2[j]:
            append arr1[i] to ans
            i++
        else:
            append arr2[j] to ans
            j++
    while i < len(arr1): append arr1[i] to ans; i++
    while j < len(arr2): append arr2[j] to ans; j++
    return ans
```
Cost: O(n + m) time, O(n + m) space for output

---

## Complexity

| Approach | Time | Space |
|---|---|---|
| Brute force (all pairs) | O(n²) | O(1) |
| Two pointers — converging | O(n) | O(1) |
| Brute force (combine + sort) | O(n log n) | O(n) |
| Two pointers — parallel merge | O(n + m) | O(n + m) |

> Moving from O(n²) → O(n) means an array of 10,000 elements goes from ~100M operations to ~10K.

---

## Key Facts

| | |
|---|---|
| 📦 **What it stores** | Two integer indices into an array or string |
| ⚡ **Main benefit** | Eliminates nested loops; linear time on sorted/symmetric input |
| 🔧 **Type of technique** | Index manipulation / greedy pointer advancement |
| 💾 **Space trade-off** | O(1) extra space (pointers only); output array may be O(n) |
| 🚫 **Brute force cost** | O(n²) for pair problems; O(n log n) for merge problems |

---

## Common Use-Cases

- ✅ Check if a string or array is a palindrome
- ✅ Find a pair in a **sorted** array that sums to a target
- ✅ Merge two sorted arrays into one sorted array
- ✅ Remove duplicates in-place from a sorted array
- ✅ Reverse an array or string in-place
- ✅ Determine if one string is a subsequence of another

---

## When to Reach for Two Pointers

> 👀 **Trigger signals:** The input is sorted (or order matters), you're searching for a pair/triplet, checking symmetry, or merging two sequences — and a nested loop feels wasteful. If you catch yourself writing `for i ... for j ...` on array data, ask: *can two pointers collapse this to one pass?*

---

## Quick Reference

```
// METHOD 1: Converging — single sorted array or symmetric string
left = 0;  right = len - 1
while left < right:
    if want bigger sum/value → left++
    if want smaller sum/value → right--
    if found → return result

// METHOD 2: Parallel — two sorted arrays
i = 0;  j = 0
while i < n AND j < m:
    process smaller of arr1[i], arr2[j]; advance that pointer
exhaust remaining elements with solo while loops

// COMPLEXITY GUARANTEE
// Both methods: O(n) or O(n+m) time, O(1) extra space
// because each pointer moves at most n steps total
```
