---
layout: post
title: "Algorithm Templates: Heap"
date: 2026-01-05 00:00:00 -0700
categories: leetcode templates heap priority-queue
permalink: /posts/2026-01-05-leetcode-templates-heap/
tags: [leetcode, templates, heap, priority-queue, data-structures]
---

{% raw %}
Welcome to the Heap templates page! Here you'll find battle-tested C++ snippets for every common heap (priority queue) pattern on LeetCode — from basic min/max heaps to advanced techniques like K-way merge, Two Heaps for medians, and Dijkstra's shortest path. Each section is self-contained so you can copy-paste directly into your solutions. See also [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/) for related patterns.

> **New to Heaps?** A heap (priority queue) always gives you the smallest (min-heap) or largest (max-heap) element in O(1). Think of it as a self-sorting container. Whenever a problem says "k largest", "k smallest", "median", or "merge sorted lists", think heap.

## Contents

- [Heap Overview](#heap-overview)
- [Min Heap](#min-heap)
- [Max Heap](#max-heap)
- [Custom Comparators](#custom-comparators)
- [Common Patterns](#common-patterns)
- [K-way Merge](#k-way-merge)
- [Top K Elements](#top-k-elements)
- [Two Heaps](#two-heaps)
- [Dijkstra's Algorithm](#dijkstras-algorithm)

## Heap Overview

A **heap** (priority queue) is a complete binary tree that satisfies the heap property:
- **Min Heap**: Parent node is always less than or equal to its children
- **Max Heap**: Parent node is always greater than or equal to its children

In C++, `std::priority_queue` is a max-heap by default. To get a min-heap, pass `greater<int>` as the comparator.

**Key Operations:**

| Operation | What it does | Time |
|-----------|-------------|------|
| `push(x)` | Insert element | O(log n) |
| `pop()` | Remove top element | O(log n) |
| `top()` | Access top element (min or max) | O(1) |
| `empty()` | Check if empty | O(1) |
| `size()` | Get number of elements | O(1) |

**Use Cases:**
- Finding K largest/smallest elements
- Merging K sorted sequences
- Maintaining running median
- Shortest path algorithms (Dijkstra's)
- Scheduling problems (meeting rooms, task ordering)
- Stream processing (continuously arriving data)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 305" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="350" y="18" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">Min-Heap: Tree Structure and Array Representation</text>
  <!-- Tree edges -->
  <line x1="350" y1="60" x2="210" y2="105" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="350" y1="60" x2="490" y2="105" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="210" y1="135" x2="140" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="210" y1="135" x2="280" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="490" y1="135" x2="420" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <!-- Tree nodes with index annotations -->
  <circle cx="350" cy="48" r="20" fill="#D4D8D0" stroke="#8B9B86" stroke-width="2"/>
  <text x="350" y="53" text-anchor="middle" font-size="15" font-weight="700" fill="#3A3530">1</text>
  <text x="374" y="37" font-size="9" fill="#9A9792">i=0</text>
  <circle cx="210" cy="120" r="18" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="210" y="125" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">3</text>
  <text x="232" y="109" font-size="9" fill="#9A9792">i=1</text>
  <circle cx="490" cy="120" r="18" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="490" y="125" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">5</text>
  <text x="512" y="109" font-size="9" fill="#9A9792">i=2</text>
  <circle cx="140" cy="188" r="16" fill="#E8D5D0" stroke="#B8A5A0" stroke-width="1.5"/>
  <text x="140" y="193" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">7</text>
  <text x="160" y="178" font-size="9" fill="#9A9792">i=3</text>
  <circle cx="280" cy="188" r="16" fill="#E8D5D0" stroke="#B8A5A0" stroke-width="1.5"/>
  <text x="280" y="193" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">9</text>
  <text x="300" y="178" font-size="9" fill="#9A9792">i=4</text>
  <circle cx="420" cy="188" r="16" fill="#E8D5D0" stroke="#B8A5A0" stroke-width="1.5"/>
  <text x="420" y="193" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">8</text>
  <text x="440" y="178" font-size="9" fill="#9A9792">i=5</text>
  <!-- Array representation -->
  <text x="350" y="228" text-anchor="middle" font-size="11" font-weight="600" fill="#5A5752">Array: stored level-by-level, left to right</text>
  <rect x="155" y="236" width="48" height="28" rx="4" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="179" y="254" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">1</text>
  <rect x="203" y="236" width="48" height="28" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="227" y="254" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">3</text>
  <rect x="251" y="236" width="48" height="28" rx="4" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="275" y="254" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">5</text>
  <rect x="299" y="236" width="48" height="28" rx="4" fill="#E8D5D0" stroke="#B8A5A0" stroke-width="1.5"/>
  <text x="323" y="254" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">7</text>
  <rect x="347" y="236" width="48" height="28" rx="4" fill="#E8D5D0" stroke="#B8A5A0" stroke-width="1.5"/>
  <text x="371" y="254" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">9</text>
  <rect x="395" y="236" width="48" height="28" rx="4" fill="#E8D5D0" stroke="#B8A5A0" stroke-width="1.5"/>
  <text x="419" y="254" text-anchor="middle" font-size="13" font-weight="600" fill="#3A3530">8</text>
  <!-- Array index labels -->
  <text x="179" y="278" text-anchor="middle" font-size="9" fill="#9A9792">[0]</text>
  <text x="227" y="278" text-anchor="middle" font-size="9" fill="#9A9792">[1]</text>
  <text x="275" y="278" text-anchor="middle" font-size="9" fill="#9A9792">[2]</text>
  <text x="323" y="278" text-anchor="middle" font-size="9" fill="#9A9792">[3]</text>
  <text x="371" y="278" text-anchor="middle" font-size="9" fill="#9A9792">[4]</text>
  <text x="419" y="278" text-anchor="middle" font-size="9" fill="#9A9792">[5]</text>
  <!-- Relationship formulas -->
  <text x="350" y="300" text-anchor="middle" font-size="10" fill="#7A7772">parent = (i-1)/2 · left child = 2i+1 · right child = 2i+2 · parent ≤ children everywhere</text>
</svg>

### How a Min-Heap Works (Visualization)

<svg viewBox="0 0 400 280" xmlns="http://www.w3.org/2000/svg" style="max-width:400px;font-family:monospace">
  <!-- Edges -->
  <line x1="200" y1="38" x2="120" y2="98" stroke="#b8a9c9" stroke-width="2"/>
  <line x1="200" y1="38" x2="280" y2="98" stroke="#b8a9c9" stroke-width="2"/>
  <line x1="120" y1="98" x2="80" y2="158" stroke="#b8a9c9" stroke-width="2"/>
  <line x1="120" y1="98" x2="160" y2="158" stroke="#b8a9c9" stroke-width="2"/>
  <line x1="280" y1="98" x2="240" y2="158" stroke="#b8a9c9" stroke-width="2"/>
  <!-- Nodes -->
  <circle cx="200" cy="35" r="20" fill="#a3b18a" stroke="#588157" stroke-width="2"/>
  <text x="200" y="40" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">1</text>
  <circle cx="120" cy="95" r="20" fill="#dda15e" stroke="#bc6c25" stroke-width="2"/>
  <text x="120" y="100" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">3</text>
  <circle cx="280" cy="95" r="20" fill="#dda15e" stroke="#bc6c25" stroke-width="2"/>
  <text x="280" y="100" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">2</text>
  <circle cx="80" cy="155" r="20" fill="#e9c46a" stroke="#c9a227" stroke-width="2"/>
  <text x="80" y="160" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">7</text>
  <circle cx="160" cy="155" r="20" fill="#e9c46a" stroke="#c9a227" stroke-width="2"/>
  <text x="160" y="160" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">4</text>
  <circle cx="240" cy="155" r="20" fill="#e9c46a" stroke="#c9a227" stroke-width="2"/>
  <text x="240" y="160" text-anchor="middle" fill="#fff" font-size="14" font-weight="bold">5</text>
  <!-- Labels -->
  <text x="200" y="210" text-anchor="middle" fill="#6b705c" font-size="12">Array: [1, 3, 2, 7, 4, 5]</text>
  <text x="200" y="230" text-anchor="middle" fill="#6b705c" font-size="11">push(x): add to end, bubble UP to maintain order</text>
  <text x="200" y="248" text-anchor="middle" fill="#6b705c" font-size="11">pop(): remove root (min), move last to root, bubble DOWN</text>
  <text x="200" y="266" text-anchor="middle" fill="#6b705c" font-size="11">top(): always returns root = smallest element → O(1)</text>
</svg>

## Min Heap

**When to use:** You need the smallest element quickly — "k largest elements" (use min-heap of size k), sorting streams, or Dijkstra's algorithm.

Min heap keeps the smallest element at the top.

```cpp
#include <queue>
#include <vector>

// Min heap (smallest element at top) - using greater<>
priority_queue<int, vector<int>, greater<int>> minHeap;

// Min heap using greater<> (C++14+)
priority_queue<int, vector<int>, greater<>> minHeap2;

// Min heap using lambda comparator (decltype required)
auto minCmp = [](int a, int b) { return a > b; };
priority_queue<int, vector<int>, decltype(minCmp)> minHeap3(minCmp);

// Note: decltype is REQUIRED for lambdas because each lambda has a unique type
// You cannot use: priority_queue<int, vector<int>, [](auto& a, auto& b) { return a > b; }>  // ❌ Invalid

// Basic operations
minHeap.push(5);
minHeap.push(2);
minHeap.push(8);
minHeap.push(1);

minHeap.top();    // Returns 1 (smallest)
minHeap.pop();    // Removes 1
minHeap.top();    // Returns 2 (next smallest)
```

### Example: Find K Smallest Elements

```cpp
vector<int> findKSmallest(vector<int>& nums, int k) {
    priority_queue<int, vector<int>, greater<int>> minHeap;
    
    for(int num : nums) {
        minHeap.push(num);
    }
    
    vector<int> result;
    for(int i = 0; i < k && !minHeap.empty(); i++) {
        result.push_back(minHeap.top());
        minHeap.pop();
    }
    
    return result;
}
```

## Max Heap

**When to use:** You need the largest element quickly — "k smallest elements" (use max-heap of size k), greedy scheduling, or "last stone weight" style problems.

Max heap keeps the largest element at the top (default in C++).

```cpp
#include <queue>
#include <vector>

// Max heap (largest element at top) - default
priority_queue<int> maxHeap;

// Max heap explicitly using less<> (default comparator)
priority_queue<int, vector<int>, less<int>> maxHeap2;

// Max heap using lambda comparator (decltype required)
auto maxCmp = [](int a, int b) { return a < b; };
priority_queue<int, vector<int>, decltype(maxCmp)> maxHeap3(maxCmp);

// Note: decltype is REQUIRED for lambdas because each lambda has a unique type
// You cannot use: priority_queue<int, vector<int>, [](auto& a, auto& b) { return a < b; }>  // ❌ Invalid

// Basic operations
maxHeap.push(5);
maxHeap.push(2);
maxHeap.push(8);
maxHeap.push(1);

maxHeap.top();    // Returns 8 (largest)
maxHeap.pop();    // Removes 8
maxHeap.top();    // Returns 5 (next largest)
```

### Example: Find K Largest Elements

```cpp
vector<int> findKLargest(vector<int>& nums, int k) {
    priority_queue<int> maxHeap;
    
    for(int num : nums) {
        maxHeap.push(num);
    }
    
    vector<int> result;
    for(int i = 0; i < k && !maxHeap.empty(); i++) {
        result.push_back(maxHeap.top());
        maxHeap.pop();
    }
    
    return result;
}
```

## Custom Comparators

**When to use:** The heap elements are structs, pairs, or tuples and you need to order by a specific field (e.g., sort by cost, frequency, or distance).

### Using Struct

```cpp
// Custom comparator for pairs: min heap by second element
struct Compare {
    bool operator()(pair<int, int>& a, pair<int, int>& b) {
        return a.second > b.second; // Min heap (smaller second element on top)
    }
};
priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;

// Example: {value, frequency} - keep element with smallest frequency on top
pq.push({1, 5});
pq.push({2, 3});
pq.push({3, 7});
pq.top(); // Returns {2, 3} (smallest frequency)
```

```cpp
// Custom struct with comparator: min heap by cost
struct Node {
    int cost;
    int id;
};

struct Compare {
    bool operator()(const Node& a, const Node& b) {
        return a.cost > b.cost; // Min heap (smaller cost on top)
    }
};

priority_queue<Node, vector<Node>, Compare> pq;

// Example usage
pq.push({10, 1}); // cost 10, id 1
pq.push({5, 2});  // cost 5, id 2
pq.push({15, 3}); // cost 15, id 3
pq.top(); // Returns {5, 2} (smallest cost)
```

### Using Lambda

```cpp
// Min heap by distance (for Dijkstra's algorithm)
auto distCmp = [](pair<int, int>& a, pair<int, int>& b) {
    return a.first > b.first; // {distance, node} - min heap by distance
};
priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(distCmp)> pq(distCmp);

// Example usage
pq.push({10, 0}); // distance 10 to node 0
pq.push({5, 1});  // distance 5 to node 1
pq.top(); // Returns {5, 1} (smallest distance)
```

### Custom Object Comparator

```cpp
// Custom object with comparator
struct Point {
    int x, y;
    int dist() const { return x*x + y*y; }
};

struct PointCompare {
    bool operator()(const Point& a, const Point& b) {
        return a.dist() > b.dist(); // Min heap by distance
    }
};
priority_queue<Point, vector<Point>, PointCompare> pq;
```

## Common Patterns

### Pattern 1: Maintain K Elements

Keep only K elements in heap, remove smallest/largest when size exceeds K.

```cpp
// Keep K largest elements
priority_queue<int, vector<int>, greater<int>> minHeap; // Min heap to keep K largest

for(int num : nums) {
    minHeap.push(num);
    if(minHeap.size() > k) {
        minHeap.pop(); // Remove smallest
    }
}
// Now minHeap contains K largest elements
```

### Pattern 2: Frequency-Based

Use heap with frequency counts.

```cpp
// Top K frequent elements
unordered_map<int, int> freq;
for(int num : nums) freq[num]++;

priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
// {frequency, element} - min heap by frequency

for(auto& [num, count] : freq) {
    minHeap.push({count, num});
    if(minHeap.size() > k) {
        minHeap.pop();
    }
}
```

## K-way Merge

**When to use:** The problem says "merge k sorted lists/arrays" or you need to produce a globally sorted sequence from multiple sorted sources.

Merge K sorted lists/arrays using a min heap.

```cpp
// Merge K sorted lists
ListNode* mergeKLists(vector<ListNode*>& lists) {
    auto cmp = [](ListNode* a, ListNode* b) {
        return a->val > b->val; // Min heap by value
    };
    priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
    
    // Push first node of each list
    for(ListNode* list : lists) {
        if(list) pq.push(list);
    }
    
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    
    while(!pq.empty()) {
        ListNode* node = pq.top();
        pq.pop();
        cur->next = node;
        cur = cur->next;
        if(node->next) {
            pq.push(node->next);
        }
    }
    
    return dummy->next;
}
```

### K-way Merge for Arrays

```cpp
// Merge K sorted arrays
vector<int> mergeKSortedArrays(vector<vector<int>>& arrays) {
    using T = tuple<int, int, int>; // {value, array_index, position}
    priority_queue<T, vector<T>, greater<T>> pq;
    
    // Push first element of each array
    for(int i = 0; i < arrays.size(); i++) {
        if(!arrays[i].empty()) {
            pq.push({arrays[i][0], i, 0});
        }
    }
    
    vector<int> result;
    while(!pq.empty()) {
        auto [val, arrIdx, pos] = pq.top();
        pq.pop();
        result.push_back(val);
        
        if(pos + 1 < arrays[arrIdx].size()) {
            pq.push({arrays[arrIdx][pos + 1], arrIdx, pos + 1});
        }
    }
    
    return result;
}
```

## Top K Elements

**When to use:** The problem asks for "kth largest", "top k frequent", "k closest" — maintain a heap of size k and evict the least relevant element.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 250" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="ah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#8B8680"/></marker>
    <marker id="ahg" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#8B9B86"/></marker>
    <marker id="ahr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#B8A5A0"/></marker>
  </defs>
  <text x="360" y="20" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">Top-K Pattern: Min-Heap of Size K Filters the K Largest</text>
  <!-- Input stream -->
  <text x="25" y="60" font-size="11" font-weight="600" fill="#5A5752">Input stream</text>
  <rect x="15" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="30" y="86" text-anchor="middle" font-size="11" fill="#3A3530">4</text>
  <rect x="49" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="64" y="86" text-anchor="middle" font-size="11" fill="#3A3530">7</text>
  <rect x="83" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="98" y="86" text-anchor="middle" font-size="11" fill="#3A3530">2</text>
  <rect x="117" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="132" y="86" text-anchor="middle" font-size="11" fill="#3A3530">9</text>
  <rect x="151" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="166" y="86" text-anchor="middle" font-size="11" fill="#3A3530">1</text>
  <rect x="185" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="200" y="86" text-anchor="middle" font-size="11" fill="#3A3530">5</text>
  <rect x="219" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="234" y="86" text-anchor="middle" font-size="11" fill="#3A3530">8</text>
  <rect x="253" y="70" width="30" height="24" rx="4" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1"/>
  <text x="268" y="86" text-anchor="middle" font-size="11" fill="#3A3530">3</text>
  <!-- Arrow to heap -->
  <line x1="290" y1="82" x2="348" y2="82" stroke="#8B8680" stroke-width="1.5" marker-end="url(#ah)"/>
  <!-- Heap container -->
  <rect x="358" y="38" width="180" height="130" rx="10" fill="#FAF8F5" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="448" y="56" text-anchor="middle" font-size="11" font-weight="600" fill="#5A5752">Min-Heap (K = 3)</text>
  <!-- Heap tree inside -->
  <line x1="448" y1="80" x2="412" y2="108" stroke="#B8B5B0" stroke-width="1.2"/>
  <line x1="448" y1="80" x2="484" y2="108" stroke="#B8B5B0" stroke-width="1.2"/>
  <circle cx="448" cy="74" r="14" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="448" y="78" text-anchor="middle" font-size="12" font-weight="600" fill="#3A3530">7</text>
  <circle cx="412" cy="114" r="14" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="412" y="118" text-anchor="middle" font-size="12" font-weight="600" fill="#3A3530">8</text>
  <circle cx="484" cy="114" r="14" fill="#D4D8E0" stroke="#8B8680" stroke-width="1.5"/>
  <text x="484" y="118" text-anchor="middle" font-size="12" font-weight="600" fill="#3A3530">9</text>
  <text x="448" y="152" text-anchor="middle" font-size="9" fill="#7A7772">top() = smallest kept</text>
  <!-- Arrow to result -->
  <line x1="543" y1="82" x2="598" y2="82" stroke="#8B9B86" stroke-width="1.5" marker-end="url(#ahg)"/>
  <!-- Result box -->
  <rect x="608" y="56" width="100" height="56" rx="8" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="658" y="76" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">Top-3</text>
  <text x="658" y="94" text-anchor="middle" font-size="12" fill="#3A3530">{7, 8, 9}</text>
  <text x="658" y="108" text-anchor="middle" font-size="9" fill="#7A7772">K largest</text>
  <!-- Eviction arrow -->
  <line x1="448" y1="170" x2="448" y2="200" stroke="#B8A5A0" stroke-width="1.5" marker-end="url(#ahr)"/>
  <!-- Evicted info -->
  <text x="448" y="220" text-anchor="middle" font-size="11" fill="#B8A5A0">Evicted: 1, 2, 3, 4, 5</text>
  <text x="448" y="238" text-anchor="middle" font-size="10" fill="#9A9792">new &gt; top() → push new, pop smallest</text>
</svg>

### Top K Frequent Elements

```cpp
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for(int num : nums) freq[num]++;
    
    // Min heap: {frequency, element}
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap;
    
    for(auto& [num, count] : freq) {
        minHeap.push({count, num});
        if(minHeap.size() > k) {
            minHeap.pop(); // Remove element with smallest frequency
        }
    }
    
    vector<int> result;
    while(!minHeap.empty()) {
        result.push_back(minHeap.top().second);
        minHeap.pop();
    }
    
    return result;
}
```

### K Closest Points to Origin

```cpp
vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    auto distCmp = [](vector<int>& a, vector<int>& b) {
        int distA = a[0]*a[0] + a[1]*a[1];
        int distB = b[0]*b[0] + b[1]*b[1];
        return distA < distB; // Max heap (larger distance on top)
    };
    priority_queue<vector<int>, vector<vector<int>>, decltype(distCmp)> maxHeap(distCmp);
    
    for(auto& point : points) {
        maxHeap.push(point);
        if(maxHeap.size() > k) {
            maxHeap.pop(); // Remove point with largest distance
        }
    }
    
    vector<vector<int>> result;
    while(!maxHeap.empty()) {
        result.push_back(maxHeap.top());
        maxHeap.pop();
    }
    
    return result;
}
```

### Kth Largest Element in an Array (LC 215)

**Solution 1: Min Heap (O(n log k))**

Keep a min heap of size k. The top element will be the kth largest.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<>> minHeap;
        for(int num: nums) {
            minHeap.push(num);
            if(minHeap.size() > k) minHeap.pop();
        }
        return minHeap.top();
    }
};
```

**Solution 2: QuickSelect (O(n) average, O(n²) worst case)**

Use partition-based selection algorithm.

```cpp
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        const int N = nums.size();
        return quickSelect(nums, 0, N - 1, N - k);
    }
private:
    int quickSelect(vector<int>& nums, int l, int r, int k) {
        if(l == r) return nums[k];
        int pivot = nums[l], i = l - 1, j = r + 1;
        while(i < j) {
            do i++; while(nums[i] < pivot);
            do j--; while(nums[j] > pivot);
            if(i < j)
                swap(nums[i], nums[j]);
        }
        if(k <= j) return quickSelect(nums, l, j, k);
        else return quickSelect(nums, j + 1, r, k);
    }
};
```

**Comparison:**
- **Heap**: O(n log k) time, O(k) space - Simple and efficient for small k
- **QuickSelect**: O(n) average time, O(n²) worst case, O(1) space - Better for large k

## Two Heaps

**When to use:** The problem mentions "median", "sliding median", or requires tracking the middle value of a dynamic stream. Use a max-heap for the lower half and a min-heap for the upper half.

Maintain two heaps to find median or balance elements.

### Find Median from Data Stream

```cpp
class MedianFinder {
    priority_queue<int> maxHeap; // Lower half (max heap)
    priority_queue<int, vector<int>, greater<int>> minHeap; // Upper half (min heap)
    
public:
    void addNum(int num) {
        maxHeap.push(num);
        minHeap.push(maxHeap.top());
        maxHeap.pop();
        
        if(maxHeap.size() < minHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    
    double findMedian() {
        if(maxHeap.size() > minHeap.size()) {
            return maxHeap.top();
        }
        return (maxHeap.top() + minHeap.top()) / 2.0;
    }
};
```

### Sliding Window Median

```cpp
vector<double> medianSlidingWindow(vector<int>& nums, int k) {
    multiset<int> window(nums.begin(), nums.begin() + k);
    auto mid = next(window.begin(), k / 2);
    vector<double> medians;
    
    for(int i = k; i <= nums.size(); i++) {
        medians.push_back((double(*mid) + *prev(mid, 1 - k % 2)) / 2.0);
        
        if(i == nums.size()) break;
        
        window.insert(nums[i]);
        if(nums[i] < *mid) mid--;
        if(nums[i - k] <= *mid) mid++;
        window.erase(window.lower_bound(nums[i - k]));
    }
    
    return medians;
}
```

## Dijkstra's Algorithm

**When to use:** The problem asks for "shortest path", "minimum cost path", or "cheapest route" in a weighted graph with non-negative edges.

Use min heap for shortest path finding.

```cpp
// Shortest path from source to all nodes
vector<int> dijkstra(vector<vector<pair<int, int>>>& graph, int start) {
    int n = graph.size();
    vector<int> dist(n, INT_MAX);
    dist[start] = 0;
    
    // Min heap: {distance, node}
    auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
        return a.first > b.first; // Min heap by distance
    };
    priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
    pq.push({0, start});
    
    while(!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        
        if(d > dist[u]) continue; // Already processed with better distance
        
        for(auto& [v, weight] : graph[u]) {
            int newDist = dist[u] + weight;
            if(newDist < dist[v]) {
                dist[v] = newDist;
                pq.push({newDist, v});
            }
        }
    }
    
    return dist;
}
```

## Easy Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 703 | Kth Largest Element in a Stream | [Link](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | - |
| 1046 | Last Stone Weight | [Link](https://leetcode.com/problems/last-stone-weight/) | - |
| 1167 | Minimum Cost to Connect Sticks | [Link](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | - |

## Medium Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/hard-23-merge-k-sorted-lists/) |
| 215 | Kth Largest Element in an Array | [Link](https://leetcode.com/problems/kth-largest-element-in-an-array/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/05/medium-215-kth-largest-element-in-an-array/) |
| 253 | Meeting Rooms II | [Link](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-medium-253-meeting-rooms-ii/) |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) | - |
| 347 | Top K Frequent Elements | [Link](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-347-top-k-frequent-elements/) |
| 378 | Kth Smallest Element in a Sorted Matrix | [Link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | - |
| 692 | Top K Frequent Words | [Link](https://leetcode.com/problems/top-k-frequent-words/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-692-top-k-frequent-words/) |
| 621 | Task Scheduler | [Link](https://leetcode.com/problems/task-scheduler/) | - |
| 767 | Reorganize String | [Link](https://leetcode.com/problems/reorganize-string/) | - |
| 973 | K Closest Points to Origin | [Link](https://leetcode.com/problems/k-closest-points-to-origin/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-973-k-closest-points-to-origin/) |
| 1976 | Number of Ways to Arrive at Destination | [Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/28/medium-1976-number-of-ways-to-arrive-at-destination/) |
| 2406 | Divide Intervals Into Minimum Number of Groups | [Link](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/16/medium-2406-divide-intervals-into-minimum-number-of-groups/) |
| 1353 | Maximum Number of Events That Can Be Attended | [Link](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/13/medium-1353-maximum-number-of-events-that-can-be-attended/) |

## Hard Problems

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 480 | Sliding Window Median | [Link](https://leetcode.com/problems/sliding-window-median/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-480-sliding-window-median/) |
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) | - |
| 787 | Cheapest Flights Within K Stops | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | - |
| 871 | Minimum Number of Refueling Stops | [Link](https://leetcode.com/problems/minimum-number-of-refueling-stops/) | - |

## Common Heap Patterns

### Pattern 1: K Largest/Smallest
- Use min heap to keep K largest (remove smallest when size > K)
- Use max heap to keep K smallest (remove largest when size > K)

### Pattern 2: Frequency-Based
- Count frequencies, use heap to find top K by frequency

### Pattern 3: K-way Merge
- Push first element of each sequence into min heap
- Pop smallest, push next element from same sequence

### Pattern 4: Two Heaps
- Maintain two balanced heaps for median finding
- One heap for lower half, one for upper half

### Pattern 5: Shortest Path
- Use min heap in Dijkstra's algorithm
- Store {distance, node} pairs

## Key Insights

1. **Min Heap for K Largest**: Keep K largest by removing smallest
2. **Max Heap for K Smallest**: Keep K smallest by removing largest
3. **Custom Comparators**: Use lambda or struct for complex ordering
4. **Two Heaps**: Balance two heaps for median problems
5. **Efficiency**: Heap operations are O(log n), making it efficient for dynamic problems

## Time Complexity

| Operation | Time Complexity |
|-----------|----------------|
| `push()` | O(log n) |
| `pop()` | O(log n) |
| `top()` | O(1) |
| `empty()` | O(1) |
| `size()` | O(1) |

## Space Complexity

- **Heap Storage**: O(n) where n is number of elements
- **Auxiliary Space**: O(1) for operations (excluding storage)

## When to Use Heap

1. **K Largest/Smallest**: Finding top K elements
2. **K-way Merge**: Merging K sorted sequences
3. **Scheduling**: Meeting rooms, task scheduling
4. **Shortest Path**: Dijkstra's algorithm
5. **Median Finding**: Two heaps pattern
6. **Frequency Problems**: Top K frequent elements

## Common Mistakes

1. **Wrong Comparator**: Using `>` instead of `<` (or vice versa) for min/max heap
2. **Not Handling Empty**: Accessing `top()` without checking `empty()`
3. **Wrong Heap Type**: Using max heap when min heap is needed
4. **Not Maintaining Size**: Forgetting to pop when size exceeds K
5. **Custom Comparator Logic**: Reversing the comparison logic incorrectly

## Related Data Structures

- **Set/Multiset**: For maintaining sorted order with duplicates
- **Map**: For frequency counting before heap operations
- **Deque**: For sliding window problems (alternative to heap)

## Summary Table

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Min Heap | "k largest", "sort" | Keep smallest on top |
| Max Heap | "k smallest" | Keep largest on top |
| K-way Merge | "merge k sorted" | Push heads, pop smallest |
| Top K | "kth largest", "top k frequent" | Heap of size k |
| Two Heaps | "median", "sliding median" | Max-heap for lower half, min-heap for upper |
| Dijkstra | "shortest path", "minimum cost" | Greedy + min-heap |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (heap, monotonic queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph (Dijkstra):** [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)

{% endraw %}

