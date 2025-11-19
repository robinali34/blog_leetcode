---
layout: post
title: "[Easy] 203. Remove Linked List Elements"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm easy cpp linked-list iteration problem-solving
permalink: /posts/2025-11-18-easy-203-remove-linked-list-elements/
tags: [leetcode, easy, linked-list, two-pointers, dummy-node]
---

# [Easy] 203. Remove Linked List Elements

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

## Solution: Dummy Node Approach

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

## How the Algorithm Works

### Step-by-Step Example: `head = [1,2,6,3,4,5,6]`, `val = 6`

```
Initial:  dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> nullptr
          ↑       ↑
         prev    curr

Step 1:   curr->val = 1 ≠ 6, move prev forward
          dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> nullptr
                  ↑    ↑
                 prev curr

Step 2:   curr->val = 2 ≠ 6, move prev forward
          dummy -> 1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6 -> nullptr
                       ↑    ↑
                      prev curr

Step 3:   curr->val = 6 == 6, remove node
          prev->next = curr->next (skip 6)
          delete curr
          dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> nullptr
                       ↑    ↑
                      prev curr

Step 4:   curr->val = 3 ≠ 6, move prev forward
          dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> nullptr
                            ↑    ↑
                           prev curr

Step 5:   curr->val = 4 ≠ 6, move prev forward
          dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> nullptr
                                 ↑    ↑
                                prev curr

Step 6:   curr->val = 5 ≠ 6, move prev forward
          dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> nullptr
                                      ↑    ↑
                                     prev curr

Step 7:   curr->val = 6 == 6, remove node
          prev->next = curr->next (skip 6)
          delete curr
          dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> nullptr
                                      ↑    ↑
                                     prev curr (nullptr)

Result:   Return dummy.next = [1,2,3,4,5]
```

### Visual Representation

```
Before:  [1] -> [2] -> [6] -> [3] -> [4] -> [5] -> [6] -> nullptr
         ↑
        head

After:   [1] -> [2] -> [3] -> [4] -> [5] -> nullptr
         ↑
        head
```

## Key Insights

1. **Dummy Node**: Using a dummy node simplifies edge cases, especially when the head needs to be removed
2. **Two Pointers**: `prev` tracks the previous valid node, `curr` traverses the list
3. **Memory Management**: Properly delete removed nodes to prevent memory leaks
4. **Pointer Updates**: Only update `prev` when we don't remove a node; otherwise, `prev` stays the same

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

## Edge Cases

1. **Empty list**: `head = []` → return `[]`
2. **Head needs removal**: `head = [7,7,7,7], val = 7` → return `[]`
3. **All nodes removed**: `head = [1,1,1], val = 1` → return `[]`
4. **No nodes removed**: `head = [1,2,3], val = 4` → return `[1,2,3]`
5. **Remove from middle**: `head = [1,2,3,2,4], val = 2` → return `[1,3,4]`

## Common Mistakes

1. **Not using dummy node**: Makes it harder to handle head removal
2. **Incorrect pointer updates**: Forgetting to update `prev` only when keeping a node
3. **Memory leaks**: Not deleting removed nodes
4. **Returning wrong pointer**: Should return `dummy.next`, not `head`
5. **Null pointer dereference**: Not checking if `head` is `nullptr` first

## Alternative Approaches

### Approach 2: Recursive Solution

**Time Complexity:** O(n)  
**Space Complexity:** O(n) - Due to recursion stack

```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(head == nullptr) return head;
        
        head->next = removeElements(head->next, val);
        
        return head->val == val ? head->next : head;
    }
};
```

### Approach 3: Simplified Iterative (No Memory Deletion)

For LeetCode submissions where memory management isn't required:

```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        ListNode* curr = head;
        
        while(curr != nullptr) {
            if(curr->val == val) {
                prev->next = curr->next;
            } else {
                prev = curr;
            }
            curr = curr->next;
        }
        
        return dummy.next;
    }
};
```

## Complexity Analysis

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Iterative with Dummy** | O(n) | O(1) | Space efficient, handles all cases | Requires memory management |
| **Recursive** | O(n) | O(n) | Elegant, concise | Stack overflow risk for long lists |
| **Simplified Iterative** | O(n) | O(1) | Simple, no memory management | Doesn't free memory (fine for LeetCode) |

## Related Problems

- [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/) - Remove duplicates
- [82. Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/) - Remove all duplicates
- [237. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/) - Delete without head reference
- [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) - Remove specific node

## Optimization Notes

1. **Dummy Node Pattern**: Essential for simplifying linked list deletion problems
2. **Memory Management**: In production code, always delete removed nodes
3. **Early Termination**: Could optimize by checking if list is empty first
4. **Pointer Safety**: Always check for `nullptr` before dereferencing

---

*This problem demonstrates the importance of using dummy nodes to handle edge cases in linked list manipulation, and proper memory management in C++.*

