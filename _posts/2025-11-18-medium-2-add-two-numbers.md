---
layout: post
title: "[Medium] 2. Add Two Numbers"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp linked-list recursion problem-solving
permalink: /posts/2025-11-18-medium-2-add-two-numbers/
tags: [leetcode, medium, linked-list, recursion, math, carry]
---
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Examples

**Example 1:**
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

**Example 2:**
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

**Example 3:**
```
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998
```

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.

## Thinking Process

1. **Recursive Structure**: Each recursive call processes one digit from each list

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

**Time Complexity:** O(max(m, n)) where m and n are the lengths of l1 and l2  
**Space Complexity:** O(max(m, n)) due to recursion stack

This solution uses a recursive helper function that processes both lists simultaneously, handling carry propagation naturally through the recursion.

### Solution: Recursive Helper

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addTwoNumbersHelper(l1, l2, 0);
    }

    ListNode* addTwoNumbersHelper(ListNode* l1, ListNode* l2, int carry) {
        // Base case: if both lists are null and no carry
        if (l1 == nullptr && l2 == nullptr && carry == 0) {
            return nullptr;
        }
        
        int sum = carry;
        if (l1 != nullptr) {
            sum += l1->val;
        }
        if (l2 != nullptr) {
            sum += l2->val;
        }
        
        ListNode* newNode = new ListNode(sum % 10);
        newNode->next = addTwoNumbersHelper(
            l1 != nullptr ? l1->next : nullptr,
            l2 != nullptr ? l2->next : nullptr,
            sum / 10
        );
        
        return newNode;
    }
};
```

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** 1. **Recursive Structure**: Each recursive call processes one digit from each list

**How the code works:**
1. **Recursive Structure**: Each recursive call processes one digit from each list
- Draw pointers before rewriting links.
- Dummy head simplifies insert/delete at the head.
- Slow/fast pointers find middle or detect cycles in one pass.

**Walkthrough** — input `l1 = [2,4,3], l2 = [5,6,4]`, expected output `[7,0,8]`:

342 + 465 = 807.

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Recursive** | O(max(m,n)) | O(max(m,n)) | Elegant, natural carry handling | Stack overflow risk, O(n) space |
| **Iterative (Dummy)** | O(max(m,n)) | O(1) | Space efficient, clean code | Requires dummy node |
| **Iterative (No Dummy)** | O(max(m,n)) | O(1) | Space efficient | More edge case handling |
## Algorithm Breakdown

```cpp
ListNode* addTwoNumbersHelper(ListNode* l1, ListNode* l2, int carry) {
    // Base case: all digits processed and no carry
    if (l1 == nullptr && l2 == nullptr && carry == 0) {
        return nullptr;
    }
    
    // Calculate sum: carry + l1->val + l2->val
    int sum = carry;
    if (l1 != nullptr) sum += l1->val;
    if (l2 != nullptr) sum += l2->val;
    
    // Create new node with ones digit
    ListNode* newNode = new ListNode(sum % 10);
    
    // Recursively process next digits
    newNode->next = addTwoNumbersHelper(
        l1 != nullptr ? l1->next : nullptr,  // Move to next or null
        l2 != nullptr ? l2->next : nullptr,  // Move to next or null
        sum / 10                              // Pass carry forward
    );
    
    return newNode;
}
```

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Recursive** | O(max(m,n)) | O(max(m,n)) | Elegant, natural carry handling | Stack overflow risk, O(n) space |
| **Iterative (Dummy)** | O(max(m,n)) | O(1) | Space efficient, clean code | Requires dummy node |
| **Iterative (No Dummy)** | O(max(m,n)) | O(1) | Space efficient | More edge case handling |

## Implementation Details

### Recursive Base Case

```cpp
if (l1 == nullptr && l2 == nullptr && carry == 0) {
    return nullptr;
}
```

**Why all three conditions?**
- `l1 == nullptr && l2 == nullptr`: Both lists exhausted
- `carry == 0`: No remaining carry to propagate
- If carry > 0, we need to create one more node

### Digit Extraction

```cpp
int sum = carry;
if (l1 != nullptr) sum += l1->val;
if (l2 != nullptr) sum += l2->val;

