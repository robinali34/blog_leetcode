---
layout: post
title: "[Medium] 1856. Maximum Sum of Minimum Product"
date: 2025-10-17 22:36:25 -0700
categories: leetcode algorithm medium cpp stack monotonic-stack prefix-sum problem-solving
---
The **minimum product** of a subarray is the minimum value in the subarray multiplied by the sum of the subarray.

Given an array of integers `nums`, return the **maximum minimum product** of any non-empty subarray of `nums`.

## Examples

**Example 1:**
```
Input: nums = [1,2,3,2]
Output: 14
Explanation: 
- Subarray [2,3,2] has minimum value 2 and sum 7
- Minimum product = 2 * 7 = 14
- This is the maximum minimum product
```

**Example 2:**
```
Input: nums = [2,3,3,1,2]
Output: 18
Explanation: 
- Subarray [3,3,1,2] has minimum value 1 and sum 9
- Minimum product = 1 * 9 = 9
- Subarray [2,3,3,1,2] has minimum value 1 and sum 11
- Minimum product = 1 * 11 = 11
- Subarray [3,3] has minimum value 3 and sum 6
- Minimum product = 3 * 6 = 18
- Maximum is 18
```

**Example 3:**
```
Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: 
- Subarray [5,6,4,2] has minimum value 2 and sum 17
- Minimum product = 2 * 17 = 34
- Subarray [5,6] has minimum value 5 and sum 11
- Minimum product = 5 * 11 = 55
- Subarray [5,6,4] has minimum value 4 and sum 15
- Minimum product = 4 * 15 = 60
- Maximum is 60
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^7`

## Thinking Process

1. **Maintains order:** Elements in decreasing order
1. **Range sum calculation:** O(1) for any subarray sum
1. **Minimum as pivot:** Consider each element as minimum

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Stack</text>

  <rect x="100" y="30" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="46" text-anchor="middle" font-size="10">top</text>
  <rect x="100" y="54" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="100" y="78" width="80" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="200" y="70" font-size="11" fill="#6B6560">push / pop</text>
  <path d="M90 42v60" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="115" text-anchor="middle" font-size="11" fill="#6B6560">LIFO — monotonic stack scans array</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Monotonic stack** *(this problem)* | O(n) | O(n) | Next greater/smaller element |
| Parentheses matching | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |

## Solution

**Time Complexity:** O(n) where n is the length of array  
**Space Complexity:** O(n) for prefix array and stack

Use monotonic stack to find the range where each element is minimum, then calculate the maximum product using prefix sums.

```cpp
class Solution {
public:
    int maxSumMinProduct(vector<int>& nums) {
        int n = nums.size();
        vector<long long> prefix(n + 1, 0);
        
        // Build prefix sum array
        for(int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
        
        vector<int> left(n, -1), right(n, n);
        stack<int> s;
        
        // Find boundaries in single pass
        for(int i = 0; i < n; i++) {
            // Find right boundaries for elements in stack
            while(!s.empty() && nums[s.top()] >= nums[i]) {
                right[s.top()] = i;
                s.pop();
            }
            // Set left boundary for current element
            if(!s.empty()) left[i] = s.top();
            s.push(i);
        }
        
        long long maxProduct = 0;
        
        // Calculate maximum product for each element as minimum
        for(int i = 0; i < n; i++) {
            long long totalSum = prefix[right[i]] - prefix[left[i] + 1];
            maxProduct = max(maxProduct, totalSum * nums[i]);
        }
        
        return (int)(maxProduct % 1000000007);
    }
};
```

### Solution Explanation
**Key Insight:** For each element, find the largest subarray where it is the minimum, then calculate the product of minimum value and subarray sum.

**Steps:**
1. **Build prefix sum array** for efficient range sum calculation
2. **Find boundaries in single pass** using monotonic stack:
   - When popping elements, set their right boundary to current index
   - Set current element's left boundary to stack top
3. **For each element as minimum:**
   - Calculate subarray sum using prefix array
   - Calculate product: `sum * minimum_value`
   - Update maximum product
4. **Return result** modulo 10^9 + 7

## Step-by-Step Example

### Example: `nums = [1,2,3,2]`

**Step 1: Build prefix sum array**
```
nums = [1, 2, 3, 2]
prefix = [0, 1, 3, 6, 8]
```

**Step 2: Find left boundaries (nearest smaller to the left)**
```
nums = [1, 2, 3, 2]
left = [-1, 0, 1, 0]
```

**Step 3: Find right boundaries (nearest smaller to the right)**
```
nums = [1, 2, 3, 2]
right = [4, 3, 4, 4]
```

**Step 4: Calculate products for each element as minimum**

| Index | Element | Left | Right | Subarray | Sum | Product |
|-------|---------|------|-------|----------|-----|---------|
| 0 | 1 | -1 | 4 | [1,2,3,2] | 8 | 1×8 = 8 |
| 1 | 2 | 0 | 3 | [2,3] | 5 | 2×5 = 10 |
| 2 | 3 | 1 | 4 | [3] | 3 | 3×3 = 9 |
| 3 | 2 | 0 | 4 | [2,3,2] | 7 | 2×7 = 14 |

**Maximum product:** 14

## Algorithm Breakdown

