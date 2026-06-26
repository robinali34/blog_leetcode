---
layout: post
title: "[Medium] 43. Multiply Strings"
date: 2026-02-17
categories: [leetcode, medium, string, math, simulation]
tags: [leetcode, medium, string, math, big-integer, simulation]
permalink: /2026/02/17/medium-43-multiply-strings/
---
Given two non-negative integers represented as strings `num1` and `num2`, return their product as a string. You **cannot** convert the inputs to integers directly (numbers can be very large).

## Examples

**Example 1:**

```
Input: num1 = "2", num2 = "3"
Output: "6"
```

**Example 2:**

```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Constraints

- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only
- Neither contains leading zeros (except `"0"` itself)

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | $O(n)$ | $O(1)$ | Palindrome, parsing |
| Hash map / frequency | $O(n)$ | $O(k)$ | Anagram, character counts |
| KMP / rolling hash | $O(n)$ | $O(n)$ | Pattern matching |
| Stack parsing | $O(n)$ | $O(n)$ | Decode string, parentheses |

## Thinking Process

This is **big integer multiplication** -- simulate digit-by-digit multiplication exactly like grade school arithmetic.

### Key Observations

If `num1` has length `n` and `num2` has length `m`:
- The product has **at most `n + m` digits**
- Allocate a result array of size `n + m`

### Index Formula

When multiplying `num1[i] * num2[j]`, the contribution goes to:

$$\text{result}[i + j + 1] \quad \text{(ones place)}$$
$$\text{result}[i + j] \quad \text{(carry)}$$

This is because position `i` from the end of `num1` and position `j` from the end of `num2` together shift the product by `(n-1-i) + (m-1-j)` places, which maps to index `i + j + 1` in the result array.

### Walk-Through: `123 × 45`

```
         1  2  3
       ×    4  5
      -----------
  positions: result[0..4]

  3×5 = 15 → result[4] += 15  → result[4]=5, carry 1 to result[3]
  2×5 = 10 → result[3] += 10+1 = 11 → result[3]=1, carry 1 to result[2]
  1×5 =  5 → result[2] += 5+1 = 6

  3×4 = 12 → result[3] += 12  → result[3]=3, carry 1 to result[2]
  2×4 =  8 → result[2] += 8+1 = 15 → result[2]=5, carry 1 to result[1]
  1×4 =  4 → result[1] += 4+1 = 5

  result = [0, 5, 5, 3, 5] → "05535" → skip leading zero → "5535"
```

Wait -- `123 × 45 = 5535`. Correct!



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

## Approach: Grade School Multiplication -- $O(nm)$

Multiply each digit pair, accumulate into a result array with carry propagation.

{% raw %}
```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0") return "0";

        int n = num1.size();
        int m = num2.size();
        vector<int> result(n + m, 0);

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int sum = mul + result[i + j + 1];

                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }

        string ans;
        for (int num : result) {
            if (!(ans.empty() && num == 0))
                ans += to_string(num);
        }

        return ans.empty() ? "0" : ans;
    }
};
```

### Solution Explanation

**Approach:** Two pointers on string (this problem)

**Key idea:** This is **big integer multiplication** -- simulate digit-by-digit multiplication exactly like grade school arithmetic.

**How the code works:**
- The product has **at most `n + m` digits**
- Allocate a result array of size `n + m`
-----------

**Walkthrough** — input `num1 = "2", num2 = "3"`, expected output `"6"`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Forgetting the early return for `"0"` inputs (otherwise you get `"000..."`)
- Off-by-one on the index formula (`i + j` vs `i + j + 1`)
- Not handling leading zeros when converting the result array to a string

## Key Takeaways

- **Big integer multiplication** follows the same algorithm you learned in school
- The index formula `result[i + j + 1]` is the core insight -- memorize it
- Always allocate `n + m` digits for the result
- Faster algorithms exist (Karatsuba $O(n^{1.58})$, FFT $O(n \log n)$) but are overkill for interview constraints

## Related Problems

- [2. Add Two Numbers](https://www.leetcode.com/problems/add-two-numbers/) -- big integer addition on linked lists
- [67. Add Binary](https://www.leetcode.com/problems/add-binary/) -- string addition with carry
- [415. Add Strings](https://www.leetcode.com/problems/add-strings/) -- big integer addition on strings

## References

- [LC 43: Multiply Strings on LeetCode](https://www.leetcode.com/problems/multiply-strings/)
- [LeetCode Discuss — LC 43: Multiply Strings](https://www.leetcode.com/problems/multiply-strings/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/multiply-strings/editorial/) *(may require premium)*

## Template Reference

- [Math & Bit Manipulation](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/)
- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
