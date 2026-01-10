---
layout: post
title: "LeetCode Templates: String Processing"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates string
permalink: /posts/2025-11-24-leetcode-templates-string-processing/
tags: [leetcode, templates, string, algorithms]
---

{% raw %}
## Contents

- [Sliding Window](#sliding-window)
- [Two Pointers](#two-pointers)
- [String Matching](#string-matching)
- [String Manipulation](#string-manipulation)
- [Parsing](#parsing)

## Sliding Window

### Longest Substring Without Repeating Characters

```cpp
int lengthOfLongestSubstring(string s) {
    vector<int> cnt(256, 0);
    int dup = 0, best = 0;
    
    for (int l = 0, r = 0; r < s.size(); ++r) {
        dup += (++cnt[(unsigned char)s[r]] == 2);
        
        while (dup > 0) {
            dup -= (--cnt[(unsigned char)s[l++]] == 1);
        }
        
        best = max(best, r - l + 1);
    }
    
    return best;
}
```

### Minimum Window Substring

```cpp
string minWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;
    
    int left = 0, right = 0;
    int valid = 0;
    int start = 0, len = INT_MAX;
    
    while (right < s.size()) {
        char c = s[right++];
        if (need.count(c)) {
            window[c]++;
            if (window[c] == need[c]) valid++;
        }
        
        while (valid == need.size()) {
            if (right - left < len) {
                start = left;
                len = right - left;
            }
            
            char d = s[left++];
            if (need.count(d)) {
                if (window[d] == need[d]) valid--;
                window[d]--;
            }
        }
    }
    
    return len == INT_MAX ? "" : s.substr(start, len);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 3 | Longest Substring Without Repeating Characters | [Link](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/10/medium-3-longest-substring-without-repeating-characters/) |
| 76 | Minimum Window Substring | [Link](https://leetcode.com/problems/minimum-window-substring/) | - |
| 424 | Longest Repeating Character Replacement | [Link](https://leetcode.com/problems/longest-repeating-character-replacement/) | - |

## Two Pointers

### Valid Palindrome

```cpp
bool isPalindrome(string s) {
    int left = 0, right = s.size() - 1;
    
    while (left < right) {
        while (left < right && !isalnum(s[left])) left++;
        while (left < right && !isalnum(s[right])) right--;
        
        if (tolower(s[left]) != tolower(s[right])) {
            return false;
        }
        left++;
        right--;
    }
    
    return true;
}
```

### Reverse String

```cpp
void reverseString(vector<char>& s) {
    int left = 0, right = s.size() - 1;
    while (left < right) {
        swap(s[left++], s[right--]);
    }
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/) |
| 125 | Valid Palindrome | [Link](https://leetcode.com/problems/valid-palindrome/) | - |
| 344 | Reverse String | [Link](https://leetcode.com/problems/reverse-string/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-29-easy-344-reverse-string/) |
| 647 | Palindromic Substrings | [Link](https://leetcode.com/problems/palindromic-substrings/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-647-palindromic-substrings/) |

## String Matching

### KMP Algorithm

```cpp
vector<int> buildKMP(string pattern) {
    int m = pattern.size();
    vector<int> lps(m, 0);
    int len = 0, i = 1;
    
    while (i < m) {
        if (pattern[i] == pattern[len]) {
            lps[i++] = ++len;
        } else {
            if (len != 0) {
                len = lps[len - 1];
            } else {
                lps[i++] = 0;
            }
        }
    }
    
    return lps;
}

int kmpSearch(string text, string pattern) {
    int n = text.size(), m = pattern.size();
    vector<int> lps = buildKMP(pattern);
    int i = 0, j = 0;
    
    while (i < n) {
        if (text[i] == pattern[j]) {
            i++;
            j++;
        }
        
        if (j == m) {
            return i - j; // Found at index i - j
        } else if (i < n && text[i] != pattern[j]) {
            if (j != 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }
    
    return -1;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 28 | Find the Index of the First Occurrence in a String | [Link](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/) | - |

## String Manipulation

### Group Anagrams

```cpp
vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    
    for (string& str : strs) {
        string key = str;
        sort(key.begin(), key.end());
        groups[key].push_back(str);
    }
    
    vector<vector<string>> result;
    for (auto& [key, values] : groups) {
        result.push_back(values);
    }
    
    return result;
}
```

### Remove Duplicates

```cpp
// Remove All Adjacent Duplicates
string removeDuplicates(string s) {
    string result;
    for (char c : s) {
        if (!result.empty() && result.back() == c) {
            result.pop_back();
        } else {
            result.push_back(c);
        }
    }
    return result;
}

// Remove All Adjacent Duplicates II (k duplicates)
string removeDuplicates(string s, int k) {
    vector<pair<char, int>> st;
    
    for (char c : s) {
        if (!st.empty() && st.back().first == c) {
            st.back().second++;
            if (st.back().second == k) {
                st.pop_back();
            }
        } else {
            st.push_back({c, 1});
        }
    }
    
    string result;
    for (auto& [c, count] : st) {
        result.append(count, c);
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 49 | Group Anagrams | [Link](https://leetcode.com/problems/group-anagrams/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-49-group-anagrams/) |
| 1047 | Remove All Adjacent Duplicates In String | [Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-1047-remove-all-adjacent-duplicates-in-string/) |
| 1209 | Remove All Adjacent Duplicates in String II | [Link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-1209-remove-all-adjacent-duplicates-in-string-ii/) |

## Parsing

### Valid Word Abbreviation

```cpp
bool validWordAbbreviation(string word, string abbr) {
    int i = 0, j = 0;
    int n = word.size(), m = abbr.size();
    
    while (i < n && j < m) {
        if (isdigit(abbr[j])) {
            if (abbr[j] == '0') return false; // Leading zero
            int num = 0;
            while (j < m && isdigit(abbr[j])) {
                num = num * 10 + (abbr[j] - '0');
                j++;
            }
            i += num;
        } else {
            if (word[i] != abbr[j]) return false;
            i++;
            j++;
        }
    }
    
    return i == n && j == m;
}
```

### Decode String

```cpp
string decodeString(string s) {
    stack<int> numStack;
    stack<string> strStack;
    string current;
    int num = 0;
    
    for (char c : s) {
        if (isdigit(c)) {
            num = num * 10 + (c - '0');
        } else if (c == '[') {
            numStack.push(num);
            strStack.push(current);
            num = 0;
            current = "";
        } else if (c == ']') {
            int repeat = numStack.top();
            numStack.pop();
            string temp = current;
            current = strStack.top();
            strStack.pop();
            while (repeat--) {
                current += temp;
            }
        } else {
            current += c;
        }
    }
    
    return current;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 408 | Valid Word Abbreviation | [Link](https://leetcode.com/problems/valid-word-abbreviation/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-easy-408-valid-word-abbreviation/) |
| 394 | Decode String | [Link](https://leetcode.com/problems/decode-string/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/19/medium-394-decode-string/) |
{% endraw %}

