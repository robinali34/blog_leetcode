---
layout: post
title: "455. Assign Cookies"
date: 2026-01-03 00:00:00 -0700
categories: [leetcode, easy, array, greedy, sorting, two-pointers]
permalink: /2026/01/03/easy-455-assign-cookies/
---

# 455. Assign Cookies

## Problem Statement

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child **at most one cookie**.

Each child `i` has a **greed factor** `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to **maximize the number of your content children** and output the maximum number.

## Examples

**Example 1:**
```
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
```

**Example 2:**
```
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.
```

## Constraints

- `1 <= g.length <= 3 * 10^4`
- `0 <= s.length <= 3 * 10^4`
- `1 <= g[i], s[j] <= 2^31 - 1`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Assignment rule**: Can one cookie satisfy multiple children? (Assumption: No - one cookie can only satisfy one child)

2. **Cookie size requirement**: What size cookie is needed for a child? (Assumption: Cookie size must be >= child's greed factor)

3. **Optimization goal**: What are we optimizing for? (Assumption: Maximize the number of satisfied children - greedy approach)

4. **Cookie reuse**: Can we use the same cookie multiple times? (Assumption: No - each cookie can only be used once)

5. **Ordering**: Does the order of children or cookies matter? (Assumption: No - we can assign in any order, but sorting helps optimize)

## Interview Deduction Process (10 minutes)

### Step 1: Brute-Force Approach (2 minutes)
**Initial Thought**: "I need to assign cookies to children. Let me try all possible assignments."

**Naive Solution**: Try all possible cookie-to-child assignments, count valid ones. Use nested loops or backtracking.

**Complexity**: O(n × m) or exponential time, O(1) space

**Issues**:
- Very inefficient for large inputs
- Doesn't leverage greedy property
- Overcomplicated for this problem

### Step 2: Semi-Optimized Approach (3 minutes)
**Insight**: "I should match smallest cookie to smallest child first. This is a greedy approach."

**Improved Solution**: Sort both arrays. Use two pointers to match smallest available cookie to smallest unsatisfied child greed factor.

**Complexity**: O(n log n + m log m) time, O(1) space

**Improvements**:
- Greedy matching is optimal
- Sorting enables efficient matching
- Two-pointer technique is clean
- Handles all cases correctly

### Step 3: Optimized Solution (5 minutes)
**Final Optimization**: "The greedy two-pointer approach is already optimal. Sorting is necessary for correctness."

**Best Solution**: Sort both arrays, use greedy matching with two pointers. This maximizes number of satisfied children.

**Key Realizations**:
1. Greedy approach is optimal for this problem
2. Sorting enables efficient O(n + m) matching after sort
3. Two-pointer technique is elegant
4. O(n log n) sorting dominates time complexity

## Solution Approach

This is a classic **greedy algorithm** problem. The key insight is to use a greedy strategy: assign the smallest cookie that satisfies each child's greed factor, starting with the child with the smallest greed factor.

### Key Insights:

1. **Sorting**: Sort both arrays to process in order
2. **Greedy Choice**: Always assign the smallest cookie that satisfies a child
3. **Two Pointers**: Use two pointers to match children with cookies efficiently
4. **Optimal**: This greedy approach maximizes the number of content children

### Algorithm:

1. **Sort**: Sort `g` (children's greed factors) and `s` (cookie sizes)
2. **Match**: Use two pointers to match smallest cookie to smallest child
3. **Count**: Count successful assignments

## Solution

### **Solution 1: Two Pointers with Conditional Advancement**

```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int count = 0, i = 0, j = 0;
        while(i < g.size() && j < s.size()){
            if(s[j] >= g[i]) {
                count++;
                i++;
                j++;
            } else {
                j++;
            }
        }
        return count;
    }
};
```

### **Solution 2: Two Pointers with While Loop for Cookie**

```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        const int numOfChildren = g.size(), numOfCookies = s.size();
        int count = 0;
        for(int i = 0, j = 0; i < numOfChildren && j < numOfCookies; i++, j++) {
            while(j < numOfCookies && g[i] > s[j]) {
                j++;
            }
            if(j < numOfCookies) {
                count++;
            }
        }
        return count;
    }
};
```

### **Algorithm Explanation:**

**Solution 1:**
1. **Sort Arrays (Lines 4-5)**:
   - Sort `g` in ascending order (children's greed factors)
   - Sort `s` in ascending order (cookie sizes)

2. **Two Pointers Matching (Lines 6-14)**:
   - **Initialize**: `i` for children, `j` for cookies, `count` for assignments
   - **While both arrays have elements**:
     - **If cookie satisfies child**: `s[j] >= g[i]`
       - Increment `count`
       - Move to next child (`i++`)
       - Move to next cookie (`j++`)
     - **Else**: Cookie too small, skip it (`j++`)

**Solution 2:**
1. **Sort Arrays (Lines 4-5)**: Same as Solution 1

2. **For Each Child (Lines 7-13)**:
   - **Skip small cookies**: Use `while` loop to skip cookies smaller than child's greed
   - **Check bounds**: Ensure `j < numOfCookies` after skipping
   - **Assign if valid**: If cookie found, increment count
   - **Advance both**: Move to next child and cookie

### **Example Walkthrough:**

**Example 1: `g = [1,2,3]`, `s = [1,1]`**

**After sorting:**
```
g = [1, 2, 3]
s = [1, 1]
```

**Solution 1 Execution:**
```
Initial: i=0, j=0, count=0

