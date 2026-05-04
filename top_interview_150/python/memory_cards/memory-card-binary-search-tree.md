# 🌳 Binary Search Tree — Memory Card

> **Pattern:** Hierarchical sorted structure where left < node < right at every level — O(log n) avg for search, insert, delete; degrades to O(n) when unbalanced.

---

## What is it?

A **Binary Search Tree (BST)** is a binary tree where every node satisfies one invariant: all values in its left subtree are smaller, and all values in its right subtree are larger.

```
Insert [8, 3, 10, 1, 6, 14, 4, 7] into a BST:

           8
          / \
         3   10
        / \    \
       1   6   14
          / \
         4   7

Left of 8 → all < 8: {3, 1, 6, 4, 7} ✓
Right of 8 → all > 8: {10, 14}       ✓
This holds recursively at every subtree.
```

---

## The Core Invariant

```
For every node N:
  max(N.left subtree)  < N.val < min(N.right subtree)
```

**Why it works:** At each node, you eliminate half the remaining candidates — if the key is smaller, the entire right subtree is irrelevant, and vice versa. This is the same logic as binary search on a sorted array, but dynamic (supports insert/delete without shifting).

---

## Visual — Searching for 6

```
Tree:          Search key = 6
       8        Step 1: 6 < 8  → go left
      / \
     3   10     Step 2: 6 > 3  → go right
    / \
   1   6        Step 3: 6 == 6 → FOUND ✓

Path traced: 8 → 3 → 6   (3 comparisons, not 8)
```

---

## Building the BST

```
function insert(root, key):
  if root is null:
    return new Node(key)        // base case: found the spot
  if key < root.val:
    root.left  = insert(root.left,  key)
  else if key > root.val:
    root.right = insert(root.right, key)
  // key == root.val → duplicate, ignore (or handle per policy)
  return root

// Build from array [8, 3, 10, 1, 6, 14]:
root = null
for each value in [8, 3, 10, 1, 6, 14]:
  root = insert(root, value)
```

**Cost:** O(h) per insert where h = height. O(n log n) to build from n elements (balanced case).

---

## Deletion — Three Cases

```
Case 1 — Leaf node (no children):
  Remove directly.
  Delete 1:  3          →   3
            / \              \
           1   6              6

Case 2 — One child:
  Replace node with its child.
  Delete 10:  10         →   14
                \
                14

Case 3 — Two children:
  Replace with inorder successor (leftmost node of right subtree),
  then delete the successor from the right subtree.
  Delete 3:   3          →   4
             / \            / \
            1   6          1   6
               /               \
              4                 (4 deleted from here)
```

---

## Traversals

```
Tree:        Inorder   (L→Root→R): 1 3 4 6 7 8 10 14  ← sorted!
       8     Preorder  (Root→L→R): 8 3 1 6 4 7 10 14
      / \    Postorder (L→R→Root): 1 4 7 6 3 14 10 8
     3   10  Level-order (BFS):    8 3 10 1 6 14 4 7
    / \    \
   1   6   14
      / \
     4   7

Pseudocode — inorder:
  function inorder(node):
    if node is null: return
    inorder(node.left)
    visit(node)          // prints in sorted order
    inorder(node.right)
```

---

## Complexity

| Phase | Average | Worst Case | Notes |
|---|---|---|---|
| Search | O(log n) | O(n) | Worst = skewed tree |
| Insert | O(log n) | O(n) | Always inserts as leaf |
| Delete | O(log n) | O(n) | Finding successor costs O(h) |
| Inorder traversal | O(n) | O(n) | Visits every node once |
| Space (tree storage) | O(n) | O(n) | One node per element |
| Space (call stack) | O(log n) | O(n) | Recursion depth = height |

> Brute force sorted lookup in an array costs O(n) per search with O(1) insert overhead, or O(log n) search but O(n) insert. BST gives O(log n) for **both** operations simultaneously — the gain is dynamic sorted access without shifting.

---

## Key Facts

| | |
|---|---|
| 📦 **What it stores** | Nodes with val, left pointer, right pointer |
| ⚡ **Main benefit** | O(log n) avg search + insert + delete in one structure |
| 🔧 **Type of technique** | Divide & conquer tree — halves search space at each node |
| 💾 **Space trade-off** | O(n) extra vs. a plain array; each node needs two pointers |
| 🚫 **Brute force cost** | O(n) linear scan per search on unsorted data |

---

## Common Use-Cases

- ✅ Implementing sorted sets and maps (`std::map`, Java `TreeMap`, Python `SortedList`)
- ✅ Range queries: "find all values between 10 and 50" — traverse a bounded subtree
- ✅ Symbol tables in compilers — fast identifier lookup with dynamic insertion
- ✅ Database indexing (foundation for B-trees)
- ✅ Auto-complete / ordered iteration — inorder gives sorted stream for free
- ✅ Base structure for self-balancing trees: AVL, Red-Black, Splay

---

## When to Reach for BST

> 👀 You need a data structure that stays **sorted at all times** and supports fast lookup, insertion, and deletion. If you find yourself sorting an array after every insert — or doing a binary search but also needing to add/remove elements — reach for a BST (or a self-balancing variant like AVL/Red-Black if worst-case O(n) is unacceptable).

---

## Quick Reference

```
// SEARCH — O(h) time
search(node, key):
  if null → not found
  if key == node.val → found
  if key < node.val  → search(node.left, key)
  else               → search(node.right, key)

// INSERT — always a new leaf
insert(node, key):
  if null → return new Node(key)
  if key < node.val → node.left  = insert(node.left, key)
  else              → node.right = insert(node.right, key)
  return node

// INORDER SUCCESSOR (used in deletion case 3)
inorder_successor(node):
  current = node.right
  while current.left is not null:
    current = current.left
  return current          // smallest in right subtree

// HEIGHT — determines performance
height(node):
  if null → return 0
  return 1 + max(height(node.left), height(node.right))
  // Balanced: h ≈ log₂(n)  |  Skewed: h = n
```
