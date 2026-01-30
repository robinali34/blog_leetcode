---
layout: post
title: "645. Set Mismatch"
date: 2026-01-19 00:00:00 -0700
categories: [leetcode, easy, array, hash-table, math]
permalink: /2026/01/19/easy-645-set-mismatch/
tags: [leetcode, easy, array, hash-table, math, bit-manipulation, negative-marking]
---

# 645. Set Mismatch

## Problem Statement

You have a set of integers `s`, which originally contains all the numbers from `1` to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated to another number in the set, which results in **repetition of one** number and **loss of another** number.

You are given an integer array `nums` representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form `[duplicate, missing]`.

## Examples

**Example 1:**
```
Input: nums = [1,2,2,4]
Output: [2,3]
Explanation: 2 is duplicated, 3 is missing.
```

**Example 2:**
```
Input: nums = [1,1]
Output: [1,2]
Explanation: 1 is duplicated, 2 is missing.
```

## Constraints

- `2 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^4`
- Exactly one number appears twice, exactly one is missing.

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Array properties**: What are the properties of the array? (Assumption: Array contains numbers from 1 to n, with one duplicate and one missing)

2. **Output format**: What should we return - duplicate first or missing first? (Assumption: Return [duplicate, missing] - duplicate appears first)

3. **Single duplicate**: Is there exactly one duplicate and one missing? (Assumption: Yes - exactly one number appears twice, one number is missing)

4. **Array modification**: Can we modify the input array? (Assumption: Typically yes for space optimization, but should clarify)

5. **Range**: What is the range of numbers? (Assumption: Numbers are from 1 to n, where n is array length)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Use a hash set to track seen numbers. Iterate through the array, if a number is already in the set, it's the duplicate. After iteration, find the missing number by checking which number from 1 to n is not in the set. This approach uses O(n) extra space and O(n) time.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use the array itself for marking: since numbers are from 1 to n, we can use the array indices. For each number, mark the corresponding index as negative (or use a different marking scheme). The duplicate will be detected when we try to mark an already-marked index. The missing number is the index that remains unmarked. This uses O(1) extra space but modifies the input array.

**Step 3: Optimized Solution (5 minutes)**

Use mathematical approach: calculate the expected sum S = n×(n+1)/2 and actual sum. The difference gives us duplicate - missing. Also calculate expected sum of squares and actual sum of squares. Use these two equations to solve for duplicate and missing. Alternatively, use the marking approach with O(1) space if array modification is allowed. The mathematical approach achieves O(n) time with O(1) space without modifying the array, which is optimal. The key insight is leveraging the properties that we have exactly one duplicate and one missing, allowing us to use mathematical relationships to find both.

## Solution Approach

This problem requires finding both a duplicate and a missing number in an array that should contain numbers from 1 to n. There are several approaches:

1. **Mathematical Approach**: Use sum and sum of squares to derive equations
2. **Negative Marking**: Mark visited indices in-place
3. **Hash Map/Count Array**: Count occurrences of each number
4. **XOR Approach**: Use bit manipulation

### Key Insights:

1. **Mathematical Relations**: 
   - Sum difference: `sum(nums) - sum(1..n) = duplicate - missing`
   - Square sum difference: `sum(nums²) - sum(1²..n²) = duplicate² - missing²`
   - Can solve system of equations

2. **Negative Marking**: Use array indices to track visited numbers
3. **XOR**: Use XOR properties to find both numbers

## Solution 1: Mathematical Approach (Sum & Square Sum)

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        const int N = nums.size();
        long long x = 0, y = 0;
        for(int i = 1; i <= N; i++) {
            x += nums[i - 1] - i;
            y += (long long) nums[i - 1] * nums[i - 1] - (long long)i * i;
        }
        int missing = (y - x * x) / (2 * x);
        int duplicate = missing + x;
        return {duplicate, missing};
    }
};
```

### Algorithm Explanation:

1. **Calculate Differences**:
   - `x = sum(nums) - sum(1..n) = duplicate - missing`
   - `y = sum(nums²) - sum(1²..n²) = duplicate² - missing²`

2. **Derive Equations**:
   - From `y = duplicate² - missing² = (duplicate - missing)(duplicate + missing)`
   - We have: `duplicate + missing = y / x`
   - And: `duplicate - missing = x`

3. **Solve System**:
   - `missing = (y/x - x) / 2 = (y - x²) / (2x)`
   - `duplicate = missing + x`

### Example Walkthrough:

**Input:** `nums = [1,2,2,4]`, `N = 4`

```
Expected: [1,2,3,4]
Actual:   [1,2,2,4]

Calculate x (sum difference):
  i=1: nums[0] - 1 = 1 - 1 = 0
  i=2: nums[1] - 2 = 2 - 2 = 0
  i=3: nums[2] - 3 = 2 - 3 = -1
  i=4: nums[3] - 4 = 4 - 4 = 0
  x = 0 + 0 + (-1) + 0 = -1
  x = duplicate - missing = -1

Calculate y (square sum difference):
  i=1: 1² - 1² = 0
  i=2: 2² - 2² = 0
  i=3: 2² - 3² = 4 - 9 = -5
  i=4: 4² - 4² = 0
  y = 0 + 0 + (-5) + 0 = -5
  y = duplicate² - missing² = -5

Solve:
  missing = (y - x²) / (2x) = (-5 - 1) / (-2) = -6 / -2 = 3 ✓
  duplicate = missing + x = 3 + (-1) = 2 ✓

