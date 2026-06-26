---
layout: post
title: "[Easy] 455. Assign Cookies"
date: 2026-01-03 00:00:00 -0700
categories: [leetcode, easy, array, greedy, sorting, two-pointers]
permalink: /2026/01/03/easy-455-assign-cookies/
---
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

## Thinking Process

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child **at most one cookie**.

Each child `i` has a **greed factor** `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to **maximize the number of your content children** and output the maximum number.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | $O(n \log n)$ | $O(1)$ | Interval scheduling, assignment |
| Local greedy choice | $O(n)$ | $O(1)$ | Jump game, gas station |
| Greedy + heap | $O(n \log n)$ | $O(n)$ | Merge streams, room allocation |
| Exchange argument | $O(n)$ | $O(1)$ | Prove greedy choice is safe |

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

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** Assume you are an awesome parent and want to give your children some cookies. But, you should give each child **at most one cookie**.

**How the code works:**
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `g = [1,2,3], s = [1,1]`, expected output `1`:

You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

**Time:** - **Sorting**: O(g log g + s log s) where g = |g|, s = |s| · **Space:** O(1) - only using a few variables (excluding input arrays)

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

## Edge Cases

1. **No cookies**: `s = []` → return 0
2. **No children**: `g = []` → return 0
3. **All cookies too small**: `g = [5,6,7]`, `s = [1,2,3]` → return 0
4. **All children satisfied**: `g = [1,2]`, `s = [3,4,5]` → return 2
5. **Single child, single cookie**: `g = [1]`, `s = [1]` → return 1

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [135. Candy](https://www.leetcode.com/problems/candy/) - Greedy with constraints
- [406. Queue Reconstruction by Height](https://www.leetcode.com/problems/queue-reconstruction-by-height/) - Greedy with sorting
- [452. Minimum Number of Arrows to Burst Balloons](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) - Interval greedy
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) - Greedy interval selection

## Tags

`Array`, `Greedy`, `Sorting`, `Two Pointers`, `Easy`

## Key Takeaways

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

## References

- [LC 455: Assign Cookies on LeetCode](https://www.leetcode.com/problems/assign-cookies/)
- [LeetCode Discuss — LC 455: Assign Cookies](https://www.leetcode.com/problems/assign-cookies/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/assign-cookies/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
