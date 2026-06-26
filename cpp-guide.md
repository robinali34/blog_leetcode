---
layout: page
title: C++ Guide
permalink: /cpp-guide/
---

# C++ Guide: From Basics to LeetCode-Ready

A practical reference for learning C++ with a focus on competitive programming and technical interviews. Whether you're picking up C++ for the first time or brushing up before a contest, this page covers what matters.

> **New to LeetCode?** Start with the [Beginner's Guide](/blog_leetcode/2026/06/25/leetcode-beginners-guide/) to understand the platform, difficulty levels, and which problems to solve first.

---

## Why C++ for Algorithms?

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

```cpp
unordered_map<string, int> freq = {{"apple", 3}, {"banana", 1}};
unordered_set<int> seen = {1, 2, 3};

if (freq.contains("apple")) { /* ... */ }    // cleaner than freq.count("apple")
if (seen.contains(42)) { /* ... */ }         // cleaner than seen.find(42) != seen.end()

// Works on all associative containers:
// set, map, unordered_set, unordered_map, multiset, multimap
```

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
