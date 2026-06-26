---
layout: post
title: "[Medium] 708. Insert into a Sorted Circular Linked List"
date: 2025-10-27 21:06:00 -0700
categories: leetcode medium linked-list circular
permalink: /posts/2025-10-27-medium-708-insert-into-a-sorted-circular-linked-list/
tags: [leetcode, medium, linked-list, circular, insertion, two-pointers]
---
**Difficulty:** Medium  
**Category:** Linked List, Circular List  
**Companies:** Amazon, Facebook, Google, Microsoft


Given a circular linked list, represented by a Node class, insert a new value into the list while maintaining the circular and sorted order of the list.

The list is circular, so the last node points back to the first node. The list is sorted in ascending order.

## Examples
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

## Constraints
- The number of nodes in the list is in the range `[0, 5 * 10^4]`
- `-10^6 <= Node.val, insertVal <= 10^6`
- List is sorted in ascending order
- List is circular

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

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** Difficulty:** Medium

**How the code works:**
**Difficulty:** Medium
**Category:** Linked List, Circular List
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.

**Walkthrough** — input `head = [3,4,1], insertVal = 2`, expected output `[3,4,1,2]`:

Insert 2 between 1 and 3, maintaining the circular sorted order.
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [LC 23: Swap Nodes in Pairs](https://www.leetcode.com/problems/swap-nodes-in-pairs/) - Linked list manipulation
- [LC 25: Reverse Nodes in k-Group](https://www.leetcode.com/problems/reverse-nodes-in-k-group/) - Linked list reversal
- [LC 141: Linked List Cycle](https://www.leetcode.com/problems/linked-list-cycle/) - Detect cycle in linked list
- [LC 708: Insert into Sorted Circular List](https://www.leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) *(This problem)*

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

## Key Takeaways

- **Pattern:** Iterative pointer walk (this problem)
- Difficulty:** Medium
- Category:** Linked List, Circular List

## References

- [LC 708: Insert into a Sorted Circular Linked List on LeetCode](https://www.leetcode.com/problems/insert-into-a-sorted-circular-linked-list/)
- [LeetCode Discuss — LC 708: Insert into a Sorted Circular Linked List](https://www.leetcode.com/problems/insert-into-a-sorted-circular-linked-list/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/insert-into-a-sorted-circular-linked-list/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)

## Thinking Process

**Difficulty:** Medium

**Category:** Linked List, Circular List

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
