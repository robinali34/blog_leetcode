---
layout: post
title: "418. Sentence Screen Fitting"
date: 2025-12-31 19:30:00 -0700
categories: [leetcode, medium, dynamic-programming, string, simulation]
permalink: /2025/12/31/medium-418-sentence-screen-fitting/
---

# 418. Sentence Screen Fitting

## Problem Statement

Given a `rows x cols` screen and a sentence represented as a list of strings, return *the number of times the given sentence can be fitted on the screen*.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words on a line.

## Examples

**Example 1:**
```
Input: sentence = ["hello","world"], rows = 2, cols = 8
Output: 1
Explanation:
hello---
world---
The character '-' signifies an empty space on the screen.
```

**Example 2:**
```
Input: sentence = ["a", "bcd", "e"], rows = 3, cols = 6
Output: 2
Explanation:
a-bcd-
e-a---
bcd-e-
The character '-' signifies an empty space on the screen.
```

**Example 3:**
```
Input: sentence = ["i","had","apple","pie"], rows = 4, cols = 5
Output: 1
Explanation:
i-had
apple
pie-i
had--
The character '-' signifies an empty space on the screen.
```

## Constraints

- `1 <= sentence.length <= 100`
- `1 <= sentence[i].length <= 10`
- `1 <= rows, cols <= 2 * 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Screen layout**: How is the screen laid out? (Assumption: rows x cols grid - words are placed left to right, wrapping to next row when needed)

2. **Word placement**: How are words placed? (Assumption: Words separated by single space, words don't wrap - whole word must fit on same row)

3. **Sentence repetition**: Can sentence repeat? (Assumption: Yes - sentence can be repeated multiple times to fill screen)

4. **Return value**: What should we return? (Assumption: Integer - number of times sentence can be fitted on screen)

5. **Space handling**: How are spaces handled? (Assumption: Single space between words, spaces at end of row are allowed)

## Solution Approach

This problem requires fitting a sentence on a screen row by row, where words cannot be split and must be separated by spaces. We can solve this efficiently using **dynamic programming** to precompute how many complete sentences fit starting from each word position.

### Key Insights:

1. **DP Precomputation**: For each starting word, compute how many complete sentences fit in one row
2. **Next Word Tracking**: Track which word starts the next row after fitting current row
3. **Row Simulation**: Simulate each row using precomputed values
4. **Optimization**: Avoid recomputing for same starting positions

### Algorithm:

1. **Precompute DP**: For each word as starting position, calculate sentences and next word
2. **Simulate Rows**: For each row, use DP to get sentences and move to next word
3. **Accumulate Count**: Sum up complete sentences across all rows

## Solution

### **Solution: Dynamic Programming with Next Word Tracking**

```cpp
class Solution {
public:
    int wordsTyping(vector<string>& sentence, int rows, int cols) {
        const int N = sentence.size();
        vector<int> dp(N, 0);
        vector<int> next(N, 0);
        for(int i = 0; i < N; i++) {
            int count = 0, ptr = i, cur = cols;
            while(cur >= (int)sentence[ptr].size()) {
                cur -= sentence[ptr].size() + 1;
                ptr++;
                if(ptr == N) {
                    count++;
                    ptr = 0;
                }
            }
            dp[i] = count;
            next[i] = ptr;
        }

        int count = 0, cur = 0;
        for(int i = 0; i < rows; i++) {
            count += dp[cur];
            cur = next[cur];
        }
        return count;
    }
};
```

### **Algorithm Explanation:**

1. **Initialize DP Arrays (Lines 5-6)**:
   - `dp[i]`: Number of complete sentences that fit in one row starting from word `i`
   - `next[i]`: Index of word that starts the next row after fitting one row starting from word `i`

2. **Precompute for Each Starting Word (Lines 7-18)**:
   - For each word `i` as starting position:
     - Initialize: `count = 0` (complete sentences), `ptr = i` (current word), `cur = cols` (remaining columns)
     - **Fit words**: While current word fits in remaining space:
       - Subtract word length + 1 (space): `cur -= sentence[ptr].size() + 1`
       - Move to next word: `ptr++`
       - **Complete sentence**: If `ptr == N`, increment count and reset to 0
     - Store results: `dp[i] = count`, `next[i] = ptr`

3. **Simulate All Rows (Lines 20-24)**:
   - Start with `cur = 0` (first word)
   - For each row:
     - Add complete sentences: `count += dp[cur]`
     - Move to next starting word: `cur = next[cur]`
   - Return total count

### **Example Walkthrough:**

**For `sentence = ["a", "bcd", "e"], rows = 3, cols = 6`:**

```
Step 1: Precompute DP arrays