Step 1: s[0]=1 >= g[0]=1 ✓
  count=1, i=1, j=1

Step 2: s[1]=1 < g[1]=2 ✗
  j=2 (out of bounds)

Result: count=1
```

**Solution 2 Execution:**
```
Initial: i=0, j=0, count=0

i=0: g[0]=1
  while: j=0, s[0]=1 >= 1, no skip
  j=0 < 2 ✓, count=1
  i=1, j=1

i=1: g[1]=2
  while: j=1, s[1]=1 < 2, j=2 (out of bounds)
  j=2 >= 2 ✗, no assignment

Result: count=1
```

**Example 2: `g = [1,2]`, `s = [1,2,3]`**

**After sorting:**
```
g = [1, 2]
s = [1, 2, 3]
```

**Solution 1 Execution:**
```
Initial: i=0, j=0, count=0

Step 1: s[0]=1 >= g[0]=1 ✓
  count=1, i=1, j=1

Step 2: s[1]=2 >= g[1]=2 ✓
  count=2, i=2 (out of bounds)

Result: count=2
```

**Solution 2 Execution:**
```
Initial: i=0, j=0, count=0

i=0: g[0]=1
  while: j=0, s[0]=1 >= 1, no skip
  j=0 < 3 ✓, count=1
  i=1, j=1

i=1: g[1]=2
  while: j=1, s[1]=2 >= 2, no skip
  j=1 < 3 ✓, count=2
  i=2 (out of bounds)

Result: count=2
```

## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy is optimal because:
1. **Smallest First**: Assign smallest cookie to smallest child maximizes remaining options
2. **No Regret**: If we skip a cookie for a child, we can't use it later (each child gets at most one)
3. **Optimal Substructure**: After assigning a cookie, the subproblem (remaining children and cookies) is independent

### **Why Sorting is Necessary**

Without sorting, we might:
- Assign a large cookie to a child with small greed factor
- Miss opportunities to satisfy more children
- Need to check all combinations (O(n²))

With sorting:
- Process in order (smallest to largest)
- Greedy choice is optimal
- Linear time matching

### **Comparison of Solutions**

**Solution 1:**
- **Advancement**: Cookie pointer advances in both branches
- **Logic**: Clear if-else structure
- **Efficiency**: Both pointers advance optimally

**Solution 2:**
- **Advancement**: Cookie pointer skips multiple small cookies at once
- **Logic**: Uses while loop to skip cookies
- **Efficiency**: Same time complexity, slightly different style

Both solutions have the same time complexity and produce the same result.

## Time & Space Complexity

- **Time Complexity**: 
  - **Sorting**: O(g log g + s log s) where g = |g|, s = |s|
  - **Matching**: O(g + s) - each element visited at most once
  - **Total**: O(g log g + s log s)
- **Space Complexity**: O(1) - only using a few variables (excluding input arrays)

## Key Points

1. **Greedy Algorithm**: Always make locally optimal choice
2. **Sorting**: Essential for greedy approach to work
3. **Two Pointers**: Efficient matching technique
4. **Optimal**: Greedy strategy maximizes number of content children
5. **Simple**: Straightforward implementation

## Alternative Approaches

### **Approach 1: Greedy with Sorting (Current Solutions)**
- **Time**: O(g log g + s log s)
- **Space**: O(1)
- **Best for**: General case, optimal solution

### **Approach 2: Brute Force (Check All Combinations)**
- **Time**: O(g × s)
- **Space**: O(1)
- **Use when**: Arrays are very small (not practical)

### **Approach 3: Binary Search (For Each Child)**
- **Time**: O(g log s)
- **Space**: O(1)
- **Use when**: Cookies array is much larger than children array

## Edge Cases

1. **No cookies**: `s = []` → return 0
2. **No children**: `g = []` → return 0
3. **All cookies too small**: `g = [5,6,7]`, `s = [1,2,3]` → return 0
4. **All children satisfied**: `g = [1,2]`, `s = [3,4,5]` → return 2
5. **Single child, single cookie**: `g = [1]`, `s = [1]` → return 1

## Related Problems

- [135. Candy](https://leetcode.com/problems/candy/) - Greedy with constraints
- [406. Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) - Greedy with sorting
- [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) - Interval greedy
- [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) - Greedy interval selection

## Tags

`Array`, `Greedy`, `Sorting`, `Two Pointers`, `Easy`

