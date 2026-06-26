---
layout: post
title: "[Medium] 3. Longest Substring Without Repeating Characters"
date: 2025-10-09 21:47:51 -0700
categories: leetcode algorithm medium cpp sliding-window hash-map string two-pointers problem-solving
---
Given a string `s`, find the length of the **longest substring** without repeating characters.

## Examples

**Example 1:**
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

**Example 2:**
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

**Example 3:**
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Thinking Process

1. **Sliding Window**: Use two pointers (`start` and `end`) to maintain a valid window

- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Sliding window</text>

  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | $O(n)$ | $O(1)$ | Window size known upfront |
| Variable-size window | $O(n)$ | $O(1)$ | Expand/shrink until valid |
| Window + hash map | $O(n)$ | $O(k)$ | Track character/count frequencies |
| Deque window max | $O(n)$ | $O(k)$ | Monotonic deque for max/min in window |

## Solution

**Time Complexity:** O(n)  
**Space Complexity:** O(min(m, n)) where m is the size of the charset

Use a sliding window approach with a hash map to track character positions and efficiently update the window boundaries.

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max_len = 0;
        unordered_map<char, int> hashmap;

        for (int start = 0, end = 0; end < s.length(); end++) {
            char cur = s[end];
            
            // If character exists and is within current window
            if (hashmap.find(cur) != hashmap.end() && hashmap[cur] >= start) {
                start = hashmap[cur] + 1;  // Move start past the duplicate
            }
            
            hashmap[cur] = end;  // Update character position
            max_len = max(max_len, end - start + 1);  // Update max length
        }
        return max_len;
    }
};
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Sliding Window**: Use two pointers (`start` and `end`) to maintain a valid window

**How the code works:**
1. **Sliding Window**: Use two pointers (`start` and `end`) to maintain a valid window
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

**Walkthrough** — input `s = "abcabcbb"`, expected output `3`:

The answer is "abc", with the length of 3.

| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n³) | O(min(m, n)) |
| Sliding Window + Set | O(n) | O(min(m, n)) |
| Sliding Window + Hash Map | O(n) | O(min(m, n)) |
## Algorithm Breakdown

### 1. Initialize Variables
```cpp
int max_len = 0;
unordered_map<char, int> hashmap;
```

### 2. Expand Window
```cpp
for (int start = 0, end = 0; end < s.length(); end++) {
    char cur = s[end];
```

### 3. Handle Duplicates
```cpp
if (hashmap.find(cur) != hashmap.end() && hashmap[cur] >= start) {
    start = hashmap[cur] + 1;  // Move start past duplicate
}
```

### 4. Update and Track
```cpp
hashmap[cur] = end;  // Update character position
max_len = max(max_len, end - start + 1);  // Update max length
```

### Complexity
| Approach | Time Complexity | Space Complexity |
|----------|----------------|------------------|
| Brute Force | O(n³) | O(min(m, n)) |
| Sliding Window + Set | O(n) | O(min(m, n)) |
| Sliding Window + Hash Map | O(n) | O(min(m, n)) |

## Why This Solution is Optimal

1. **Single Pass**: Each character is visited exactly once
2. **Efficient Lookup**: Hash map provides O(1) character position lookup
3. **Smart Window Adjustment**: Directly jumps to the correct position instead of sliding one by one
4. **Minimal Space**: Only stores character positions, not the entire substring

## Common Mistakes

1. **Empty string**: `s = ""` → `0`
2. **Single character**: `s = "a"` → `1`
3. **All same characters**: `s = "aaaa"` → `1`
4. **No duplicates**: `s = "abcdef"` → `6`

1. **Not checking if duplicate is within current window**
2. **Using `start = end` instead of `start = hashmap[cur] + 1`**
3. **Forgetting to update `max_len` after each iteration**
4. **Not handling edge cases like empty string**

## Related Problems

- [159. Longest Substring with At Most Two Distinct Characters](https://www.leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)
- [340. Longest Substring with At Most K Distinct Characters](https://www.leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/)
- [424. Longest Repeating Character Replacement](https://www.leetcode.com/problems/longest-repeating-character-replacement/)
- [76. Minimum Window Substring](https://www.leetcode.com/problems/minimum-window-substring/)

## References

- [LC 3: Longest Substring Without Repeating Characters on LeetCode](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/)
- [LeetCode Discuss — LC 3: Longest Substring Without Repeating Characters](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/longest-substring-without-repeating-characters/editorial/) *(may require premium)*

## Key Takeaways

1. **Sliding Window**: Use two pointers (`start` and `end`) to maintain a valid window
2. **Hash Map Tracking**: Store the last position of each character
3. **Efficient Updates**: When a duplicate is found, move `start` to `hashmap[cur] + 1`
4. **Single Pass**: Process each character exactly once