Starting from word 0 ("a"):
  cur = 6, ptr = 0
  "a" fits: cur = 6 - 1 - 1 = 4, ptr = 1
  "bcd" fits: cur = 4 - 3 - 1 = 0, ptr = 2
  "e" doesn't fit (need 1 + 1 = 2, but cur = 0)
  ptr = 2, count = 0 (no complete sentence)
  dp[0] = 0, next[0] = 2

Starting from word 1 ("bcd"):
  cur = 6, ptr = 1
  "bcd" fits: cur = 6 - 3 - 1 = 2, ptr = 2
  "e" fits: cur = 2 - 1 - 1 = 0, ptr = 0 (wrapped)
  count = 1 (one complete sentence)
  "a" doesn't fit (need 1 + 1 = 2, but cur = 0)
  dp[1] = 1, next[1] = 0

Starting from word 2 ("e"):
  cur = 6, ptr = 2
  "e" fits: cur = 6 - 1 - 1 = 4, ptr = 0 (wrapped)
  count = 1
  "a" fits: cur = 4 - 1 - 1 = 2, ptr = 1
  "bcd" doesn't fit (need 3 + 1 = 4, but cur = 2)
  dp[2] = 1, next[2] = 1

dp = [0, 1, 1]
next = [2, 0, 1]

Step 2: Simulate rows

Row 0: cur = 0
  count += dp[0] = 0
  cur = next[0] = 2

Row 1: cur = 2
  count += dp[2] = 1
  cur = next[2] = 1

Row 2: cur = 1
  count += dp[1] = 1
  cur = next[1] = 0

Total count = 0 + 1 + 1 = 2

Visual representation:
Row 0: a-bcd-  (starts with "a", ends at "bcd", next starts with "e")
Row 1: e-a---  (starts with "e", completes sentence, next starts with "bcd")
Row 2: bcd-e-  (starts with "bcd", completes sentence, next starts with "a")
```

## Algorithm Breakdown

### **Key Insight: DP Precomputation**

Instead of simulating each row character by character, we precompute:
- **How many complete sentences** fit starting from each word
- **Which word starts the next row** after fitting one row

This allows O(1) lookup per row instead of O(cols) simulation.

### **DP State Definition**

**`dp[i]`**: Number of complete sentences that fit in one row when starting from word `i`

**`next[i]`**: Index of word that starts the next row after fitting one row starting from word `i`

### **Why This Works**

1. **Repetitive Pattern**: Sentence repeats, so starting positions repeat
2. **State Reuse**: Same starting word always leads to same result
3. **Efficient Lookup**: O(1) per row instead of O(cols) simulation
4. **Accumulation**: Sum DP values across all rows

## Complexity Analysis

### **Time Complexity:** O(N × cols + rows)
- **Precomputation**: O(N × cols) - for each word, simulate up to cols characters
- **Row simulation**: O(rows) - one lookup per row
- **Total**: O(N × cols + rows) where N = sentence length

### **Space Complexity:** O(N)
- **DP arrays**: O(N) for `dp` and `next`
- **Total**: O(N)

## Key Points

1. **DP Precomputation**: Precompute results for each starting word
2. **Next Word Tracking**: Track which word starts next row
3. **Row Simulation**: Use precomputed values for each row
4. **Efficient**: O(rows) for row simulation instead of O(rows × cols)
5. **Space Optimization**: Only store O(N) state

## Alternative Approaches

### **Approach 1: DP with Next Tracking (Current Solution)**
- **Time**: O(N × cols + rows)
- **Space**: O(N)
- **Best for**: Optimal solution with precomputation

### **Approach 2: Character-by-Character Simulation**
- **Time**: O(rows × cols)
- **Space**: O(1)
- **Simulate**: Place each character, track position
- **Inefficient**: O(rows × cols) time

### **Approach 3: String Concatenation**
- **Time**: O(rows + N)
- **Space**: O(N)
- **Concatenate**: Join sentence with spaces
- **Simulate**: Track pointer in concatenated string
- **Efficient**: But different approach

## Detailed Example Walkthrough

### **Example: `sentence = ["i","had","apple","pie"], rows = 4, cols = 5`**

```
Step 1: Precompute DP

