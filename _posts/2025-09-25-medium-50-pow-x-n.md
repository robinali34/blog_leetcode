---
layout: post
title: "[Medium] 50. Pow(x, n)"
categories: leetcode algorithm math data-structures recursion bit-manipulation medium cpp pow problem-solving
---
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

## Thinking Process

There are two main approaches to implement exponentiation efficiently:

1. **Recursive Approach**: Use divide-and-conquer with recursion
2. **Iterative Approach**: Use bit manipulation and iterative computation

Both approaches achieve O(log n) time complexity by reducing the problem size by half in each step.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 90" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Bit manipulation</text>

  <text x="40" y="50" font-family="monospace" font-size="14" fill="#3A3530">1 0 1 1 0 1 0</text>
  <text x="40" y="75" font-size="11" fill="#6B6560">XOR pairs · masks · shifts</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **XOR tricks** *(this problem)* | O(n) | O(1) | Single number, swap without temp |
| Bit masks | O(2^n) | O(n) | Subset enumeration |
| Brian Kernighan | O(log n) | O(1) | Count set bits |
| Shift operations | O(n) | O(1) | Power of two, divide by 2 |

## Solution

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

### Solution Explanation

**Approach:** XOR tricks (this problem)

**Key idea:** There are two main approaches to implement exponentiation efficiently:

**How the code works:**
1. **Recursive Approach**: Use divide-and-conquer with recursion
2. **Iterative Approach**: Use bit manipulation and iterative computation

**Walkthrough** — input `x = 2.00000, n = 10`, expected output `1024.00000`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Step-by-Step Example (Solution 2)

For x = 2, n = 10:

1. **Initial**: rtn = 1, x = 2, n = 10 (binary: 1010)
2. **n = 10 (even)**: x = 4, n = 5
3. **n = 5 (odd)**: rtn = 4, x = 16, n = 2
4. **n = 2 (even)**: x = 256, n = 1
5. **n = 1 (odd)**: rtn = 1024, x = 65536, n = 0
6. **n = 0**: return 1024

## Common Mistakes

1. **Integer overflow** when n = -2^31 (can't negate directly)
2. **Not handling negative exponents** properly
3. **Naive O(n) approach** instead of O(log n)
4. **Precision issues** with floating point arithmetic

- n = 0: return 1.0
- n = 1: return x
- n = -1: return 1/x
- x = 0: return 0 (if n > 0)
- x = 1: return 1 for any n

## Related Problems

- [69. Sqrt(x)](https://www.leetcode.com/problems/sqrtx/)
- [367. Valid Perfect Square](https://www.leetcode.com/problems/valid-perfect-square/)
- [372. Super Pow](https://www.leetcode.com/problems/super-pow/)

## References

- [LC 50: Pow(x, n) on LeetCode](https://www.leetcode.com/problems/pow-x-n/)
- [LeetCode Discuss — LC 50: Pow(x, n)](https://www.leetcode.com/problems/pow-x-n/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/pow-x-n/editorial/) *(may require premium)*

## Key Takeaways

1. **Divide and Conquer**: x^n = (x^(n/2))^2 for even n, x^n = (x^(n/2))^2 * x for odd n
2. **Negative Exponents**: x^(-n) = 1/x^n
3. **Integer Overflow**: Use `long long` to handle n = -2^31 case
4. **Bit Manipulation**: Iterative approach uses binary representation of n
