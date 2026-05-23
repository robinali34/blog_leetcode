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

## Solution 1: Head Insertion -- $O(n)$ time, $O(1)$ space

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
{% endraw %}

### How the Inner Loop Works

Each iteration moves `curr->next` to the front of the sublist:

```
Before iteration:   prev → [... → curr → tmp → rest]
After iteration:    prev → [tmp → ... → curr → rest]
```

- `curr->next = tmp->next` -- detach `tmp` from its position
- `tmp->next = prev->next` -- point `tmp` to the current front of the sublist
- `prev->next = tmp` -- make `tmp` the new front

Note that `curr` never moves -- it starts as the first node of the sublist and ends as the last.

## Solution 2: Classic Reversal -- $O(n)$ time, $O(1)$ space

{% raw %}
```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if (!head || left == right) return head;

        ListNode* cur = head;
        ListNode* pre = nullptr;
        while (left > 1) {
            pre = cur;
            cur = cur->next;
            left--;
            right--;
        }

        ListNode* con = pre;
        ListNode* tail = cur;
        ListNode* third = nullptr;
        while (right > 0) {
            third = cur->next;
            cur->next = pre;
            pre = cur;
            cur = third;
            right--;
        }

        if (con != nullptr) {
            con->next = pre;
        } else {
            head = pre;
        }
        tail->next = cur;

        return head;
    }
};
```
{% endraw %}

### Walk-through

```
head = [1, 2, 3, 4, 5], left = 2, right = 4

Phase 1: Advance to position left
  pre = node(1), cur = node(2)   [left=1, right=3 after decrement]

Phase 2: Reverse right nodes starting from cur
  con = node(1)   (node before sublist)
  tail = node(2)  (will become tail of reversed sublist)

  Iteration 1: reverse 2→3  →  2←3   cur=node(3), pre=node(2)... wait
  Actually: 2→1 (wrong link, but ok), pre=2, cur=3, right=2
  Iteration 2: 3→2, pre=3, cur=4, right=1
  Iteration 3: 4→3, pre=4, cur=5, right=0

Phase 3: Reconnect
  con.next = pre  →  node(1).next = node(4)
  tail.next = cur →  node(2).next = node(5)

Result: 1 → 4 → 3 → 2 → 5  ✓
```

| Pointer | Role |
|---|---|
| `con` | Node before the sublist (saved before reversal) |
| `tail` | First node of original sublist = last node after reversal |
| `pre` | Last node reversed = new head of sublist |
| `cur` | First node after the reversed sublist |

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
- Both approaches are $O(n)$ time and $O(1)$ space -- the choice is about clarity, not performance

## Related Problems

- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) -- full list reversal
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) -- reverse segments of size k
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) -- special case of k=2 reversal
- [1669. Merge In Between Linked Lists](https://leetcode.com/problems/merge-in-between-linked-lists/) -- similar pointer surgery on a sublist range

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
