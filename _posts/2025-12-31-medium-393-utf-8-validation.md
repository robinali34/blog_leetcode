---
layout: post
title: "393. UTF-8 Validation"
date: 2025-12-31 22:30:00 -0700
categories: [leetcode, medium, bit-manipulation, string, array]
permalink: /2025/12/31/medium-393-utf-8-validation/
---

# 393. UTF-8 Validation

## Problem Statement

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

## Solution Approach

This problem requires validating UTF-8 encoding by checking bit patterns. UTF-8 has specific rules for how bytes are structured, and we need to verify the sequence follows these rules.

### Key Insights:

1. **UTF-8 Byte Patterns**:
   - 1-byte: `0xxxxxxx` (starts with 0)
   - 2-byte: `110xxxxx 10xxxxxx`
   - 3-byte: `1110xxxx 10xxxxxx 10xxxxxx`
   - 4-byte: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

2. **Bit Masks**: Use bit masks to check byte patterns
3. **Continuation Bytes**: All bytes after the first must start with `10`
4. **Length Validation**: Ensure we have enough bytes for multi-byte characters

### Algorithm:

1. **Check first byte**: Determine number of bytes in character
2. **Validate continuation**: Check that following bytes start with `10`
3. **Length check**: Ensure enough bytes available
4. **Process**: Move to next character

## Solution

### **Solution: Bit Manipulation with Masks**

```cpp
class Solution {
private:
    static const int MASK1 = 1 << 7;
    static const int MASK2 = MASK1 + (1 << 6);

    bool isValid(int num) {
        return (num & MASK2) == MASK1;
    }

    int getBytes(int num) {
        if((num & MASK1) == 0) return 1;
        int n = 0, mask = MASK1;
        while ((num & mask) != 0) {
            n++;
            if(n > 4) return -1;
            mask >>= 1;
        }
        return n >=2 ? n : -1;
    }
public:
    bool validUtf8(vector<int>& data) {
        const int M = data.size();
        int idx = 0;
        while(idx < M) {
            int num = data[idx];
            int n = getBytes(num);
            if(n < 0 || idx + n > M) return false;
            for(int i = 1; i < n; i++) {
                if(!isValid(data[idx + i])) return false;
            }
            idx += n;
        }
        return true;
    }
};
```

### **Algorithm Explanation:**

1. **Bit Masks (Lines 3-4)**:
   - `MASK1 = 1 << 7 = 10000000` (0x80): Checks if bit 7 is set
   - `MASK2 = MASK1 + (1 << 6) = 11000000` (0xC0): Checks bits 7 and 6

2. **isValid Helper (Lines 6-8)**:
   - Checks if a byte is a valid continuation byte
   - Continuation bytes must start with `10` (bits 7=1, 6=0)
   - `(num & MASK2) == MASK1` checks: bit 7=1 AND bit 6=0

3. **getBytes Helper (Lines 10-20)**:
   - Determines number of bytes in UTF-8 character
   - **1-byte check**: If `(num & MASK1) == 0`, return 1
   - **Multi-byte**: Count leading 1s
     - Start with `mask = MASK1` (bit 7)
     - Count consecutive 1s from left
     - If count > 4: invalid (return -1)
     - If count < 2: invalid (return -1)
     - Return count (2, 3, or 4)

4. **Main Validation (Lines 21-33)**:
   - Process data array sequentially
   - For each character:
     - Get byte count: `n = getBytes(data[idx])`
     - Check validity: `n < 0` or not enough bytes → return false
     - Validate continuation bytes: Check bytes `idx+1` to `idx+n-1`
     - Move to next character: `idx += n`

### **Example Walkthrough:**

**Example 1: `data = [197,130,1]`**

```
Step 1: Process first byte (197)
197 in binary: 11000101
getBytes(197):
  (197 & MASK1) = (197 & 128) = 128 ≠ 0 → not 1-byte
  Count leading 1s:
    mask = 128 (10000000)
    197 & 128 = 128 ≠ 0 → n=1, mask = 64
    197 & 64 = 64 ≠ 0 → n=2, mask = 32
    197 & 32 = 0 → stop
  n = 2 → 2-byte character
  Check: idx + 2 = 0 + 2 = 2 <= 3 ✓

Step 2: Validate continuation byte
data[1] = 130
130 in binary: 10000010
isValid(130):
  (130 & MASK2) = (130 & 192) = 128
  MASK1 = 128
  128 == 128 ✓ → valid continuation byte

Step 3: Process next character (1)
1 in binary: 00000001
getBytes(1):
  (1 & MASK1) = (1 & 128) = 0 → 1-byte character ✓

Result: true
```

**Example 2: `data = [235,140,4]`**

```
Step 1: Process first byte (235)
235 in binary: 11101011
getBytes(235):
  Count leading 1s:
    235 & 128 = 128 ≠ 0 → n=1
    235 & 64 = 64 ≠ 0 → n=2
    235 & 32 = 32 ≠ 0 → n=3
    235 & 16 = 0 → stop
  n = 3 → 3-byte character
  Check: idx + 3 = 0 + 3 = 3 <= 3 ✓

Step 2: Validate first continuation byte
data[1] = 140
140 in binary: 10001100
isValid(140):
  (140 & 192) = 128 == 128 ✓ → valid

Step 3: Validate second continuation byte
data[2] = 4
4 in binary: 00000100
isValid(4):
  (4 & 192) = 0 ≠ 128 ✗ → invalid continuation byte

Result: false
```

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

## Complexity Analysis

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

## Alternative Approaches

### **Approach 1: Bit Masks (Current Solution)**
- **Time**: O(n)
- **Space**: O(1)
- **Best for**: Clear and efficient solution

### **Approach 2: Right Shift Comparison**
- **Time**: O(n)
- **Space**: O(1)
- **Use right shift**: Compare with patterns like `0b110`, `0b1110`
- **Similar performance**: Different implementation style

### **Approach 3: State Machine**
- **Time**: O(n)
- **Space**: O(1)
- **State tracking**: Track expected continuation bytes
- **More complex**: But can be more readable

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

## Related Problems

- [393. UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/) - Current problem
- [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) - Bit manipulation
- [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) - Bit manipulation
- [136. Single Number](https://leetcode.com/problems/single-number/) - Bit manipulation

## Tags

`Bit Manipulation`, `Array`, `String`, `Medium`

