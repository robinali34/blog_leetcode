---
layout: post
title: "1868. Product of Two Run-Length Encoded Arrays"
date: 2025-10-20 13:30:00 -0700
categories: leetcode algorithm medium run-length-encoding two-pointers array-processing
permalink: /2025/10/20/medium-1868-product-of-two-run-length-encoded-arrays/
---

# 1868. Product of Two Run-Length Encoded Arrays

**Difficulty:** Medium  
**Category:** Run-Length Encoding, Two Pointers, Array Processing

## Problem Statement

Run-length encoding is a compression algorithm that allows for an integer array `nums` with many segments of repeated numbers to be represented by a (generally smaller) 2D array `encoded`. Each `encoded[i] = [vali, freqi]` describes the `ith` segment of repeated numbers in `nums` where `vali` is the value that is repeated `freqi` times.

For example, `nums = [1,1,1,2,2,2,2,2]` is represented by the run-length encoded array `encoded = [[1,3],[2,5]]`. Another way to read this is "three 1's followed by five 2's".

The **product** of two run-length encoded arrays `encoded1` and `encoded2` is a run-length encoded array that represents the product of `nums1` and `nums2`.

Given two run-length encoded arrays `encoded1` and `encoded2`, both of length `n`, return the **product** of `encoded1` and `encoded2`.

**Note:** Compression does not affect the product, and you can assume that the product of `nums1` and `nums2` does not exceed `10^9`.

## Examples

### Example 1:
```
Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,6]]
Explanation: encoded1 represents [1,1,1,2,2,2] and encoded2 represents [6,6,6,3,3,3].
The product is [6,6,6,6,6,6], which is represented by [[6,6]].
```

### Example 2:
```
Input: encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]
Output: [[2,3],[6,1],[9,2]]
Explanation: encoded1 represents [1,1,1,2,3,3] and encoded2 represents [2,2,2,3,3,3].
The product is [2,2,2,6,9,9], which is represented by [[2,3],[6,1],[9,2]].
```

## Constraints

- `2 <= encoded1.length, encoded2.length <= 10^5`
- `encoded1[i].length == encoded2[j].length == 2`
- `1 <= vali, freqi <= 10^4`

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Run-length encoding**: What is run-length encoding? (Assumption: [value, frequency] pairs - value appears frequency times consecutively)

2. **Product calculation**: How is product calculated? (Assumption: Element-wise product - multiply corresponding elements from decoded arrays)

3. **Array length**: Are arrays guaranteed to have same length? (Assumption: Yes - after decoding, both arrays have same length)

4. **Return format**: What should we return? (Assumption: Run-length encoded result - array of [value, frequency] pairs)

5. **Encoding optimization**: Should we optimize the encoding? (Assumption: Yes - combine consecutive same values in result)

## Approach

The key insight is to process both encoded arrays simultaneously using two pointers, computing the product of corresponding elements and merging consecutive segments with the same value.

### Algorithm:
1. Use two pointers `i` and `j` to traverse both encoded arrays
2. At each step, take the minimum frequency between the current segments
3. Compute the product of the values and the minimum frequency
4. If the result array is not empty and the last segment has the same value, merge frequencies
5. Otherwise, add a new segment
6. Decrease frequencies and advance pointers when segments are exhausted

## Solution

```cpp
class Solution {
public:
    vector<vector<int>> findRLEArray(vector<vector<int>>& encoded1, vector<vector<int>>& encoded2) {
        int i = 0, j = 0;
        vector<vector<int>> rtn;
        while(i < (int)encoded1.size() && j < (int)encoded2.size()) {
            int freq = min(encoded1[i][1], encoded2[j][1]);
            int val = encoded1[i][0] * encoded2[j][0];
            encoded1[i][1] -= freq;
            encoded2[j][1] -= freq;
            if(!rtn.empty() && rtn.back()[0] == val) {
                rtn.back()[1] += freq;
            } else {
                rtn.push_back({val, freq});
            }
            if(encoded1[i][1] == 0) i++;
            if(encoded2[j][1] == 0) j++;
        }
        return rtn;
    }
};
```

## Explanation

### Step-by-Step Process:

1. **Initialize pointers:** `i = 0, j = 0` to track positions in both arrays
2. **Process segments:** While both arrays have unprocessed segments:
   - Take minimum frequency: `freq = min(encoded1[i][1], encoded2[j][1])`
   - Compute product: `val = encoded1[i][0] * encoded2[j][0]`
   - Decrease frequencies: Subtract `freq` from both current segments
3. **Merge or add segment:**
   - If result is empty or last segment has different value: add new segment
   - If last segment has same value: merge frequencies
4. **Advance pointers:** Move to next segment when current frequency reaches 0

### Example Walkthrough:
For `encoded1 = [[1,3],[2,3]]` and `encoded2 = [[6,3],[3,3]]`:

- **Step 1:** `min(3,3) = 3`, `val = 1*6 = 6`, add `[6,3]`
- **Step 2:** `min(3,3) = 3`, `val = 2*3 = 6`, merge with previous: `[6,6]`
- **Result:** `[[6,6]]`

## Complexity Analysis

**Time Complexity:** O(n + m) where n and m are the lengths of the encoded arrays
- Each segment is processed exactly once
- Merging operations are O(1)

**Space Complexity:** O(n + m) for the result array
- In worst case, no segments can be merged

## Key Insights

1. **Two-pointer technique:** Efficiently process both arrays simultaneously
2. **Frequency management:** Always consume the minimum frequency to avoid gaps
3. **Segment merging:** Combine consecutive segments with same values to maintain compression
4. **In-place modification:** Modify input arrays to track remaining frequencies

This approach efficiently computes the product while maintaining the run-length encoded format and optimal compression.
