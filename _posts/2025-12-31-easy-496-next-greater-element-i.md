---
layout: post
title: "[Easy] 496. Next Greater Element I"
date: 2025-12-31 18:30:00 -0700
categories: [leetcode, easy, array, stack, monotonic-stack, hash-table]
permalink: /2025/12/31/easy-496-next-greater-element-i/
---
The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the **next greater element** of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return *an array `ans` of length `nums1.length` such that `ans[i]` is the **next greater element** as described above*.

## Thinking Process

The **next greater element** of some element `x` in an array is the **first greater** element that is **to the right** of `x` in the same array.

You are given two **distinct 0-indexed** integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

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

## Examples

**Example 1:**
```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
```

**Example 2:**
```
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```

## Constraints

- `1 <= nums1.length <= nums2.length <= 1000`
- `0 <= nums1[i], nums2[i] <= 10^4`
- All integers in `nums1` and `nums2` are **unique**.
- All the integers of `nums1` also appear in `nums2`.

## Algorithm Breakdown

### **Key Insight: Monotonic Stack**

The stack maintains elements in **decreasing order** (from bottom to top):
- When we see a new element, pop all smaller or equal elements
- The top of stack is the next greater element
- Push current element to maintain monotonic property

### **Right-to-Left Traversal**

Processing from right to left ensures:
- We've already processed elements to the right
- Stack contains potential next greater elements
- Each element's next greater is already in stack

### **Why This Works**

1. **Stack Property**: Stack stores elements in decreasing order
2. **Popping Logic**: Elements ≤ current can't be next greater for anything left
3. **Top Element**: Top of stack is the first greater element to the right
4. **Hash Map**: Stores results for O(1) lookup later

## Monotonic Stack Template

Here's the general template for next greater element problems:

```cpp
vector<int> nextGreaterElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1);
    stack<int> stk;
    
    // Traverse from right to left
    for(int i = n - 1; i >= 0; i--) {
        // Pop elements that can't be next greater
        while(!stk.empty() && nums[i] >= stk.top()) {
            stk.pop();
        }
        
        // Top of stack is next greater element
        if(!stk.empty()) {
            result[i] = stk.top();
        }
        
        // Push current element
        stk.push(nums[i]);
    }
    
    return result;
}
```

### **Key Template Components:**

1. **Right-to-Left Traversal**: Process array backwards
2. **Monotonic Stack**: Maintain decreasing order
3. **Pop Condition**: Remove elements ≤ current
4. **Result Storage**: Store next greater or -1

### Complexity
### **Time Complexity:** O(n + m)
- **Process nums2**: O(n) where n = nums2.length
- **Query nums1**: O(m) where m = nums1.length
- **Total**: O(n + m)

### **Space Complexity:** O(n)
- **Hash map**: O(n) - stores next greater for each element in nums2
- **Stack**: O(n) - worst case all elements in stack
- **Total**: O(n)

## Key Points

1. **Monotonic Stack**: Maintains elements in decreasing order
2. **Right-to-Left**: Process from end to find next greater efficiently
3. **Hash Map**: O(1) lookup for results
4. **Single Pass**: Process nums2 once, query nums1 once
5. **Efficient**: O(n + m) time complexity

## Detailed Example Walkthrough

### **Example: `nums1 = [2,4], nums2 = [1,2,3,4]`**

```
Step 1: Process nums2 from right to left

i=3: num = 4
  Stack: []
  Pop: nothing
  hashmap[4] = -1
  Stack: [4]

i=2: num = 3
  Stack: [4]
  Pop: 4 <= 3? No → keep 4
  hashmap[3] = 4
  Stack: [3, 4]

i=1: num = 2
  Stack: [3, 4]
  Pop: 3 <= 2? No → keep 3
  hashmap[2] = 3
  Stack: [2, 3, 4]

i=0: num = 1
  Stack: [2, 3, 4]
  Pop: 2 <= 1? No → keep 2
  hashmap[1] = 2
  Stack: [1, 2, 3, 4]

hashmap = {4: -1, 3: 4, 2: 3, 1: 2}

Step 2: Query nums1
nums1[0] = 2 → hashmap[2] = 3
nums1[1] = 4 → hashmap[4] = -1

Result: [3, -1]
```

## Edge Cases

1. **No greater element**: Element is maximum in nums2 → return -1
2. **Single element**: nums2 has one element → return -1
3. **All decreasing**: nums2 in decreasing order → all return -1
4. **All increasing**: nums2 in increasing order → each has next greater
5. **Duplicate handling**: Problem states all integers are unique

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Related Problems

- [496. Next Greater Element I](https://www.leetcode.com/problems/next-greater-element-i/) - Current problem
- [503. Next Greater Element II](https://www.leetcode.com/problems/next-greater-element-ii/) - Circular array
- [739. Daily Temperatures](https://www.leetcode.com/problems/daily-temperatures/) - Similar next greater pattern
- [84. Largest Rectangle in Histogram](https://www.leetcode.com/problems/largest-rectangle-in-histogram/) - Monotonic stack application

## Tags

`Array`, `Stack`, `Monotonic Stack`, `Hash Table`, `Easy`

## Key Takeaways

- Stack matches nested or LIFO structure (parentheses, monotonic scans).
- Push on open / larger; pop when the current element resolves pending work.
- Monotonic stack finds next greater/smaller in O(n).

## References

- [LC 496: Next Greater Element I on LeetCode](https://www.leetcode.com/problems/next-greater-element-i/)
- [LeetCode Discuss — LC 496: Next Greater Element I](https://www.leetcode.com/problems/next-greater-element-i/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/next-greater-element-i/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
