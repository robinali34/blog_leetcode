---
layout: post
title: "[Medium] 33. Search in Rotated Sorted Array"
date: 2025-09-23 10:00:00 -0000
categories: leetcode algorithm C++
---

# 📚 C++ STL Quick Reference for LeetCode

---

## 🧰 Containers

### ✅ Strings

```cpp
s.length();         // Length of the string
s.size();           // Same as length()
s.empty();          // Checks if string is empty
s[i];               // Access character at index
s.substr(pos, len); // Substring
s.find("abc");      // Find position of substring
s.erase(pos, len);  // Erase part of string
s.insert(pos, str); // Insert str at pos
s += "abc";         // Append
to_string(x);       // Convert int to string
stoi(s);            // Convert string to int
```

---

### ✅ Vectors (`std::vector`)

```cpp
v.size();
v.empty();
v.push_back(x);
v.pop_back();
v[i];
v.front();
v.back();
v.clear();
v.insert(it, x);
v.erase(it);
sort(v.begin(), v.end());
reverse(v.begin(), v.end());
```

---

### ✅ Arrays

```cpp
int arr[100]; // C-style
std::array<int, 5> a = {1, 2, 3, 4, 5};
```

---

### ✅ Sets / Multisets

```cpp
set<int> s;
s.insert(x);
s.erase(x);
s.find(x);
s.count(x);          // 0 or 1 (set), >1 for multiset
s.lower_bound(x);    // >= x
s.upper_bound(x);    // > x
```

---

### ✅ Maps / Unordered Maps

```cpp
map<int, int> m;
unordered_map<int, int> um;

m[key] = val;
m.count(key);
m.find(key);
for (auto& [k, v] : m) {
    // structured binding (C++17)
}
```

---

## 🔄 Algorithms (`<algorithm>`)

### ✅ Sorting & Searching

```cpp
sort(v.begin(), v.end());
sort(v.rbegin(), v.rend());
reverse(v.begin(), v.end());
binary_search(v.begin(), v.end(), x);
lower_bound(v.begin(), v.end(), x);
upper_bound(v.begin(), v.end(), x);
```

---

### ✅ Min / Max / Others

```cpp
min(a, b);
max(a, b);
swap(a, b);
accumulate(v.begin(), v.end(), 0); // Sum
count(v.begin(), v.end(), x);
next_permutation(v.begin(), v.end());
prev_permutation(v.begin(), v.end());
unique(v.begin(), v.end()); // Remove dupes (after sort)
rotate(v.begin(), v.begin() + k, v.end());
```

---

## 📐 Math Utilities (`<cmath>`, `<numeric>`)

```cpp
abs(x);
pow(a, b);
sqrt(x);
gcd(a, b);   // C++17
lcm(a, b);   // C++17
```

---

## 🧵 Queues, Stacks, Deques

### ✅ Queue

```cpp
queue<int> q;
q.push(x);
q.pop();
q.front();
q.back();
q.empty();
```

### ✅ Stack

```cpp
stack<int> s;
s.push(x);
s.pop();
s.top();
s.empty();
```

### ✅ Deque

```cpp
deque<int> dq;
dq.push_front(x);
dq.push_back(x);
dq.pop_front();
dq.pop_back();
```

### ✅ Priority Queue (Heap)

```cpp
priority_queue<int> maxHeap;
priority_queue<int, vector<int>, greater<int>> minHeap;
```

---

## 🧠 Bit Manipulation

```cpp
__builtin_popcount(x);  // Count 1-bits
__builtin_clz(x);       // Leading zeros
__builtin_ctz(x);       // Trailing zeros
x & (x - 1);            // Remove lowest 1-bit
x & -x;                 // Isolate lowest 1-bit
```

---

## 📌 Common LeetCode Structures

| Concept       | STL Equivalent              |
|--------------|------------------------------|
| Hash Map     | `unordered_map<K, V>`         |
| Hash Set     | `unordered_set<T>`            |
| Tree Map     | `map<K, V>`                   |
| Tree Set     | `set<T>`                      |
| Min Heap     | `priority_queue<T, vector<T>, greater<T>>` |
| Max Heap     | `priority_queue<T>`           |
| Stack        | `stack<T>`                    |
| Queue        | `queue<T>`                    |
| Deque        | `deque<T>`                    |
| StringBuilder| `ostringstream` or `+=`       |
| Graph        | `vector<vector<int>>`         |

---

## ✍️ Input/Output Tips

```cpp
cin >> n;
getline(cin, s);      // Full line
stoi(s);              // String to int

// Fast IO
ios::sync_with_stdio(false);
cin.tie(0);
```

---