### Single Pass Boundary Finding:
```cpp
for(int i = 0; i < n; i++) {
    // Find right boundaries for elements in stack
    while(!s.empty() && nums[s.top()] >= nums[i]) {
        right[s.top()] = i;
        s.pop();
    }
    // Set left boundary for current element
    if(!s.empty()) left[i] = s.top();
    s.push(i);
}
```

**Process:**
1. **When popping elements:** Set their right boundary to current index
2. **Set left boundary:** Current element's left boundary is stack top
3. **Push current index** to stack
4. **Single pass:** Both boundaries found in one traversal

### Product Calculation:
```cpp
for(int i = 0; i < n; i++) {
    long long totalSum = prefix[right[i]] - prefix[left[i] + 1];
    maxProduct = max(maxProduct, totalSum * nums[i]);
}
```

**Process:**
1. **Calculate subarray sum** using prefix array
2. **Multiply by minimum value** (current element)
3. **Update maximum product**

### Complexity
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Prefix sum | O(n) | O(n) |
| Single pass boundaries | O(n) | O(n) |
| Product calculation | O(n) | O(1) |
| **Total** | **O(n)** | **O(n)** |

Where n is the length of the array.

## Detailed Example Walkthrough

### Example: `nums = [2,3,3,1,2]`

**Step 1: Prefix sum array**
```
nums = [2, 3, 3, 1, 2]
prefix = [0, 2, 5, 8, 9, 11]
```

**Step 2: Left boundaries**
```
nums = [2, 3, 3, 1, 2]
left = [-1, 0, 0, -1, 3]
```

**Step 3: Right boundaries**
```
nums = [2, 3, 3, 1, 2]
right = [3, 3, 3, 5, 5]
```

**Step 4: Product calculation**

| Index | Element | Left | Right | Subarray | Sum | Product |
|-------|---------|------|-------|----------|-----|---------|
| 0 | 2 | -1 | 3 | [2,3,3] | 8 | 2×8 = 16 |
| 1 | 3 | 0 | 3 | [3] | 3 | 3×3 = 9 |
| 2 | 3 | 0 | 3 | [3] | 3 | 3×3 = 9 |
| 3 | 1 | -1 | 5 | [2,3,3,1,2] | 11 | 1×11 = 11 |
| 4 | 2 | 3 | 5 | [2] | 2 | 2×2 = 4 |

**Maximum product:** 16

## Common Mistakes

1. **Single element:** `nums = [5]` → `5 * 5 = 25`
2. **All same elements:** `nums = [3,3,3]` → `3 * 9 = 27`
3. **Increasing array:** `nums = [1,2,3,4]` → `1 * 10 = 10`
4. **Decreasing array:** `nums = [4,3,2,1]` → `1 * 10 = 10`

1. **Wrong boundary calculation:** Not handling empty stack correctly
2. **Index off-by-one:** Incorrect prefix sum calculation
3. **Overflow issues:** Not using long long for large products
4. **Modulo placement:** Applying modulo at wrong time

## Related Problems

- [84. Largest Rectangle in Histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/)
- [85. Maximal Rectangle](https://www.leetcode.com/problems/maximal-rectangle/)
- [907. Sum of Subarray Minimums](https://www.leetcode.com/problems/sum-of-subarray-minimums/)
- [2104. Sum of Subarray Ranges](https://www.leetcode.com/problems/sum-of-subarray-ranges/)

## Why This Solution Works

### Monotonic Stack:
1. **Efficient boundary finding:** O(n) time to find all boundaries
2. **Maintains order:** Elements in decreasing order
3. **Optimal removal:** Can remove multiple elements at once
4. **Correct boundaries:** Finds nearest smaller elements accurately

### Prefix Sum:
1. **Range sum calculation:** O(1) for any subarray sum
2. **Efficient computation:** Pre-computed sums
3. **Memory trade-off:** Uses O(n) extra space for O(1) queries

### Product Maximization:
1. **Minimum as pivot:** Consider each element as minimum
2. **Largest subarray:** Find maximum subarray where element is minimum
3. **Greedy approach:** Take largest possible subarray for each minimum
4. **Optimal result:** Ensures maximum product calculation

## References

- [LC 1856: Maximum Sum of Minimum Product on LeetCode](https://www.leetcode.com/problems/maximum-sum-of-minimum-product/)
- [LeetCode Discuss — LC 1856: Maximum Sum of Minimum Product](https://www.leetcode.com/problems/maximum-sum-of-minimum-product/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximum-sum-of-minimum-product/editorial/) *(may require premium)*

## Key Takeaways

### Monotonic Stack:
1. **Maintains order:** Elements in decreasing order
2. **Efficient removal:** Can remove multiple elements at once
3. **Boundary finding:** Finds nearest smaller elements efficiently
4. **O(n) complexity:** Each element pushed and popped once

### Prefix Sum:
1. **Range sum calculation:** O(1) for any subarray sum
2. **Efficient computation:** Pre-computed sums
3. **Memory trade-off:** Uses O(n) extra space for O(1) queries

### Product Maximization:
1. **Minimum as pivot:** Consider each element as minimum
2. **Largest subarray:** Find maximum subarray where element is minimum
3. **Greedy approach:** Take largest possible subarray for each minimum
