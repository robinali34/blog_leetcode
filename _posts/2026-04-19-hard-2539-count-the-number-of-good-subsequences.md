---
layout: post
title: "[Hard] 2539. Count the Number of Good Subsequences"
date: 2026-04-19
categories: [leetcode, hard, combinatorics]
tags: [leetcode, hard, combinatorics, modular-arithmetic, math, string]
permalink: /2026/04/19/hard-2539-count-the-number-of-good-subsequences/
---
Given a string `s`, return the number of **non-empty good subsequences** of `s`. A subsequence is **good** if every character in it appears the **same number of times**. Answer modulo 10^9 + 7.

## Examples

**Example 1:**

```
Input: s = "aabb"
Output: 11

Good subsequences:
  k=1: "a","a","b","b","ab","ab","ab","ab" → 8
  k=2: "aa","bb","aabb" → 3
  Total = 11
```

**Example 2:**

```
Input: s = "leet"
Output: 7

freq: l=1, e=2, t=1
  k=1: "l","e","e","t","le","lt","et","le","lt","et" ...
  (counted via formula below)
```

## Constraints

- `1 <= s.length <= 10^4`
- `s` consists of lowercase English letters only

## Thinking Process

### Why Brute Force Fails

Enumerating all 2^n - 1 non-empty subsequences and checking each one is exponential. We need a combinatorial approach.

### The Key Insight

Instead of generating subsequences, **fix a target frequency `k`** and count how many subsequences have every chosen character appearing exactly `k` times.

For a fixed `k`:
- For each character `c` with `freq[c] >= k`, we can either **include** it (choose exactly `k` of its `freq[c]` occurrences: binom{freq[c]}{k} ways) or **exclude** it entirely (1 way)
- Characters with `freq[c] < k` must be excluded

So the total for a given `k`:

$text{ways}(k) = prod_{text{all chars } c} left(1 + binom{freq[c]}{k} · [freq[c] ge k]right) - 1

The -1 removes the empty subsequence (where every character is excluded).

### Final Answer

text{answer} = sum_{k=1}^{max\_freq} text{ways}(k)

### Efficient Combinations

We need \binom{n}{k} for various n, k up to \max\_freq. Using a Pascal table would be O(n^2) memory, which can blow up for large frequencies.

Instead, precompute factorials and use **Fermat's little theorem** for modular inverse:

binom{n}{k} = frac{n!}{k! · (n-k)!} = n! · (k!)^{-1} · ((n-k)!)^{-1} pmod{10^9+7}



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Two pointers</text>

  <rect x="30" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="66" text-anchor="middle" font-size="10">1</text>
  <rect x="62" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="76" y="66" text-anchor="middle" font-size="10">3</text>
  <rect x="106" y="50" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="66" text-anchor="middle" font-size="10">5</text>
  <rect x="138" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="152" y="66" text-anchor="middle" font-size="10">7</text>
  <rect x="170" y="50" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="184" y="66" text-anchor="middle" font-size="10">9</text>
  <text x="44" y="42" text-anchor="middle" font-size="10" fill="#7A8EA0" font-weight="600">L</text>
  <text x="184" y="42" text-anchor="middle" font-size="10" fill="#A08888" font-weight="600">R</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">move L/R based on comparison</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Solution

{% raw %}
```cpp
class Solution {
public:
    static const int MOD = 1e9 + 7;

    long long modPow(long long a, long long b) {
        long long res = 1;
        while (b) {
            if (b & 1) res = res * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return res;
    }

    int countGoodSubsequences(string s) {
        unordered_map<char, int> freq;
        for (char c : s) freq[c]++;

        int max_f = 0;
        for (auto& [c, f] : freq) max_f = max(max_f, f);

        vector<long long> fact(max_f + 1, 1), invfact(max_f + 1, 1);
        for (int i = 1; i <= max_f; i++) {
            fact[i] = fact[i - 1] * i % MOD;
        }
        invfact[max_f] = modPow(fact[max_f], MOD - 2);
        for (int i = max_f - 1; i >= 0; i--) {
            invfact[i] = invfact[i + 1] * (i + 1) % MOD;
        }

        auto comb = [&](int n, int k) {
            return fact[n] % MOD * invfact[k] % MOD * invfact[n - k] % MOD;
        };

        long long result = 0;
        for (int k = 1; k <= max_f; k++) {
            long long ways = 1;
            for (auto& [c, f] : freq) {
                if (f >= k) {
                    ways = ways * (1 + comb(f, k)) % MOD;
                }
            }
            ways = (ways - 1 + MOD) % MOD;
            result = (result + ways) % MOD;
        }
        return result;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** ### Why Brute Force Fails

**How the code works:**
- For each character `c` with `freq[c] >= k`, we can either **include** it (choose exactly `k` of its `freq[c]` occurrences: \binom{freq[c]}{k} ways) or **exclude** it entirely (1 way)
- Characters with `freq[c] < k` must be excluded

**Walkthrough** — input `s = "aabb"`, expected output `11`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.

**Time:** O(\text{maxFreq} \times |\Sigma|) where |\Sigma| \le 26 · **Space:** O(\text{maxFreq}) for factorial arrays## Walk-through: `s = "aabb"`
## Why Not Pascal's Triangle?

For inputs like `"jjjjjj..."` (single character, frequency 10^4), a Pascal table would need O(n^2) space -- up to 10^8 entries. The factorial + modular inverse approach uses only O(n) space and computes each \binom{n}{k} in O(1).

| Approach | Space | Per-query |
|---|---|---|
| Pascal's triangle | O(n^2) | O(1) |
| Factorial + mod inverse | O(n) | O(1) |

## Common Mistakes

- **Forgetting the -1:** The product includes the case where every character is excluded (empty subsequence), which must be subtracted
- **Not clamping combinations:** Only characters with `freq[c] >= k` contribute; others must be skipped (their factor is just 1)
- **Using Pascal table for large n:** Causes MLE; always use factorial arrays with Fermat inverse
- **Missing modular arithmetic:** Intermediate products can overflow without `% MOD` at each step

## Key Takeaways

- **"Fix a parameter and count"** is a powerful combinatorial strategy -- here we fix the target frequency `k`
- For each character, the choice is binary: include (choose k copies) or exclude -- giving a product formula
- **Modular inverse via Fermat's little theorem** (a^{-1} \equiv a^{p-2} \pmod{p}) is essential for efficient \binom{n}{k} under modulo
- Grouping by frequency is a clean optimization when characters share the same count

## Related Problems

- [1569. Number of Ways to Reorder Array to Get Same BST](https://www.leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/) -- combinatorics with modular inverse
- [62. Unique Paths](https://www.leetcode.com/problems/unique-paths/) -- basic combinatorics \binom{m+n-2}{m-1}$
- [1512. Number of Good Pairs](https://www.leetcode.com/problems/number-of-good-pairs/) -- frequency counting
- [940. Distinct Subsequences II](https://www.leetcode.com/problems/distinct-subsequences-ii/) -- subsequence counting with DP

## References

- [LC 2539: Count the Number of Good Subsequences on LeetCode](https://www.leetcode.com/problems/count-the-number-of-good-subsequences/)
- [LeetCode Discuss — LC 2539: Count the Number of Good Subsequences](https://www.leetcode.com/problems/count-the-number-of-good-subsequences/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/count-the-number-of-good-subsequences/editorial/) *(may require premium)*

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
