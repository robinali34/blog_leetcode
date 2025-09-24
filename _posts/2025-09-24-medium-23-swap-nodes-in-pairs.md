---
layout: post
title: "[Medium] 24. Swap Nodes in Pairs"
date: 2025-09-24 15:11:00 -0000
categories: leetcode algorithm linked-list recursive
---

# [Medium] 24. Swap Nodes in Pairs

This is a classic linked list problem that requires understanding how to manipulate pointers and traverse linked lists. The key insight is understanding pointer manipulation, recursion, and iterative approaches with dummy nodes.

## Problem Description

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

### Examples

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

### Constraints
- The number of nodes in the list is in the range [0, 100]
- 0 <= Node.val <= 100

## Template in C++

### ListNode definition

```cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```
Typical Leetcode template includes:

- Convert std::vector<int> → ListNode* (linked list)

- Convert ListNode* → std::vector<int>

- Auto memory cleanup (freeList)
- Clean, reusable design for testing LeetCode-style problems

## Approach

There are two main approaches to solve this problem:

1. **Recursive Approach**: Use recursion to swap pairs and handle the rest of the list
2. **Iterative Approach**: Use a dummy node and pointers to traverse and swap pairs

## Solution in C++

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

### Iterative Approach

**Time Complexity:** O(n) - We visit each node once  
**Space Complexity:** O(1) - Only using constant extra space

The iterative approach works by:
1. Create a dummy node to handle edge cases
2. Use a previous pointer to keep track of the last processed node
3. For each pair, swap the nodes and update pointers
4. Move to the next pair

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
        ListNode dummy(-1); // Stack allocation - automatically destroyed when function returns
        dummy.next = head;
        ListNode *pre = &dummy; // Pointer to dummy node's address
        while((head != nullptr) && (head->next != nullptr)) {
            ListNode *first = head, *second = head->next;
            pre->next = second;
            first->next = second->next;
            second->next = first;
            pre = first;
            head = first->next;
        }
        return dummy.next;
    }
};
```

## Step-by-Step Example

Let's trace through the recursive solution with input `[1,2,3,4]`:

**Initial:** `1 -> 2 -> 3 -> 4 -> null`

**Step 1:** Swap first pair (1,2)
- `first = 1`, `second = 2`
- `first->next = swapPairs(3)` (recursive call)
- `second->next = first`
- Result: `2 -> 1 -> [result of swapPairs(3)]`

**Step 2:** Recursive call with `3 -> 4 -> null`
- `first = 3`, `second = 4`
- `first->next = swapPairs(null)` (returns null)
- `second->next = first`
- Result: `4 -> 3 -> null`

**Final:** `2 -> 1 -> 4 -> 3 -> null`

## Key Insights

1. **Dummy Node**: The iterative approach uses a dummy node to simplify edge cases
2. **Pointer Manipulation**: Understanding how to update multiple pointers correctly
3. **Recursion vs Iteration**: Recursive is more elegant but uses O(n) space; iterative uses O(1) space
4. **Base Cases**: Always handle empty list and single node cases

## Common Mistakes

- Forgetting to update the `pre` pointer in iterative approach
- Not handling the case where there's an odd number of nodes
- Incorrectly connecting pointers during the swap operation
