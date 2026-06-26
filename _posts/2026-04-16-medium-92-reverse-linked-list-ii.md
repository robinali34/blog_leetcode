---
layout: post
title: "[Medium] 92. Reverse Linked List II"
date: 2026-04-16
categories: [leetcode, medium, linked-list]
tags: [leetcode, medium, linked-list, reversal, pointer-manipulation]
permalink: /2026/04/16/medium-92-reverse-linked-list-ii/
---
Given the `head` of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right` (1-indexed), and return the reversed list.

## Examples

**Example 1:**

```
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

1 → [2 → 3 → 4] → 5
      ↓ reverse ↓
1 → [4 → 3 → 2] → 5
```

**Example 2:**

```
Input: head = [5], left = 1, right = 1
Output: [5]
```

## Constraints

- `1 <= n <= 500` (number of nodes)
- `-500 <= Node.val <= 500`
- `1 <= left <= right <= n`

## Thinking Process

### Break It Into 3 Parts

1. **Traverse** to the node before `left` -- call it `prev`
2. **Reverse** the sublist `[left .. right]`
3. **Reconnect**: `prev → new head of reversed sublist`, `tail of reversed sublist → node after right`

### The Head Insertion Trick

Instead of doing a standard three-pointer reversal and then reconnecting, we can use **head insertion**: repeatedly pull the node after `curr` to the front of the sublist. This avoids re-traversing and naturally keeps all connections intact.

```
Initial:  prev → [a → b → c → d] → next
                  ↑             ↑
                left          right

Step 1: move b before a
          prev → [b → a → c → d] → next

Step 2: move c before b
          prev → [c → b → a → d] → next

Step 3: move d before c
          prev → [d → c → b → a] → next
```

Each step does 3 pointer swaps and the sublist grows by one node at the front.

### Edge Cases

| Case | Handling |
|---|---|
| `left == 1` (head changes) | Dummy node absorbs head change |
| `left == right` (no-op) | Early return |
| Single node | Early return |



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

{% raw %}
```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;

        for (int i = 1; i < left; ++i) {
            prev = prev->next;
        }

        ListNode* curr = prev->next;
        for (int i = 0; i < right - left; ++i) {
            ListNode* tmp = curr->next;
            curr->next = tmp->next;
            tmp->next = prev->next;
            prev->next = tmp;
        }

        return dummy.next;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** ### Break It Into 3 Parts

**How the code works:**
1. **Traverse** to the node before `left` -- call it `prev`
2. **Reverse** the sublist `[left .. right]`
3. **Reconnect**: `prev → new head of reversed sublist`, `tail of reversed sublist → node after right`

**Walkthrough** — input `head = [1,2,3,4,5], left = 2, right = 4`, expected output `[1,4,3,2,5]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Comparison

| Aspect | Head Insertion | Classic Reversal |
|---|---|---|
| Uses dummy node | Yes (handles `left == 1`) | No (explicit `if` for `left == 1`) |
| `curr` pointer movement | Stays fixed | Advances through sublist |
| Reconnection | Automatic (pointers stay connected) | Manual (set `con.next` and `tail.next`) |
| Conceptual complexity | Lower -- single pattern repeated | Higher -- two distinct phases |

## Common Mistakes

- **Off-by-one on `prev`:** Walking `left` steps from dummy lands on node `left`, but we need node `left - 1`. Walk `left - 1` steps instead.
- **Moving `curr` in head insertion:** `curr` should stay fixed -- it's always the tail of the growing reversed sublist. Only `tmp` moves.
- **Forgetting `left == 1`:** Without a dummy, the head of the list changes. Either use a dummy or handle this case explicitly.

## Key Takeaways

- **Head insertion** is the cleanest pattern for partial reversal -- no separate reconnection step needed
- A **dummy node** eliminates the `left == 1` edge case entirely
- Both approaches are O(n) time and O(1) space -- the choice is about clarity, not performance

## Related Problems

- [206. Reverse Linked List](https://www.leetcode.com/problems/reverse-linked-list/) -- full list reversal
- [25. Reverse Nodes in k-Group](https://www.leetcode.com/problems/reverse-nodes-in-k-group/) -- reverse segments of size k
- [24. Swap Nodes in Pairs](https://www.leetcode.com/problems/swap-nodes-in-pairs/) -- special case of k=2 reversal
- [1669. Merge In Between Linked Lists](https://www.leetcode.com/problems/merge-in-between-linked-lists/) -- similar pointer surgery on a sublist range

## References

- [LC 92: Reverse Linked List II on LeetCode](https://www.leetcode.com/problems/reverse-linked-list-ii/)
- [LeetCode Discuss — LC 92: Reverse Linked List II](https://www.leetcode.com/problems/reverse-linked-list-ii/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/reverse-linked-list-ii/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
