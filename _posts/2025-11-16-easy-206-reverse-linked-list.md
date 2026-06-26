---
layout: post
title: "[Easy] 206. Reverse Linked List"
date: 2025-11-16 00:00:00 -0800
categories: leetcode algorithm easy cpp linked-list recursion iteration problem-solving
---
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

## Thinking Process

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.

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

**Time Complexity:** O(n)  
**Space Complexity:** O(1) iterative, O(n) recursive

We can reverse a linked list using either an iterative approach (preferred for space efficiency) or a recursive approach (more elegant but uses stack space).

### Solution 1: Brute-Force Approach (Array Collection)

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

Collect all node values into an array, then rebuild the list by assigning values in reverse order.

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;
        
        vector<int> values;
        ListNode* curr = head;
        while (curr) {
            values.push_back(curr->val);
            curr = curr->next;
        }
        
        curr = head;
        for (int i = values.size() - 1; i >= 0; i--) {
            curr->val = values[i];
            curr = curr->next;
        }
        return head;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.

**How the code works:**
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.

**Walkthrough** — input `head = [1,2,3,4,5]`, expected output `[5,4,3,2,1]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

| Approach | Time | Space |
|----------|------|-------|
| **Iterative** | O(n) | O(1) |
| **Recursive** | O(n) | O(n) |

### Solution 2: Iterative Approach (Recommended - C++20 Optimized)

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

### Complexity
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

### Iterative Approach (Optimal)

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

**Key Steps**:
1. Initialize `prev = nullptr`, `curr = head`
2. For each node: save next, reverse link, advance pointers
3. Return `prev` as new head

### Recursive Approach (Alternative)

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

**Key Steps**:
1. Base case: empty or single node
2. Recursively reverse rest of list
3. Reverse current node's link
4. Return new head from recursion

## Common Mistakes

1. **Empty list**: `head = nullptr` → return `nullptr`
2. **Single node**: `head = [1]` → return `[1]`
3. **Two nodes**: `head = [1,2]` → return `[2,1]`
4. **Long list**: Works for lists up to 5000 nodes

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

## Key Takeaways

- **Pattern:** Iterative pointer walk (this problem)
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.

## References

- [LC 206: Reverse Linked List on LeetCode](https://www.leetcode.com/problems/reverse-linked-list/)
- [LeetCode Discuss — LC 206: Reverse Linked List](https://www.leetcode.com/problems/reverse-linked-list/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/reverse-linked-list/editorial/) *(may require premium)*

## Related Problems

- [92. Reverse Linked List II](https://www.leetcode.com/problems/reverse-linked-list-ii/) - Reverse portion of list
- [25. Reverse Nodes in k-Group](https://www.leetcode.com/problems/reverse-nodes-in-k-group/) - Reverse in groups
- [24. Swap Nodes in Pairs](https://www.leetcode.com/problems/swap-nodes-in-pairs/) - Swap adjacent nodes
- [143. Reorder List](https://www.leetcode.com/problems/reorder-list/) - Reorder list
