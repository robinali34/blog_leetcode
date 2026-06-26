---
layout: post
title: "[Medium] 393. UTF-8 Validation"
date: 2025-12-31 22:30:00 -0700
categories: [leetcode, medium, bit-manipulation, string, array]
permalink: /2025/12/31/medium-393-utf-8-validation/
---
Given an integer array `data` representing the data, return whether it is a valid **UTF-8** encoding (i.e., it translates to a sequence of valid UTF-8 encoded characters).

A character in **UTF8** can be from **1 to 4 bytes** long, subjected to the following rules:

1. For a **1-byte** character, the first bit is a `0`, followed by its Unicode code.
2. For an **n-byte** character, the first `n` bits are all one's, the `n+1` bit is `0`, followed by `n-1` bytes with the most significant 2 bits being `10`.

This is how the UTF-8 encoding would work:

```
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

**Note:** The input is an array of integers. Only the **least significant 8 bits** of each integer is used to store the data. This means each integer represents only 1 byte of data.

## Thinking Process

Given an integer array `data` representing the data, return whether it is a valid **UTF-8** encoding (i.e., it translates to a sequence of valid UTF-8 encoded characters).

A character in **UTF8** can be from **1 to 4 bytes** long, subjected to the following rules:

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 90" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Bit manipulation</text>

  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Examples

**Example 1:**
```
Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-byte character followed by a 1-byte character.
```

**Example 2:**
```
Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-byte character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
```

## Constraints

- `1 <= data.length <= 2 * 10^4`
- `0 <= data[i] <= 255`

## Algorithm Breakdown

### **Key Insight: UTF-8 Bit Patterns**

UTF-8 encoding uses specific bit patterns:

**1-byte character:**
```
0xxxxxxx
Bit 7 = 0
```

**2-byte character:**
```
110xxxxx 10xxxxxx
Bits 7-5 = 110, then continuation bytes with 10
```

**3-byte character:**
```
1110xxxx 10xxxxxx 10xxxxxx
Bits 7-4 = 1110, then continuation bytes with 10
```

**4-byte character:**
```
11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Bits 7-3 = 11110, then continuation bytes with 10
```

### **Bit Mask Operations**

**MASK1 (0x80 = 10000000)**:
- Checks if most significant bit is set
- Used to detect 1-byte vs multi-byte characters

**MASK2 (0xC0 = 11000000)**:
- Checks bits 7 and 6 together
- Used to validate continuation bytes (must be `10xxxxxx`)

**getBytes Logic**:
- Counts leading 1s from left
- Stops when encountering 0
- Validates count is 2-4

### **Validation Process**

1. **First byte**: Determine character length
2. **Length check**: Ensure enough bytes available
3. **Continuation bytes**: All following bytes must start with `10`
4. **Move pointer**: Advance by character length

### Complexity
### **Time Complexity:** O(n)
- **Single pass**: Process each byte exactly once
- **Bit operations**: O(1) per byte
- **Total**: O(n) where n = data.length

### **Space Complexity:** O(1)
- **Variables**: Only use constant space
- **No extra arrays**: Process in-place
- **Total**: O(1)

## Key Points

1. **Bit Masks**: Use masks to check bit patterns efficiently
2. **Leading 1s**: Count leading 1s to determine byte count
3. **Continuation Bytes**: All continuation bytes must start with `10`
4. **Length Validation**: Ensure enough bytes for multi-byte characters
5. **Single Pass**: Process array once, O(n) time

## UTF-8 Encoding Rules

### **Byte Patterns**

| Bytes | Pattern | Binary Format |
|-------|---------|---------------|
| 1 | ASCII | `0xxxxxxx` |
| 2 | 2-byte | `110xxxxx 10xxxxxx` |
| 3 | 3-byte | `1110xxxx 10xxxxxx 10xxxxxx` |
| 4 | 4-byte | `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` |

### **Validation Rules**

1. **First byte**: Must match one of the patterns above
2. **Continuation bytes**: Must start with `10` (bits 7=1, 6=0)
3. **Length**: Must have exactly `n` bytes for `n`-byte character
4. **Range**: Character length must be 1-4 bytes

## Detailed Example Walkthrough

### **Example: `data = [240,162,138,147]` (4-byte character)**

```
Step 1: Process first byte (240)
240 in binary: 11110000
getBytes(240):
  Count leading 1s:
    240 & 128 = 128 ≠ 0 → n=1
    240 & 64 = 64 ≠ 0 → n=2
    240 & 32 = 32 ≠ 0 → n=3
    240 & 16 = 16 ≠ 0 → n=4
    240 & 8 = 0 → stop
  n = 4 → 4-byte character
  Check: idx + 4 = 4 <= 4 ✓

Step 2: Validate continuation bytes
data[1] = 162: (162 & 192) == 128 ✓
data[2] = 138: (138 & 192) == 128 ✓
data[3] = 147: (147 & 192) == 128 ✓

All continuation bytes valid → true
```

### **Example: `data = [255]` (Invalid)**

```
Process first byte (255)
255 in binary: 11111111
getBytes(255):
  Count leading 1s:
    255 & 128 = 128 ≠ 0 → n=1
    255 & 64 = 64 ≠ 0 → n=2
    255 & 32 = 32 ≠ 0 → n=3
    255 & 16 = 16 ≠ 0 → n=4
    255 & 8 = 8 ≠ 0 → n=5
    n > 4 → return -1

Result: false (invalid pattern)
```

## Edge Cases

1. **Single byte**: Array with one 1-byte character
2. **All 1-bytes**: Array of ASCII characters
3. **Invalid pattern**: Byte starting with `10` (continuation byte as first)
4. **Too many leading 1s**: More than 4 leading 1s
5. **Insufficient bytes**: Multi-byte character without enough bytes

## Bit Manipulation Tips

### **Common Bit Operations**

```cpp
// Check if bit 7 is set
(num & 0x80) != 0

// Check if bits 7-6 are "10"
(num & 0xC0) == 0x80

// Count leading 1s
int count = 0;
int mask = 0x80;
while ((num & mask) != 0 && count < 4) {
    count++;
    mask >>= 1;
}
```

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [393. UTF-8 Validation](https://www.leetcode.com/problems/utf-8-validation/) - Current problem
- [191. Number of 1 Bits](https://www.leetcode.com/problems/number-of-1-bits/) - Bit manipulation
- [190. Reverse Bits](https://www.leetcode.com/problems/reverse-bits/) - Bit manipulation
- [136. Single Number](https://www.leetcode.com/problems/single-number/) - Bit manipulation

## Tags

`Bit Manipulation`, `Array`, `String`, `Medium`

## Key Takeaways

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.

## References

- [LC 393: UTF-8 Validation on LeetCode](https://www.leetcode.com/problems/utf-8-validation/)
- [LeetCode Discuss — LC 393: UTF-8 Validation](https://www.leetcode.com/problems/utf-8-validation/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/utf-8-validation/editorial/) *(may require premium)*

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
