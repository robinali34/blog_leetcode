---
layout: post
title: "1177. Can Make Palindrome from Substring"
date: 2026-01-01 01:00:00 -0700
categories: [leetcode, medium, string, bit-manipulation, prefix-sum, hash-table]
permalink: /2026/01/01/medium-1177-can-make-palindrome-from-substring/
---

# 1177. Can Make Palindrome from Substring

## Problem Statement

You are given a string `s` and array `queries` where `queries[i] = [left, right, k]`. We may **rearrange** the substring `s[left...right]` and then choose **up to `k`** of its characters to replace with any lowercase English letter.

If the substring can be made a **palindrome** after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return an array `answer`, where `answer[i]` is the result of the `i`-th query `queries[i]`.

Note that: Each letter is counted **individually** for replacement, so if, for example `s[left...right] = "aaa"`, and `k = 2`, we can only replace 2 of the letters. Also, note that the initial string `s` is never modified.

## Examples

**Example 1:**
```
Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]

Explanation:
- queries[0]: substring = "d", could be changed to "d" which is palindrome. true
- queries[1]: substring = "bc", could not get palindrome by rearranging without replacement. false
- queries[2]: substring = "abcd", could not get palindrome by rearranging and replacing 1 character. false
- queries[3]: substring = "abcd", could get palindrome by rearranging to "abba" and replacing 2 characters. true
- queries[4]: substring = "abcda", could get palindrome by rearranging to "aacda" and replacing 1 character. true
```

**Example 2:**
```
Input: s = "lyb", queries = [[0,1,0],[2,2,1]]
Output: [false,true]
```

## Constraints

- `1 <= s.length, queries.length <= 10^5`
- `0 <= left <= right < s.length`
- `0 <= k <= s.length`
- `s` consists of lowercase English letters.

## Solution Approach

This problem requires checking if a substring can be rearranged and have at most `k` characters replaced to form a palindrome. The key insight is that a palindrome can have **at most one character with odd frequency** (the center character).

### Key Insights:

1. **Palindrome Property**: A palindrome can have at most 1 character with odd frequency
2. **Bit Manipulation**: Use XOR to track character parity (odd/even frequency)
3. **Prefix XOR**: Build prefix XOR array to quickly get character frequencies for any range
4. **Count Odd Frequencies**: Count bits set in XOR result to find characters with odd frequency
5. **Replacement Formula**: Need at most `(odd_count - 1) / 2` replacements

### Algorithm:

1. **Build Prefix XOR Array**: Track character parity using bit manipulation
2. **For Each Query**: 
   - Get XOR of range to find characters with odd frequency
   - Count number of odd frequencies
   - Check if `odd_count <= 2 * k + 1`

## Solution

### **Solution: Bit Manipulation with Prefix XOR**

```cpp
class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        const int N = s.size();
        vector<int> count(N + 1);
        for(int i = 0; i < N; i++) {
            count[i + 1] = count[i] ^ (1 << (s[i] - 'a'));
        }
        vector<bool> rtn;
        for(auto& query : queries) {
            int left = query[0], right = query[1], k = query[2];
            int bits = 0, x = count[right + 1] ^ count[left];
            while(x > 0) {
                x &= x - 1;
                bits++;
            }
            rtn.push_back(bits <= k * 2 + 1);
        }
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Build Prefix XOR Array (Lines 5-9)**:
   - **Initialize**: `count[0] = 0` (no characters)
   - **For each character**: `count[i + 1] = count[i] ^ (1 << (s[i] - 'a'))`
   - **XOR Property**: Toggles the bit for character `s[i]`
   - **Result**: `count[i]` tracks parity of all characters from index 0 to i-1
     - Bit `j` is set if character `'a' + j` appears odd number of times

2. **Process Each Query (Lines 11-19)**:
   - **Get range XOR**: `x = count[right + 1] ^ count[left]`
     - This gives parity of characters in range `[left, right]`
     - Bit `j` is set if character `'a' + j` appears odd times in range
   - **Count odd frequencies**: Count number of set bits in `x` using Brian Kernighan's algorithm
   - **Check palindrome**: `bits <= k * 2 + 1`
     - A palindrome can have at most 1 odd frequency (center)
     - With `k` replacements, we can fix `2k` odd frequencies (each replacement fixes 2)
     - Plus 1 for the center character if needed

### **Example Walkthrough:**

**Initialization: `s = "abcda"`**
```
s = "a b c d a"
    0 1 2 3 4

Build prefix XOR:
count[0] = 0 (no characters)

i=0: s[0]='a' → count[1] = count[0] ^ (1 << 0) = 0 ^ 1 = 1
     (bit 0 set: 'a' appears odd times)

i=1: s[1]='b' → count[2] = count[1] ^ (1 << 1) = 1 ^ 2 = 3
     (bits 0,1 set: 'a' and 'b' appear odd times)

i=2: s[2]='c' → count[3] = count[2] ^ (1 << 2) = 3 ^ 4 = 7
     (bits 0,1,2 set: 'a', 'b', 'c' appear odd times)

i=3: s[3]='d' → count[4] = count[3] ^ (1 << 3) = 7 ^ 8 = 15
     (bits 0,1,2,3 set: 'a', 'b', 'c', 'd' appear odd times)