Return: [2, 3] ✓
```

### Complexity Analysis:

- **Time Complexity:** O(n)
  - Single pass through array to calculate sums
  - Constant time arithmetic operations

- **Space Complexity:** O(1)
  - Only using a few variables (x, y, missing, duplicate)
  - No extra data structures

## Solution 2: Negative Marking (In-place)

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int duplicate = -1;
        int n = nums.size();

        // First pass: find duplicate by marking visited indices negative
        for (int x : nums) {
            int idx = abs(x) - 1;  // convert to 0-based index
            if (nums[idx] < 0) {
                // Already negative => this value seen before
                duplicate = abs(x);
            } else {
                nums[idx] = -nums[idx];  // Mark as visited
            }
        }

        // Second pass: find missing number (index with positive value)
        int missing = -1;
        for (int i = 0; i < n; ++i) {
            if (nums[i] > 0) {
                missing = i + 1;
                break;
            }
        }

        return {duplicate, missing};
    }
};
```

### Algorithm Explanation:

1. **First Pass - Find Duplicate**:
   - For each number `x`, use `abs(x) - 1` as index
   - If `nums[idx]` is already negative, `x` is duplicate
   - Otherwise, mark `nums[idx]` as negative (visited)

2. **Second Pass - Find Missing**:
   - Find index `i` where `nums[i] > 0`
   - Missing number is `i + 1`

### Complexity Analysis:

- **Time Complexity:** O(n) - Two passes
- **Space Complexity:** O(1) - Modifies input array in-place

## Solution 3: Hash Map / Count Array

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        vector<int> count(n + 1, 0);
        int duplicate = -1, missing = -1;

        // Count occurrences
        for (int x : nums) {
            count[x]++;
        }

        // Find duplicate (count == 2) and missing (count == 0)
        for (int i = 1; i <= n; ++i) {
            if (count[i] == 2) duplicate = i;
            else if (count[i] == 0) missing = i;
        }

        return {duplicate, missing};
    }
};
```

### Complexity Analysis:

- **Time Complexity:** O(n) - Count then scan
- **Space Complexity:** O(n) - Count array

## Solution 4: XOR Approach

```cpp
class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int xor_all = 0;
        
        // XOR all numbers in nums and 1..n
        for (int i = 0; i < n; i++) {
            xor_all ^= nums[i];
            xor_all ^= (i + 1);
        }
        
        // xor_all = duplicate ^ missing
        // Find rightmost set bit
        int rightmost_bit = xor_all & (-xor_all);
        
        int xor0 = 0, xor1 = 0;
        // Separate numbers into two groups based on rightmost bit
        for (int i = 0; i < n; i++) {
            if (nums[i] & rightmost_bit) {
                xor1 ^= nums[i];
            } else {
                xor0 ^= nums[i];
            }
            if ((i + 1) & rightmost_bit) {
                xor1 ^= (i + 1);
            } else {
                xor0 ^= (i + 1);
            }
        }
        
        // Determine which is duplicate and which is missing
        for (int num : nums) {
            if (num == xor0) {
                return {xor0, xor1};
            }
        }
        return {xor1, xor0};
    }
};
```

### Complexity Analysis:

- **Time Complexity:** O(n) - Multiple passes
- **Space Complexity:** O(1) - Only variables

## Key Insights

1. **Mathematical Approach**: Elegant solution using sum and square sum differences
2. **Negative Marking**: Space-efficient in-place solution
3. **Hash Map**: Simple and intuitive, uses extra space
4. **XOR**: Bit manipulation approach, more complex but interesting

## Edge Cases

1. **Smallest input**: `nums = [1,1]` → `[1,2]`
2. **Largest input**: `nums = [1,2,3,...,n-1,n,n]` → `[n, n+1]` (but n+1 > n, so invalid)
3. **Duplicate at start**: `nums = [2,2,3,4]` → `[2,1]`
4. **Duplicate at end**: `nums = [1,2,3,3]` → `[3,4]` (but 4 > 3, so invalid)
5. **Missing at start**: `nums = [2,2,3,4]` → `[2,1]`
6. **Missing at end**: `nums = [1,1,2,3]` → `[1,4]` (but 4 > 3, so invalid)

## Common Mistakes

1. **Integer overflow**: Not using `long long` for square calculations
2. **Index off-by-one**: Confusing 0-based vs 1-based indexing
3. **Sign errors**: Incorrect handling of negative values in mathematical approach
4. **Division by zero**: Not checking if `x == 0` (shouldn't happen per constraints)
5. **Wrong order**: Returning `[missing, duplicate]` instead of `[duplicate, missing]`

## Comparison of Approaches

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Mathematical** | O(n) | O(1) | Elegant, no modification | Requires careful math, overflow risk |
| **Negative Marking** | O(n) | O(1) | In-place, efficient | Modifies input array |
| **Hash Map** | O(n) | O(n) | Simple, clear | Uses extra space |
| **XOR** | O(n) | O(1) | Bit manipulation | Complex logic |

## When to Use Each Approach

- **Mathematical**: When you want elegant solution, no array modification
- **Negative Marking**: When space optimization is critical, modification allowed
- **Hash Map**: When clarity is priority, space is available
- **XOR**: When learning bit manipulation techniques

## Related Problems

- [LC 41: First Missing Positive](https://leetcode.com/problems/first-missing-positive/) - Find missing positive number
- [LC 268: Missing Number](https://leetcode.com/problems/missing-number/) - Find single missing number
- [LC 442: Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/) - Find all duplicates
- [LC 448: Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/) - Find all missing numbers
- [LC 287: Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/) - Find duplicate (no missing)

---

*This problem demonstrates multiple solution approaches including **mathematical derivation**, **in-place marking**, and **hash-based counting**. The mathematical approach is particularly elegant, using sum and square sum differences to solve a system of equations.*

