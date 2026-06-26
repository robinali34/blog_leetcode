---
layout: post
title: "[Easy] 203. Remove Linked List Elements"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm easy cpp linked-list iteration problem-solving
permalink: /posts/2025-11-18-easy-203-remove-linked-list-elements/
tags: [leetcode, easy, linked-list, two-pointers, dummy-node]
---
Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has `Node.val == val`, and return *the new head*.

## Examples

**Example 1:**
```
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
```

**Example 2:**
```
Input: head = [], val = 1
Output: []
```

**Example 3:**
```
Input: head = [7,7,7,7], val = 7
Output: []
```

## Constraints

- The number of nodes in the list is in the range `[0, 10^4]`.
- `1 <= Node.val <= 50`
- `0 <= val <= 50`

## Thinking Process

1. **Dummy Node**: Using a dummy node simplifies edge cases, especially when the head needs to be removed

- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

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

**Time Complexity:** O(n) - We visit each node once  
**Space Complexity:** O(1) - Only using constant extra space

The key insight is to use a dummy node to handle edge cases where the head itself needs to be removed. We traverse the list with two pointers: `prev` (previous node) and `curr` (current node), removing nodes that match the target value.

### Solution: Iterative with Dummy Node

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
    ListNode* removeElements(ListNode* head, int val) {
        if(head == nullptr) return head;
        
        ListNode dummy = ListNode(0, head);
        ListNode* prev = &dummy;
        ListNode* curr = head;
        ListNode* toDelete = nullptr;
        
        while(curr != nullptr) {
            if (curr->val == val) {
                prev->next = curr->next;
                toDelete = curr;
            } else {
                prev = curr;
            }
            curr = curr->next;
            
            if(toDelete != nullptr) {
                delete toDelete;
                toDelete = nullptr;
            }
        }
        
        ListNode *ret = dummy.next;
        return ret;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** 1. **Dummy Node**: Using a dummy node simplifies edge cases, especially when the head needs to be removed

**How the code works:**
1. **Dummy Node**: Using a dummy node simplifies edge cases, especially when the head needs to be removed
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.

**Walkthrough** — input `head = [1,2,6,3,4,5,6], val = 6`, expected output `[1,2,3,4,5]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Iterative with Dummy** | O(n) | O(1) | Space efficient, handles all cases | Requires memory management |
| **Recursive** | O(n) | O(n) | Elegant, concise | Stack overflow risk for long lists |
| **Simplified Iterative** | O(n) | O(1) | Simple, no memory management | Doesn't free memory (fine for LeetCode) |
## Algorithm Breakdown

```cpp
ListNode* removeElements(ListNode* head, int val) {
    // Handle empty list
    if(head == nullptr) return head;
    
    // Create dummy node to simplify edge cases
    ListNode dummy(0, head);
    ListNode* prev = &dummy;  // Previous valid node
    ListNode* curr = head;    // Current node being checked
    ListNode* toDelete = nullptr;
    
    while(curr != nullptr) {
        if (curr->val == val) {
            // Skip the current node
            prev->next = curr->next;
            toDelete = curr;  // Mark for deletion
        } else {
            // Move prev forward only when we keep the node
            prev = curr;
        }
        
        // Move to next node
        curr = curr->next;
        
        // Delete removed node
        if(toDelete != nullptr) {
            delete toDelete;
            toDelete = nullptr;
        }
    }
    
    return dummy.next;  // Return new head
}
```

## Common Mistakes

1. **Empty list**: `head = []` → return `[]`
2. **Head needs removal**: `head = [7,7,7,7], val = 7` → return `[]`
3. **All nodes removed**: `head = [1,1,1], val = 1` → return `[]`
4. **No nodes removed**: `head = [1,2,3], val = 4` → return `[1,2,3]`
5. **Remove from middle**: `head = [1,2,3,2,4], val = 2` → return `[1,3,4]`

1. **Not using dummy node**: Makes it harder to handle head removal
2. **Incorrect pointer updates**: Forgetting to update `prev` only when keeping a node
3. **Memory leaks**: Not deleting removed nodes
4. **Returning wrong pointer**: Should return `dummy.next`, not `head`
5. **Null pointer dereference**: Not checking if `head` is `nullptr` first

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Iterative with Dummy** | O(n) | O(1) | Space efficient, handles all cases | Requires memory management |
| **Recursive** | O(n) | O(n) | Elegant, concise | Stack overflow risk for long lists |
| **Simplified Iterative** | O(n) | O(1) | Simple, no memory management | Doesn't free memory (fine for LeetCode) |

## Related Problems

- [83. Remove Duplicates from Sorted List](https://www.leetcode.com/problems/remove-duplicates-from-sorted-list/) - Remove duplicates
- [82. Remove Duplicates from Sorted List II](https://www.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) - Remove all duplicates
- [237. Delete Node in a Linked List](https://www.leetcode.com/problems/delete-node-in-a-linked-list/) - Delete without head reference
- [19. Remove Nth Node From End of List](https://www.leetcode.com/problems/remove-nth-node-from-end-of-list/) - Remove specific node

## Optimization Notes

1. **Dummy Node Pattern**: Essential for simplifying linked list deletion problems
2. **Memory Management**: In production code, always delete removed nodes
3. **Early Termination**: Could optimize by checking if list is empty first
4. **Pointer Safety**: Always check for `nullptr` before dereferencing

## Key Takeaways

1. **Dummy Node**: Using a dummy node simplifies edge cases, especially when the head needs to be removed
2. **Two Pointers**: `prev` tracks the previous valid node, `curr` traverses the list
3. **Memory Management**: Properly delete removed nodes to prevent memory leaks
4. **Pointer Updates**: Only update `prev` when we don't remove a node; otherwise, `prev` stays the same

## References

- [LC 203: Remove Linked List Elements on LeetCode](https://www.leetcode.com/problems/remove-linked-list-elements/)
- [LeetCode Discuss — LC 203: Remove Linked List Elements](https://www.leetcode.com/problems/remove-linked-list-elements/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/remove-linked-list-elements/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
