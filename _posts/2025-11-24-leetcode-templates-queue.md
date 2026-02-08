---
layout: post
title: "Algorithm Templates: Queue"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates queue
permalink: /posts/2025-11-24-leetcode-templates-queue/
tags: [leetcode, templates, queue, data-structures]
---

{% raw %}
Minimal, copy-paste C++ for BFS queue, monotonic queue, priority queue, circular queue, and deque. See also [Graph](/posts/2025-10-29-leetcode-templates-graph/) and [Data Structures](/posts/2025-10-29-leetcode-templates-data-structures/) (monotonic queue).

## Contents

- [Basic Queue Operations](#basic-queue-operations)
- [BFS with Queue](#bfs-with-queue)
- [Monotonic Queue](#monotonic-queue)
- [Priority Queue](#priority-queue)
- [Circular Queue](#circular-queue)
- [Double-ended Queue (Deque)](#double-ended-queue-deque)

## Basic Queue Operations

```cpp
#include <queue>

// Standard queue operations
queue<int> q;
q.push(1);        // Enqueue
q.front();        // Peek front
q.back();         // Peek back
q.pop();          // Dequeue
q.empty();        // Check if empty
q.size();         // Get size
```

### Implement Queue using Stacks

```cpp
class MyQueue {
    stack<int> input, output;
public:
    void push(int x) {
        input.push(x);
    }
    
    int pop() {
        peek();
        int val = output.top();
        output.pop();
        return val;
    }
    
    int peek() {
        if (output.empty()) {
            while (!input.empty()) {
                output.push(input.top());
                input.pop();
            }
        }
        return output.top();
    }
    
    bool empty() {
        return input.empty() && output.empty();
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 232 | Implement Queue using Stacks | [Link](https://leetcode.com/problems/implement-queue-using-stacks/) | - |

## BFS with Queue

Queue is essential for Breadth-First Search (level-order traversal).

```cpp
// BFS on graph
void bfs(vector<vector<int>>& graph, int start) {
    queue<int> q;
    vector<bool> visited(graph.size(), false);
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int node = q.front();
        q.pop();
        // Process node
        
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                visited[neighbor] = true;
                q.push(neighbor);
            }
        }
    }
}

// Level-order traversal (BFS on tree)
vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> result;
    if (!root) return result;
    
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        int size = q.size();
        vector<int> level;
        
        for (int i = 0; i < size; ++i) {
            TreeNode* node = q.front();
            q.pop();
            level.push_back(node->val);
            
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        
        result.push_back(level);
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 102 | Binary Tree Level Order Traversal | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal/) | - |
| 107 | Binary Tree Level Order Traversal II | [Link](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/) | - |

## Monotonic Queue

Maintain queue with monotonic property (increasing or decreasing).

```cpp
// Monotonic decreasing queue (for sliding window maximum)
class MonotonicQueue {
    deque<int> dq;
public:
    void push(int val) {
        // Remove elements smaller than val
        while (!dq.empty() && dq.back() < val) {
            dq.pop_back();
        }
        dq.push_back(val);
    }
    
    void pop(int val) {
        if (!dq.empty() && dq.front() == val) {
            dq.pop_front();
        }
    }
    
    int max() {
        return dq.front();
    }
};

// Sliding Window Maximum
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    MonotonicQueue mq;
    vector<int> result;
    
    for (int i = 0; i < nums.size(); ++i) {
        if (i < k - 1) {
            mq.push(nums[i]);
        } else {
            mq.push(nums[i]);
            result.push_back(mq.max());
            mq.pop(nums[i - k + 1]);
        }
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 1438 | Longest Continuous Subarray With Absolute Diff <= Limit | [Link](https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/) | - |

## Priority Queue

Priority queue (heap) for maintaining order.

```cpp
#include <queue>
#include <vector>

// Max heap (default)
priority_queue<int> maxHeap;

// Min heap
priority_queue<int, vector<int>, greater<int>> minHeap;

// Custom comparator using struct
struct Compare {
    bool operator()(pair<int, int>& a, pair<int, int>& b) {
        return a.second > b.second; // Min heap by second element
    }
};
priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq;

// Custom comparator using lambda operator
auto cmp = [](pair<int, int>& a, pair<int, int>& b) {
    return a.second > b.second; // Min heap by second element
};
priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);

// Lambda example: Min heap by distance (for Dijkstra's algorithm)
auto distCmp = [](pair<int, int>& a, pair<int, int>& b) {
    return a.first > b.first; // {distance, node} - min heap by distance
};
priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(distCmp)> pq(distCmp);
```

### K-way Merge

```cpp
// Merge k sorted lists using priority queue
ListNode* mergeKLists(vector<ListNode*>& lists) {
    auto cmp = [](ListNode* a, ListNode* b) { return a->val > b->val; };
    priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> pq(cmp);
    
    for (ListNode* list : lists) {
        if (list) pq.push(list);
    }
    
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    
    while (!pq.empty()) {
        ListNode* node = pq.top();
        pq.pop();
        cur->next = node;
        cur = cur->next;
        if (node->next) pq.push(node->next);
    }
    
    return dummy->next;
}
```

### Top K Elements

```cpp
// Find top k frequent elements
vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) freq[num]++;
    
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    
    for (auto& [num, count] : freq) {
        pq.push({count, num});
        if (pq.size() > k) pq.pop();
    }
    
    vector<int> result;
    while (!pq.empty()) {
        result.push_back(pq.top().second);
        pq.pop();
    }
    
    return result;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | - |
| 347 | Top K Frequent Elements | [Link](https://leetcode.com/problems/top-k-frequent-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-21-medium-347-top-k-frequent-elements/) |
| 295 | Find Median from Data Stream | [Link](https://leetcode.com/problems/find-median-from-data-stream/) | - |
| 215 | Kth Largest Element in an Array | [Link](https://leetcode.com/problems/kth-largest-element-in-an-array/) | - |
| 973 | K Closest Points to Origin | [Link](https://leetcode.com/problems/k-closest-points-to-origin/) | - |
| 253 | Meeting Rooms II | [Link](https://leetcode.com/problems/meeting-rooms-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-12-11-medium-253-meeting-rooms-ii/) |
| 378 | Kth Smallest Element in a Sorted Matrix | [Link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) | - |
| 703 | Kth Largest Element in a Stream | [Link](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | - |
| 767 | Reorganize String | [Link](https://leetcode.com/problems/reorganize-string/) | - |
| 1046 | Last Stone Weight | [Link](https://leetcode.com/problems/last-stone-weight/) | - |
| 1167 | Minimum Cost to Connect Sticks | [Link](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) | - |
| 621 | Task Scheduler | [Link](https://leetcode.com/problems/task-scheduler/) | - |
| 743 | Network Delay Time | [Link](https://leetcode.com/problems/network-delay-time/) | - |
| 787 | Cheapest Flights Within K Stops | [Link](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | - |

## Circular Queue

```cpp
class MyCircularQueue {
    vector<int> data;
    int head, tail, size, capacity;
public:
    MyCircularQueue(int k) : data(k), head(0), tail(0), size(0), capacity(k) {}
    
    bool enQueue(int value) {
        if (isFull()) return false;
        data[tail] = value;
        tail = (tail + 1) % capacity;
        size++;
        return true;
    }
    
    bool deQueue() {
        if (isEmpty()) return false;
        head = (head + 1) % capacity;
        size--;
        return true;
    }
    
    int Front() {
        return isEmpty() ? -1 : data[head];
    }
    
    int Rear() {
        return isEmpty() ? -1 : data[(tail - 1 + capacity) % capacity];
    }
    
    bool isEmpty() {
        return size == 0;
    }
    
    bool isFull() {
        return size == capacity;
    }
};
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 622 | Design Circular Queue | [Link](https://leetcode.com/problems/design-circular-queue/) | - |

## Double-ended Queue (Deque)

```cpp
#include <deque>

deque<int> dq;
dq.push_front(1);  // Add to front
dq.push_back(2);   // Add to back
dq.pop_front();     // Remove from front
dq.pop_back();      // Remove from back
dq.front();         // Access front
dq.back();          // Access back
```

### Sliding Window with Deque

```cpp
// Sliding window maximum using deque
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;
    vector<int> result;
    
    for (int i = 0; i < nums.size(); ++i) {
        // Remove indices outside window
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }
        
        // Remove indices with smaller values
        while (!dq.empty() && nums[dq.back()] <= nums[i]) {
            dq.pop_back();
        }
        
        dq.push_back(i);
        
        if (i >= k - 1) {
            result.push_back(nums[dq.front()]);
        }
    }
    
    return result;
}
```

### Two Deques Pattern (Middle Element Access)

Use two deques to efficiently access middle elements in a queue.

```cpp
// Front Middle Back Queue: Two deques with rebalancing
class FrontMiddleBackQueue {
    deque<int> front_cache, back_cache;
    
    void rebalance() {
        // Maintain: front_cache.size() <= back_cache.size() <= front_cache.size() + 1
        while(front_cache.size() > back_cache.size()) {
            back_cache.push_front(front_cache.back());
            front_cache.pop_back();
        }
        while(back_cache.size() > front_cache.size() + 1) {
            front_cache.push_back(back_cache.front());
            back_cache.pop_front();
        }
    }
    
public:
    void pushMiddle(int val) {
        front_cache.push_back(val);
        rebalance();
    }
    
    int popMiddle() {
        if(front_cache.empty() && back_cache.empty()) return -1;
        if(front_cache.size() == back_cache.size()) {
            int val = front_cache.back();
            front_cache.pop_back();
            return val;
        } else {
            int val = back_cache.front();
            back_cache.pop_front();
            return val;
        }
    }
};
```

**Key points:**
- Split queue into two halves: `front_cache` and `back_cache`
- Maintain balance: `front_cache.size() <= back_cache.size() <= front_cache.size() + 1`
- Middle element is `front_cache.back()` (if sizes equal) or `back_cache.front()` (if back_cache larger)
- Rebalance after each modification

| ID | Title | Link | Solution |
|---|---|---|---|
| 239 | Sliding Window Maximum | [Link](https://leetcode.com/problems/sliding-window-maximum/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-04-hard-239-sliding-window-maximum/) |
| 1670 | Design Front Middle Back Queue | [Link](https://leetcode.com/problems/design-front-middle-back-queue/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/13/medium-1670-design-front-middle-back-queue/) |

## More templates

- **Data structures (monotonic queue):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **BFS, Graph:** [BFS](/posts/2025-11-24-leetcode-templates-bfs/), [Graph](/posts/2025-10-29-leetcode-templates-graph/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

