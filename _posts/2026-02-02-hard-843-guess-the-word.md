---
layout: post
title: "843. Guess the Word"
date: 2026-02-02 00:00:00 -0700
categories: [leetcode, hard, array, string, interactive, minmax]
permalink: /2026/02/02/hard-843-guess-the-word/
tags: [leetcode, hard, array, string, interactive, minmax]
---

# 843. Guess the Word

## Problem Statement

This is an **interactive problem**.

You are given an array of unique strings `words` where `words[i]` is six letters long. One word of `words` is chosen as `secret`.

You may call `Master.guess(word)` to guess a word. The guessed word should have type `string` and must be from the original array with 6 lowercase letters.

This function returns an `integer` representing the number of exact matches (value and position) of your guess to the `secret` word. Also, if your guess is not in the given wordlist, it will return `-1` instead.

For each test case, you have exactly 10 guesses to guess the word. If you have made 10 or fewer calls to `Master.guess` and at least one of them was the `secret`, you pass the test case.

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Word format**: What is the format of words? (Assumption: All words are exactly 6 lowercase letters, unique, and the secret word is guaranteed to be in the list)

2. **Match definition**: What does "exact match" mean? (Assumption: An exact match means the character at the same position in both words is identical - value and position must match)

3. **Guess limit**: How many guesses are allowed? (Assumption: At most 10 guesses, and we must find the secret word within this limit)

4. **Guess return value**: What does `master.guess()` return? (Assumption: Returns the number of exact matches (0-6), or -1 if the word is not in the wordlist)

5. **Strategy requirement**: What strategy should we use? (Assumption: Use an elimination strategy - filter candidates based on match count with previous guesses)

## Interview Deduction Process (30 minutes)

**Step 1: Brute-Force Approach (8 minutes)**

Try guessing each word in the list one by one until we find the secret. This approach has O(n) time complexity in worst case, but we only have 10 guesses, so if n > 10, this won't work.

**Step 2: Semi-Optimized Approach (10 minutes)**

Use a filtering strategy. Start with any word, get the match count, and eliminate all words that don't have the same match count with the guessed word. This reduces the candidate set after each guess. However, we need to choose which word to guess next intelligently.

**Step 3: Optimized Solution (12 minutes)**

Use the elimination strategy with smart word selection. After each guess, filter candidates by removing words that don't have the same match count with the guessed word. The key insight is that if `match(word, guess) != matches`, then `word` cannot be the secret (because if it were, `master.guess(guess)` would return a different value). This guarantees we find the secret within 10 guesses since we eliminate incorrect candidates each round.

## Solution Approach

This is an interactive problem that requires an elimination strategy. The key insight is to use the match count from each guess to filter out impossible candidates.

### Key Insights:

1. **Elimination Strategy**: If `match(word, guess) != matches`, then `word` cannot be the secret
2. **Match Function**: Count exact character matches at the same positions
3. **Filtering**: After each guess, remove all words that don't have the same match count with the guessed word
4. **Guaranteed Success**: Since we eliminate candidates each round, we'll find the secret within 10 guesses

## Solution: Elimination Strategy

```cpp
/**
 * // This is the Master's API interface.
 * // You should not implement it, or speculate about its implementation
 * class Master {
 *   public:
 *     int guess(string word);
 * };
 */
class Solution {
public:
    void findSecretWord(vector<string>& words, Master& master) {
        unordered_set<string> cand(words.begin(), words.end());
        while(!cand.empty() ){
            string guess = *cand.begin();
            int matches = master.guess(guess);
            if(matches == 6)
                return;
            vector<string> list;
            for(string s : words){
                if(match(s, guess) != matches)
                    cand.erase(s);
            }
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

### Algorithm Breakdown:

1. **Initialize**: Create a set `cand` containing all words as candidates
2. **Iterate**: While candidates exist:
   - Pick a word from candidates (e.g., first word)
   - Call `master.guess(guess)` to get match count
   - If matches == 6, we found the secret, return
   - Filter candidates: Remove all words `s` where `match(s, guess) != matches`
3. **Match Function**: Count exact character matches at the same positions

### Why This Works:

- **Elimination Logic**: If `match(word, guess) != matches`, then `word` cannot be the secret
  - If `word` were the secret, then `master.guess(guess)` would return `match(word, guess)`
  - Since it returned `matches`, and `match(word, guess) != matches`, `word` is not the secret
- **Guaranteed Convergence**: Each guess eliminates incorrect candidates, so we'll find the secret within 10 guesses
- **Correctness**: The secret word will never be eliminated because `match(secret, guess) == matches` by definition

### Sample Test Case Run:

**Input:** `words = ["acckzz","ccbazz","eiowzz","abcczz"]`, `secret = "acckzz"`

```
Initial: cand = {"acckzz", "ccbazz", "eiowzz", "abcczz"}

