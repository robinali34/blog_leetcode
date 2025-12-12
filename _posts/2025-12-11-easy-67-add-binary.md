---
layout: post
title: "[Easy] 67. Add Binary"
date: 2025-12-11 00:00:00 -0800
categories: leetcode algorithm easy cpp string math bit-manipulation problem-solving
---

# [Easy] 67. Add Binary

Given two binary strings `a` and `b`, return their sum as a binary string.

## Examples

**Example 1:**
```
Input: a = "11", b = "1"
Output: "100"
```

**Example 2:**
```
Input: a = "1010", b = "1011"
Output: "10101"
```

## Constraints

- `1 <= a.length, b.length <= 10^4`
- `a` and `b` consist only of `'0'` or `'1'` characters.
- Each string does not contain leading zeros except for the zero itself.

## Solution 1: Optimized Single Pass (Recommended)

**Time Complexity:** O(max(m, n)) where m and n are lengths of a and b  
**Space Complexity:** O(max(m, n)) for the result string

This solution ensures the longer string is processed first, and uses a single carry variable that accumulates both digits efficiently.

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        int n = a.size(), m = b.size();
        if(n < m)
            return addBinary(b, a);
        
        string rtn;
        int carry = 0, j = m - 1;
        
        for(int i = n - 1; i >= 0; i--) {
            if (a[i] == '1') carry++;
            if(j >= 0 && b[j--] == '1') carry++;
            rtn.push_back((carry % 2) ? '1': '0');
            carry /= 2;
        }
        
        if(carry == 1) rtn.push_back('1');
        reverse(rtn.begin(), rtn.end());
        return rtn;
    }
};
```

### How Solution 1 Works

1. **Ensure longer string first**: If `a` is shorter, swap to process longer string first
2. **Process from right to left**: Start from least significant bit (end of strings)
3. **Accumulate carry**: 
   - Add 1 to carry if current bit in `a` is '1'
   - Add 1 to carry if current bit in `b` is '1' (if available)
4. **Calculate result digit**: `carry % 2` gives the result bit (0 or 1)
5. **Update carry**: `carry /= 2` gives the new carry (0 or 1)
6. **Handle final carry**: If carry remains after processing all bits, add '1'
7. **Reverse result**: Since we built it from right to left, reverse to get correct order

### Key Insight

The carry variable accumulates both digits:
- `carry` can be 0, 1, 2, or 3 (0+0, 0+1, 1+1, 1+1+carry)
- `carry % 2` gives the result bit
- `carry / 2` gives the new carry (always 0 or 1 for binary)

## Solution 2: Standard Two-Pointer Approach

**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(max(m, n))

This is the more traditional approach that processes both strings simultaneously.

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            if (i >= 0) {
                sum += a[i] - '0';
                i--;
            }
            if (j >= 0) {
                sum += b[j] - '0';
                j--;
            }
            result.push_back((sum % 2) + '0');
            carry = sum / 2;
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
};
```

### How Solution 2 Works

1. **Two pointers**: `i` for string `a`, `j` for string `b`
2. **Process while either string has digits or carry exists**
3. **Calculate sum**: Add carry + digit from `a` (if available) + digit from `b` (if available)
4. **Append result**: `sum % 2` gives the bit, convert to character
5. **Update carry**: `sum / 2` gives the new carry
6. **Reverse result**: Built from right to left, so reverse at the end

## Solution 3: Using Built-in Conversion (Not Recommended for Interviews)

**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(max(m, n))

This approach uses language built-ins to convert, add, and convert back. Not recommended for interviews but useful for quick solutions.

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        // Convert binary strings to integers
        long long num1 = stoll(a, nullptr, 2);
        long long num2 = stoll(b, nullptr, 2);
        
        // Add and convert back to binary
        long long sum = num1 + num2;
        if (sum == 0) return "0";
        
        string result;
        while (sum > 0) {
            result.push_back((sum % 2) + '0');
            sum /= 2;
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
```

**Note:** This approach has limitations:
- May overflow for very large binary strings (beyond `long long` range)
- Not suitable for interview settings where manual bit manipulation is expected
- Useful for quick prototyping or when constraints guarantee small inputs

## Solution 4: Bit Manipulation Style

**Time Complexity:** O(max(m, n))  
**Space Complexity:** O(max(m, n))

A variation that explicitly handles bit operations.

```cpp
class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        int i = a.size() - 1, j = b.size() - 1;
        int carry = 0;
        
        while (i >= 0 || j >= 0 || carry) {
            int bit1 = (i >= 0) ? (a[i--] - '0') : 0;
            int bit2 = (j >= 0) ? (b[j--] - '0') : 0;
            
            int sum = bit1 + bit2 + carry;
            result.push_back((sum & 1) + '0');  // sum % 2 using bitwise AND
            carry = sum >> 1;  // sum / 2 using right shift
        }
        
        reverse(result.begin(), result.end());
        return result;
    }
};
```

### Key Differences

- Uses bitwise AND (`& 1`) instead of modulo for getting the bit
- Uses right shift (`>> 1`) instead of division for carry
- More explicit about bit operations

## Example Walkthrough

**Input:** `a = "1010"`, `b = "1011"`

### Solution 1 (Optimized):
```
a = "1010" (longer, n=4)
b = "1011" (shorter, m=4, j=3)

