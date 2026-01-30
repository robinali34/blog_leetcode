---
layout: post
title: "[Easy] 408. Valid Word Abbreviation"
date: 2025-11-24 00:00:00 -0800
categories: leetcode algorithm easy cpp string two-pointers problem-solving
permalink: /posts/2025-11-24-easy-408-valid-word-abbreviation/
tags: [leetcode, easy, string, two-pointers, parsing]
---

# [Easy] 408. Valid Word Abbreviation

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Abbreviation format**: What is the abbreviation format? (Assumption: Mix of letters and numbers - numbers represent skipped characters, letters represent actual characters)

2. **Validation rules**: What makes an abbreviation valid? (Assumption: Abbreviation must match word exactly - numbers skip that many characters, letters must match)

3. **Return value**: What should we return? (Assumption: Boolean - true if abbreviation is valid, false otherwise)

4. **Leading zeros**: Are leading zeros allowed? (Assumption: No - per constraints, no leading zeros in abbreviation)

5. **Number parsing**: How are numbers parsed? (Assumption: Consecutive digits form a number - skip that many characters in word)

## Solution: Single-Pass with Position Tracking

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

## How the Algorithm Works

### Key Insight: Track Word Position

**Variables:**
- `abbrLen`: Current position in the word (characters processed so far)
- `num`: Current number being parsed from abbreviation

**Logic:**
- When we see a **letter**: Add `num` (skip) + 1 (current letter) to `abbrLen`, verify match
- When we see a **digit**: Build the number, check for leading zeros
- At the end: `abbrLen + num` should equal `wordLen`

### Step-by-Step Example: `word = "internationalization"`, `abbr = "i12iz4n"`

```
Initial: abbrLen = 0, num = 0

i=0: 'i' (letter)
  abbrLen = 0 + 0 + 1 = 1
  num = 0
  Check: word[0] == 'i' ✓
  abbrLen = 1

i=1: '1' (digit)
  num = 0 * 10 + 1 = 1

i=2: '2' (digit)
  num = 1 * 10 + 2 = 12

i=3: 'i' (letter)
  abbrLen = 1 + 12 + 1 = 14
  num = 0
  Check: word[13] == 'i' ✓ (position 14 - 1 = 13)
  abbrLen = 14

i=4: 'z' (letter)
  abbrLen = 14 + 0 + 1 = 15
  num = 0
  Check: word[14] == 'z' ✓
  abbrLen = 15

i=5: '4' (digit)
  num = 0 * 10 + 4 = 4

i=6: 'n' (letter)
  abbrLen = 15 + 4 + 1 = 20
  num = 0
  Check: word[19] == 'n' ✓
  abbrLen = 20

Final: abbrLen + num = 20 + 0 = 20 == wordLen (20) ✓
```

**Visual Representation:**
```
word:  i n t e r n a t i o n a l i z a t i o n
       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

abbr:  i 12 i z 4 n
       │ │  │ │ │ │
       │ │  │ │ │ └─> pos 19: 'n' ✓
       │ │  │ │ └───> skip 4: pos 15→19
       │ │  │ └─────> pos 14: 'z' ✓
       │ │  └───────> pos 13: 'i' ✓
       │ └───────────> skip 12: pos 1→13
       └─────────────> pos 0: 'i' ✓
```

## Key Insights

1. **Position tracking**: Track where we are in the word (`abbrLen`)
2. **Number accumulation**: Build multi-digit numbers digit by digit
3. **Leading zero check**: Reject if digit is '0' when `num == 0`
4. **Final validation**: Ensure total length matches word length
5. **Bounds checking**: Verify we don't exceed word length

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

## Edge Cases

1. **Leading zeros**: `"s010n"` → invalid (leading zero)
2. **Exact match**: `"word"` and `"4"` → valid (skip all 4 characters)
3. **No skips**: `"word"` and `"word"` → valid (all letters)
4. **Overflow**: `"word"` and `"w5d"` → invalid (skip 5 but only 3 chars remain)
5. **Underflow**: `"word"` and `"w2d"` → invalid (skip 2, but 'd' doesn't match position)
6. **Empty abbreviation**: Not possible per constraints

## Alternative Approaches

### Approach 2: Two-Pointer Method

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```cpp
class Solution {
public:
    bool validWordAbbreviation(string word, string abbr) {
        int i = 0, j = 0;  // i for word, j for abbr
        
        while(i < word.length() && j < abbr.length()) {
            if(abbr[j] >= 'a' && abbr[j] <= 'z') {
                // Letter: must match
                if(word[i] != abbr[j]) {
                    return false;
                }
                i++;
                j++;
            } else {
                // Digit: parse number and skip
                if(abbr[j] == '0') {
                    return false;  // Leading zero
                }
                
                int num = 0;
                while(j < abbr.length() && isdigit(abbr[j])) {
                    num = num * 10 + (abbr[j] - '0');
                    j++;
                }
                
                i += num;  // Skip num characters in word
            }
        }
        
        return i == word.length() && j == abbr.length();
    }
};
```

**Pros:**
- More intuitive: two pointers for word and abbreviation
- Easier to understand flow

**Cons:**
- Slightly more verbose
- Same complexity as single-pass approach

## Complexity Analysis

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

- [411. Minimum Unique Word Abbreviation](https://leetcode.com/problems/minimum-unique-word-abbreviation/) - Generate valid abbreviations
- [320. Generalized Abbreviation](https://leetcode.com/problems/generalized-abbreviation/) - Generate all abbreviations
- [422. Valid Word Square](https://leetcode.com/problems/valid-word-square/) - Similar validation problem
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

---

*This problem demonstrates how to parse and validate string abbreviations by tracking position and handling both letters and numbers correctly.*

