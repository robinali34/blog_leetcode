---
layout: post
title: "[Easy] 206. Reverse Linked List"
date: 2025-11-16 00:00:00 -0800
categories: leetcode algorithm easy cpp linked-list recursion iteration problem-solving
---

# [Easy] 206. Reverse Linked List

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

## Examples

**Example 1:**
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
```

**Example 2:**
```
Input: head = [1,2]
Output: [2,1]
```

**Example 3:**
```
Input: head = []
Output: []
```

## Constraints

- The number of nodes in the list is the range `[0, 5000]`.
- `-5000 <= Node.val <= 5000`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Reversal definition**: What does "reverse" mean? (Assumption: Reverse the order of nodes - first becomes last, last becomes first)

2. **In-place requirement**: Should we reverse in-place? (Assumption: Yes - modify pointers, not create new nodes)

3. **Return value**: What should we return? (Assumption: Head of reversed linked list - new head node)

4. **Empty list**: What if list is empty? (Assumption: Return nullptr - no nodes to reverse)

5. **Single node**: What if list has one node? (Assumption: Return same node - already reversed)

## Solution: Iterative and Recursive Approaches

**Time Complexity:** O(n)  
**Space Complexity:** O(1) iterative, O(n) recursive

We can reverse a linked list using either an iterative approach (preferred for space efficiency) or a recursive approach (more elegant but uses stack space).

### Solution 1: Iterative Approach (Recommended - C++20 Optimized)

```cpp
using namespace std;

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
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            ListNode* next = curr->next;  // Save next node
            curr->next = prev;             // Reverse link
            prev = curr;                   // Move prev forward
            curr = next;                   // Move curr forward
        }
        
        return prev;  // prev is now the new head
    }
};
```

### Solution 2: Recursive Approach (C++20 Optimized)

```cpp
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        // Base case: empty list or single node
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        // Recursively reverse the rest of the list
        ListNode* newHead = reverseList(head->next);
        
        // Reverse the link: head->next now points to head
        head->next->next = head;
        head->next = nullptr;
        
        return newHead;
    }
};
```

### Solution 3: Iterative with Explicit Null Checks

```cpp
using namespace std;

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) {
            return nullptr;
        }
        
        ListNode* prev = nullptr;
        ListNode* curr = head;
        
        while (curr != nullptr) {
            ListNode* next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        
        return prev;
    }
};
```

## How the Iterative Algorithm Works

### Step-by-Step Example: `head = [1,2,3,4,5]`

```
Initial:  1 -> 2 -> 3 -> 4 -> 5 -> nullptr
          ↑
         head

Step 1:   nullptr <- 1    2 -> 3 -> 4 -> 5 -> nullptr
          ↑        ↑     ↑
         prev    curr  next

Step 2:   nullptr <- 1 <- 2    3 -> 4 -> 5 -> nullptr
                 ↑        ↑    ↑
                prev    curr  next

Step 3:   nullptr <- 1 <- 2 <- 3    4 -> 5 -> nullptr
                      ↑        ↑    ↑
                     prev    curr  next

Step 4:   nullptr <- 1 <- 2 <- 3 <- 4    5 -> nullptr
                           ↑        ↑    ↑
                          prev    curr  next

Step 5:   nullptr <- 1 <- 2 <- 3 <- 4 <- 5
                                ↑        ↑
                               prev    curr (nullptr)

Result:   5 -> 4 -> 3 -> 2 -> 1 -> nullptr
          ↑
        return prev
```

### Visual Representation

```
Before:  [1] -> [2] -> [3] -> [4] -> [5] -> nullptr

After:   [1] <- [2] <- [3] <- [4] <- [5]
         ↑                            ↑
       tail                         head
```

## How the Recursive Algorithm Works

### Recursive Call Stack

```
reverseList([1,2,3,4,5])
  ├─ reverseList([2,3,4,5])
  │   ├─ reverseList([3,4,5])
  │   │   ├─ reverseList([4,5])
  │   │   │   ├─ reverseList([5])
  │   │   │   │   └─ return [5]  (base case)
  │   │   │   ├─ 5->next = 4, 4->next = nullptr
  │   │   │   └─ return [5,4]
  │   │   ├─ 4->next = 3, 3->next = nullptr
  │   │   └─ return [5,4,3]
  │   ├─ 3->next = 2, 2->next = nullptr
  │   └─ return [5,4,3,2]
  ├─ 2->next = 1, 1->next = nullptr
  └─ return [5,4,3,2,1]
```

### Step-by-Step Recursive Process

```
Initial:  1 -> 2 -> 3 -> 4 -> 5 -> nullptr

After recursive call returns [5,4,3,2]:
  1 -> 2 -> 3 -> 4 <- 5
  ↑              ↑
head          head->next

After reversing link:
  1 -> 2 -> 3 <- 4 <- 5
  ↑         ↑
head    head->next

Final:
  1 <- 2 <- 3 <- 4 <- 5
  ↑
head (now tail)
```

## Key Optimizations (C++20)

1. **Explicit null checks**: Prevents undefined behavior
2. **Clear variable names**: `prev`, `curr`, `next` for readability
3. **No unnecessary operations**: Direct pointer manipulation
4. **Simple and efficient**: O(1) space for iterative approach

## Complexity Analysis

| Approach | Time | Space |
|----------|------|-------|
| **Iterative** | O(n) | O(1) |
| **Recursive** | O(n) | O(n) |

### Why Iterative is Preferred

- **Space efficient**: O(1) vs O(n) for recursive
- **No stack overflow risk**: For very long lists
- **Better performance**: No function call overhead
- **Easier to understand**: Linear flow

## Algorithm Breakdown

### Iterative Approach

```cpp
ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;  // Previous node (initially null)
    ListNode* curr = head;       // Current node
    
    while (curr != nullptr) {
        ListNode* next = curr->next;  // Save next before reversing
        curr->next = prev;            // Reverse the link
        prev = curr;                  // Move prev forward
        curr = next;                  // Move curr forward
    }
    
    return prev;  // prev is the new head
}
```

### Recursive Approach

```cpp
ListNode* reverseList(ListNode* head) {
    // Base case
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    
    // Recursively reverse rest
    ListNode* newHead = reverseList(head->next);
    
    // Reverse current link
    head->next->next = head;  // Reverse the link
    head->next = nullptr;     // Break old link
    
    return newHead;
}
```

## Edge Cases

1. **Empty list**: `head = nullptr` → return `nullptr`
2. **Single node**: `head = [1]` → return `[1]`
3. **Two nodes**: `head = [1,2]` → return `[2,1]`
4. **Long list**: Works for lists up to 5000 nodes

## Common Mistakes

1. **Losing reference to next node**: Must save `next` before reversing
2. **Not setting head->next to nullptr**: In recursive, must break old link
3. **Returning wrong pointer**: Should return `prev` (iterative) or `newHead` (recursive)
4. **Not handling empty list**: Check for `nullptr` before operations
5. **Memory leaks**: Be careful with pointer manipulation

## Iterative vs Recursive Comparison

| Aspect | Iterative | Recursive |
|--------|-----------|-----------|
| **Space** | O(1) | O(n) |
| **Stack** | No risk | Risk for long lists |
| **Performance** | Faster | Slower (call overhead) |
| **Readability** | Straightforward | More elegant |
| **When to use** | Production code | Interviews/learning |

## Related Problems

- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) - Reverse portion of list
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) - Reverse in groups
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) - Swap adjacent nodes
- [143. Reorder List](https://leetcode.com/problems/reorder-list/) - Reorder list

