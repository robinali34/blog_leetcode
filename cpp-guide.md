---
layout: page
title: C++ Guide
permalink: /cpp-guide/
---

# C++ Guide: From Basics to LeetCode-Ready

A practical reference for learning C++ with a focus on competitive programming and technical interviews. Whether you're picking up C++ for the first time or brushing up before a contest, this page covers what matters.

> **New to LeetCode?** Start with the [Beginner's Guide](/blog_leetcode/2026/06/25/leetcode-beginners-guide/) to understand the platform, difficulty levels, and which problems to solve first.

<svg viewBox="0 0 740 200" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="guide-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#8B8680"/>
    </marker>
  </defs>

  <text x="370" y="22" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">How This Guide Is Organized</text>

  <!-- Part boxes - top row -->
  <rect x="10" y="38" width="120" height="52" rx="8" fill="#E8D5D0" stroke="#C08070" stroke-width="1.8"/>
  <text x="70" y="60" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Part 1</text>
  <text x="70" y="78" font-size="9" fill="#7A7772" text-anchor="middle">Language Basics</text>

  <rect x="145" y="38" width="120" height="52" rx="8" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.8"/>
  <text x="205" y="60" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Part 2</text>
  <text x="205" y="78" font-size="9" fill="#7A7772" text-anchor="middle">STL Toolkit</text>

  <rect x="280" y="38" width="120" height="52" rx="8" fill="#D4D8E0" stroke="#7080A0" stroke-width="1.8"/>
  <text x="340" y="60" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Part 3</text>
  <text x="340" y="78" font-size="9" fill="#7A7772" text-anchor="middle">Patterns</text>

  <rect x="415" y="38" width="120" height="52" rx="8" fill="#E8E3D8" stroke="#B8A880" stroke-width="1.8"/>
  <text x="475" y="60" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Part 4</text>
  <text x="475" y="78" font-size="9" fill="#7A7772" text-anchor="middle">Solution Template</text>

  <!-- Arrows top row -->
  <line x1="130" y1="64" x2="143" y2="64" stroke="#8B8680" stroke-width="1.5" marker-end="url(#guide-arr)"/>
  <line x1="265" y1="64" x2="278" y2="64" stroke="#8B8680" stroke-width="1.5" marker-end="url(#guide-arr)"/>
  <line x1="400" y1="64" x2="413" y2="64" stroke="#8B8680" stroke-width="1.5" marker-end="url(#guide-arr)"/>

  <!-- Part boxes - bottom row -->
  <rect x="145" y="115" width="150" height="52" rx="8" fill="#E8D5D0" stroke="#C08070" stroke-width="1.8"/>
  <text x="220" y="137" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Part 5</text>
  <text x="220" y="155" font-size="9" fill="#7A7772" text-anchor="middle">Learning Path (Roadmap)</text>

  <rect x="320" y="115" width="150" height="52" rx="8" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.8"/>
  <text x="395" y="137" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Part 6</text>
  <text x="395" y="155" font-size="9" fill="#7A7772" text-anchor="middle">Modern C++ (20/23)</text>

  <rect x="495" y="115" width="150" height="52" rx="8" fill="#D4D8E0" stroke="#7080A0" stroke-width="1.8"/>
  <text x="570" y="137" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Quick Ref</text>
  <text x="570" y="155" font-size="9" fill="#7A7772" text-anchor="middle">Cheat Sheet</text>

  <!-- Vertical connections -->
  <line x1="205" y1="90" x2="220" y2="113" stroke="#8B8680" stroke-width="1.2" stroke-dasharray="4"/>
  <line x1="340" y1="90" x2="395" y2="113" stroke="#8B8680" stroke-width="1.2" stroke-dasharray="4"/>
  <line x1="475" y1="90" x2="570" y2="113" stroke="#8B8680" stroke-width="1.2" stroke-dasharray="4"/>

  <!-- Legend -->
  <text x="370" y="192" font-size="10" fill="#9A9792" text-anchor="middle">Top row: learn in order → Bottom row: reference anytime</text>
</svg>

---

## Why C++ for Algorithms?

<svg viewBox="0 0 740 180" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Central node -->
  <rect x="275" y="10" width="190" height="44" rx="22" fill="#D4D8E0" stroke="#7080A0" stroke-width="2"/>
  <text x="370" y="37" font-size="14" fill="#3A3530" font-weight="700" text-anchor="middle">C++ for Algorithms</text>

  <!-- Branches -->
  <line x1="275" y1="32" x2="145" y2="80" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="325" y1="54" x2="295" y2="80" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="415" y1="54" x2="445" y2="80" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="465" y1="32" x2="595" y2="80" stroke="#B8B5B0" stroke-width="1.5"/>

  <!-- Speed -->
  <rect x="40" y="78" width="150" height="40" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="115" y="97" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Fastest Runtime</text>
  <text x="115" y="112" font-size="9" fill="#9A9792" text-anchor="middle">compiled to native code</text>

  <!-- STL -->
  <rect x="220" y="78" width="150" height="40" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="295" y="97" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Rich STL</text>
  <text x="295" y="112" font-size="9" fill="#9A9792" text-anchor="middle">containers + algorithms</text>

  <!-- Control -->
  <rect x="400" y="78" width="150" height="40" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="475" y="97" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Fine Control</text>
  <text x="475" y="112" font-size="9" fill="#9A9792" text-anchor="middle">pointers, bits, memory</text>

  <!-- Platform standard -->
  <rect x="560" y="78" width="150" height="40" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="635" y="97" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Industry Standard</text>
  <text x="635" y="112" font-size="9" fill="#9A9792" text-anchor="middle">ICPC, CF, LC, interviews</text>

  <!-- Bottom bar -->
  <rect x="80" y="140" width="580" height="28" rx="14" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="370" y="159" font-size="11" fill="#5A5752" font-weight="600" text-anchor="middle">Result: Write less code → Run faster → Solve harder problems</text>
</svg>

| Advantage | Details |
|---|---|
| **Speed** | Compiled to native code -- fastest runtime of any mainstream language |
| **STL** | The Standard Template Library provides battle-tested containers and algorithms |
| **Industry standard for CP** | Codeforces, ICPC, AtCoder, and LeetCode all favor C++ |
| **Fine-grained control** | Pointers, memory layout, and bit manipulation are first-class citizens |
| **Interview-friendly** | Many interviewers are comfortable reading C++ |

---

## Part 1: Language Essentials

### Hello World and Compilation

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

Compile and run:

```bash
g++ -std=c++17 -O2 -o solution solution.cpp
./solution
```

| Flag | Purpose |
|---|---|
| `-std=c++17` | Use C++17 standard (recommended minimum) |
| `-O2` | Optimization level (matches online judges) |
| `-Wall -Wextra` | Enable all warnings -- catch bugs early |
| `-fsanitize=address,undefined` | Debug mode: catch memory errors and UB |

### Fundamental Types

```cpp
int x = 42;              // 32-bit, range: ~±2×10⁹
long long y = 1e18;      // 64-bit, range: ~±9.2×10¹⁸
double pi = 3.14159;     // 64-bit floating point
char c = 'A';            // single character
bool flag = true;        // true or false
string s = "hello";      // dynamic string (from <string>)
```

**Common pitfall:** `int` overflow. When `n` can reach $10^5$ and you multiply two values, use `long long`:

```cpp
long long area = (long long)width * height;
```

### Control Flow

```cpp
// if-else
if (x > 0) {
    // positive
} else if (x < 0) {
    // negative
} else {
    // zero
}

// for loop
for (int i = 0; i < n; ++i) {
    // 0 to n-1
}

// range-based for
for (int val : arr) {
    // read-only iteration
}
for (int& val : arr) {
    // modify in place
}

// while
while (condition) { /* ... */ }
```

### Functions

```cpp
// Pass by value (copy)
int add(int a, int b) {
    return a + b;
}

// Pass by reference (no copy, can modify)
void doubleIt(int& x) {
    x *= 2;
}

// Pass by const reference (no copy, read-only -- best for large objects)
int sumVector(const vector<int>& v) {
    int total = 0;
    for (int x : v) total += x;
    return total;
}
```

### Pointers and References

```cpp
int x = 10;
int* ptr = &x;     // pointer: holds address of x
int& ref = x;      // reference: alias for x

*ptr = 20;         // dereference: x is now 20
ref = 30;          // x is now 30

// Null pointer
int* p = nullptr;
if (p != nullptr) { /* safe to dereference */ }
```

For LeetCode, you'll encounter pointers mainly in **linked list** and **tree** problems:

```cpp
struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};
```

---

## Part 2: The STL — Your Competitive Programming Toolkit

### Which Container Should I Use?

Most beginners waste time picking the wrong container. This flowchart settles it:

<svg viewBox="0 0 780 440" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="stl-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#8B8680"/>
    </marker>
  </defs>

  <!-- Start -->
  <rect x="260" y="10" width="260" height="38" rx="19" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="390" y="34" font-size="13" fill="#3A3530" font-weight="600" text-anchor="middle">What do you need?</text>

  <!-- Branch lines -->
  <line x1="310" y1="48" x2="120" y2="88" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#stl-arr)"/>
  <line x1="390" y1="48" x2="390" y2="88" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#stl-arr)"/>
  <line x1="470" y1="48" x2="660" y2="88" stroke="#B8B5B0" stroke-width="1.3" marker-end="url(#stl-arr)"/>

  <!-- Labels -->
  <text x="200" y="66" font-size="10" fill="#9A9792" font-style="italic">ordered sequence</text>
  <text x="385" y="76" font-size="10" fill="#9A9792" font-style="italic">key → value</text>
  <text x="565" y="66" font-size="10" fill="#9A9792" font-style="italic">sorted / priority</text>

  <!-- Sequence containers -->
  <rect x="30" y="92" width="180" height="34" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="120" y="114" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">Sequence Containers</text>

  <line x1="70" y1="126" x2="70" y2="158" stroke="#B8B5B0" stroke-width="1.2" marker-end="url(#stl-arr)"/>
  <line x1="170" y1="126" x2="170" y2="158" stroke="#B8B5B0" stroke-width="1.2" marker-end="url(#stl-arr)"/>
  <text x="55" y="146" font-size="9" fill="#9A9792">random access</text>
  <text x="175" y="146" font-size="9" fill="#9A9792">both ends</text>

  <rect x="20" y="162" width="100" height="30" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="70" y="182" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">vector</text>
  <text x="70" y="205" font-size="9" fill="#9A9792" text-anchor="middle">95% of the time</text>

  <rect x="140" y="162" width="100" height="30" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="190" y="182" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">deque</text>
  <text x="190" y="205" font-size="9" fill="#9A9792" text-anchor="middle">sliding window</text>

  <!-- Associative containers -->
  <rect x="300" y="92" width="180" height="34" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="390" y="114" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">Key-Value / Lookup</text>

  <line x1="350" y1="126" x2="330" y2="158" stroke="#B8B5B0" stroke-width="1.2" marker-end="url(#stl-arr)"/>
  <line x1="430" y1="126" x2="460" y2="158" stroke="#B8B5B0" stroke-width="1.2" marker-end="url(#stl-arr)"/>
  <text x="310" y="146" font-size="9" fill="#9A9792">need order?</text>
  <text x="465" y="146" font-size="9" fill="#9A9792">no</text>

  <rect x="275" y="162" width="110" height="30" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="330" y="182" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">map / set</text>
  <text x="330" y="205" font-size="9" fill="#9A9792" text-anchor="middle">O(log n), sorted</text>

  <rect x="405" y="162" width="140" height="30" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="475" y="182" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">unordered_map/set</text>
  <text x="475" y="205" font-size="9" fill="#9A9792" text-anchor="middle">O(1) avg, default</text>

  <!-- Priority containers -->
  <rect x="580" y="92" width="170" height="34" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="665" y="114" font-size="12" fill="#5A5752" font-weight="600" text-anchor="middle">Sorted / Priority</text>

  <line x1="625" y1="126" x2="610" y2="158" stroke="#B8B5B0" stroke-width="1.2" marker-end="url(#stl-arr)"/>
  <line x1="705" y1="126" x2="720" y2="158" stroke="#B8B5B0" stroke-width="1.2" marker-end="url(#stl-arr)"/>

  <rect x="560" y="162" width="110" height="30" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="615" y="182" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">priority_queue</text>
  <text x="615" y="205" font-size="9" fill="#9A9792" text-anchor="middle">top-K, Dijkstra</text>

  <rect x="685" y="162" width="80" height="30" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="725" y="182" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">multiset</text>
  <text x="725" y="205" font-size="9" fill="#9A9792" text-anchor="middle">sorted + dupes</text>

  <!-- Adaptor row -->
  <text x="390" y="240" font-size="12" fill="#7A7772" font-weight="600" text-anchor="middle">Adaptors (built on top of other containers)</text>
  <line x1="100" y1="248" x2="680" y2="248" stroke="#E0DDD8" stroke-width="1"/>

  <rect x="80" y="260" width="100" height="30" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="130" y="280" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">stack</text>
  <text x="130" y="300" font-size="9" fill="#9A9792" text-anchor="middle">LIFO, DFS</text>

  <rect x="210" y="260" width="100" height="30" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="260" y="280" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">queue</text>
  <text x="260" y="300" font-size="9" fill="#9A9792" text-anchor="middle">FIFO, BFS</text>

  <rect x="340" y="260" width="100" height="30" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.2"/>
  <text x="390" y="280" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">string</text>
  <text x="390" y="300" font-size="9" fill="#9A9792" text-anchor="middle">text, like vector</text>

  <!-- Quick decision box -->
  <rect x="50" y="330" width="680" height="100" rx="10" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.5"/>
  <text x="390" y="355" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Quick Decision Rule</text>
  <text x="70" y="378" font-size="11" fill="#5A5752">Need fast lookup by key?</text>
  <text x="420" y="378" font-size="11" fill="#8B8680">→ unordered_map</text>
  <text x="70" y="398" font-size="11" fill="#5A5752">Need sorted order or range queries?</text>
  <text x="420" y="398" font-size="11" fill="#8B8680">→ set / map</text>
  <text x="70" y="418" font-size="11" fill="#5A5752">Everything else?</text>
  <text x="420" y="418" font-size="11" fill="#8B8680">→ vector (seriously, just use vector)</text>
</svg>

### Containers at a Glance

| Container | Access | Insert/Delete | Use When |
|---|---|---|---|
| `vector<T>` | $O(1)$ index | $O(1)$ amortized push_back | Default choice for sequences |
| `string` | $O(1)$ index | $O(n)$ insert | Text manipulation |
| `deque<T>` | $O(1)$ front/back | $O(1)$ push/pop both ends | Sliding window, BFS |
| `stack<T>` | $O(1)$ top | $O(1)$ push/pop | DFS, expression parsing |
| `queue<T>` | $O(1)$ front | $O(1)$ push/pop | BFS |
| `priority_queue<T>` | $O(1)$ top | $O(\log n)$ push/pop | Top-K, Dijkstra |
| `set<T>` / `map<K,V>` | $O(\log n)$ | $O(\log n)$ | Sorted order needed |
| `unordered_set<T>` / `unordered_map<K,V>` | $O(1)$ avg | $O(1)$ avg | Fast lookup |

### vector — The Workhorse

```cpp
#include <vector>

vector<int> v = {1, 2, 3, 4, 5};

v.push_back(6);          // append: {1,2,3,4,5,6}
v.pop_back();             // remove last: {1,2,3,4,5}
v.size();                 // 5
v.empty();                // false
v[0];                     // 1 (no bounds check)
v.at(0);                  // 1 (throws if out of bounds)
v.front();                // 1
v.back();                 // 5

// 2D vector (m rows, n cols, initialized to 0)
vector<vector<int>> grid(m, vector<int>(n, 0));

// Sort
sort(v.begin(), v.end());                    // ascending
sort(v.begin(), v.end(), greater<int>());    // descending

// Reverse
reverse(v.begin(), v.end());

// Min/Max element
*min_element(v.begin(), v.end());
*max_element(v.begin(), v.end());

// Binary search (requires sorted vector)
bool found = binary_search(v.begin(), v.end(), target);
auto it = lower_bound(v.begin(), v.end(), target);  // first >= target
auto it = upper_bound(v.begin(), v.end(), target);  // first > target
```

### string — Essential Operations

```cpp
#include <string>

string s = "hello";
s += " world";              // concatenation
s.substr(0, 5);             // "hello"
s.find("world");            // 6 (index), or string::npos if not found
s.length();                 // 11 (same as s.size())

// Character checks
isalpha(c);  isdigit(c);  isalnum(c);
tolower(c);  toupper(c);

// String ↔ Number
int n = stoi("42");
string s = to_string(42);
```

### unordered_map — Fast Lookups

```cpp
#include <unordered_map>

unordered_map<string, int> freq;
freq["apple"] = 3;
freq["banana"]++;            // auto-initializes to 0, then increments

if (freq.count("apple")) {  // check existence
    cout << freq["apple"];
}

// Iterate
for (auto& [key, val] : freq) {
    cout << key << ": " << val << endl;
}
```

### priority_queue — Heaps

```cpp
#include <queue>

// Max-heap (default)
priority_queue<int> maxHeap;
maxHeap.push(3);
maxHeap.push(1);
maxHeap.push(4);
maxHeap.top();    // 4
maxHeap.pop();    // removes 4

// Min-heap
priority_queue<int, vector<int>, greater<int>> minHeap;
minHeap.push(3);
minHeap.push(1);
minHeap.top();    // 1

// Custom comparator (e.g., sort by second element)
auto cmp = [](pair<int,int>& a, pair<int,int>& b) {
    return a.second > b.second;
};
priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(cmp)> pq(cmp);
```

### set and map — Sorted Containers

```cpp
#include <set>
#include <map>

set<int> s = {3, 1, 4, 1, 5};  // {1, 3, 4, 5} — sorted, unique
s.insert(2);                     // {1, 2, 3, 4, 5}
s.erase(3);                      // {1, 2, 4, 5}
s.count(4);                      // 1 (exists)

auto it = s.lower_bound(3);     // iterator to first element >= 3

// multiset allows duplicates
multiset<int> ms = {1, 1, 2, 3};

// map: sorted by key
map<string, int> m;
m["zebra"] = 1;
m["apple"] = 2;
// iteration order: apple, zebra
```

---

## Part 3: Patterns You'll Use Every Day

These patterns appear in almost every LeetCode solution. Master them and you'll write cleaner code faster.

<svg viewBox="0 0 700 160" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Pattern boxes -->
  <rect x="10" y="10" width="130" height="50" rx="8" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="75" y="32" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Custom Sort</text>
  <text x="75" y="48" font-size="9" fill="#9A9792" text-anchor="middle">comparators, lambda</text>

  <rect x="155" y="10" width="130" height="50" rx="8" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="220" y="32" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Lambdas</text>
  <text x="220" y="48" font-size="9" fill="#9A9792" text-anchor="middle">inline functions</text>

  <rect x="300" y="10" width="130" height="50" rx="8" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="365" y="32" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">Struct Bindings</text>
  <text x="365" y="48" font-size="9" fill="#9A9792" text-anchor="middle">auto [k, v] = ...</text>

  <rect x="445" y="10" width="130" height="50" rx="8" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="510" y="32" font-size="11" fill="#5A5752" font-weight="700" text-anchor="middle">STL Algorithms</text>
  <text x="510" y="48" font-size="9" fill="#9A9792" text-anchor="middle">sort, accumulate, ...</text>

  <!-- Where they're used -->
  <rect x="30" y="80" width="630" height="70" rx="8" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.2"/>
  <text x="345" y="100" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">Where You'll Use Them</text>
  <text x="50" y="122" font-size="10" fill="#5A5752">Custom sort → interval problems, greedy, priority queues</text>
  <text x="50" y="138" font-size="10" fill="#5A5752">Lambdas → DFS closures, sort comparators, STL algorithms</text>
</svg>

### Sorting with Custom Comparators

```cpp
// Sort by absolute value
sort(v.begin(), v.end(), [](int a, int b) {
    return abs(a) < abs(b);
});

// Sort intervals by end time
sort(intervals.begin(), intervals.end(), [](auto& a, auto& b) {
    return a[1] < b[1];
});

// Sort a struct
struct Edge {
    int u, v, w;
};
sort(edges.begin(), edges.end(), [](Edge& a, Edge& b) {
    return a.w < b.w;
});
```

### Lambda Functions

```cpp
// Basic lambda
auto square = [](int x) { return x * x; };
cout << square(5); // 25

// Capture variables
int offset = 10;
auto add = [offset](int x) { return x + offset; };

// Capture by reference
auto increment = [&offset]() { offset++; };
```

### Structured Bindings (C++17)

```cpp
// Pair
auto [first, second] = make_pair(1, "hello");

// Map iteration
for (auto& [key, val] : myMap) {
    cout << key << " -> " << val << endl;
}

// BFS with coordinates
auto [row, col] = queue.front();
```

### Useful Standard Algorithms

```cpp
#include <algorithm>
#include <numeric>

// Accumulate (sum)
int total = accumulate(v.begin(), v.end(), 0);
long long total = accumulate(v.begin(), v.end(), 0LL);

// Count
int cnt = count(v.begin(), v.end(), target);

// Fill
fill(v.begin(), v.end(), 0);

// Unique (remove adjacent duplicates — sort first)
sort(v.begin(), v.end());
v.erase(unique(v.begin(), v.end()), v.end());

// next_permutation
sort(v.begin(), v.end());
do {
    // process permutation
} while (next_permutation(v.begin(), v.end()));

// Min/Max of multiple values
int best = min({a, b, c, d});
int worst = max({a, b, c});
```

---

## Part 4: LeetCode Solution Template

Every LeetCode solution follows the same skeleton. Here's how the pieces fit together:

<svg viewBox="0 0 700 190" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <!-- Solution class box -->
  <rect x="30" y="10" width="640" height="170" rx="12" fill="#FAF8F5" stroke="#D4D1CC" stroke-width="1.5"/>
  <text x="60" y="32" font-size="12" fill="#7A7772" font-weight="600">class Solution { ... };</text>

  <!-- Public method -->
  <rect x="60" y="46" width="270" height="50" rx="8" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.5"/>
  <text x="195" y="66" font-size="11" fill="#3A6B3A" font-weight="700" text-anchor="middle">Public Method</text>
  <text x="195" y="84" font-size="9" fill="#5A5752" text-anchor="middle">return type + function(params)</text>

  <!-- Private helpers -->
  <rect x="360" y="46" width="280" height="50" rx="8" fill="#D4D8E0" stroke="#7080A0" stroke-width="1.5"/>
  <text x="500" y="66" font-size="11" fill="#3A3530" font-weight="700" text-anchor="middle">Private Helpers</text>
  <text x="500" y="84" font-size="9" fill="#5A5752" text-anchor="middle">DFS, BFS, custom sort, etc.</text>

  <!-- Body: what goes inside -->
  <rect x="60" y="108" width="130" height="55" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="125" y="128" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Edge cases</text>
  <text x="125" y="148" font-size="9" fill="#9A9792" text-anchor="middle">if (!root) return</text>

  <rect x="210" y="108" width="130" height="55" rx="6" fill="#D4D8D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="275" y="128" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Data structures</text>
  <text x="275" y="148" font-size="9" fill="#9A9792" text-anchor="middle">vector, map, queue</text>

  <rect x="360" y="108" width="130" height="55" rx="6" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="425" y="128" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Core logic</text>
  <text x="425" y="148" font-size="9" fill="#9A9792" text-anchor="middle">loops, recursion</text>

  <rect x="510" y="108" width="130" height="55" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="575" y="128" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Return result</text>
  <text x="575" y="148" font-size="9" fill="#9A9792" text-anchor="middle">return ans;</text>
</svg>

A clean starting template for C++ submissions:

```cpp
class Solution {
public:
    ReturnType functionName(ParamType param) {
        // Your solution here
    }
};
```

### Common Patterns in LeetCode C++

**Two pointers:**

```cpp
int left = 0, right = n - 1;
while (left < right) {
    // process
    left++;
    right--;
}
```

**BFS on grid:**

```cpp
int dirs[4][2] = { {0,1},{1,0},{0,-1},{-1,0} };
queue<pair<int,int>> q;
q.push({startR, startC});
visited[startR][startC] = true;

while (!q.empty()) {
    auto [r, c] = q.front();
    q.pop();
    for (auto& d : dirs) {
        int nr = r + d[0], nc = c + d[1];
        if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
            visited[nr][nc] = true;
            q.push({nr, nc});
        }
    }
}
```

**DFS with memoization:**

```cpp
vector<vector<int>> memo(m, vector<int>(n, -1));

int dfs(int i, int j) {
    if (base_case) return base_value;
    if (memo[i][j] != -1) return memo[i][j];

    int result = /* recursive computation */;
    return memo[i][j] = result;
}
```

**Sliding window:**

```cpp
int left = 0, best = 0;
for (int right = 0; right < n; ++right) {
    // expand window: add nums[right]
    while (/* window invalid */) {
        // shrink window: remove nums[left]
        left++;
    }
    best = max(best, right - left + 1);
}
```

---

## Part 5: Learning Path

Follow these stages in order. Each one builds on the last — don't skip ahead.

<svg viewBox="0 0 780 340" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="lp-arr" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#8B8680"/>
    </marker>
  </defs>

  <!-- Stage 1 -->
  <rect x="10" y="30" width="140" height="70" rx="10" fill="#E8D5D0" stroke="#C08070" stroke-width="2"/>
  <text x="80" y="55" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Stage 1</text>
  <text x="80" y="73" font-size="10" fill="#7A7772" text-anchor="middle">Syntax &amp; Basics</text>
  <text x="80" y="88" font-size="9" fill="#9A9792" text-anchor="middle">1-2 weeks</text>

  <!-- Arrow 1→2 -->
  <line x1="150" y1="65" x2="168" y2="65" stroke="#8B8680" stroke-width="1.8" marker-end="url(#lp-arr)"/>

  <!-- Stage 2 -->
  <rect x="170" y="30" width="140" height="70" rx="10" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="2"/>
  <text x="240" y="55" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Stage 2</text>
  <text x="240" y="73" font-size="10" fill="#7A7772" text-anchor="middle">STL Mastery</text>
  <text x="240" y="88" font-size="9" fill="#9A9792" text-anchor="middle">2-3 weeks</text>

  <!-- Arrow 2→3 -->
  <line x1="310" y1="65" x2="328" y2="65" stroke="#8B8680" stroke-width="1.8" marker-end="url(#lp-arr)"/>

  <!-- Stage 3 -->
  <rect x="330" y="30" width="140" height="70" rx="10" fill="#D4D8E0" stroke="#7080A0" stroke-width="2"/>
  <text x="400" y="55" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Stage 3</text>
  <text x="400" y="73" font-size="10" fill="#7A7772" text-anchor="middle">Pointers &amp; Memory</text>
  <text x="400" y="88" font-size="9" fill="#9A9792" text-anchor="middle">1-2 weeks</text>

  <!-- Arrow 3→4 -->
  <line x1="470" y1="65" x2="488" y2="65" stroke="#8B8680" stroke-width="1.8" marker-end="url(#lp-arr)"/>

  <!-- Stage 4 -->
  <rect x="490" y="30" width="140" height="70" rx="10" fill="#E8E3D8" stroke="#B8A880" stroke-width="2"/>
  <text x="560" y="55" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Stage 4</text>
  <text x="560" y="73" font-size="10" fill="#7A7772" text-anchor="middle">Modern C++</text>
  <text x="560" y="88" font-size="9" fill="#9A9792" text-anchor="middle">1 week</text>

  <!-- Arrow 4→5 -->
  <line x1="630" y1="65" x2="648" y2="65" stroke="#8B8680" stroke-width="1.8" marker-end="url(#lp-arr)"/>

  <!-- Stage 5 -->
  <rect x="650" y="30" width="120" height="70" rx="10" fill="#D4D1CC" stroke="#8B8680" stroke-width="2"/>
  <text x="710" y="55" font-size="13" fill="#5A5752" font-weight="700" text-anchor="middle">Stage 5</text>
  <text x="710" y="73" font-size="10" fill="#7A7772" text-anchor="middle">Algorithms</text>
  <text x="710" y="88" font-size="9" fill="#9A9792" text-anchor="middle">Ongoing</text>

  <!-- Details below each stage -->
  <rect x="10" y="120" width="140" height="95" rx="8" fill="#FAF8F5" stroke="#E0DDD8" stroke-width="1"/>
  <text x="20" y="138" font-size="9" fill="#5A5752">variables, types</text>
  <text x="20" y="152" font-size="9" fill="#5A5752">if/else, for, while</text>
  <text x="20" y="166" font-size="9" fill="#5A5752">functions, references</text>
  <text x="20" y="180" font-size="9" fill="#5A5752">arrays, cin/cout</text>
  <text x="20" y="200" font-size="9" fill="#3A6B3A" font-weight="600">10-15 Easy problems</text>

  <rect x="170" y="120" width="140" height="95" rx="8" fill="#FAF8F5" stroke="#E0DDD8" stroke-width="1"/>
  <text x="180" y="138" font-size="9" fill="#5A5752">vector, string, pair</text>
  <text x="180" y="152" font-size="9" fill="#5A5752">map, set, unordered_*</text>
  <text x="180" y="166" font-size="9" fill="#5A5752">stack, queue, pq</text>
  <text x="180" y="180" font-size="9" fill="#5A5752">sort, lower_bound</text>
  <text x="180" y="200" font-size="9" fill="#3A6B3A" font-weight="600">20-30 Easy/Med</text>

  <rect x="330" y="120" width="140" height="95" rx="8" fill="#FAF8F5" stroke="#E0DDD8" stroke-width="1"/>
  <text x="340" y="138" font-size="9" fill="#5A5752">pointers vs refs</text>
  <text x="340" y="152" font-size="9" fill="#5A5752">ListNode*, TreeNode*</text>
  <text x="340" y="166" font-size="9" fill="#5A5752">new/delete (avoid)</text>
  <text x="340" y="180" font-size="9" fill="#5A5752">smart pointers</text>
  <text x="340" y="200" font-size="9" fill="#3A6B3A" font-weight="600">LL + Tree problems</text>

  <rect x="490" y="120" width="140" height="95" rx="8" fill="#FAF8F5" stroke="#E0DDD8" stroke-width="1"/>
  <text x="500" y="138" font-size="9" fill="#5A5752">auto, structured bindings</text>
  <text x="500" y="152" font-size="9" fill="#5A5752">lambdas, captures</text>
  <text x="500" y="166" font-size="9" fill="#5A5752">initializer_list</text>
  <text x="500" y="180" font-size="9" fill="#5A5752">range-based for</text>
  <text x="500" y="200" font-size="9" fill="#3A6B3A" font-weight="600">Refactor solutions</text>

  <rect x="650" y="120" width="120" height="95" rx="8" fill="#FAF8F5" stroke="#E0DDD8" stroke-width="1"/>
  <text x="660" y="138" font-size="9" fill="#5A5752">two pointers</text>
  <text x="660" y="152" font-size="9" fill="#5A5752">BFS, DFS</text>
  <text x="660" y="166" font-size="9" fill="#5A5752">DP patterns</text>
  <text x="660" y="180" font-size="9" fill="#5A5752">graph, backtracking</text>
  <text x="660" y="200" font-size="9" fill="#3A6B3A" font-weight="600">Templates blog</text>

  <!-- Timeline bar -->
  <rect x="10" y="240" width="760" height="30" rx="15" fill="#F0EBE6" stroke="#D4D1CC" stroke-width="1"/>
  <rect x="10" y="240" width="140" height="30" rx="15" fill="#E8D5D0"/>
  <rect x="150" y="240" width="180" height="30" fill="#D4D8D0"/>
  <rect x="330" y="240" width="140" height="30" fill="#D4D8E0"/>
  <rect x="470" y="240" width="120" height="30" fill="#E8E3D8"/>
  <rect x="590" y="240" width="180" height="30" rx="15" fill="#D4D1CC"/>

  <text x="80" y="260" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Week 1-2</text>
  <text x="240" y="260" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Week 3-5</text>
  <text x="400" y="260" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Week 6-7</text>
  <text x="530" y="260" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Week 8</text>
  <text x="680" y="260" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">Week 9+</text>

  <!-- Milestone markers -->
  <text x="390" y="305" font-size="12" fill="#3A6B3A" font-weight="700" text-anchor="middle">Milestones</text>
  <text x="80" y="325" font-size="10" fill="#5A5752" text-anchor="middle">"I can write C++"</text>
  <text x="240" y="325" font-size="10" fill="#5A5752" text-anchor="middle">"I know which container"</text>
  <text x="400" y="325" font-size="10" fill="#5A5752" text-anchor="middle">"I get pointers"</text>
  <text x="560" y="325" font-size="10" fill="#5A5752" text-anchor="middle">"Cleaner code"</text>
  <text x="710" y="325" font-size="10" fill="#5A5752" text-anchor="middle">"Interview ready"</text>
</svg>

### Stage 1 — Syntax & Basics (1-2 weeks)

- [ ] Variables, types, operators
- [ ] Control flow (if/else, for, while)
- [ ] Functions (pass by value, reference, const reference)
- [ ] Arrays and strings
- [ ] Basic I/O (`cin`, `cout`)

**Practice:** Solve 10-15 LeetCode Easy problems using C++.

### Stage 2 — STL Mastery (2-3 weeks)

- [ ] `vector`, `string`, `pair`
- [ ] `unordered_map`, `unordered_set`
- [ ] `set`, `map`, `multiset`
- [ ] `stack`, `queue`, `deque`
- [ ] `priority_queue` (min-heap, max-heap)
- [ ] `sort`, `lower_bound`, `upper_bound`
- [ ] Iterators and range-based for loops

**Practice:** Solve 20-30 LeetCode Easy/Medium problems. For each one, ask: "Which STL container makes this easier?"

### Stage 3 — Pointers & Memory (1-2 weeks)

- [ ] Pointers vs references
- [ ] `new` / `delete` (and why to avoid them)
- [ ] `ListNode*`, `TreeNode*` patterns
- [ ] Smart pointers (`unique_ptr`, `shared_ptr`) — for real projects, not LeetCode

**Practice:** Solve linked list and tree problems (LC 206, 21, 141, 104, 226, 102).

### Stage 4 — Modern C++ Features (1 week)

- [ ] `auto` type deduction
- [ ] Structured bindings (`auto& [k, v]`)
- [ ] Lambda functions and captures
- [ ] `initializer_list` (`min({a, b, c})`)
- [ ] Range-based for with references

### Stage 5 — Algorithm Templates (Ongoing)

At this point, you're ready to focus on algorithms rather than language features. Work through the [LeetCode Templates](/blog_leetcode/leetcode-templates/) on this blog:

1. [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/) — two pointers, sliding window
2. [Search](/blog_leetcode/posts/2026-01-20-leetcode-templates-search/) — binary search patterns
3. [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/) / [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/) — graph and tree traversal
4. [Dynamic Programming](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/) — 1D, 2D, bitmask
5. [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/) — topological sort, Dijkstra, DSU

---

## Part 6: Modern C++ Features (C++20 / C++23)

Most online judges now support C++20, and some support C++23. These features can make your code shorter, safer, and more expressive.

<svg viewBox="0 0 740 280" xmlns="http://www.w3.org/2000/svg" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="cpp-arr" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="#8B8680"/>
    </marker>
  </defs>

  <!-- Timeline bar -->
  <rect x="30" y="10" width="680" height="28" rx="14" fill="#F0EBE6" stroke="#D4D1CC" stroke-width="1"/>
  <rect x="30" y="10" width="260" height="28" rx="14" fill="#D4D8E0"/>
  <rect x="290" y="10" width="210" height="28" fill="#D4D8D0"/>
  <rect x="500" y="10" width="210" height="28" rx="14" fill="#E8D5D0"/>
  <text x="160" y="29" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">C++11 / 14 / 17</text>
  <text x="395" y="29" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">C++20</text>
  <text x="605" y="29" font-size="12" fill="#3A3530" font-weight="700" text-anchor="middle">C++23</text>

  <!-- C++17 features -->
  <rect x="30" y="52" width="115" height="32" rx="6" fill="#E4E7ED" stroke="#B8B5B0" stroke-width="1"/>
  <text x="87" y="72" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">auto, lambdas</text>

  <rect x="155" y="52" width="135" height="32" rx="6" fill="#E4E7ED" stroke="#B8B5B0" stroke-width="1"/>
  <text x="222" y="72" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">structured bindings</text>

  <!-- C++20 features -->
  <rect x="300" y="52" width="90" height="32" rx="6" fill="#DEE3DB" stroke="#B8B5B0" stroke-width="1"/>
  <text x="345" y="72" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">&lt;bit&gt;</text>

  <rect x="400" y="52" width="90" height="32" rx="6" fill="#DEE3DB" stroke="#B8B5B0" stroke-width="1"/>
  <text x="445" y="72" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">contains()</text>

  <!-- C++23 features -->
  <rect x="510" y="52" width="90" height="32" rx="6" fill="#ECD9D4" stroke="#B8B5B0" stroke-width="1"/>
  <text x="555" y="72" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">views::zip</text>

  <rect x="610" y="52" width="90" height="32" rx="6" fill="#ECD9D4" stroke="#B8B5B0" stroke-width="1"/>
  <text x="655" y="72" font-size="10" fill="#5A5752" font-weight="600" text-anchor="middle">std::print</text>

  <!-- Feature → Problem mapping -->
  <text x="370" y="115" font-size="12" fill="#5A5752" font-weight="700" text-anchor="middle">What Each Feature Replaces</text>
  <line x1="50" y1="122" x2="690" y2="122" stroke="#E0DDD8" stroke-width="1"/>

  <rect x="30" y="132" width="340" height="30" rx="6" fill="#F5F0EB" stroke="#E0DDD8" stroke-width="1"/>
  <text x="40" y="152" font-size="10" fill="#C06050" font-weight="600">Before:</text>
  <text x="95" y="152" font-size="10" fill="#7A7772">__builtin_popcount(x)</text>

  <rect x="380" y="132" width="340" height="30" rx="6" fill="#F0F5F0" stroke="#E0DDD8" stroke-width="1"/>
  <text x="390" y="152" font-size="10" fill="#3A6B3A" font-weight="600">After:</text>
  <text x="435" y="152" font-size="10" fill="#5A5752">std::popcount(x)</text>

  <rect x="30" y="170" width="340" height="30" rx="6" fill="#F5F0EB" stroke="#E0DDD8" stroke-width="1"/>
  <text x="40" y="190" font-size="10" fill="#C06050" font-weight="600">Before:</text>
  <text x="95" y="190" font-size="10" fill="#7A7772">if (mp.find(k) != mp.end())</text>

  <rect x="380" y="170" width="340" height="30" rx="6" fill="#F0F5F0" stroke="#E0DDD8" stroke-width="1"/>
  <text x="390" y="190" font-size="10" fill="#3A6B3A" font-weight="600">After:</text>
  <text x="435" y="190" font-size="10" fill="#5A5752">if (mp.contains(k))</text>

  <rect x="30" y="208" width="340" height="30" rx="6" fill="#F5F0EB" stroke="#E0DDD8" stroke-width="1"/>
  <text x="40" y="228" font-size="10" fill="#C06050" font-weight="600">Before:</text>
  <text x="95" y="228" font-size="10" fill="#7A7772">for (int i = 0; i &lt; n; i++)</text>

  <rect x="380" y="208" width="340" height="30" rx="6" fill="#F0F5F0" stroke="#E0DDD8" stroke-width="1"/>
  <text x="390" y="228" font-size="10" fill="#3A6B3A" font-weight="600">After:</text>
  <text x="435" y="228" font-size="10" fill="#5A5752">for (auto x : v | views::filter(...))</text>

  <!-- Recommendation -->
  <rect x="100" y="250" width="540" height="24" rx="12" fill="#D4D8D0" stroke="#6B8B6B" stroke-width="1.2"/>
  <text x="370" y="266" font-size="10" fill="#3A6B3A" font-weight="600" text-anchor="middle">Recommendation: Use C++20 features freely on LeetCode. C++23 — check judge support first.</text>
</svg>

### `<bit>` Header (C++20) — Bit Manipulation Made Clean

Replaces hand-rolled bit tricks with readable, portable functions.

```cpp
#include <bit>

int n = 42;  // binary: 101010

popcount((unsigned)n);        // 3  — number of set bits
has_single_bit((unsigned)n);  // false — true only for powers of 2
bit_ceil((unsigned)n);        // 64 — smallest power of 2 >= n
bit_floor((unsigned)n);       // 32 — largest power of 2 <= n
bit_width((unsigned)n);       // 6  — min bits needed (= floor(log2(n)) + 1)
countl_zero((unsigned)n);     // 26 — leading zeros (32-bit)
countr_zero((unsigned)n);     // 1  — trailing zeros
rotl((unsigned)n, 2);         // rotate bits left by 2
rotr((unsigned)n, 2);         // rotate bits right by 2
```

Before C++20, you'd write `__builtin_popcount(n)` (GCC-specific). The `<bit>` header is standard and portable.

### `contains()` for Associative Containers (C++20)

No more `.count()` or `.find() != .end()`:

{% raw %}
```cpp
unordered_map<string, int> freq = {{"apple", 3}, {"banana", 1}};
unordered_set<int> seen = {1, 2, 3};

if (freq.contains("apple")) { /* ... */ }    // cleaner than freq.count("apple")
if (seen.contains(42)) { /* ... */ }         // cleaner than seen.find(42) != seen.end()

// Works on all associative containers:
// set, map, unordered_set, unordered_map, multiset, multimap
```
{% endraw %}

### String `starts_with()` / `ends_with()` (C++20)

```cpp
string s = "hello_world";

s.starts_with("hello");    // true
s.starts_with("world");    // false
s.ends_with("world");      // true
s.ends_with("hello");      // false

// Also works with string_view and char
s.starts_with('h');         // true
```

### `std::ssize()` — Signed Size (C++20)

Eliminates the classic warning when comparing `int i` with `v.size()` (which returns `size_t`, unsigned):

```cpp
#include <iterator>

vector<int> v = {1, 2, 3};

// Before: warning about signed/unsigned comparison
for (int i = 0; i < (int)v.size(); ++i) { /* ... */ }

// After: clean and safe
for (int i = 0; i < ssize(v); ++i) { /* ... */ }
```

### `std::midpoint` and `std::lerp` (C++20)

Overflow-safe midpoint calculation — critical for binary search:

```cpp
#include <numeric>

int lo = 1'000'000'000, hi = 2'000'000'000;

int mid = midpoint(lo, hi);    // correct: no overflow
// vs. (lo + hi) / 2           // BUG: integer overflow!

// Also works with pointers and floating point
double t = lerp(0.0, 100.0, 0.3);  // 30.0 — linear interpolation
```

### `erase` / `erase_if` — Uniform Container Erasure (C++20)

Remove elements from any container without the erase-remove idiom:

```cpp
#include <vector>
#include <string>
#include <set>

vector<int> v = {1, 2, 3, 2, 4, 2, 5};
erase(v, 2);                        // v = {1, 3, 4, 5} — remove all 2s
erase_if(v, [](int x) { return x % 2 == 0; });  // remove all even numbers

string s = "hello world";
erase(s, 'l');                       // "heo word"

// Works on sets, maps, etc.
set<int> st = {1, 2, 3, 4, 5};
erase_if(st, [](int x) { return x > 3; });  // {1, 2, 3}
```

Before C++20, removing from a vector required the awkward `v.erase(remove(v.begin(), v.end(), val), v.end())`.

### Ranges Library (C++20) — Cleaner Algorithm Calls

Ranges let you pass containers directly instead of `.begin()` / `.end()` pairs, and compose operations with views.

```cpp
#include <ranges>
#include <algorithm>

vector<int> v = {5, 3, 1, 4, 2};

// Before
sort(v.begin(), v.end());

// After — pass the container directly
ranges::sort(v);
ranges::sort(v, greater<>{});    // descending

// Other range-based algorithms
auto it = ranges::find(v, 3);
int mn = ranges::min(v);
int mx = ranges::max(v);
bool all_pos = ranges::all_of(v, [](int x) { return x > 0; });
bool any_neg = ranges::any_of(v, [](int x) { return x < 0; });
int cnt = ranges::count_if(v, [](int x) { return x % 2 == 0; });
```

### Views — Lazy, Composable Pipelines (C++20)

Views transform data lazily (no copies, no allocations). Chain them with `|`.

```cpp
#include <ranges>

vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

// Filter + Transform — get squares of even numbers
auto result = v
    | views::filter([](int x) { return x % 2 == 0; })
    | views::transform([](int x) { return x * x; });

for (int x : result) {
    cout << x << " ";    // 4 16 36 64 100
}

// Generate a range of integers (replaces manual for loops)
for (int i : views::iota(0, 10)) {
    // i = 0, 1, 2, ..., 9
}

// Take first N elements
for (int x : v | views::take(3)) {
    // x = 1, 2, 3
}

// Drop first N elements
for (int x : v | views::drop(7)) {
    // x = 8, 9, 10
}

// Reverse view (no copy)
for (int x : v | views::reverse) {
    // x = 10, 9, 8, ..., 1
}

// Enumerate with index (C++23)
// for (auto [i, val] : v | views::enumerate) { ... }
```

### `views::zip` (C++23) — Iterate Multiple Containers Together

```cpp
#include <ranges>

vector<string> names = {"Alice", "Bob", "Carol"};
vector<int> scores = {95, 87, 92};

for (auto [name, score] : views::zip(names, scores)) {
    cout << name << ": " << score << endl;
}

// Before C++23, you'd use index-based loops:
// for (int i = 0; i < n; ++i) cout << names[i] << ": " << scores[i];
```

### `<numbers>` Constants (C++20)

```cpp
#include <numbers>

double pi   = numbers::pi;       // 3.14159265358979...
double e    = numbers::e;        // 2.71828182845904...
double ln2  = numbers::ln2;      // 0.69314718055994...
double sqrt2 = numbers::sqrt2;   // 1.41421356237309...
```

### Designated Initializers (C++20)

Name the fields when initializing structs — self-documenting and order-safe:

```cpp
struct Edge {
    int from;
    int to;
    int weight;
};

Edge e = {.from = 0, .to = 5, .weight = 10};

// Compare with positional (error-prone with many fields):
// Edge e = {0, 5, 10};  // which is from? which is weight?
```

### Three-Way Comparison / Spaceship Operator (C++20)

Auto-generate all comparison operators from one definition:

```cpp
struct Point {
    int x, y;
    auto operator<=>(const Point&) const = default;
};

Point a{1, 2}, b{1, 3};
// Now all of these work: a == b, a != b, a < b, a > b, a <= b, a >= b

// Useful for sorting custom structs without writing a comparator
vector<Point> points = { {3,1}, {1,2}, {1,1} };
ranges::sort(points);  // sorted by x, then y
```

### `std::format` (C++20) / `std::print` (C++23)

Python-style string formatting:

```cpp
#include <format>

string s = format("x = {}, y = {}", 42, 3.14);
// s = "x = 42, y = 3.14"

string padded = format("{:>10}", "hello");
// padded = "     hello"

string hex = format("{:#x}", 255);
// hex = "0xff"

// C++23: print directly to stdout (no cout needed)
// #include <print>
// println("Hello, {}!", "world");
```

### Feature Availability Summary

| Feature | Standard | LeetCode | Codeforces | AtCoder |
|---|---|---|---|---|
| `<bit>` popcount, etc. | C++20 | Yes | Yes | Yes |
| `contains()` | C++20 | Yes | Yes | Yes |
| `starts_with` / `ends_with` | C++20 | Yes | Yes | Yes |
| `ssize()` | C++20 | Yes | Yes | Yes |
| `midpoint` | C++20 | Yes | Yes | Yes |
| `erase` / `erase_if` | C++20 | Yes | Yes | Yes |
| `ranges::sort`, etc. | C++20 | Yes | Yes | Yes |
| `views::filter/transform` | C++20 | Yes | Partial | Yes |
| `views::zip` | C++23 | Varies | No | Varies |
| `std::format` | C++20 | Varies | Partial | Yes |
| `std::print` | C++23 | Varies | No | Varies |

When in doubt on a judge, stick to C++17 features. Use C++20 when you know it's supported — it genuinely makes code cleaner.

---

## Quick Reference Card

### Time Complexity Cheat Sheet

| Operation | `vector` | `unordered_map` | `map` | `priority_queue` |
|---|---|---|---|---|
| Access by index | $O(1)$ | — | — | — |
| Search | $O(n)$ | $O(1)$ avg | $O(\log n)$ | — |
| Insert | $O(1)$* | $O(1)$ avg | $O(\log n)$ | $O(\log n)$ |
| Delete | $O(n)$ | $O(1)$ avg | $O(\log n)$ | $O(\log n)$ |
| Min/Max | $O(n)$ | $O(n)$ | $O(1)$** | $O(1)$ |

\* amortized push_back | ** begin()/rbegin()

### Integer Limits

| Type | Max Value | Approximate |
|---|---|---|
| `int` | 2,147,483,647 | $2 \times 10^9$ |
| `long long` | 9,223,372,036,854,775,807 | $9.2 \times 10^{18}$ |
| `unsigned int` | 4,294,967,295 | $4.3 \times 10^9$ |

### Must-Know Macros & Constants

```cpp
#include <climits>
INT_MAX;    // 2147483647
INT_MIN;    // -2147483648
LLONG_MAX;  // 9223372036854775807

#include <cfloat>
DBL_MAX;    // ~1.8 × 10³⁰⁸
```

---

## Resources

- [cppreference.com](https://en.cppreference.com/) — the definitive C++ reference
- [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/) — best practices by Bjarne Stroustrup
- [Compiler Explorer (Godbolt)](https://godbolt.org/) — see what your C++ compiles to
- [LeetCode Templates on this blog](/blog_leetcode/leetcode-templates/) — algorithm patterns in C++
- [LeetCode Beginner's Guide](/blog_leetcode/2026/06/25/leetcode-beginners-guide/) — getting started with the platform
