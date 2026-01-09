---
layout: post
title: "692. Top K Frequent Words"
date: 2026-01-08 00:00:00 -0700
categories: [leetcode, medium, hash-table, heap, sorting, string]
permalink: /2026/01/08/medium-692-top-k-frequent-words/
tags: [leetcode, medium, hash-table, heap, sorting, string, priority-queue]
---

# 692. Top K Frequent Words

## Problem Statement

Given an array of strings `words` and an integer `k`, return *the* `k` *most frequent strings*.

Return the answer **sorted by the frequency** from highest to lowest. Sort the words with the same frequency by their **lexicographical order**.

## Examples

**Example 1:**
```
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.
```

**Example 2:**
```
Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 2
Output: ["the","is"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.
```

## Constraints

- `1 <= words.length <= 500`
- `1 <= words[i].length <= 10`
- `words[i]` consists of lowercase English letters.
- `k` is in the range `[1, The number of unique words[i]]`

## Solution Approach

This problem is similar to [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/), but with two key differences:
1. **Strings instead of integers**: Need to handle string comparison
2. **Lexicographic ordering**: When frequencies are equal, sort alphabetically

### Key Insights:

1. **Frequency Counting**: Use hash map to count word frequencies
2. **Custom Sorting**: Sort by frequency (descending), then by lexicographic order (ascending)
3. **Top K Selection**: Return only the first k elements after sorting

### Algorithm:

1. **Count frequencies**: Use `unordered_map` to count occurrences of each word
2. **Collect unique words**: Extract all unique words from the map
3. **Sort**: Sort by frequency (descending), then lexicographically (ascending)
4. **Return top k**: Take first k elements

## Solution

### **Solution: Hash Map + Custom Sorting**

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for(auto& word: words) {
            cnt[word]++;
        }
        vector<string> rtn;
        for(auto& [key, value]: cnt) {
            rtn.emplace_back(key);
        }
        sort(rtn.begin(), rtn.end(), [&](const string& a, const string& b){
            return cnt[a] == cnt[b]? a < b : cnt[a] > cnt[b];
        });
        rtn.erase(rtn.begin() + k, rtn.end());
        return rtn;
    }
};
```

### **Algorithm Explanation:**

1. **Count Frequencies (Lines 3-6)**:
   - Create `unordered_map<string, int>` to count word occurrences
   - Iterate through all words and increment their counts

2. **Collect Unique Words (Lines 7-10)**:
   - Extract all unique words (keys) from the frequency map
   - Store them in result vector `rtn`

3. **Custom Sort (Lines 11-13)**:
   - **Primary sort**: By frequency (descending) - `cnt[a] > cnt[b]`
   - **Secondary sort**: By lexicographic order (ascending) - `a < b` when frequencies are equal
   - Uses lambda with capture-by-reference `[&]` to access `cnt` map

4. **Return Top K (Lines 14-15)**:
   - Erase elements after index `k` to keep only top k
   - Return the result

### **Why This Works:**

- **Hash map counting**: Efficiently counts frequencies in O(n) time
- **Custom comparator**: Handles both frequency and lexicographic ordering
- **Sorting approach**: Simple and straightforward for small input sizes

### **Example Walkthrough:**

**For `words = ["i","love","leetcode","i","love","coding"], k = 2`:**

```
Step 1: Count frequencies
cnt = {
    "i": 2,
    "love": 2,
    "leetcode": 1,
    "coding": 1
}

Step 2: Collect unique words
rtn = ["i", "love", "leetcode", "coding"]

Step 3: Sort with custom comparator
Compare pairs:
  - "i" vs "love": cnt["i"] == cnt["love"] (both 2) → "i" < "love" → "i" comes first
  - "leetcode" vs "coding": cnt["leetcode"] == cnt["coding"] (both 1) → "coding" < "leetcode" → "coding" comes first
  - "i"/"love" vs "leetcode"/"coding": cnt["i"] > cnt["leetcode"] → higher frequency comes first

After sorting:
rtn = ["i", "love", "coding", "leetcode"]

Step 4: Take top k = 2
rtn = ["i", "love"]

Result: ["i", "love"]
```

### **Complexity Analysis:**

- **Time Complexity:** O(n + m log m) where n is total words, m is unique words
  - O(n) for frequency counting
  - O(m) for collecting unique words
  - O(m log m) for sorting m unique words
  - O(k) for erasing (can be optimized to O(1) by using resize)
- **Space Complexity:** O(m) where m is number of unique words
  - O(m) for frequency map
  - O(m) for result vector

### **Optimization Note:**

Instead of `erase`, we could use `resize(k)` which is more efficient:
```cpp
rtn.resize(k);
return rtn;
```

## Alternative Approaches

### **Approach 2: Min Heap (Better for Large k)**

For cases where k is much smaller than the number of unique words, a min heap approach would be more efficient:

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for(auto& word: words) {
            cnt[word]++;
        }
        
        auto cmp = [&](const string& a, const string& b) {
            return cnt[a] == cnt[b] ? a > b : cnt[a] < cnt[b];
        };
        
        priority_queue<string, vector<string>, decltype(cmp)> pq(cmp);
        for(auto& [word, freq]: cnt) {
            pq.push(word);
            if(pq.size() > k) pq.pop();
        }
        
        vector<string> rtn;
        while(!pq.empty()) {
            rtn.push_back(pq.top());
            pq.pop();
        }
        reverse(rtn.begin(), rtn.end());
        return rtn;
    }
};
```

**Time Complexity:** O(n + m log k) where m is unique words  
**Space Complexity:** O(m + k)

### **Approach 3: Bucket Sort**

Similar to LC 347, but requires additional sorting within each bucket:

```cpp
class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> cnt;
        for(auto& word: words) {
            cnt[word]++;
        }
        
        int maxFreq = 0;
        for(auto& [word, freq]: cnt) {
            maxFreq = max(maxFreq, freq);
        }
        
        vector<vector<string>> buckets(maxFreq + 1);
        for(auto& [word, freq]: cnt) {
            buckets[freq].push_back(word);
        }
        
        vector<string> rtn;
        for(int i = maxFreq; i >= 1 && rtn.size() < k; i--) {
            sort(buckets[i].begin(), buckets[i].end());
            for(auto& word: buckets[i]) {
                rtn.push_back(word);
                if(rtn.size() == k) break;
            }
        }
        return rtn;
    }
};
```

**Time Complexity:** O(n + m log m) in worst case  
**Space Complexity:** O(m)

## Key Insights

1. **Custom Comparator**: The key is the two-level sorting: frequency first, then lexicographic order
2. **Hash Map Efficiency**: `unordered_map` provides O(1) average case for frequency counting
3. **Sorting Trade-off**: Simple sorting works well for small inputs; heap is better for large k
4. **Lexicographic Order**: When frequencies are equal, use standard string comparison (`<`)

## Edge Cases

1. **All words have same frequency**: Sort purely by lexicographic order
2. **k equals number of unique words**: Return all words sorted
3. **Single word repeated**: Return that word
4. **Different frequencies, same lexicographic prefix**: Frequency takes priority

## Related Problems

- [LC 347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) - Similar problem with integers
- [LC 215: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) - Kth largest element
- [LC 451: Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) - Sort by frequency
- [LC 973: K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) - Top K with custom ordering

---

*This problem demonstrates the importance of custom comparators for multi-criteria sorting, combining frequency-based and lexicographic ordering.*

