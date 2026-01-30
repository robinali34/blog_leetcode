---
layout: post
title: "[Medium] 50. Pow(x, n)"
categories: leetcode algorithm math data-structures recursion bit-manipulation medium cpp pow problem-solving
---

# [Medium] 50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

## Examples

**Example 1:**
```
Input: x = 2.00000, n = 10
Output: 1024.00000
```

**Example 2:**
```
Input: x = 2.10000, n = 3
Output: 9.26100
```

**Example 3:**
```
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
```

## Constraints

- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- n is an integer.
- Either x is not zero or n > 0.
- -10^4 <= x^n <= 10^4

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Negative exponent**: How should we handle negative exponents? (Assumption: x^n = 1 / x^(-n) - take reciprocal when n is negative)

2. **Zero base**: What if x is 0? (Assumption: Per constraints, either x is not zero or n > 0, so 0^0 case avoided)

3. **Integer exponent**: Is n always an integer? (Assumption: Yes - per constraints, n is an integer)

4. **Precision**: What precision is required? (Assumption: Standard floating point precision - result fits in given range)

5. **Time complexity**: What time complexity is expected? (Assumption: O(log n) - use binary exponentiation, not O(n))

## Approach

There are two main approaches to implement exponentiation efficiently:

1. **Recursive Approach**: Use divide-and-conquer with recursion
2. **Iterative Approach**: Use bit manipulation and iterative computation

Both approaches achieve O(log n) time complexity by reducing the problem size by half in each step.

## Solution 1: Recursive Approach

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (n < 0) {
            x = 1/x;
            N = -N;
        }
        return myPower(x, N);
    }
    
private:
    double myPower(double x, long long n) {
        if(n == 0) return 1.0;
        double half = myPower(x, n / 2);
        return (n % 2 == 0) ? half * half : half * half * x;
    }
};
```

**Time Complexity:** O(log n) - Each recursive call reduces n by half
**Space Complexity:** O(log n) - Recursion stack depth

## Solution 2: Iterative Approach

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        return myPow(x, (long long) n);
    }

private:
    double myPow(double x, long long n) {
        if(n == 0) return 1.0;
        if(n < 0) {
            n = -n;
            x = 1 / x;
        }
        double rtn = 1;
        while(n) {
            if (n % 2 == 1) {
                rtn *= x;
                n -= 1;
            }
            x *= x;
            n /= 2;
        }
        return rtn;
    }
};
```

**Time Complexity:** O(log n) - Each iteration processes one bit of n
**Space Complexity:** O(1) - Only using constant extra space

## Step-by-Step Example (Solution 1)

For x = 2, n = 10:

1. **myPower(2, 10)**: n = 10 (even)
   - half = myPower(2, 5) = 32
   - return 32 * 32 = 1024

2. **myPower(2, 5)**: n = 5 (odd)
   - half = myPower(2, 2) = 4
   - return 4 * 4 * 2 = 32

3. **myPower(2, 2)**: n = 2 (even)
   - half = myPower(2, 1) = 2
   - return 2 * 2 = 4

4. **myPower(2, 1)**: n = 1 (odd)
   - half = myPower(2, 0) = 1
   - return 1 * 1 * 2 = 2

5. **myPower(2, 0)**: return 1.0 (base case)

Final result: 1024

## Step-by-Step Example (Solution 2)

For x = 2, n = 10:

1. **Initial**: rtn = 1, x = 2, n = 10 (binary: 1010)
2. **n = 10 (even)**: x = 4, n = 5
3. **n = 5 (odd)**: rtn = 4, x = 16, n = 2
4. **n = 2 (even)**: x = 256, n = 1
5. **n = 1 (odd)**: rtn = 1024, x = 65536, n = 0
6. **n = 0**: return 1024

## Key Insights

1. **Divide and Conquer**: x^n = (x^(n/2))^2 for even n, x^n = (x^(n/2))^2 * x for odd n
2. **Negative Exponents**: x^(-n) = 1/x^n
3. **Integer Overflow**: Use `long long` to handle n = -2^31 case
4. **Bit Manipulation**: Iterative approach uses binary representation of n

## Solution Comparison

- **Recursive**: More intuitive, but uses O(log n) stack space
- **Iterative**: More efficient in space, uses bit manipulation concepts

## Common Mistakes

1. **Integer overflow** when n = -2^31 (can't negate directly)
2. **Not handling negative exponents** properly
3. **Naive O(n) approach** instead of O(log n)
4. **Precision issues** with floating point arithmetic

## Edge Cases

- n = 0: return 1.0
- n = 1: return x
- n = -1: return 1/x
- x = 0: return 0 (if n > 0)
- x = 1: return 1 for any n

## Related Problems

- [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
- [372. Super Pow](https://leetcode.com/problems/super-pow/)
