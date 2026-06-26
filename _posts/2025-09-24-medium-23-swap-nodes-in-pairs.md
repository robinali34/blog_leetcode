---
layout: post
title: "[Medium] 24. Swap Nodes in Pairs"
date: 2025-09-24 15:11:00 -0000
categories: leetcode algorithm linked-list recursive data-structures pointers medium cpp swap-nodes recursion iterative problem-solving
---
This is a classic linked list problem that requires understanding how to manipulate pointers and traverse linked lists. The key insight is understanding pointer manipulation, recursion, and iterative approaches with dummy nodes.

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

## Examples
**Example 1:**
```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

**Example 2:**
```
Input: head = []
Output: []
```

**Example 3:**
```
Input: head = [1]
Output: [1]
```

## Constraints
- The number of nodes in the list is in the range [0, 100]
- 0 <= Node.val <= 100

## Thinking Process

There are two main approaches to solve this problem:

1. **Recursive Approach**: Use recursion to swap pairs and handle the rest of the list
2. **Iterative Approach**: Use a dummy node and pointers to traverse and swap pairs

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
### Recursive Approach

**Time Complexity:** O(n) - We visit each node once  
**Space Complexity:** O(n) - Due to recursion stack

The recursive approach works by:
1. Base case: If we have 0 or 1 nodes, return the head
2. Swap the first two nodes
3. Recursively call the function on the rest of the list
4. Connect the swapped pair with the result from recursion
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if ((head == nullptr) || (head->next == nullptr)) return head;
        ListNode *first = head;
        ListNode *second = head->next;
        first->next = swapPairs(second->next);
        second->next = first;
        return second;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** There are two main approaches to solve this problem:

**How the code works:**
1. **Recursive Approach**: Use recursion to swap pairs and handle the rest of the list
2. **Iterative Approach**: Use a dummy node and pointers to traverse and swap pairs

**Walkthrough** — input `head = [1,2,3,4]`, expected output `[2,1,4,3]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Forgetting to update the `pre` pointer in iterative approach
- Not handling the case where there's an odd number of nodes
- Incorrectly connecting pointers during the swap operation

## References

- [LC 23: Swap Nodes in Pairs on LeetCode](https://www.leetcode.com/problems/swap-nodes-in-pairs/)
- [LeetCode Discuss — LC 23: Swap Nodes in Pairs](https://www.leetcode.com/problems/swap-nodes-in-pairs/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/swap-nodes-in-pairs/editorial/) *(may require premium)*

## Key Takeaways

1. **Dummy Node**: The iterative approach uses a dummy node to simplify edge cases
2. **Pointer Manipulation**: Understanding how to update multiple pointers correctly
3. **Recursion vs Iteration**: Recursive is more elegant but uses O(n) space; iterative uses O(1) space
4. **Base Cases**: Always handle empty list and single node cases