i=3: a[3]='0', b[3]='1' → carry=1 → result='1', carry=0
i=2: a[2]='1', b[2]='1' → carry=2 → result='0', carry=1
i=1: a[1]='0', b[1]='0' → carry=1 → result='1', carry=0
i=0: a[0]='1', b[0]='1' → carry=2 → result='0', carry=1

Final carry=1 → result='1'
Reverse: "10101"
```

### Solution 2 (Standard):
```
a = "1010", b = "1011"
i=3, j=3, carry=0

Step 1: sum=0+0+1=1 → result='1', carry=0
Step 2: sum=0+1+1=2 → result='0', carry=1
Step 3: sum=1+0+0=1 → result='1', carry=0
Step 4: sum=1+1+0=2 → result='0', carry=1
Step 5: carry=1 → result='1'

Reverse: "10101"
```

## Complexity Analysis

| Solution | Time | Space | Notes |
|----------|------|-------|-------|
| Solution 1 (Optimized) | O(max(m,n)) | O(max(m,n)) | Ensures longer string processed first |
| Solution 2 (Standard) | O(max(m,n)) | O(max(m,n)) | Traditional two-pointer approach |
| Solution 3 (Built-in) | O(max(m,n)) | O(max(m,n)) | May overflow for large inputs |
| Solution 4 (Bitwise) | O(max(m,n)) | O(max(m,n)) | Explicit bit operations |

## Edge Cases

1. **Different lengths**: `"1" + "111"` → `"1000"`
2. **Carry at end**: `"1" + "1"` → `"10"`
3. **All zeros**: `"0" + "0"` → `"0"`
4. **One empty**: Not possible per constraints, but handled by `j >= 0` check
5. **Large strings**: Up to 10^4 characters each

## Common Mistakes

1. **Forgetting final carry**: Not adding carry if it remains after processing all bits
2. **Wrong order**: Not reversing the result string
3. **Index out of bounds**: Not checking if pointers are valid before accessing
4. **Character conversion**: Forgetting to convert between char and int (`'0'` vs `0`)
5. **Carry calculation**: Using wrong formula for carry (should be `sum / 2` not `sum - 2`)

## Key Insights

1. **Binary addition rules**:
   - 0 + 0 = 0 (carry 0)
   - 0 + 1 = 1 (carry 0)
   - 1 + 1 = 0 (carry 1)
   - 1 + 1 + 1 = 1 (carry 1)

2. **Carry propagation**: Carry can only be 0 or 1 in binary addition

3. **String processing**: Process from right to left (least significant to most significant)

4. **Result building**: Build result backwards, then reverse

## Optimization Tips

1. **Pre-allocate space**: Can reserve `max(m, n) + 1` for result string
2. **Early termination**: If both strings exhausted and carry is 0, can break early
3. **In-place modification**: Could modify one string in-place, but not recommended for clarity

## Related Problems

- [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) - Add numbers represented as linked lists
- [415. Add Strings](https://leetcode.com/problems/add-strings/) - Add decimal number strings
- [43. Multiply Strings](https://leetcode.com/problems/multiply-strings/) - Multiply number strings
- [66. Plus One](https://leetcode.com/problems/plus-one/) - Add one to number array
- [989. Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/) - Add number to array-form integer

## Pattern Recognition

This problem demonstrates the **"String Arithmetic with Carry"** pattern:

```
1. Process strings from right to left (least to most significant)
2. Handle different lengths gracefully
3. Track carry through iterations
4. Build result backwards, reverse at end
5. Handle final carry if exists
```

Similar problems:
- Add Strings (decimal)
- Add Two Numbers (linked list)
- Multiply Strings
- Plus One

## Real-World Applications

1. **Binary Arithmetic**: Core operation in computer arithmetic
2. **Cryptography**: Binary operations in encryption algorithms
3. **Network Protocols**: Checksum calculations
4. **Error Detection**: Parity bit calculations
5. **Digital Circuits**: Hardware adder implementations

