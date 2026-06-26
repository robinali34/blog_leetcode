---
layout: post
title: "[Easy] 408. Valid Word Abbreviation"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm easy cpp string two-pointers problem-solving
permalink: /posts/2025-11-24-easy-408-valid-word-abbreviation/
tags: [leetcode, easy, string, two-pointers, parsing]
---
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as `"substitution"` could be abbreviated as (but not limited to):

- `"s10n"` (`"s" + "ubstitutio" + "n"`)
- `"sub4u4"` (`"sub" + "stit" + "u" + "tion"`)
- `"12"` (`"substitution"`)
- `"s55n"` (`"s" + "ubsti" + "tuti" + "on"` - invalid, adjacent substrings)
- `"s010n"` (`"s" + "010" + "n"` - invalid, leading zeros)

Given a string `word` and an abbreviation `abbr`, return whether the string matches the given abbreviation.

## Examples

**Example 1:**
```
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: 
  "i12iz4n" represents:
  - "i" (1 character)
  - "12" (skip 12 characters: "nternational")
  - "iz" (2 characters: "iz")
  - "4" (skip 4 characters: "atio")
  - "n" (1 character: "n")
  Total: 1 + 12 + 2 + 4 + 1 = 20 characters ✓
```

**Example 2:**
```
Input: word = "apple", abbr = "a2e"
Output: false
Explanation: 
  "a2e" represents:
  - "a" (1 character)
  - "2" (skip 2 characters: "pp")
  - "e" (1 character: should be "e" but we're at position 4, which is "e" ✓)
  Wait, let me recalculate: "a" at pos 0, skip 2 → pos 3, "e" at pos 3... but "e" is at pos 4
  Actually: "a" at pos 0, skip 2 → pos 2 ("p"), then "e" should be at pos 4, mismatch ✗
  
  Actually the abbreviation is invalid because after skipping 2 from position 1, 
  we're at position 3, but "e" is at position 4.
```

**Example 3:**
```
Input: word = "substitution", abbr = "s010n"
Output: false
Explanation: Leading zeros are not allowed.
```

**Example 4:**
```
Input: word = "substitution", abbr = "s55n"
Output: false
Explanation: Cannot have adjacent number replacements (would need to be "s5u5n").
```

## Constraints

- `1 <= word.length <= 20`
- `word` consists of only lowercase English letters.
- `1 <= abbr.length <= 10`
- `abbr` consists of lowercase English letters and digits.
- `abbr` does not contain any leading zeros.

## Thinking Process

1. **Position tracking**: Track where we are in the word (`abbrLen`)

- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

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
| **Opposite ends** *(this problem)* | O(n) | O(1) | Sorted array pair search, reversal |
| Slow / fast pointers | O(n) | O(1) | Linked list middle, cycle detection |
| Same-direction chase | O(n) | O(1) | Remove duplicates in-place |
| Sliding window (variable) | O(n) | O(1) | Subarray with constraint |

## Solution

**Time Complexity:** O(n) where n is the length of `abbr`  
**Space Complexity:** O(1)

The key insight is to track the current position in the word while parsing the abbreviation. When we encounter a letter, we verify it matches. When we encounter digits, we parse the number and skip that many characters.

### Solution: Position Tracking Approach

```cpp
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int len = abbr.length(), wordLen = word.length();
        int abbrLen = 0, num = 0;
        
        for(int i = 0; i < len; i++) {
            if(abbr[i] >= 'a' && abbr[i] <= 'z') {
                // Letter: add accumulated number and current letter
                abbrLen += num + 1;
                num = 0;
                
                // Check bounds and character match
                if(abbrLen > wordLen || abbr[i] != word[abbrLen - 1]) {
                    return false;
                }
            } else {
                // Digit: check for leading zero and build number
                if(!num && abbr[i] == '0') {
                    return false;
                }
                num = num * 10 + abbr[i] - '0';
            }
        }
        
        // Final check: accumulated length should match word length
        return abbrLen + num == wordLen;
    }
};
```

