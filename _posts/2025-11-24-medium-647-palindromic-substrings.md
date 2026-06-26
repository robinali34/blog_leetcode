---
layout: post
title: "[Medium] 647. Palindromic Substrings"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm medium cpp string two-pointers problem-solving
permalink: /posts/2025-11-24-medium-647-palindromic-substrings/
tags: [leetcode, medium, string, two-pointers, palindrome, expand-around-center]
---
Given a string `s`, return *the number of **palindromic substrings** in it*.

A string is a **palindrome** when it reads the same backward as forward.

A **substring** is a contiguous sequence of characters within the string.

## Examples

**Example 1:**
```
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
```

**Example 2:**
```
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

**Example 3:**
```
Input: s = "racecar"
Output: 10
Explanation: 
Palindromic substrings: "r", "a", "c", "e", "c", "a", "r", "ceec", "aceca", "racecar"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.

## Thinking Process

1. **Two types of centers**: Every palindrome has either a single-character center (odd-length) or a two-character center (even-length)

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.



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
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

The key insight is that every palindrome expands from a center. For each position in the string, we can have:
1. **Odd-length palindromes**: Center at a single character (e.g., "aba" centered at 'b')
2. **Even-length palindromes**: Center between two characters (e.g., "abba" centered between two 'b's)

We iterate through each position and expand outward from both possible centers, counting all palindromic substrings found.

### Solution: Expand Around Centers

```cpp
class Solution {
private:
    int countPalindromesAroundCenter(const string& s, int low, int high) {
        int count = 0;
        while (low >= 0 && high < (int)s.size()) {
            if (s[low] != s[high]) break;
            low--;
            high++;
            count++;
        }
        return count;
    }

public:
    int countSubstrings(string s) {
        int count = 0;
        for (int i = 0; i < (int)s.size(); i++) {
            // Count odd-length palindromes (center at i)
            count += countPalindromesAroundCenter(s, i, i);
            // Count even-length palindromes (center between i and i+1)
            count += countPalindromesAroundCenter(s, i, i + 1);
        }
        return count;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** 1. **Two types of centers**: Every palindrome has either a single-character center (odd-length) or a two-character center (even-length)

**How the code works:**
1. **Two types of centers**: Every palindrome has either a single-character center (odd-length) or a two-character center (even-length)
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `s = "abc"`, expected output `3`:

Three palindromic strings: "a", "b", "c".

**Time Complexity:** O(n²)
- We iterate through each position: O(n)
- For each position, we expand outward: O(n) in worst case
- Total: O(n²)

**Space Complexity:** O(1)
- Only using a few variables
- No extra data structures
## Algorithm Breakdown

### Helper Function: `countPalindromesAroundCenter`

```cpp
int countPalindromesAroundCenter(const string& s, int low, int high) {
    int count = 0;
    while (low >= 0 && high < (int)s.size()) {
        if (s[low] != s[high]) break;
        low--;
        high++;
        count++;
    }
    return count;
}
```

**How it works:**
1. Start with `low` and `high` as the center (or centers for even-length)
2. Expand outward while characters match
3. Count each valid palindrome found
4. Stop when characters don't match or indices go out of bounds

**Why it works:**
- Each expansion creates a new palindromic substring
- We count all palindromes that can be formed from this center
- The function handles both odd and even-length palindromes based on initial `low` and `high`

### Main Function: `countSubstrings`

```cpp
int countSubstrings(string s) {
    int count = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        count += countPalindromesAroundCenter(s, i, i);      // Odd-length
        count += countPalindromesAroundCenter(s, i, i + 1); // Even-length
    }
    return count;
}
```

**How it works:**
1. For each position `i`, check both possible centers
2. Sum all palindromic substrings found
3. Return total count

### Complexity
**Time Complexity:** O(n²)
- We iterate through each position: O(n)
- For each position, we expand outward: O(n) in worst case
- Total: O(n²)

**Space Complexity:** O(1)
- Only using a few variables
- No extra data structures

## Common Mistakes

1. **Single character**: Returns 1 (the character itself is a palindrome)
2. **All same characters**: Returns n(n+1)/2 (all substrings are palindromes)
3. **No palindromes longer than 1**: Returns n (only single characters are palindromes)

1. **Missing even-length palindromes**: Forgetting to check centers between characters
2. **Double counting**: Not properly handling boundaries
3. **Index out of bounds**: Not checking bounds before accessing array
4. **Wrong expansion logic**: Not expanding symmetrically from center

## Optimization Tips

1. **Early termination**: Can stop early if no more palindromes possible (not applicable here)
2. **Use expand-around-center**: More space-efficient than DP
3. **Cache results**: Not needed for this problem, but useful for related problems

## Related Problems

- [5. Longest Palindromic Substring](https://www.leetcode.com/problems/longest-palindromic-substring/) - Find the longest palindrome (can use same technique) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/)
- [516. Longest Palindromic Subsequence](https://www.leetcode.com/problems/longest-palindromic-subsequence/) - Find longest palindromic subsequence (DP)
- [125. Valid Palindrome](https://www.leetcode.com/problems/valid-palindrome/) - Check if string is palindrome
- [680. Valid Palindrome II](https://www.leetcode.com/problems/valid-palindrome-ii/) - Check if string can be palindrome after deleting at most one character

## Pattern Recognition

This problem demonstrates the **"Expand Around Centers"** pattern:

```
1. Identify possible centers (single char or between chars)
2. For each center, expand outward symmetrically
3. Count valid expansions
```

Similar problems:
- Longest palindromic substring
- Palindrome partitioning
- Palindrome-related string problems

## Real-World Applications

1. **String Analysis**: Finding palindromic patterns in DNA sequences
2. **Text Processing**: Detecting palindromic words or phrases
3. **Algorithm Design**: Understanding palindrome detection techniques
4. **Interview Preparation**: Common pattern in coding interviews

## Key Takeaways

1. **Two types of centers**: Every palindrome has either a single-character center (odd-length) or a two-character center (even-length)

2. **Expand outward**: For each center, expand while characters match

3. **Count incrementally**: Each successful expansion creates a new palindromic substring

4. **No overlap**: Each center is checked independently, so we count all palindromes exactly once

## References

- [LC 647: Palindromic Substrings on LeetCode](https://www.leetcode.com/problems/palindromic-substrings/)
- [LeetCode Discuss — LC 647: Palindromic Substrings](https://www.leetcode.com/problems/palindromic-substrings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/palindromic-substrings/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
