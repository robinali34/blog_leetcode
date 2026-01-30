---
layout: post
title: "[Medium] 2. Add Two Numbers"
date: 2025-11-18 00:00:00 -0800
categories: leetcode algorithm medium cpp linked-list recursion problem-solving
permalink: /posts/2025-11-18-medium-2-add-two-numbers/
tags: [leetcode, medium, linked-list, recursion, math, carry]
---

# [Medium] 2. Add Two Numbers

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Number representation**: How are numbers represented? (Assumption: Each node contains a single digit, most significant digit is head, least significant is tail - reverse order)

2. **Carry handling**: How should we handle carry? (Assumption: If sum of two digits >= 10, carry 1 to next position)

3. **Different lengths**: What if lists have different lengths? (Assumption: Treat missing digits as 0 - pad shorter list with zeros)

4. **Leading zeros**: Can result have leading zeros? (Assumption: No - per constraints, no leading zeros in input, result shouldn't have them either)

5. **Return format**: Should we return a new list or modify existing? (Assumption: Return new linked list - don't modify input lists)

## Solution: Recursive Approach

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

## How the Algorithm Works

### Step-by-Step Example: `l1 = [2,4,3]`, `l2 = [5,6,4]`

```
Initial Call: addTwoNumbersHelper([2,4,3], [5,6,4], 0)

Step 1: Process first digits
  sum = 0 + 2 + 5 = 7
  newNode = ListNode(7 % 10) = ListNode(7)
  carry = 7 / 10 = 0
  Recursive call: addTwoNumbersHelper([4,3], [6,4], 0)

Step 2: Process second digits
  sum = 0 + 4 + 6 = 10
  newNode = ListNode(10 % 10) = ListNode(0)
  carry = 10 / 10 = 1
  Recursive call: addTwoNumbersHelper([3], [4], 1)

Step 3: Process third digits
  sum = 1 + 3 + 4 = 8
  newNode = ListNode(8 % 10) = ListNode(8)
  carry = 8 / 10 = 0
  Recursive call: addTwoNumbersHelper(null, null, 0)

Step 4: Base case reached
  l1 == null && l2 == null && carry == 0 → return null

Result: [7] -> [0] -> [8] -> null
```

### Visual Representation

```
l1:  2 -> 4 -> 3 -> null  (represents 342)
l2:  5 -> 6 -> 4 -> null  (represents 465)
     ↓    ↓    ↓
     7    0    8
     ↓    ↓    ↓
Result: 7 -> 0 -> 8 -> null  (represents 807)

Calculation: 342 + 465 = 807
```

### Example with Carry: `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`

```
Step 1: 9 + 9 + 0 = 18 → digit=8, carry=1
Step 2: 9 + 9 + 1 = 19 → digit=9, carry=1
Step 3: 9 + 9 + 1 = 19 → digit=9, carry=1
Step 4: 9 + 9 + 1 = 19 → digit=9, carry=1
Step 5: 9 + 0 + 1 = 10 → digit=0, carry=1
Step 6: 9 + 0 + 1 = 10 → digit=0, carry=1
Step 7: 9 + 0 + 1 = 10 → digit=0, carry=1
Step 8: 0 + 0 + 1 = 1 → digit=1, carry=0

Result: [8,9,9,9,0,0,0,1]
```

## Key Insights

1. **Recursive Structure**: Each recursive call processes one digit from each list
2. **Carry Propagation**: Carry is passed down through recursive calls and handled at each level
3. **Unequal Length Handling**: When one list ends, treat missing digits as 0
4. **Base Case**: Stop when both lists are null AND carry is 0
5. **Reverse Order**: Since digits are stored in reverse, we process from least significant to most significant

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

## Edge Cases

1. **Equal length lists**: `[2,4,3] + [5,6,4]` → `[7,0,8]`
2. **Different length lists**: `[9,9,9,9] + [9,9]` → `[8,9,0,0,1]`
3. **Carry at end**: `[9,9] + [1]` → `[0,0,1]`
4. **Single digits**: `[5] + [5]` → `[0,1]`
5. **Zero inputs**: `[0] + [0]` → `[0]`
6. **One list longer**: `[1] + [9,9,9]` → `[0,0,0,1]`

## Alternative Approaches

### Approach 2: Iterative with Dummy Node

**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(1) excluding output space

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* curr = &dummy;
        int carry = 0;
        
        while (l1 != nullptr || l2 != nullptr || carry > 0) {
            if (l1 != nullptr) {
                carry += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                carry += l2->val;
                l2 = l2->next;
            }
            
            curr->next = new ListNode(carry % 10);
            carry /= 10;
            curr = curr->next;
        }
        
        return dummy.next;
    }
};
```

**Pros:**
- O(1) space complexity (no recursion stack)
- More efficient for long lists
- Easier to understand for some developers

**Cons:**
- Requires dummy node
- More verbose

### Approach 3: Iterative Without Dummy Node

**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(1) excluding output space

```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) return l2;
        if (l2 == nullptr) return l1;
        
        ListNode* head = nullptr;
        ListNode* tail = nullptr;
        int carry = 0;
        
        while (l1 != nullptr || l2 != nullptr || carry > 0) {
            int sum = carry;
            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }
            
            ListNode* newNode = new ListNode(sum % 10);
            if (head == nullptr) {
                head = tail = newNode;
            } else {
                tail->next = newNode;
                tail = newNode;
            }
            carry = sum / 10;
        }
        
        return head;
    }
};
```

## Complexity Analysis

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

- [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) - Digits stored in forward order
- [67. Add Binary](https://leetcode.com/problems/add-binary/) - Add binary strings
- [415. Add Strings](https://leetcode.com/problems/add-strings/) - Add number strings
- [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/) - Multiply number strings
- [369. Plus One Linked List](https://leetcode.com/problems/plus-one-linked-list/) - Add one to linked list number

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