### Solution Explanation

**Approach:** Opposite ends (this problem)

**Key idea:** 1. **Position tracking**: Track where we are in the word (`abbrLen`)

**How the code works:**
1. **Position tracking**: Track where we are in the word (`abbrLen`)
- Two indices move toward each other or in the same direction.
- Works on sorted arrays or when in-place modification is required.
- Loop invariant: all indices outside `[left, right]` are already resolved.

**Walkthrough** — input `word = "internationalization", abbr = "i12iz4n"`, expected output `true`:

"i12iz4n" represents:
  - "i" (1 character)
  - "12" (skip 12 characters: "nternational")
  - "iz" (2 characters: "iz")
  - "4" (skip 4 characters: "atio")
  - "n" (1 character: "n")
  Total: 1 + 12 + 2 + 4 + 1 = 20 characters ✓

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Position Tracking** | O(n) | O(1) | Single pass, concise | Less intuitive |
| **Two-Pointer** | O(n) | O(1) | More intuitive | Slightly more code |
## Algorithm Breakdown

### Letter Handling

```cpp
if(abbr[i] >= 'a' && abbr[i] <= 'z') {
    abbrLen += num + 1;
    num = 0;
    
    if(abbrLen > wordLen || abbr[i] != word[abbrLen - 1]) {
        return false;
    }
}
```

**Why:**
- `abbrLen += num + 1`: Add skipped characters (`num`) + current letter (1)
- Reset `num = 0`: Number has been consumed
- `abbrLen - 1`: Convert to 0-indexed position
- Check bounds: `abbrLen > wordLen` prevents overflow
- Check match: Current abbreviation letter must match word letter

### Digit Handling

```cpp
else {
    if(!num && abbr[i] == '0') {
        return false;
    }
    num = num * 10 + abbr[i] - '0';
}
```

**Why:**
- `!num && abbr[i] == '0'`: Leading zero check (first digit cannot be '0')
- `num * 10 + digit`: Build number from left to right
- Don't update `abbrLen` yet: Number might continue

### Final Check

```cpp
return abbrLen + num == wordLen;
```

**Why:**
- After processing all characters, `num` might still contain unprocessed skip count
- `abbrLen + num` should equal total word length
- Ensures we've processed exactly the right number of characters

### Complexity
| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
| **Position Tracking** | O(n) | O(1) | Single pass, concise | Less intuitive |
| **Two-Pointer** | O(n) | O(1) | More intuitive | Slightly more code |

## Implementation Details

### Why `abbrLen - 1` for Index?

**Position vs Index:**
- `abbrLen` tracks **position** (1-indexed count of characters)
- Array access needs **index** (0-indexed)
- `word[abbrLen - 1]` converts position to index

**Example:**
```
After processing "i", abbrLen = 1 (1 character processed)
word[0] is the first character, so word[abbrLen - 1] = word[0] ✓
```

### Leading Zero Detection

```cpp
if(!num && abbr[i] == '0') {
    return false;
}
```

**Why this works:**
- `!num` means we haven't started building a number yet
- If first digit is '0', it's a leading zero → invalid
- Valid numbers: "1", "12", "123" (no leading zeros)
- Invalid: "01", "012" (leading zeros)

### Number Building

```cpp
num = num * 10 + abbr[i] - '0';
```

**How it works:**
- Start with `num = 0`
- For each digit: multiply by 10 and add new digit
- Example: "12" → `num = 0*10+1 = 1`, then `num = 1*10+2 = 12`

## Common Mistakes