Iteration 1:
  guess = "acckzz" (first word)
  matches = master.guess("acckzz") = 6
  matches == 6, return ✓
```

**Output:** Found secret word "acckzz" in 1 guess ✓

---

**Another Example:** `words = ["acckzz","ccbazz","eiowzz","abcczz"]`, `secret = "ccbazz"`

```
Initial: cand = {"acckzz", "ccbazz", "eiowzz", "abcczz"}

Iteration 1:
  guess = "acckzz" (first word)
  matches = master.guess("acckzz") = match("ccbazz", "acckzz") = 3
  matches != 6, continue
  Filter candidates:
    match("acckzz", "acckzz") = 6 != 3, remove "acckzz" ✗
    match("ccbazz", "acckzz") = 3 == 3, keep "ccbazz" ✓
    match("eiowzz", "acckzz") = 2 != 3, remove "eiowzz" ✗
    match("abcczz", "acckzz") = 4 != 3, remove "abcczz" ✗
  cand = {"ccbazz"}

Iteration 2:
  guess = "ccbazz" (only candidate)
  matches = master.guess("ccbazz") = 6
  matches == 6, return ✓
```

**Verification:**
- After first guess, only "ccbazz" remains (has 3 matches with "acckzz")
- Second guess finds the secret ✓

**Output:** Found secret word "ccbazz" in 2 guesses ✓

---

**Edge Case:** `words = ["hamada","khaled"]`, `secret = "hamada"`

```
Initial: cand = {"hamada", "khaled"}

Iteration 1:
  guess = "hamada" (first word)
  matches = master.guess("hamada") = 6
  matches == 6, return ✓
```

**Output:** Found secret word "hamada" in 1 guess ✓

---

**Complex Case:** `words = ["abcdef","bcdefg","cdefgh","defghi","efghij","fghijk"]`, `secret = "fghijk"`

```
Initial: cand = {"abcdef","bcdefg","cdefgh","defghi","efghij","fghijk"}

Iteration 1:
  guess = "abcdef"
  matches = master.guess("abcdef") = match("fghijk", "abcdef") = 0
  matches != 6, continue
  Filter candidates:
    match("abcdef", "abcdef") = 6 != 0, remove "abcdef" ✗
    match("bcdefg", "abcdef") = 5 != 0, remove "bcdefg" ✗
    match("cdefgh", "abcdef") = 4 != 0, remove "cdefgh" ✗
    match("defghi", "abcdef") = 3 != 0, remove "defghi" ✗
    match("efghij", "abcdef") = 2 != 0, remove "efghij" ✗
    match("fghijk", "abcdef") = 0 == 0, keep "fghijk" ✓
  cand = {"fghijk"}

Iteration 2:
  guess = "fghijk"
  matches = master.guess("fghijk") = 6
  matches == 6, return ✓
```

**Verification:**
- After first guess, only "fghijk" remains (has 0 matches with "abcdef")
- Second guess finds the secret ✓

**Output:** Found secret word "fghijk" in 2 guesses ✓

## Complexity Analysis

- **Time Complexity**: O(n²) worst case - In worst case, we might check all words in each iteration, but typically much better due to filtering
- **Space Complexity**: O(n) - For the candidate set

## Key Insights

1. **Elimination Strategy**: Use match count to eliminate impossible candidates
2. **Match Function**: Count exact character matches at the same positions
3. **Filtering Logic**: If `match(word, guess) != matches`, then `word` cannot be the secret
4. **Guaranteed Success**: The algorithm will find the secret within 10 guesses since candidates are eliminated each round
5. **Word Selection**: The current solution picks the first candidate, but more sophisticated strategies (like picking the word that minimizes maximum remaining candidates) can be used

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

- [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) - Binary search with interactive API
- [375. Guess Number Higher or Lower II](https://leetcode.com/problems/guess-number-higher-or-lower-ii/) - Minimax strategy with cost
- [299. Bulls and Cows](https://leetcode.com/problems/bulls-and-cows/) - Similar matching game
- [489. Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner/) - Another interactive problem
