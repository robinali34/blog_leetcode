---
layout: post
title: "[Hard] 25. Reverse Nodes in k-Group"
date: 2025-09-24 22:00:00 -0000
categories: leetcode algorithm linked-list recursive data-structures pointers hard cpp reverse-nodes k-group recursion problem-solving
---
This is a complex linked list problem that requires reversing nodes in groups of k. The key insight is using recursion to handle the grouping and a helper function to reverse individual groups.

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

- k is a positive integer and is less than or equal to the length of the linked list
- If the number of nodes is not a multiple of k, then left-out nodes should remain as-is
- You may not alter the values in the list's nodes, only the nodes themselves

## Examples
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

## Constraints
- The number of nodes in the list is n
- 1 <= k <= n <= 5000
- 0 <= Node.val <= 1000

## Thinking Process

The solution uses a recursive approach:

1. **Count Check**: Verify if there are at least k nodes remaining
2. **Reverse Group**: Reverse the first k nodes using a helper function
3. **Recursive Call**: Recursively process the remaining list
4. **Connect Groups**: Link the reversed group with the result from recursion

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

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** The solution uses a recursive approach:

**How the code works:**
1. **Count Check**: Verify if there are at least k nodes remaining
2. **Reverse Group**: Reverse the first k nodes using a helper function
3. **Recursive Call**: Recursively process the remaining list
4. **Connect Groups**: Link the reversed group with the result from recursion

**Walkthrough** — input `head = [1,2,3,4,5], k = 2`, expected output `[2,1,4,3,5]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
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

## Helper Function Breakdown

The `reverseLinkedList` function:
1. **Iterative Reversal**: Reverses exactly k nodes
2. **Pointer Swapping**: Uses three pointers for safe reversal
3. **Count Control**: Uses k counter to limit reversal to exactly k nodes

## Common Mistakes

- **k = 1**: No reversal needed, return original list
- **k = n**: Reverse entire list once
- **Insufficient Nodes**: Return remaining nodes unchanged
- **Empty List**: Handle null head gracefully

- **Incorrect Count Check**: Not verifying enough nodes before reversal
- **Pointer Confusion**: Mixing up head pointers after reversal
- **Infinite Recursion**: Not properly handling base cases
- **Connection Errors**: Not properly linking reversed groups

---

## References

- [LC 25: Reverse Nodes in k-Group on LeetCode](https://www.leetcode.com/problems/reverse-nodes-in-k-group/)
- [LeetCode Discuss — LC 25: Reverse Nodes in k-Group](https://www.leetcode.com/problems/reverse-nodes-in-k-group/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/reverse-nodes-in-k-group/editorial/) *(may require premium)*

## Key Takeaways

1. **Recursive Structure**: Each group is processed independently
2. **Count Validation**: Always check if there are enough nodes before reversing
3. **Pointer Management**: Careful handling of head pointers and connections
4. **Base Case**: Return original head if insufficient nodes remain