1. **Leading zeros**: `"s010n"` → invalid (leading zero)
2. **Exact match**: `"word"` and `"4"` → valid (skip all 4 characters)
3. **No skips**: `"word"` and `"word"` → valid (all letters)
4. **Overflow**: `"word"` and `"w5d"` → invalid (skip 5 but only 3 chars remain)
5. **Underflow**: `"word"` and `"w2d"` → invalid (skip 2, but 'd' doesn't match position)
6. **Empty abbreviation**: Not possible per constraints

1. **Off-by-one errors**: Forgetting `abbrLen - 1` for array indexing
2. **Leading zeros**: Not checking for '0' as first digit
3. **Final check**: Forgetting to add remaining `num` at the end
4. **Bounds checking**: Not verifying `abbrLen <= wordLen`
5. **Number parsing**: Not handling multi-digit numbers correctly
6. **Reset num**: Forgetting to reset `num = 0` after processing letter

## Optimization Tips

1. **Early termination**: Return false immediately on mismatch
2. **Single pass**: Process abbreviation in one iteration
3. **Minimal variables**: Only track necessary state

## Related Problems

- [411. Minimum Unique Word Abbreviation](https://www.leetcode.com/problems/minimum-unique-word-abbreviation/) - Generate valid abbreviations
- [320. Generalized Abbreviation](https://www.leetcode.com/problems/generalized-abbreviation/) - Generate all abbreviations
- [422. Valid Word Square](https://www.leetcode.com/problems/valid-word-square/) - Similar validation problem
- String parsing and validation problems

## Real-World Applications

1. **Text Compression**: Validating compressed text formats
2. **URL Shortening**: Verifying shortened URLs decode correctly
3. **Data Validation**: Checking format compliance
4. **Parsing**: Validating structured text representations

## Pattern Recognition

This problem demonstrates the **"String Parsing with State Tracking"** pattern:

```
1. Track current position/state while parsing
2. Handle different character types (letters vs digits)
3. Accumulate values (numbers) across multiple characters
4. Validate at each step and at the end
```

Similar problems:
- Expression parsing
- Format validation
- String matching with wildcards
- Pattern matching

## Step-by-Step Trace: `word = "apple"`, `abbr = "a2e"`

```
Initial: abbrLen = 0, num = 0, wordLen = 5

i=0: 'a' (letter)
  abbrLen = 0 + 0 + 1 = 1
  num = 0
  Check: word[0] == 'a' ✓
  abbrLen = 1

i=1: '2' (digit)
  num = 0 * 10 + 2 = 2

i=2: 'e' (letter)
  abbrLen = 1 + 2 + 1 = 4
  num = 0
  Check: word[3] == 'e' ✗ (word[3] = 'l', not 'e')
  Return false
```

**Why it fails:**
- After 'a' at position 0, skip 2 → position 2
- 'e' should be at position 2, but word[2] = 'p'
- Actually, 'e' is at position 4, so abbreviation is invalid

## Why This Solution Works

**Correctness:**
- Tracks exact position in word: `abbrLen` counts characters processed
- Validates each letter: Ensures abbreviation matches word
- Handles numbers correctly: Parses multi-digit numbers
- Prevents leading zeros: Rejects invalid abbreviations
- Final validation: Ensures total length matches

**Efficiency:**
- Single pass: O(n) where n is abbreviation length
- Constant space: Only a few variables
- Early termination: Returns false immediately on error

## Key Takeaways

1. **Position tracking**: Track where we are in the word (`abbrLen`)
2. **Number accumulation**: Build multi-digit numbers digit by digit
3. **Leading zero check**: Reject if digit is '0' when `num == 0`
4. **Final validation**: Ensure total length matches word length
5. **Bounds checking**: Verify we don't exceed word length

## References

- [LC 408: Valid Word Abbreviation on LeetCode](https://www.leetcode.com/problems/valid-word-abbreviation/)
- [LeetCode Discuss — LC 408: Valid Word Abbreviation](https://www.leetcode.com/problems/valid-word-abbreviation/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/valid-word-abbreviation/editorial/) *(may require premium)*

## Template Reference

- [String Processing](/blog_leetcode/posts/2025-11-24-leetcode-templates-string-processing/)
