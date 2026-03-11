---
layout: post
title: "LeetCode 876. Middle of the Linked List"
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

## Approach: Slow & Fast Pointer -- $O(n)$

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
{% endraw %}

**Time**: $O(n)$ -- single pass
**Space**: $O(1)$

## Common Mistakes

- Checking only `fast->next` without checking `fast` first (null dereference on even-length lists)
- Returning the first middle for even-length lists (this problem wants the second)

## Key Takeaways

- **Slow/fast pointer** is the fundamental linked list technique -- finding the middle in one pass without knowing the length
- The loop condition `while (fast && fast->next)` handles both odd and even lengths
- This is a building block for more complex problems: merge sort on linked lists needs the middle, and cycle detection uses the same two-pointer idea

## Related Problems

- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) -- same slow/fast technique for cycle detection
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) -- find cycle start
- [148. Sort List](https://leetcode.com/problems/sort-list/) -- merge sort uses middle finding as a subroutine
- [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) -- find middle, reverse second half, compare

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
