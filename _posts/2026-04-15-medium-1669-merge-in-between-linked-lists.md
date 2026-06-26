---
layout: post
title: "[Medium] 1669. Merge In Between Linked Lists"
date: 2026-04-15
categories: [leetcode, medium, linked-list]
tags: [leetcode, medium, linked-list, pointer-manipulation]
permalink: /2026/04/15/medium-1669-merge-in-between-linked-lists/
---
You are given two linked lists: `list1` and `list2` of sizes `n` and `m` respectively. Remove `list1`'s nodes from the `a`-th node to the `b`-th node (0-indexed), and put `list2` in their place.

## Examples

**Example 1:**

```
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]

list1:  10 → 1 → 13 → [6 → 9] → 5
                        ↑ remove ↑
list2:  1000000 → 1000001 → 1000002

Result: 10 → 1 → 13 → 1000000 → 1000001 → 1000002 → 5
```

**Example 2:**

```
Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
```

## Constraints

- `3 <= list1.length <= 10^4`
- `1 <= a <= b < list1.length - 1`
- `1 <= list2.length <= 10^4`

The constraints guarantee `a >= 1` and `b < n - 1`, so there is always at least one node before `a` and one node after `b`.

## Thinking Process

### What Do We Need?

We're splicing `list2` into `list1` by removing positions `a..b`. That means three pointer rewirings:

```
prevA → list2_head → ... → list2_tail → afterB
```

We need:
1. **`prevA`** -- the node at index `a - 1` (just before the removed segment)
2. **`afterB`** -- the node at index `b + 1` (just after the removed segment)
3. **`tail2`** -- the last node of `list2`

### Why No Dummy Node Needed?

Since `a >= 1`, the head of `list1` is never removed, so we don't need a dummy node to protect the head.

### Walk-through

```
list1: 10 → 1 → 13 → 6 → 9 → 5     a=3, b=4
index:  0   1    2   3   4   5

Step 1: Walk to index a-1 = 2
  prevA = node(13)

Step 2: From prevA, walk (b - a + 1) more steps to reach node at index b
  then afterB = that node's next
  afterB = node(5)

Step 3: Find tail of list2
  list2: 1000000 → 1000001 → 1000002
  tail2 = node(1000002)

Step 4: Rewire
  prevA.next = list2         →  13 → 1000000
  tail2.next = afterB        →  1000002 → 5

Result: 10 → 1 → 13 → 1000000 → 1000001 → 1000002 → 5  ✓
```

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Linked list: pointer walk</text>

  <rect x="30" y="50" width="44" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="52" y="68" text-anchor="middle" font-size="12">1</text>
  <path d="M74 66h16" stroke="#8B8680" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="90" y="50" width="44" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="112" y="68" text-anchor="middle" font-size="12">2</text>
  <path d="M134 66h16" stroke="#8B8680" stroke-width="2"/>
  <rect x="150" y="50" width="44" height="32" rx="4" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="172" y="68" text-anchor="middle" font-size="12">3</text>
  <text x="130" y="105" text-anchor="middle" font-size="11" fill="#6B6560">slow → → fast (2x speed)</text>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Iterative pointer walk** *(this problem)* | O(n) | O(1) | Traversal, insertion |
| Dummy head node | O(n) | O(1) | Simplify head-edge cases |
| Reversal (3-pointer) | O(n) | O(1) | Reverse sublist or full list |
| Slow/fast pointers | O(n) | O(1) | Middle, cycle, merge lists |

## Solution
```cpp
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode dummy(0);
        dummy.next = list1;

        ListNode* prevA = &dummy;
        for (int i = 0; i < a; ++i) {
            prevA = prevA->next;
        }

        ListNode* afterB = prevA;
        for (int i = 0; i <= b - a; ++i) {
            afterB = afterB->next;
        }
        afterB = afterB->next;

        prevA->next = list2;

        ListNode* tail = list2;
        while (tail->next) {
            tail = tail->next;
        }
        tail->next = afterB;

        return dummy.next;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** ### What Do We Need?

**How the code works:**
1. **`prevA`** -- the node at index `a - 1` (just before the removed segment)
2. **`afterB`** -- the node at index `b + 1` (just after the removed segment)
3. **`tail2`** -- the last node of `list2`

**Walkthrough** — input `list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]`, expected output `[10,1,13,1000000,1000001,1000002,5]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

**Time:** O(n + m) -- traverse `list1` up to index `b`, then traverse all of `list2` · **Space:** O(1) -- only pointer variables## Key Details
## Without Dummy (Slightly Simpler)

Since the constraints guarantee `a >= 1`, we can skip the dummy:
```cpp
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* prevA = list1;
        for (int i = 0; i < a - 1; ++i) {
            prevA = prevA->next;
        }

        ListNode* afterB = prevA;
        for (int i = 0; i <= b - a + 1; ++i) {
            afterB = afterB->next;
        }

        prevA->next = list2;

        ListNode* tail = list2;
        while (tail->next) {
            tail = tail->next;
        }
        tail->next = afterB;

        return list1;
    }
};
```

## Common Mistakes

- **Off-by-one on `prevA`:** Walking `a` steps from head lands on index `a`, but we need index `a - 1`. Use a dummy or walk `a - 1` steps.
- **Off-by-one on `afterB`:** Forgetting the final `.next` after reaching the node at index `b`.
- **Forgetting to find `tail2`:** The connection `list2_tail → afterB` is easy to miss if you only set `prevA → list2`.

## Key Takeaways

- **"Splice list into list"** = find the boundary pointers (`prevA`, `afterB`) + find the tail of the inserted list + three pointer rewirings
- When the head can never be removed, a dummy node is optional but can simplify uniform traversal
- Constraints like `a >= 1` and `b < n - 1` eliminate edge cases -- always read them carefully

## Related Problems

- [206. Reverse Linked List](https://www.leetcode.com/problems/reverse-linked-list/) -- basic pointer manipulation
- [25. Reverse Nodes in k-Group](https://www.leetcode.com/problems/reverse-nodes-in-k-group/) -- segment-based list surgery
- [86. Partition List](https://www.leetcode.com/problems/partition-list/) -- pointer rewiring with dummy nodes
- [143. Reorder List](https://www.leetcode.com/problems/reorder-list/) -- find middle, reverse, merge

## References

- [LC 1669: Merge In Between Linked Lists on LeetCode](https://www.leetcode.com/problems/merge-in-between-linked-lists/)
- [LeetCode Discuss — LC 1669: Merge In Between Linked Lists](https://www.leetcode.com/problems/merge-in-between-linked-lists/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/merge-in-between-linked-lists/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
