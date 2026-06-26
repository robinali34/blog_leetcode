---
layout: post
title: "[Hard] 843. Guess the Word"
date: 2026-02-02 00:00:00 -0700
categories: [leetcode, hard, array, string, interactive, minmax]
permalink: /2026/02/02/hard-843-guess-the-word/
tags: [leetcode, hard, array, string, interactive, minmax]
---
This is an **interactive problem**.

You are given an array of unique strings `words` where `words[i]` is six letters long. One word of `words` is chosen as `secret`.

You may call `Master.guess(word)` to guess a word. The guessed word should have type `string` and must be from the original array with 6 lowercase letters.

This function returns an `integer` representing the number of exact matches (value and position) of your guess to the `secret` word. Also, if your guess is not in the given wordlist, it will return `-1` instead.

For each test case, you have exactly 10 guesses to guess the word. If you have made 10 or fewer calls to `Master.guess` and at least one of them was the `secret`, you pass the test case.

## Thinking Process

1. **Elimination Strategy**: Use match count to eliminate impossible candidates

- Strings often need frequency maps or two-pointer scans.
- Watch index bounds and empty-string edge cases.
- Stack helps with nested or repeated patterns.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 230 110" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Array + hash map</text>

  <rect x="30" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="44" y="61" text-anchor="middle" font-size="10">2</text>
  <rect x="62" y="45" width="28" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="76" y="61" text-anchor="middle" font-size="10">7</text>
  <rect x="106" y="45" width="28" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="120" y="61" text-anchor="middle" font-size="10">11</text>
  <rect x="150" y="40" width="60" height="38" rx="4" fill="#FAF8F5" stroke="#D4D1CC"/>
  <text x="180" y="61" text-anchor="middle" font-size="10" fill="#6B6560">map</text>
  <text x="110" y="100" text-anchor="middle" font-size="11" fill="#6B6560">hash map for O(1) lookups</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Two pointers on string** *(this problem)* | O(n) | O(1) | Palindrome, parsing |
| Hash map / frequency | O(n) | O(k) | Anagram, character counts |
| KMP / rolling hash | O(n) | O(n) | Pattern matching |
| Stack parsing | O(n) | O(n) | Decode string, parentheses |

## Examples

**Example 1:**

```
Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"]
Explanation: master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
```

**Example 2:**

```
Input: secret = "hamada", words = ["hamada","khaled"], numguesses = 10
Output: You guessed the secret word correctly.
```

## Constraints

- `1 <= words.length <= 100`
- `words[i].length == 6`
- `words[i]` consist of lowercase English letters.
- All the strings of `words` are **unique**.
- `secret` exists in `words`.
- `numguesses == 10`

### Complexity
- **Time Complexity**: O(n²) worst case - In worst case, we might check all words in each iteration, but typically much better due to filtering
- **Space Complexity**: O(n) - For the candidate set

## Optimization: Minimax Strategy

A more sophisticated approach is to pick the word that minimizes the maximum number of remaining candidates across all possible match counts:

```cpp
class Solution {
public:
    void findSecretWord(vector<string>& words, Master& master) {
        vector<string> cand = words;
        while(!cand.empty()) {
            // Pick word that minimizes maximum remaining candidates
            string guess = cand[0];
            int minMax = cand.size();
            for(string word : cand) {
                vector<int> count(7, 0);
                for(string other : cand) {
                    count[match(word, other)]++;
                }
                int maxCount = *max_element(count.begin(), count.end());
                if(maxCount < minMax) {
                    minMax = maxCount;
                    guess = word;
                }
            }
            
            int matches = master.guess(guess);
            if(matches == 6) return;
            
            // Filter candidates
            vector<string> newCand;
            for(string word : cand) {
                if(match(word, guess) == matches) {
                    newCand.push_back(word);
                }
            }
            cand = newCand;
        }
    }

private:
    int match(const string& a, const string& b) {
        int cnt = 0;
        for(int i = 0; i < 6; i++) {
            cnt += (a[i] == b[i]);
        }
        return cnt;
    }
};
```

This strategy picks the word that, in the worst case, leaves the fewest remaining candidates, leading to faster convergence.

## Related Problems

- [374. Guess Number Higher or Lower](https://www.leetcode.com/problems/guess-number-higher-or-lower/) - Binary search with interactive API
- [375. Guess Number Higher or Lower II](https://www.leetcode.com/problems/guess-number-higher-or-lower-ii/) - Minimax strategy with cost
- [299. Bulls and Cows](https://www.leetcode.com/problems/bulls-and-cows/) - Similar matching game
- [489. Robot Room Cleaner](https://www.leetcode.com/problems/robot-room-cleaner/) - Another interactive problem

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

1. **Elimination Strategy**: Use match count to eliminate impossible candidates
2. **Match Function**: Count exact character matches at the same positions
3. **Filtering Logic**: If `match(word, guess) != matches`, then `word` cannot be the secret
4. **Guaranteed Success**: The algorithm will find the secret within 10 guesses since candidates are eliminated each round
5. **Word Selection**: The current solution picks the first candidate, but more sophisticated strategies (like picking the word that minimizes maximum remaining candidates) can be used

## References

- [LC 843: Guess the Word on LeetCode](https://www.leetcode.com/problems/guess-the-word/)
- [LeetCode Discuss — LC 843: Guess the Word](https://www.leetcode.com/problems/guess-the-word/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/guess-the-word/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