i=4: s[4]='a' → count[5] = count[4] ^ (1 << 0) = 15 ^ 1 = 14
     (bits 1,2,3 set: 'b', 'c', 'd' appear odd times, 'a' now even)

count = [0, 1, 3, 7, 15, 14]
```

**Query 1: `[3, 3, 0]` - substring "d"**
```
x = count[4] ^ count[3] = 15 ^ 7 = 8
Binary: 1000 (bit 3 set: 'd' appears odd times)

Count bits: bits = 1
Check: 1 <= 0 * 2 + 1 = 1 ✓
Result: true (single character is always palindrome)
```

**Query 2: `[1, 2, 0]` - substring "bc"**
```
x = count[3] ^ count[1] = 7 ^ 1 = 6
Binary: 0110 (bits 1,2 set: 'b' and 'c' appear odd times)

Count bits: bits = 2
Check: 2 <= 0 * 2 + 1 = 1 ✗
Result: false (need at least 1 replacement, but k=0)
```

**Query 3: `[0, 3, 1]` - substring "abcd"**
```
x = count[4] ^ count[0] = 15 ^ 0 = 15
Binary: 1111 (bits 0,1,2,3 set: all appear odd times)

Count bits: bits = 4
Check: 4 <= 1 * 2 + 1 = 3 ✗
Result: false (need at least 2 replacements, but k=1)
```

**Query 4: `[0, 3, 2]` - substring "abcd"**
```
x = count[4] ^ count[0] = 15 ^ 0 = 15
Binary: 1111 (bits 0,1,2,3 set: all appear odd times)

Count bits: bits = 4
Check: 4 <= 2 * 2 + 1 = 5 ✓
Result: true (can fix 4 odd frequencies with 2 replacements)
```

**Query 5: `[0, 4, 1]` - substring "abcda"**
```
x = count[5] ^ count[0] = 14 ^ 0 = 14
Binary: 1110 (bits 1,2,3 set: 'b', 'c', 'd' appear odd times)

Count bits: bits = 3
Check: 3 <= 1 * 2 + 1 = 3 ✓
Result: true (can fix 3 odd frequencies with 1 replacement)
```

## Algorithm Breakdown

### **Why XOR Works for Parity**

XOR has the property that:
- `x ^ x = 0` (even occurrences cancel out)
- `x ^ 0 = x` (odd occurrence remains)

So when we XOR all characters in a range:
- Characters with even frequency → bit becomes 0
- Characters with odd frequency → bit becomes 1

### **Prefix XOR Pattern**

Similar to prefix sums, prefix XOR allows O(1) range queries:
- `count[i]` = XOR of characters from 0 to i-1
- `count[right + 1] ^ count[left]` = XOR of characters in range [left, right]

### **Palindrome Check Formula**

For a substring to be a palindrome:
- **At most 1 character** can have odd frequency (the center)
- With `k` replacements, we can fix `2k` odd frequencies
- Plus 1 for the center: `odd_count <= 2k + 1`

**Why `2k`?**
- Each replacement changes 2 characters' frequencies
- Replacing 'a' with 'b' decreases 'a' frequency by 1 and increases 'b' frequency by 1
- Net effect: fixes 2 odd frequencies (if both were odd) or creates 2 even frequencies

### **Brian Kernighan's Algorithm**

Counting set bits efficiently:
```cpp
int bits = 0;
while(x > 0) {
    x &= x - 1;  // Clear rightmost set bit
    bits++;
}
```

Time: O(number of set bits) instead of O(32)

## Time & Space Complexity

- **Time Complexity**:
  - **Initialization**: O(n) - build prefix XOR array
  - **Each Query**: O(1) amortized - count bits (at most 26 set bits)
  - **Total**: O(n + q) where q is number of queries
- **Space Complexity**: O(n) - store prefix XOR array

## Key Points

1. **Bit Manipulation**: Use XOR to track character parity efficiently
2. **Prefix XOR**: Similar to prefix sums, enables O(1) range queries
3. **Palindrome Property**: At most 1 odd frequency allowed
4. **Replacement Formula**: `k` replacements can fix `2k` odd frequencies
5. **Efficient**: O(1) per query after O(n) preprocessing

## Alternative Approaches

### **Approach 1: Bit Manipulation (Current Solution)**
- **Time**: O(n + q)
- **Space**: O(n)
- **Best for**: Multiple queries, efficient

### **Approach 2: Frequency Count for Each Query**
- **Time**: O(n × q) - count frequencies for each query
- **Space**: O(1)
- **Use when**: Very few queries

### **Approach 3: 2D Prefix Array**
- **Time**: O(n × 26 + q)
- **Space**: O(n × 26)
- **Overkill**: Not needed, bit manipulation is more efficient

## Edge Cases

1. **Single character**: Always palindrome, `bits = 1 <= 2k + 1`
2. **All even frequencies**: `bits = 0 <= 2k + 1` (always true)
3. **All odd frequencies**: Need `(n - 1) / 2` replacements
4. **k = 0**: Only works if substring is already palindrome
5. **Empty substring**: Not possible per constraints

## Related Problems

- [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/) - Check if string can be palindrome
- [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/) - Build longest palindrome
- [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/) - Can make palindrome with 1 deletion
- [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) - Check if palindrome

## Tags

`String`, `Bit Manipulation`, `Prefix Sum`, `Hash Table`, `Medium`

