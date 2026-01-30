---
layout: post
title: "LC 708: Insert into a Sorted Circular Linked List"
date: 2025-10-27 21:06:00 -0700
categories: leetcode medium linked-list circular
permalink: /posts/2025-10-27-medium-708-insert-into-a-sorted-circular-linked-list/
tags: [leetcode, medium, linked-list, circular, insertion, two-pointers]
---

# LC 708: Insert into a Sorted Circular Linked List

**Difficulty:** Medium  
**Category:** Linked List, Circular List  
**Companies:** Amazon, Facebook, Google, Microsoft

## Problem Statement

Given a circular linked list, represented by a Node class, insert a new value into the list while maintaining the circular and sorted order of the list.

The list is circular, so the last node points back to the first node. The list is sorted in ascending order.

### Examples

**Example 1:**
```
Input: head = [3,4,1], insertVal = 2
Output: [3,4,1,2]
Explanation: Insert 2 between 1 and 3, maintaining the circular sorted order.
```

**Example 2:**
```
Input: head = [], insertVal = 1
Output: [1]
Explanation: Create a circular list with a single node.
```

**Example 3:**
```
Input: head = [1], insertVal = 0
Output: [1,0]
Explanation: Insert 0 between 1 (tail) and 1 (head), wrapping around.
```

### Constraints

- The number of nodes in the list is in the range `[0, 5 * 10^4]`
- `-10^6 <= Node.val, insertVal <= 10^6`
- List is sorted in ascending order
- List is circular

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Circular list**: What is a circular linked list? (Assumption: Last node's next points to first node - no null next pointer)

2. **Sorted order**: What does "sorted" mean? (Assumption: Values in ascending order - but may wrap around)

3. **Insert position**: Where should we insert? (Assumption: Insert in correct sorted position maintaining circular order)

4. **Return value**: What should we return? (Assumption: Head of the modified circular list - can be same or different)

5. **Empty list**: What if list is empty? (Assumption: Create new circular list with single node)

## Interview Deduction Process (20 minutes)

**Step 1: Brute-Force Approach (5 minutes)**

Traverse the entire circular list to find the insertion point. Start from head and traverse until we find the correct position (where current value <= insertVal <= next value, or we've completed a full cycle). Handle edge cases: empty list, single node, inserting at boundaries. This approach works but requires careful handling of the circular nature and edge cases.

**Step 2: Semi-Optimized Approach (7 minutes)**

Find the maximum node (or minimum node) to identify where the list "wraps around". Then determine if insertVal should be inserted before or after the wrap point. However, this adds complexity in finding the wrap point and handling various cases. The logic can become convoluted with multiple edge cases.

**Step 3: Optimized Solution (8 minutes)**

Use a single pass with careful edge case handling. Traverse the list looking for a valid insertion point: where current <= insertVal <= next (normal case), or where we've passed the maximum (current > next and insertVal > current or insertVal < next). Handle empty list and single node separately. The key insight is that in a sorted circular list, there's always a valid insertion point: either in the middle of the sequence, or at the wrap-around point. This achieves O(n) time which is optimal since we may need to traverse the entire list in the worst case.

## Solution Approaches

### Approach 1: One-Pass Insertion (Recommended)

**Key Insight:** Traverse the circular list once and look for a valid insertion point. Handle edge cases at the wrap-around point.

**Algorithm:**
1. Handle empty list by creating a self-referencing node
2. Traverse the circular list
3. Find insertion point where `curr->val <= insertVal && curr->next->val >= insertVal`
4. Handle wrap-around case where `curr->next->val < curr->val` (wrap point)
   - Insert if `insertVal >= curr->val` OR `insertVal <= curr->next->val`
5. If no valid point found after full traversal, insert after current position

**Time Complexity:** O(n) where n is the number of nodes  
**Space Complexity:** O(1)

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;

    Node() {}

    Node(int _val) {
        val = _val;
        next = NULL;
    }

    Node(int _val, Node* _next) {
        val = _val;
        next = _next;
    }
};
*/

class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        // Empty list case
        if(!head) {
            Node * newNode = new Node(insertVal);
            newNode->next = newNode;
            return newNode;
        }

        Node* curr = head;
        bool toInsert = false;
        
        do {
            // Normal case: insert between curr and curr->next
            if(curr->val <= insertVal && curr->next->val >= insertVal) {
                toInsert = true;
            } 
            // Wrap-around case: curr->next->val < curr->val indicates the wrap point
            else if(curr->next->val < curr->val) {
                // Insert at wrap-around (largest or smallest value)
                if (insertVal >= curr->val || insertVal <= curr->next->val){
                    toInsert = true;
                }
            }
            
            if(toInsert) {
                Node* ptr = new Node(insertVal);
                ptr->next = curr->next;
                curr->next = ptr;
                return head;
            }
            curr = curr->next;
        } while(curr != head);

        // All values are the same or insert at current position
        curr->next = new Node(insertVal, curr->next);
        return head;
    }
};
```

### Approach 2: Two-Pass with Preprocessing

**Algorithm:**
1. First pass: Find the node with maximum value
2. Second pass: Search from max node's next to find insertion point
3. Handle all same values case

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```cpp
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        if(!head) {
            Node* newNode = new Node(insertVal);
            newNode->next = newNode;
            return newNode;
        }

        // Find the maximum node
        Node* maxNode = head;
        Node* curr = head->next;
        
        while(curr != head) {
            if(curr->val >= maxNode->val) {
                maxNode = curr;
            }
            curr = curr->next;
        }

        // Insert at the end if value is too large
        if(insertVal >= maxNode->val || insertVal <= maxNode->next->val) {
            Node* newNode = new Node(insertVal, maxNode->next);
            maxNode->next = newNode;
            return head;
        }

        // Find the correct insertion point
        curr = maxNode->next;
        while(curr->next->val < insertVal) {
            curr = curr->next;
        }

        Node* newNode = new Node(insertVal, curr->next);
        curr->next = newNode;
        return head;
    }
};
```

### Approach 3: Simplified Logic

**Algorithm:** Streamlined version that handles all cases more elegantly.

```cpp
class Solution {
public:
    Node* insert(Node* head, int insertVal) {
        Node* newNode = new Node(insertVal);
        
        // Empty list
        if(!head) {
            newNode->next = newNode;
            return newNode;
        }

        Node* curr = head;
        
        while(curr->next != head) {
            // Normal insertion point
            if(curr->val <= insertVal && insertVal <= curr->next->val) {
                break;
            }
            // Wrap-around insertion point
            if(curr->val > curr->next->val && 
               (insertVal >= curr->val || insertVal <= curr->next->val)) {
                break;
            }
            curr = curr->next;
        }
        
        // Insert at current position
        newNode->next = curr->next;
        curr->next = newNode;
        return head;
    }
};
```

## Algorithm Analysis

### Key Insights

1. **Circular List Boundary**: The "wrap" happens when `curr->val > curr->next->val`
2. **Insertion Point Detection**: Need to check both normal range and wrap-around cases
3. **Edge Cases**: Empty list, single node, all same values
4. **Traversal Guard**: Use `do-while` to ensure at least one iteration

### Understanding the Wrap-Around Logic

```
Sorted circular list: [3, 4, 1] → 1 points to 3

