---
layout: post
title: "Algorithm Templates: Math & Bit Manipulation"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates math bit-manipulation
permalink: /posts/2025-11-24-leetcode-templates-math-bit-manipulation/
tags: [leetcode, templates, math, bit-manipulation]
---
This page collects ready-to-use C++ templates for bit manipulation, fast exponentiation, GCD/LCM, prime sieves, and basic number theory. Each snippet is self-contained — copy it into your solution and adapt as needed. If you're looking for geometry-related math, see [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/).

> **New to Bit Manipulation?** Computers store everything in binary. Bit manipulation lets you perform operations on individual bits — it's incredibly fast and often turns complex problems into elegant one-liners. The most common trick: XOR (`a ^ b`) cancels matching bits, which is why it solves "single number" problems.

<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="350" y="18" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Bit Positions — number 23 = 10111</text>
  <rect x="80" y="35" width="60" height="36" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="110" y="50" font-size="9" fill="#9A9792" text-anchor="middle">bit 4</text><text x="110" y="66" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">1</text>
  <rect x="140" y="35" width="60" height="36" rx="4" fill="#F0EBE6" stroke="#B8B5B0"/><text x="170" y="50" font-size="9" fill="#9A9792" text-anchor="middle">bit 3</text><text x="170" y="66" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">0</text>
  <rect x="200" y="35" width="60" height="36" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="230" y="50" font-size="9" fill="#9A9792" text-anchor="middle">bit 2</text><text x="230" y="66" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">1</text>
  <rect x="260" y="35" width="60" height="36" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="290" y="50" font-size="9" fill="#9A9792" text-anchor="middle">bit 1</text><text x="290" y="66" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">1</text>
  <rect x="320" y="35" width="60" height="36" rx="4" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/><text x="350" y="50" font-size="9" fill="#9A9792" text-anchor="middle">bit 0</text><text x="350" y="66" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">1</text>
  <text x="450" y="58" font-size="11" fill="#5A5752">16+4+2+1 = 23</text>
  <text x="350" y="105" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">XOR Trick — Single Number (all appear twice except one)</text>
  <text x="120" y="130" font-size="11" fill="#5A5752">4</text><text x="160" y="130" font-size="11" fill="#5A5752">^ 1</text><text x="200" y="130" font-size="11" fill="#5A5752">^ 2</text><text x="240" y="130" font-size="11" fill="#5A5752">^ 1</text><text x="300" y="130" font-size="11" fill="#5A5752">^ 4</text><text x="360" y="130" font-size="11" fill="#5A5752">^ 2</text>
  <text x="420" y="130" font-size="12" fill="#3A6B3A" font-weight="700">= 4</text>
  <text x="350" y="155" font-size="10" fill="#5A5752" text-anchor="middle">Pairs cancel (a ^ a = 0), only the unique number survives</text>
  <text x="350" y="180" font-size="10" fill="#5A5752" text-anchor="middle">num &amp; (num-1) clears lowest set bit | num &amp; (-num) gets lowest set bit</text>
</svg>

## Contents

