---
layout: post
title: "[Medium] 89. Gray Code"
categories: leetcode algorithm backtracking data-structures recursion bit-manipulation medium cpp gray-code problem-solving
---
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

## Thinking Process

There are several approaches to generate Gray codes:

1. **Backtracking**: Try all possible sequences and backtrack when invalid
2. **Recursive Construction**: Build Gray code recursively by mirroring previous sequence
3. **Iterative Construction**: Build Gray code iteratively using the same mirroring principle
4. **Mathematical Formula**: Use the formula `i ^ (i >> 1)` for each number



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Backtracking tree</text>

  <circle cx="140" cy="30" r="12" fill="#E0D8E4" stroke="#A098A8"/><text x="140" y="34" text-anchor="middle" font-size="9">start</text>
  <line x1="140" y1="42" x2="90" y2="65" stroke="#9A9792"/><line x1="140" y1="42" x2="190" y2="65" stroke="#9A9792"/>
  <circle cx="90" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/><circle cx="190" cy="72" r="10" fill="#D4D8E0" stroke="#8B8680"/>
  <line x1="90" y1="82" x2="60" y2="100" stroke="#9A9792" stroke-dasharray="3"/><line x1="190" y1="82" x2="220" y2="100" stroke="#9A9792" stroke-dasharray="3"/>
  <text x="140" y="118" text-anchor="middle" font-size="11" fill="#6B6560">choose → explore → undo (prune)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Choose / explore / unchoose** *(this problem)* | O(2^n) | O(n) | Subsets, combinations |
| Constraint pruning | Reduced search | O(n) | Early exit on invalid partial |
| Sort + skip duplicates | O(2^n) | O(n) | Combination sum II style |
| Path recording | O(n!) worst | O(n) | Permutations |

## Solution

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

### Solution Explanation

**Approach:** Choose / explore / unchoose (this problem)

**Key idea:** There are several approaches to generate Gray codes:

**How the code works:**
1. **Backtracking**: Try all possible sequences and backtrack when invalid
2. **Recursive Construction**: Build Gray code recursively by mirroring previous sequence
3. **Iterative Construction**: Build Gray code iteratively using the same mirroring principle
4. **Mathematical Formula**: Use the formula `i ^ (i >> 1)` for each number

**Walkthrough** — input `n = 2`, expected output `[0,1,3,2]`:

The binary representation of the gray code sequence is [00, 01, 11, 10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit  
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit
[0,2,3,1] is also a valid gray code sequence, whose binary representation is [00, 10, 11, 01].
## Common Mistakes

1. **Off-by-one errors** in bit shifting (`1 << (n-1)` vs `1 << n`)
2. **Forgetting to reverse** the mirrored sequence
3. **Incorrect bit manipulation** operations
4. **Not handling edge case** n = 0 properly

## Related Problems

- [1238. Circular Permutation in Binary Representation](https://www.leetcode.com/problems/circular-permutation-in-binary-representation/)
- [89. Gray Code](https://www.leetcode.com/problems/gray-code/) (this problem)

## References

- [LC 89: Gray Code on LeetCode](https://www.leetcode.com/problems/gray-code/)
- [LeetCode Discuss — LC 89: Gray Code](https://www.leetcode.com/problems/gray-code/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/gray-code/editorial/) *(may require premium)*

## Key Takeaways

1. **Mirror Property**: Gray codes can be constructed by mirroring the previous sequence and adding a high-order bit
2. **Bit Manipulation**: Use XOR (`^`) to flip bits and OR (`|`) to set bits
3. **Mathematical Formula**: `i ^ (i >> 1)` directly computes the i-th Gray code
4. **Recursive Structure**: Gray codes have a natural recursive structure