Starting from word 0 ("i"):
  cur = 5, ptr = 0
  "i" fits: cur = 5 - 1 - 1 = 3, ptr = 1
  "had" fits: cur = 3 - 3 - 1 = -1 (doesn't fit, need 4)
  dp[0] = 0, next[0] = 1

Starting from word 1 ("had"):
  cur = 5, ptr = 1
  "had" fits: cur = 5 - 3 - 1 = 1, ptr = 2
  "apple" doesn't fit (need 5 + 1 = 6, but cur = 1)
  dp[1] = 0, next[1] = 2

Starting from word 2 ("apple"):
  cur = 5, ptr = 2
  "apple" fits: cur = 5 - 5 - 1 = -1 (doesn't fit, need 6)
  Actually, "apple" is 5 chars, need 5 + 1 = 6 for next word
  But we can fit just "apple" if it's the last word
  Let me recalculate: "apple" = 5 chars, fits in 5 cols
  But we need space after, so if cur = 5, we can fit "apple" but no space after
  Actually, the algorithm checks: cur >= sentence[ptr].size()
  So if cur = 5 and "apple".size() = 5, it fits
  Then cur = 5 - 5 - 1 = -1, which fails next check
  dp[2] = 0, next[2] = 3

Starting from word 3 ("pie"):
  cur = 5, ptr = 3
  "pie" fits: cur = 5 - 3 - 1 = 1, ptr = 0 (wrapped)
  count = 1
  "i" fits: cur = 1 - 1 - 1 = -1 (doesn't fit)
  dp[3] = 1, next[3] = 0

dp = [0, 0, 0, 1]
next = [1, 2, 3, 0]

Step 2: Simulate rows

Row 0: cur = 0
  count += dp[0] = 0
  cur = next[0] = 1

Row 1: cur = 1
  count += dp[1] = 0
  cur = next[1] = 2

Row 2: cur = 2
  count += dp[2] = 0
  cur = next[2] = 3

Row 3: cur = 3
  count += dp[3] = 1
  cur = next[3] = 0

Total count = 1

Visual:
Row 0: i-had
Row 1: apple
Row 2: pie-i
Row 3: had--
```

## Edge Cases

1. **Single word**: Sentence with one word
2. **Long word**: Word longer than cols (can't fit)
3. **Exact fit**: Word exactly fits in one row
4. **Many rows**: Large number of rows
5. **Short sentence**: Sentence fits multiple times per row

## Optimization Notes

The algorithm efficiently handles:
- **Repeated patterns**: Same starting word always produces same result
- **Fast lookup**: O(1) per row instead of O(cols)
- **Memory efficient**: Only O(N) space for DP arrays

## Related Problems

- [418. Sentence Screen Fitting](https://leetcode.com/problems/sentence-screen-fitting/) - Current problem
- [68. Text Justification](https://leetcode.com/problems/text-justification/) - Similar text fitting
- [1592. Rearrange Spaces Between Words](https://leetcode.com/problems/rearrange-spaces-between-words/) - Text formatting

## Tags

`Dynamic Programming`, `String`, `Simulation`, `Medium`

