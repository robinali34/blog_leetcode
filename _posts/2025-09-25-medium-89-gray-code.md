---
layout: post
title: "[Medium] 89. Gray Code"
categories: leetcode algorithm backtracking data-structures recursion bit-manipulation medium cpp gray-code problem-solving
---

# [Medium] 89. Gray Code

An n-bit gray code sequence is a sequence of 2^n integers where:

- Every integer is between 0 and 2^n - 1 (inclusive)
- The first integer is 0
- An integer appears at most once in the sequence
- The binary representation of every pair of adjacent integers differs by exactly one bit
- The binary representation of the first and last integers differs by exactly one bit

Given an integer n, return any valid n-bit gray code sequence.

## Examples

**Example 1:**
```
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of the gray code sequence is [00, 01, 11, 10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit  
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00, 10, 11, 01].
```

**Example 2:**
```
Input: n = 1
Output: [0,1]
```

## Constraints

- 1 <= n <= 16

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Gray code definition**: What is Gray code? (Assumption: Sequence where consecutive numbers differ by exactly one bit - binary representation differs by one bit)

2. **Starting value**: What should the sequence start with? (Assumption: Typically starts with 0 - first number is 0)

3. **Sequence length**: How many numbers should be in the sequence? (Assumption: 2^n numbers - all n-bit Gray codes)

4. **Uniqueness**: Is there a unique Gray code sequence? (Assumption: No - multiple valid sequences exist, return any valid one)

5. **Return format**: What should we return? (Assumption: List of integers representing Gray code sequence)

## Approach

There are several approaches to generate Gray codes:

1. **Backtracking**: Try all possible sequences and backtrack when invalid
2. **Recursive Construction**: Build Gray code recursively by mirroring previous sequence
3. **Iterative Construction**: Build Gray code iteratively using the same mirroring principle
4. **Mathematical Formula**: Use the formula `i ^ (i >> 1)` for each number

## Solution 1: Backtracking Approach

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> rtn;
        rtn.push_back(0);
        unordered_set<int> isPresent;
        isPresent.insert(0);
        getGreyCode(rtn, n, isPresent);
        return rtn;
    }

private:
    bool getGreyCode(vector<int>& rtn, int n, unordered_set<int>& isPresent) {
        if (rtn.size() == (1 << n)) return true;
        int current = rtn[rtn.size() - 1];
        for (int i = 0; i < n; i++) {
            int next = current ^ (1 << i);
            if(isPresent.find(next) == isPresent.end()) {
                isPresent.insert(next);
                rtn.push_back(next);
                if (getGreyCode(rtn, n, isPresent)) return true;
                isPresent.erase(next);
                rtn.pop_back();
            }
        }
        return false;
    }
};
```

**Time Complexity:** O(2^n) - Exponential time due to backtracking
**Space Complexity:** O(2^n) - For the result vector and visited set

## Solution 2: Recursive Mirror Construction

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> rtn;
        getGreyCode(rtn, n);
        return rtn;
    }

private:
    void getGreyCode(vector<int>& rtn, int n) {
        if (n == 0) {
            rtn.push_back(0);
            return;
        }
        getGreyCode(rtn, n - 1);
        int cur = rtn.size();
        int mask = 1 << (n - 1);
        for (int i = cur - 1; i >= 0; i--) {
            rtn.push_back(rtn[i] | mask);
        }
        return;
    }
};
```

**Time Complexity:** O(2^n) - Each recursive call doubles the sequence
**Space Complexity:** O(2^n) - For the result vector

## Solution 3: Iterative Mirror Construction

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> rtn;
        rtn.push_back(0);
        for(int i = 1; i <= n; i++) {
            int pre = rtn.size();
            int mask = 1 << (i - 1);
            for (int j = pre - 1; j >= 0; j--) {
                rtn.push_back(mask | rtn[j]);
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(2^n) - Builds sequence iteratively
**Space Complexity:** O(2^n) - For the result vector

## Solution 4: Mathematical Formula Approach

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> rtn;
        for (int i = 0; i < (1 << n); i++) {
            rtn.push_back(i ^ (i >> 1));
        }
        return rtn;
    }
};
```

**Time Complexity:** O(2^n) - Generate each Gray code number
**Space Complexity:** O(2^n) - For the result vector

## Solution 5: Alternative Recursive with Global Variable

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> rtn;
        getGreyCode(rtn, n);
        return rtn;
    }

private:
    int nextNum = 0;

    void getGreyCode(vector<int>& rtn, int n) {
        if(n == 0) {
            rtn.push_back(nextNum);
            return;
        }
        getGreyCode(rtn, n - 1);
        nextNum = nextNum ^ (1 << (n - 1));
        getGreyCode(rtn, n - 1);
    }
};
```

**Time Complexity:** O(2^n) - Recursive construction
**Space Complexity:** O(2^n) - For the result vector

## Step-by-Step Example (Solution 3)

For n = 3:

1. Start with [0]
2. i = 1: mirror and add 1-bit mask
   - [0] → [0, 1]
3. i = 2: mirror and add 2-bit mask  
   - [0, 1] → [0, 1, 3, 2]
4. i = 3: mirror and add 3-bit mask
   - [0, 1, 3, 2] → [0, 1, 3, 2, 6, 7, 5, 4]

Final result: [0, 1, 3, 2, 6, 7, 5, 4]

## Key Insights

1. **Mirror Property**: Gray codes can be constructed by mirroring the previous sequence and adding a high-order bit
2. **Bit Manipulation**: Use XOR (`^`) to flip bits and OR (`|`) to set bits
3. **Mathematical Formula**: `i ^ (i >> 1)` directly computes the i-th Gray code
4. **Recursive Structure**: Gray codes have a natural recursive structure

## Solution Comparison

- **Backtracking**: Most intuitive but inefficient for large n
- **Recursive Mirror**: Clean recursive approach, moderate efficiency
- **Iterative Mirror**: Most efficient iterative approach
- **Mathematical Formula**: Most concise and efficient
- **Alternative Recursive**: Uses global state, less clean

## Common Mistakes

1. **Off-by-one errors** in bit shifting (`1 << (n-1)` vs `1 << n`)
2. **Forgetting to reverse** the mirrored sequence
3. **Incorrect bit manipulation** operations
4. **Not handling edge case** n = 0 properly

## Related Problems

- [1238. Circular Permutation in Binary Representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/)
- [89. Gray Code](https://leetcode.com/problems/gray-code/) (this problem)
