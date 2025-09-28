---
layout: post
title: "[Hard] 25. Reverse Nodes in k-Group"
date: 2025-09-24 22:00:00 -0000
categories: leetcode algorithm linked-list recursive
---

# [Hard] 25. Reverse Nodes in k-Group

This is a complex linked list problem that requires reversing nodes in groups of k. The key insight is using recursion to handle the grouping and a helper function to reverse individual groups.

## Problem Description

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

- k is a positive integer and is less than or equal to the length of the linked list
- If the number of nodes is not a multiple of k, then left-out nodes should remain as-is
- You may not alter the values in the list's nodes, only the nodes themselves

### Examples

**Example 1:**
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

**Example 2:**
```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

**Example 3:**
```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
```

### Constraints
- The number of nodes in the list is n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

## Approach

The solution uses a recursive approach:

1. **Count Check**: Verify if there are at least k nodes remaining
2. **Reverse Group**: Reverse the first k nodes using a helper function
3. **Recursive Call**: Recursively process the remaining list
4. **Connect Groups**: Link the reversed group with the result from recursion

## Solution in C++

**Time Complexity:** O(n) - Each node is visited once  
**Space Complexity:** O(n/k) - Recursion stack depth

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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int count = 0;
        ListNode* ptr = head;
        while(count < k && ptr != nullptr) {
            ptr = ptr->next;
            count++;
        }
        if(count == k) {
            ListNode* reversedHead = this->reverseLinkedList(head, k);
            head->next = this->reverseKGroup(ptr, k);
            return reversedHead;
        }
        return head;        
    }
private:
    ListNode* reverseLinkedList(ListNode* head, int k){
        ListNode* new_head = nullptr;
        ListNode* ptr = head;
        while(k > 0) {
            ListNode* next_node = ptr->next;
            ptr->next = new_head;
            new_head = ptr;
            ptr = next_node;
            k--;
        }
        return new_head;
    }
};
```

## Step-by-Step Example

Let's trace through the solution with head = `[1,2,3,4,5]` and k = 2:

**Step 1:** Check if we have at least 2 nodes
- Count = 2, ptr points to node 3
- We have enough nodes, proceed with reversal

**Step 2:** Reverse first group [1,2]
- `reverseLinkedList([1,2], 2)` returns [2,1]
- new_head = 2, head = 1

**Step 3:** Recursive call on remaining list
- `reverseKGroup([3,4,5], 2)` processes the rest
- This will reverse [3,4] to [4,3] and leave [5] as-is

**Step 4:** Connect the groups
- head->next (which is 1) points to the result from recursion
- Final result: [2,1,4,3,5]

## Key Insights

1. **Recursive Structure**: Each group is processed independently
2. **Count Validation**: Always check if there are enough nodes before reversing
3. **Pointer Management**: Careful handling of head pointers and connections
4. **Base Case**: Return original head if insufficient nodes remain

## Helper Function Breakdown

The `reverseLinkedList` function:
1. **Iterative Reversal**: Reverses exactly k nodes
2. **Pointer Swapping**: Uses three pointers for safe reversal
3. **Count Control**: Uses k counter to limit reversal to exactly k nodes

## Edge Cases

- **k = 1**: No reversal needed, return original list
- **k = n**: Reverse entire list once
- **Insufficient Nodes**: Return remaining nodes unchanged
- **Empty List**: Handle null head gracefully

## Common Mistakes

- **Incorrect Count Check**: Not verifying enough nodes before reversal
- **Pointer Confusion**: Mixing up head pointers after reversal
- **Infinite Recursion**: Not properly handling base cases
- **Connection Errors**: Not properly linking reversed groups

---
