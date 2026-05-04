# ➕ Prefix Sum — Memory Card

> **Pattern:** Pre-process array once in O(n) → answer any subarray sum query in O(1)

---

## What is it?

A **prefix sum** is a pre-computed array where each element at index `i` holds the **sum of all elements from index 0 up to i** (inclusive).

```
nums   = [5,  2,  1,  6,  3,  8]
prefix = [5,  7,  8, 14, 17, 25]
          ↑                   ↑
        nums[0]        5+2+1+6+3+8
```

Once built, you can find the sum of **any subarray in O(1)** — no looping required.

---

## The Core Formula

Sum of subarray from index `i` to `j` (inclusive):

```
sum(i, j) = prefix[j] - prefix[i - 1]
```

To avoid an out-of-bounds error when `i = 0`, use this safe alternative:

```
sum(i, j) = prefix[j] - prefix[i] + nums[i]
```

**Why it works:** `prefix[i - 1]` is the sum of everything *before* index `i`. Subtracting it from `prefix[j]` leaves exactly the elements from `i` to `j`.

---

## Visual

```
nums   = [5,  2,  1,  6,  3,  8]
                     ↑_________↑   ← want sum of this range

prefix[5] = 25   (sum of everything up to end)
prefix[2] = 8    (sum of everything before range)

Answer = 25 - 8 = 17  ✓  (6 + 3 + 8 = 17)
```

---

## Building the Prefix Sum

```
prefix = [nums[0]]

for i from 1 to nums.length - 1:
    prefix.append(nums[i] + prefix[i - 1])
```

- Start with just the first element
- Each new entry = current element + previous prefix value
- **Cost:** O(n) time, O(n) space

---

## Space Optimization — No Array Needed

When queries are sequential (left-to-right), you can skip the array entirely:

```
total = sum(nums)         // pre-compute full sum
leftSection = 0

for i from 0 to nums.length - 2:
    leftSection += nums[i]
    rightSection = total - leftSection

    if leftSection >= rightSection:
        answer++
```

Same prefix sum concept, O(1) space.

---

## Complexity

| Phase | Time | Space |
|---|---|---|
| **Build prefix array** | O(n) | O(n) |
| **Each subarray query** | O(1) | O(1) |
| **vs. brute force per query** | O(n) ❌ | — |

> Building once saves huge time across many queries:
> `m` queries go from **O(n × m)** → **O(n + m)**

---

## Key Facts

| | |
|---|---|
| 📦 **What it stores** | `prefix[i]` = sum of `nums[0..i]` |
| ⚡ **Main benefit** | Any subarray sum in O(1) after O(n) build |
| 🔧 **Type of technique** | Pre-processing / pre-computation |
| 💾 **Space trade-off** | O(n) extra space, but queries become O(1) |
| 🚫 **Brute force cost** | O(n) per query → O(n²) total for many queries |

---

## Common Use-Cases

- ✅ Sum of any subarray in O(1)
- ✅ Answering multiple range-sum queries
- ✅ Splitting arrays into two sections by sum
- ✅ Counting subarrays with sum equal to / less than / greater than k
- ✅ 2D prefix sums for matrix range queries

---

## When to Reach for Prefix Sum

> 👀 If a problem asks for **sums of subarrays** — especially with **multiple queries** or comparisons between sections — think **Prefix Sum** immediately.

---

## Quick Reference

```
// Build
prefix[0] = nums[0]
prefix[i] = nums[i] + prefix[i-1]

// Query sum from i to j
sum = prefix[j] - prefix[i-1]        // i > 0
sum = prefix[j] - prefix[i] + nums[i] // safe for any i
```