- [Bit Operations](#bit-operations)
- [Common Bit Tricks](#common-bit-tricks)
- [Fast Exponentiation](#fast-exponentiation)
- [GCD and LCM](#gcd-and-lcm)
- [Prime Numbers](#prime-numbers)
- [Number Theory](#number-theory)

## Bit Operations

**When to use:** You need to inspect, set, clear, or toggle individual bits in a number — common in bitmask DP, permission flags, and encoding state compactly.

### Basic Operations

```cpp
// Set bit at position i
int setBit(int num, int i) {
    return num | (1 << i);
}

// Clear bit at position i
int clearBit(int num, int i) {
    return num & ~(1 << i);
}

// Toggle bit at position i
int toggleBit(int num, int i) {
    return num ^ (1 << i);
}

// Check if bit is set
bool isBitSet(int num, int i) {
    return (num >> i) & 1;
}

// Count set bits
int countSetBits(int num) {
    int count = 0;
    while (num) {
        count += num & 1;
        num >>= 1;
    }
    return count;
}

// Count set bits (Brian Kernighan's algorithm)
int countSetBitsFast(int num) {
    int count = 0;
    while (num) {
        num &= (num - 1);
        count++;
    }
    return count;
}
```

### Common Bit Tricks

```cpp
// Get lowest set bit
int lowestSetBit(int num) {
    return num & (-num);
}

// Clear lowest set bit
int clearLowestSetBit(int num) {
    return num & (num - 1);
}

// Check if power of 2
bool isPowerOfTwo(int num) {
    return num > 0 && (num & (num - 1)) == 0;
}

// Get next power of 2
int nextPowerOfTwo(int num) {
    num--;
    num |= num >> 1;
    num |= num >> 2;
    num |= num >> 4;
    num |= num >> 8;
    num |= num >> 16;
    return num + 1;
}

// Swap two numbers
void swap(int& a, int& b) {
    a ^= b;
    b ^= a;
    a ^= b;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 29 | Divide Two Integers | [Link](https://leetcode.com/problems/divide-two-integers/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/14/medium-29-divide-two-integers/) |
| 36 | Valid Sudoku | [Link](https://leetcode.com/problems/valid-sudoku/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/14/medium-36-valid-sudoku/) |
| 67 | Add Binary | [Link](https://leetcode.com/problems/add-binary/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-easy-67-add-binary/) |
| 191 | Number of 1 Bits | [Link](https://leetcode.com/problems/number-of-1-bits/) | - |
| 231 | Power of Two | [Link](https://leetcode.com/problems/power-of-two/) | - |
| 338 | Counting Bits | [Link](https://leetcode.com/problems/counting-bits/) | - |
| 393 | UTF-8 Validation | [Link](https://leetcode.com/problems/utf-8-validation/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/medium-393-utf-8-validation/) |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) |
| 593 | Valid Square | [Link](https://leetcode.com/problems/valid-square/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-02-medium-593-valid-square/) |
| 2571 | Minimum Operations to Reduce an Integer to 0 | [Link](https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/20/medium-2571-minimum-operations-to-reduce-an-integer-to-0/) |

## Common Bit Tricks

**When to use:** The problem mentions "single number", "missing number", "find the duplicate", or any scenario where XOR's self-cancelling property (`x ^ x = 0`) can isolate an answer.

### Single Number

```cpp
// Single Number (all appear twice except one)
int singleNumber(vector<int>& nums) {
    int result = 0;
    for (int num : nums) {
        result ^= num;
    }
    return result;
}

// Single Number II (all appear three times except one)
int singleNumberII(vector<int>& nums) {
    int ones = 0, twos = 0;
    for (int num : nums) {
        ones = (ones ^ num) & ~twos;
        twos = (twos ^ num) & ~ones;
    }
    return ones;
}
```

### Gray Code

```cpp
vector<int> grayCode(int n) {
    vector<int> result;
    for (int i = 0; i < (1 << n); ++i) {
        result.push_back(i ^ (i >> 1));
    }
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 136 | Single Number | [Link](https://leetcode.com/problems/single-number/) | - |
| 137 | Single Number II | [Link](https://leetcode.com/problems/single-number-ii/) | - |
| 89 | Gray Code | [Link](https://leetcode.com/problems/gray-code/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-89-gray-code/) |
| 389 | Find the Difference | [Link](https://leetcode.com/problems/find-the-difference/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/27/easy-389-find-the-difference/) |
| 260 | Single Number III | [Link](https://leetcode.com/problems/single-number-iii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/31/medium-260-single-number-iii/) |
| 2433 | Find The Original Array of Prefix Xor | [Link](https://leetcode.com/problems/find-the-original-array-of-prefix-xor/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/05/medium-2433-find-the-original-array-of-prefix-xor/) |

## Fast Exponentiation

**When to use:** You need to compute `x^n` (or modular exponentiation) efficiently — e.g. "pow(x, n)", matrix exponentiation for DP, or any problem requiring O(log n) power computation.

### Power Function

```cpp
// Fast exponentiation: x^n
double myPow(double x, int n) {
    long long N = n;
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }
    
    double result = 1;
    double current = x;
    
    while (N > 0) {
        if (N % 2 == 1) {
            result *= current;
        }
        current *= current;
        N /= 2;
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 50 | Pow(x, n) | [Link](https://leetcode.com/problems/powx-n/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/25/medium-50-pow-x-n/) |

## GCD and LCM

**When to use:** Problems ask for "greatest common divisor", "least common multiple", reducing fractions, or checking divisibility relationships between numbers.

```cpp
// Greatest Common Divisor (Euclidean algorithm)
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Recursive GCD
int gcdRecursive(int a, int b) {
    return b == 0 ? a : gcdRecursive(b, a % b);
}

// Least Common Multiple
int lcm(int a, int b) {
    return a / gcd(a, b) * b;
}
```

## Prime Numbers

**When to use:** Problems involve "count primes", prime factorization, or need to quickly test whether numbers are prime. The sieve is ideal when you need all primes up to N.

### Check Prime

```cpp
bool isPrime(int n) {
    if (n < 2) return false;
    if (n == 2) return true;
    if (n % 2 == 0) return false;
    
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    
    return true;
}
```

### Sieve of Eratosthenes

```cpp
vector<bool> sieveOfEratosthenes(int n) {
    vector<bool> isPrime(n + 1, true);
    isPrime[0] = isPrime[1] = false;
    
    for (int i = 2; i * i <= n; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    
    return isPrime;
}
```

## Number Theory

**When to use:** Problems involve digit manipulation (reverse, palindrome), trailing zeroes in factorials, modular arithmetic, or large number operations.

### Factorial Trailing Zeroes

```cpp
int trailingZeroes(int n) {
    int count = 0;
    while (n > 0) {
        n /= 5;
        count += n;
    }
    return count;
}
```

### Reverse Integer

```cpp
int reverse(int x) {
    int result = 0;
    while (x != 0) {
        if (result > INT_MAX / 10 || result < INT_MIN / 10) {
            return 0;
        }
        result = result * 10 + x % 10;
        x /= 10;
    }
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 172 | Factorial Trailing Zeroes | [Link](https://leetcode.com/problems/factorial-trailing-zeroes/) | - |
| 7 | Reverse Integer | [Link](https://leetcode.com/problems/reverse-integer/) | - |
| 9 | Palindrome Number | [Link](https://leetcode.com/problems/palindrome-number/) | - |
| 279 | Perfect Squares | [Link](https://leetcode.com/problems/perfect-squares/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-14-medium-279-perfect-squares/) |
| 43 | Multiply Strings | [Link](https://leetcode.com/problems/multiply-strings/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/17/medium-43-multiply-strings/) |
| 2539 | Count the Number of Good Subsequences | [Link](https://leetcode.com/problems/count-the-number-of-good-subsequences/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/19/hard-2539-count-the-number-of-good-subsequences/) |

---

## Quick Reference

| Topic | Signal Phrases | Key Trick |
|---|---|---|
| XOR | "single number", "missing number" | x ^ x = 0, x ^ 0 = x |
| Bit counting | "number of 1 bits", "counting bits" | n & (n-1) removes lowest set bit |
| Power of 2 | "is power of 2" | n & (n-1) == 0 |
| Fast Exponent | "pow(x,n)", "modular exponent" | Square-and-multiply |
| GCD/LCM | "greatest common divisor" | Euclidean algorithm |
| Sieve | "count primes" | Sieve of Eratosthenes |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Math & Geometry:** [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/)
- **Advanced (bitwise trie):** [Advanced Techniques](/posts/2025-10-29-leetcode-templates-advanced/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
