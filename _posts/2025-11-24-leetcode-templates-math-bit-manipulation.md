---
layout: post
title: "Algorithm Templates: Math & Bit Manipulation"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates math bit-manipulation
permalink: /posts/2025-11-24-leetcode-templates-math-bit-manipulation/
tags: [leetcode, templates, math, bit-manipulation]
---

{% raw %}
Minimal, copy-paste C++ for bit operations, fast exponentiation, GCD/LCM, primes, and number theory. See also [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/).

## Contents

- [Bit Operations](#bit-operations)
- [Common Bit Tricks](#common-bit-tricks)
- [Fast Exponentiation](#fast-exponentiation)
- [GCD and LCM](#gcd-and-lcm)
- [Prime Numbers](#prime-numbers)
- [Number Theory](#number-theory)

## Bit Operations

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
| 67 | Add Binary | [Link](https://leetcode.com/problems/add-binary/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-easy-67-add-binary/) |
| 191 | Number of 1 Bits | [Link](https://leetcode.com/problems/number-of-1-bits/) | - |
| 231 | Power of Two | [Link](https://leetcode.com/problems/power-of-two/) | - |
| 338 | Counting Bits | [Link](https://leetcode.com/problems/counting-bits/) | - |
| 393 | UTF-8 Validation | [Link](https://leetcode.com/problems/utf-8-validation/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/medium-393-utf-8-validation/) |
| 1177 | Can Make Palindrome from Substring | [Link](https://leetcode.com/problems/can-make-palindrome-from-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/01/medium-1177-can-make-palindrome-from-substring/) |
| 593 | Valid Square | [Link](https://leetcode.com/problems/valid-square/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-02-medium-593-valid-square/) |

## Common Bit Tricks

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

## Fast Exponentiation

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

## More templates

- **Math & Geometry:** [Math & Geometry](/posts/2025-10-29-leetcode-templates-math-geometry/)
- **Advanced (bitwise trie):** [Advanced Techniques](/posts/2025-10-29-leetcode-templates-advanced/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