int digit = sum % 10;  // Ones digit
int newCarry = sum / 10;  // Tens digit (carry)
```

### Null Handling

```cpp
l1 != nullptr ? l1->next : nullptr
```

When a list ends, we pass `nullptr` to indicate no more digits from that list.

## Common Mistakes

1. **Equal length lists**: `[2,4,3] + [5,6,4]` → `[7,0,8]`
2. **Different length lists**: `[9,9,9,9] + [9,9]` → `[8,9,0,0,1]`
3. **Carry at end**: `[9,9] + [1]` → `[0,0,1]`
4. **Single digits**: `[5] + [5]` → `[0,1]`
5. **Zero inputs**: `[0] + [0]` → `[0]`
6. **One list longer**: `[1] + [9,9,9]` → `[0,0,0,1]`

1. **Forgetting final carry**: Not handling carry after both lists end
2. **Wrong base case**: Returning too early when carry > 0
3. **Null pointer dereference**: Accessing `l1->val` when `l1` is null
4. **Wrong digit calculation**: Using `sum / 10` instead of `sum % 10` for digit
5. **Memory leaks**: Not properly managing dynamically allocated nodes

## Optimization Tips

1. **Iterative Preferred**: For production code, use iterative approach to avoid stack overflow
2. **Dummy Node**: Simplifies code by avoiding special cases for head
3. **Early Termination**: Can optimize by checking if both lists are null and carry is 0
4. **In-place Modification**: Could modify one list in-place to save space (not recommended)

## Related Problems

- [445. Add Two Numbers II](https://www.leetcode.com/problems/add-two-numbers-ii/) - Digits stored in forward order
- [67. Add Binary](https://www.leetcode.com/problems/add-binary/) - Add binary strings
- [415. Add Strings](https://www.leetcode.com/problems/add-strings/) - Add number strings
- [43. Multiply Strings](https://www.leetcode.com/problems/multiply-strings/) - Multiply number strings
- [369. Plus One Linked List](https://www.leetcode.com/problems/plus-one-linked-list/) - Add one to linked list number

## Real-World Applications

1. **Big Integer Arithmetic**: Handling numbers larger than standard data types
2. **Calculator Implementation**: Adding large numbers digit by digit
3. **Cryptography**: Modular arithmetic operations
4. **Financial Systems**: Precise decimal calculations
5. **Scientific Computing**: High-precision arithmetic

## Pattern Recognition

This problem demonstrates the **"Two Pointers with Carry"** pattern:

```
Process two sequences simultaneously:
  - Handle different lengths gracefully
  - Propagate carry/borrow through iterations
  - Create result on-the-fly
```

Similar problems:
- Add Binary
- Add Strings
- Multiply Strings
- Plus One Linked List

## Recursive vs Iterative

### When to Use Recursive

- **Pros**: 
  - More elegant and concise
  - Natural carry propagation
  - Easier to reason about
  
- **Cons**:
  - O(n) space for recursion stack
  - Risk of stack overflow for very long lists
  - Slightly slower due to function call overhead

### When to Use Iterative

- **Pros**:
  - O(1) space complexity
  - No stack overflow risk
  - Better performance
  
- **Cons**:
  - More verbose code
  - Requires careful pointer management

**Recommendation**: Use iterative approach for production code, recursive for interviews/learning.

---

*This problem is a classic introduction to linked list manipulation and demonstrates how recursion can elegantly handle carry propagation in arithmetic operations.*

## Key Takeaways

1. **Recursive Structure**: Each recursive call processes one digit from each list
2. **Carry Propagation**: Carry is passed down through recursive calls and handled at each level
3. **Unequal Length Handling**: When one list ends, treat missing digits as 0
4. **Base Case**: Stop when both lists are null AND carry is 0
5. **Reverse Order**: Since digits are stored in reverse, we process from least significant to most significant

## References

- [LC 2: Add Two Numbers on LeetCode](https://www.leetcode.com/problems/add-two-numbers/)
- [LeetCode Discuss — LC 2: Add Two Numbers](https://www.leetcode.com/problems/add-two-numbers/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/add-two-numbers/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
