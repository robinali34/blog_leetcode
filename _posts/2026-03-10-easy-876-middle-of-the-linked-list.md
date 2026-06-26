---
layout: post
title: "[Easy] 876. Middle of the Linked List"
date: 2026-03-10
categories: [leetcode, easy, linked-list, two-pointers]
tags: [leetcode, easy, linked-list, two-pointers, slow-fast]
permalink: /2026/03/10/easy-876-middle-of-the-linked-list/
---
Given the `head` of a singly linked list, return the **middle** node. If there are two middle nodes, return the **second** middle node.

## Examples

**Example 1:**

```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node is 3.
```

**Example 2:**

```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Two middle nodes (3 and 4), return the second one.
```

## Constraints

- The number of nodes is in `[1, 100]`
- `1 <= Node.val <= 100`

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Iterative pointer walk** *(this problem)* | O(n) | O(1) | Traversal, insertion |
| Dummy head node | O(n) | O(1) | Simplify head-edge cases |
| Reversal (3-pointer) | O(n) | O(1) | Reverse sublist or full list |
| Slow/fast pointers | O(n) | O(1) | Middle, cycle, merge lists |

## Thinking Process

### Slow & Fast Pointer

Move `slow` one step and `fast` two steps at a time. When `fast` reaches the end, `slow` is at the middle.

**Why it works:** `fast` travels at 2x speed. When `fast` has covered the full list, `slow` has covered exactly half.

### Odd vs Even Length

```
Odd (5 nodes):   1 → 2 → 3 → 4 → 5
                          ↑ slow stops here (fast at 5, fast->next is null)

Even (6 nodes):  1 → 2 → 3 → 4 → 5 → 6
                              ↑ slow stops here (fast at null)
```

For even-length lists, this naturally returns the **second** middle node, matching the problem requirement.



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

## Approach: Slow & Fast Pointer -- O(n)

{% raw %}
```cpp
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* slow = head, *fast = head;
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
        }
        return slow;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** ### Slow & Fast Pointer

**How the code works:**
**Why it works:** `fast` travels at 2x speed. When `fast` has covered the full list, `slow` has covered exactly half.

**Walkthrough** — input `head = [1,2,3,4,5]`, expected output `[3,4,5]`:

The middle node is 3.
## Common Mistakes

- Checking only `fast->next` without checking `fast` first (null dereference on even-length lists)
- Returning the first middle for even-length lists (this problem wants the second)

## Key Takeaways

- **Slow/fast pointer** is the fundamental linked list technique -- finding the middle in one pass without knowing the length
- The loop condition `while (fast && fast->next)` handles both odd and even lengths
- This is a building block for more complex problems: merge sort on linked lists needs the middle, and cycle detection uses the same two-pointer idea

## Related Problems

- [141. Linked List Cycle](https://www.leetcode.com/problems/linked-list-cycle/) -- same slow/fast technique for cycle detection
- [142. Linked List Cycle II](https://www.leetcode.com/problems/linked-list-cycle-ii/) -- find cycle start
- [148. Sort List](https://www.leetcode.com/problems/sort-list/) -- merge sort uses middle finding as a subroutine
- [234. Palindrome Linked List](https://www.leetcode.com/problems/palindrome-linked-list/) -- find middle, reverse second half, compare

## References

- [LC 876: Middle of the Linked List on LeetCode](https://www.leetcode.com/problems/middle-of-the-linked-list/)
- [LeetCode Discuss — LC 876: Middle of the Linked List](https://www.leetcode.com/problems/middle-of-the-linked-list/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/middle-of-the-linked-list/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