When curr = 4, curr->next = 1:
  - We're at the wrap point (largest → smallest)
  - insertVal = 2: insertVal >= 4? No, insertVal <= 1? No → continue
  - insertVal = 5: insertVal >= 4? Yes → insert here
  - insertVal = 0: insertVal <= 1? Yes → insert here
```

## Implementation Details

### Empty List Handling
```cpp
if(!head) {
    Node * newNode = new Node(insertVal);
    newNode->next = newNode;  // Self-referencing
    return newNode;
}
```

### Normal Insertion Case
```cpp
// Insert between curr and curr->next
if(curr->val <= insertVal && curr->next->val >= insertVal) {
    Node* newNode = new Node(insertVal, curr->next);
    curr->next = newNode;
    return head;
}
```

### Wrap-Around Insertion Case
```cpp
// At the wrap point (largest to smallest)
if(curr->next->val < curr->val) {
    // Insert if value is larger than max OR smaller than min
    if(insertVal >= curr->val || insertVal <= curr->next->val) {
        // Insert here
    }
}
```

## Edge Cases

1. **Empty List**: Create a circular list with single node
2. **Single Node**: Insert anywhere (trivially maintains order)
3. **All Same Values**: Insert at any position
4. **Insert at Head**: Special care needed for wrap logic
5. **Insert Largest Value**: Should go after maximum node
6. **Insert Smallest Value**: Should go before minimum node

## Follow-up Questions

- What if the list is not guaranteed to be sorted?
- How would you handle duplicate insertion values?
- What if you need to insert multiple values at once?
- How would you delete a value from a circular list?

## Related Problems

- [LC 23: Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) - Linked list manipulation
- [LC 25: Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) - Linked list reversal
- [LC 141: Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) - Detect cycle in linked list
- [LC 708: Insert into Sorted Circular List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) *(This problem)*

## Optimization Techniques

1. **Single Pass**: Most efficient with O(n) time
2. **Early Exit**: Return immediately after insertion
3. **Edge Case Handling**: Handle empty list, single node separately
4. **Wrap Detection**: Identify wrap point by comparing adjacent values

## Code Quality Notes

1. **Readability**: Clear variable names and logic separation
2. **Correctness**: Handles all edge cases properly
3. **Performance**: Optimal O(n) time complexity
4. **Memory**: O(1) space complexity

---

*This problem demonstrates sophisticated circular list manipulation and requires careful handling of wrap-around cases and edge conditions.*

