---
layout: post
title: "[Medium] 418. Sentence Screen Fitting"
date: 2025-12-31 19:30:00 -0700
categories: [leetcode, medium, dynamic-programming, string, simulation]
permalink: /2025/12/31/medium-418-sentence-screen-fitting/
---
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

## Thinking Process

Given a `rows x cols` screen and a sentence represented as a list of strings, return *the number of times the given sentence can be fitted on the screen*.

The order of words in the sentence must remain unchanged, and a word cannot be split into two lines. A single space must separate two consecutive words on a line.

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 105" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">1D DP recurrence</text>

  <text x="30" y="38" font-size="10" fill="#9A9792">dp[i]</text>
  <rect x="30" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="48" y="58" text-anchor="middle" font-size="11">0</text>
  <rect x="66" y="42" width="36" height="28" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="84" y="58" text-anchor="middle" font-size="11">1</text>
  <rect x="102" y="42" width="36" height="28" rx="3" fill="#E0D8E4" stroke="#A098A8"/><text x="120" y="58" text-anchor="middle" font-size="11">2</text>
  <rect x="138" y="42" width="36" height="28" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="156" y="58" text-anchor="middle" font-size="11">?</text>
  <path d="M120 70v8M84 70v8" stroke="#C4956A" stroke-width="1.5"/>
  <text x="120" y="95" text-anchor="middle" font-size="11" fill="#6B6560">dp[i] from smaller indices / subproblems</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **1D DP** *(this problem)* | $O(n)$ | $O(n)$ or $O(1)$ | Linear recurrence |
| 2D DP | $O(nm)$ | $O(nm)$ or $O(n)$ | Grid or two-sequence problems |
| State machine DP | $O(n)$ | $O(1)$ | Buy/sell, hold/not-hold states |
| Memoization (top-down) | Same as DP | $O(n)$ | Recursive + cache |

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

### Solution Explanation

**Approach:** 1D DP (this problem)

**Key idea:** Given a `rows x cols` screen and a sentence represented as a list of strings, return *the number of times the given sentence can be fitted on the screen*.

**How the code works:**
- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

**Walkthrough** — input `sentence = ["hello","world"], rows = 2, cols = 8`, expected output `1`:

hello---
world---
The character '-' signifies an empty space on the screen.

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

### Complexity
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

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Related Problems

- [418. Sentence Screen Fitting](https://www.leetcode.com/problems/sentence-screen-fitting/) - Current problem
- [68. Text Justification](https://www.leetcode.com/problems/text-justification/) - Similar text fitting
- [1592. Rearrange Spaces Between Words](https://www.leetcode.com/problems/rearrange-spaces-between-words/) - Text formatting

## Tags

`Dynamic Programming`, `String`, `Simulation`, `Medium`

## Key Takeaways

- Define state: what subproblem does `dp[i]` (or `dp[i][j]`) represent?
- Recurrence: how does the answer build from smaller indices?
- Base cases first; optimize space if only prior row/layer is needed.

## References

- [LC 418: Sentence Screen Fitting on LeetCode](https://www.leetcode.com/problems/sentence-screen-fitting/)
- [LeetCode Discuss — LC 418: Sentence Screen Fitting](https://www.leetcode.com/problems/sentence-screen-fitting/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/sentence-screen-fitting/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
