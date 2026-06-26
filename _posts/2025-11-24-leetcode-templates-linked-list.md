---
layout: post
title: "Algorithm Templates: Linked List"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates linked-list
permalink: /posts/2025-11-24-leetcode-templates-linked-list/
tags: [leetcode, templates, linked-list]
---

{% raw %}
This page collects battle-tested C++ templates for every major linked-list pattern you'll see on LeetCode. Each section includes ready-to-use code, the signal phrases that tell you which pattern to reach for, and a quick explanation of the core idea. Bookmark it, copy what you need, and focus your energy on the actual problem logic.

> **New to Linked Lists?** A linked list is a chain of nodes where each node points to the next. Unlike arrays, you can't jump to index *i* — you must walk from the head. The tradeoff: O(1) insert/delete at known positions, but O(n) access.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="max-width:680px;width:100%;height:auto;display:block;margin:1.5em auto">
  <style>
    .ll-node { fill: #A8B5A2; stroke: #6B7D65; stroke-width: 1.5; rx: 8; }
    .ll-dummy { fill: #C4A882; stroke: #9A7E5A; stroke-width: 1.5; rx: 8; }
    .ll-null { fill: #D4A5A5; stroke: #B07878; stroke-width: 1.5; rx: 8; }
    .ll-text { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 14px; fill: #3A3A3A; text-anchor: middle; dominant-baseline: central; }
    .ll-label { font-family: system-ui, -apple-system, sans-serif; font-size: 12px; fill: #6B6B6B; text-anchor: middle; }
    .ll-title { font-family: system-ui, -apple-system, sans-serif; font-size: 13px; fill: #555; font-weight: 600; }
    .ll-arrow { stroke: #7A7A7A; stroke-width: 1.5; fill: none; marker-end: url(#arrowhead); }
  </style>
  <defs>
    <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#7A7A7A"/>
    </marker>
  </defs>
  <!-- Row 1: Basic linked list -->
  <text x="30" y="18" class="ll-title">Basic linked list</text>
  <text x="55" y="45" class="ll-label">head</text>
  <line x1="55" y1="52" x2="55" y2="62" stroke="#999" stroke-width="1" marker-end="url(#arrowhead)"/>
  <rect x="20" y="65" width="70" height="35" class="ll-node"/>
  <text x="55" y="82" class="ll-text">1</text>
  <line x1="90" y1="82" x2="130" y2="82" class="ll-arrow"/>
  <rect x="130" y="65" width="70" height="35" class="ll-node"/>
  <text x="165" y="82" class="ll-text">2</text>
  <line x1="200" y1="82" x2="240" y2="82" class="ll-arrow"/>
  <rect x="240" y="65" width="70" height="35" class="ll-node"/>
  <text x="275" y="82" class="ll-text">3</text>
  <line x1="310" y1="82" x2="350" y2="82" class="ll-arrow"/>
  <rect x="350" y="65" width="70" height="35" class="ll-null"/>
  <text x="385" y="82" class="ll-text">null</text>
  <!-- Row 2: Dummy node pattern -->
  <text x="30" y="142" class="ll-title">Dummy node pattern</text>
  <text x="55" y="162" class="ll-label">dummy</text>
  <line x1="55" y1="169" x2="55" y2="177" stroke="#999" stroke-width="1" marker-end="url(#arrowhead)"/>
  <rect x="20" y="180" width="70" height="35" class="ll-dummy"/>
  <text x="55" y="197" class="ll-text">0</text>
  <line x1="90" y1="197" x2="130" y2="197" class="ll-arrow"/>
  <text x="165" y="162" class="ll-label">head</text>
  <line x1="165" y1="169" x2="165" y2="177" stroke="#999" stroke-width="1" marker-end="url(#arrowhead)"/>
  <rect x="130" y="180" width="70" height="35" class="ll-node"/>
  <text x="165" y="197" class="ll-text">1</text>
  <line x1="200" y1="197" x2="240" y2="197" class="ll-arrow"/>
  <rect x="240" y="180" width="70" height="35" class="ll-node"/>
  <text x="275" y="197" class="ll-text">2</text>
  <line x1="310" y1="197" x2="350" y2="197" class="ll-arrow"/>
  <rect x="350" y="180" width="70" height="35" class="ll-node"/>
  <text x="385" y="197" class="ll-text">3</text>
  <line x1="420" y1="197" x2="460" y2="197" class="ll-arrow"/>
  <rect x="460" y="180" width="70" height="35" class="ll-null"/>
  <text x="495" y="197" class="ll-text">null</text>
</svg>

## Contents

- [ListNode Definition](#listnode-definition)
- [Basic Operations](#basic-operations)
- [Two Pointers](#two-pointers)
- [Dummy Node Pattern](#dummy-node-pattern)
- [Reversal](#reversal)
- [Merge](#merge)
- [Cycle Detection](#cycle-detection)
- [Circular Linked List](#circular-linked-list)

## ListNode Definition

**When to use:** Every linked-list problem — this is the building block. Know the struct by heart so you never waste time on boilerplate.

### Standard Definition

```cpp
// Standard ListNode definition used in LeetCode
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
```

### Alternative Definitions

```cpp
// Without default constructor
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// With pointer initialization
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x = 0) : val(x), next(nullptr) {}
};
```

### Common Construction Methods

```cpp
// Method 1: Manual construction
ListNode* createList(vector<int>& values) {
    if (values.empty()) return nullptr;
    
    ListNode* head = new ListNode(values[0]);
    ListNode* cur = head;
    
    for (int i = 1; i < values.size(); ++i) {
        cur->next = new ListNode(values[i]);
        cur = cur->next;
    }
    
    return head;
}

// Method 2: Recursive construction
ListNode* createListRecursive(vector<int>& values, int index) {
    if (index >= values.size()) return nullptr;
    ListNode* node = new ListNode(values[index]);
    node->next = createListRecursive(values, index + 1);
    return node;
}

// Method 3: Using dummy node
ListNode* createListWithDummy(vector<int>& values) {
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    
    for (int val : values) {
        cur->next = new ListNode(val);
        cur = cur->next;
    }
    
    return dummy->next;
}

// Method 4: Create list from array
ListNode* createListFromArray(int arr[], int n) {
    if (n == 0) return nullptr;
    
    ListNode* head = new ListNode(arr[0]);
    ListNode* cur = head;
    
    for (int i = 1; i < n; ++i) {
        cur->next = new ListNode(arr[i]);
        cur = cur->next;
    }
    
    return head;
}
```

### Utility Functions

```cpp
// Print linked list (for debugging)
void printList(ListNode* head) {
    ListNode* cur = head;
    while (cur != nullptr) {
        cout << cur->val;
        if (cur->next != nullptr) cout << " -> ";
        cur = cur->next;
    }
    cout << endl;
}

// Get length of linked list
int getLength(ListNode* head) {
    int length = 0;
    ListNode* cur = head;
    while (cur != nullptr) {
        length++;
        cur = cur->next;
    }
    return length;
}

// Convert linked list to vector
vector<int> listToVector(ListNode* head) {
    vector<int> result;
    ListNode* cur = head;
    while (cur != nullptr) {
        result.push_back(cur->val);
        cur = cur->next;
    }
    return result;
}

// Delete entire linked list (free memory)
void deleteList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}
```

### Example Usage

```cpp
// Example: Create list [1, 2, 3, 4, 5]
vector<int> values = {1, 2, 3, 4, 5};
ListNode* head = createList(values);

// Print the list
printList(head);  // Output: 1 -> 2 -> 3 -> 4 -> 5

// Get length
int len = getLength(head);  // len = 5

// Convert to vector
vector<int> vec = listToVector(head);  // vec = [1, 2, 3, 4, 5]

// Clean up
deleteList(head);
```

## Basic Operations

**When to use:** You need to "visit every node", "count nodes", "find a value", or "collect values into an array". Also the foundation for insert/delete at arbitrary positions.

### Traversal

```cpp
// Iterative traversal
void traverse(ListNode* head) {
    ListNode* cur = head;
    while (cur != nullptr) {
        // Process cur->val
        cur = cur->next;
    }
}

// Recursive traversal
void traverseRecursive(ListNode* head) {
    if (head == nullptr) return;
    // Process head->val
    traverseRecursive(head->next);
}
```

### Insertion

```cpp
// Insert at head
ListNode* insertAtHead(ListNode* head, int val) {
    ListNode* newNode = new ListNode(val);
    newNode->next = head;
    return newNode;
}

// Insert after node
void insertAfter(ListNode* node, int val) {
    ListNode* newNode = new ListNode(val);
    newNode->next = node->next;
    node->next = newNode;
}
```

### Deletion

```cpp
// Delete node (given node to delete, not head)
void deleteNode(ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;
}

// Delete node with value
ListNode* deleteNode(ListNode* head, int val) {
    if (head == nullptr) return nullptr;
    if (head->val == val) return head->next;
    
    ListNode* cur = head;
    while (cur->next != nullptr) {
        if (cur->next->val == val) {
            cur->next = cur->next->next;
            break;
        }
        cur = cur->next;
    }
    return head;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 203 | Remove Linked List Elements | [Link](https://leetcode.com/problems/remove-linked-list-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-203-remove-linked-list-elements/) |
| 237 | Delete Node in a Linked List | [Link](https://leetcode.com/problems/delete-node-in-a-linked-list/) | - |

## Two Pointers

**When to use:** The problem says "middle of list", "kth from end", "intersection of two lists", or "split list into halves". Use fast/slow pointers to solve in one pass without knowing the length.

### Fast and Slow Pointers

```cpp
// Find middle node
ListNode* findMiddle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}

// Find kth node from end
ListNode* findKthFromEnd(ListNode* head, int k) {
    ListNode* fast = head;
    for (int i = 0; i < k; ++i) {
        if (fast == nullptr) return nullptr;
        fast = fast->next;
    }
    ListNode* slow = head;
    while (fast != nullptr) {
        slow = slow->next;
        fast = fast->next;
    }
    return slow;
}
```

### Two Pointers for Partitioning

```cpp
// Partition list around value x
ListNode* partition(ListNode* head, int x) {
    ListNode* less = new ListNode(0);
    ListNode* greater = new ListNode(0);
    ListNode* lessCur = less;
    ListNode* greaterCur = greater;
    
    while (head != nullptr) {
        if (head->val < x) {
            lessCur->next = head;
            lessCur = lessCur->next;
        } else {
            greaterCur->next = head;
            greaterCur = greaterCur->next;
        }
        head = head->next;
    }
    
    greaterCur->next = nullptr;
    lessCur->next = greater->next;
    return less->next;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 876 | Middle of the Linked List | [Link](https://leetcode.com/problems/middle-of-the-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/10/easy-876-middle-of-the-linked-list/) |
| 19 | Remove Nth Node From End of List | [Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | - |

## Dummy Node Pattern

**When to use:** The problem involves "delete head", "merge lists", "insert at front", or any operation where the head might change. A dummy node in front of head eliminates null-check edge cases.

```cpp
// Remove elements with dummy node
ListNode* removeElements(ListNode* head, int val) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* cur = dummy;
    
    while (cur->next != nullptr) {
        if (cur->next->val == val) {
            cur->next = cur->next->next;
        } else {
            cur = cur->next;
        }
    }
    
    return dummy->next;
}
```

**Key Benefits:**
- Handles empty list case
- Simplifies head deletion
- Reduces special case handling

| ID | Title | Link | Solution |
|---|---|---|---|
| 203 | Remove Linked List Elements | [Link](https://leetcode.com/problems/remove-linked-list-elements/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-easy-203-remove-linked-list-elements/) |

## Reversal

**When to use:** The problem says "reverse linked list", "reverse between positions", "reverse in groups of k", or "palindrome linked list". The core trick is rewiring `next` pointers as you walk.

### Reverse Entire List

```cpp
// Iterative reversal
ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    ListNode* cur = head;
    while (cur != nullptr) {
        ListNode* next = cur->next;
        cur->next = prev;
        prev = cur;
        cur = next;
    }
    return prev;
}

// Recursive reversal
ListNode* reverseListRecursive(ListNode* head) {
    if (head == nullptr || head->next == nullptr) return head;
    ListNode* newHead = reverseListRecursive(head->next);
    head->next->next = head;
    head->next = nullptr;
    return newHead;
}
```

### Reverse Between Positions

```cpp
// Reverse nodes from position left to right
ListNode* reverseBetween(ListNode* head, int left, int right) {
    ListNode* dummy = new ListNode(0);
    dummy->next = head;
    ListNode* prev = dummy;
    
    // Move to left position
    for (int i = 1; i < left; ++i) {
        prev = prev->next;
    }
    
    // Reverse
    ListNode* cur = prev->next;
    for (int i = 0; i < right - left; ++i) {
        ListNode* next = cur->next;
        cur->next = next->next;
        next->next = prev->next;
        prev->next = next;
    }
    
    return dummy->next;
}
```

### Reverse in Groups

```cpp
// Reverse nodes in k-group
ListNode* reverseKGroup(ListNode* head, int k) {
    ListNode* cur = head;
    int count = 0;
    while (cur != nullptr && count < k) {
        cur = cur->next;
        count++;
    }
    
    if (count == k) {
        cur = reverseKGroup(cur, k);
        while (count-- > 0) {
            ListNode* next = head->next;
            head->next = cur;
            cur = head;
            head = next;
        }
        head = cur;
    }
    return head;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 206 | Reverse Linked List | [Link](https://leetcode.com/problems/reverse-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-16-easy-206-reverse-linked-list/) |
| 92 | Reverse Linked List II | [Link](https://leetcode.com/problems/reverse-linked-list-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/16/medium-92-reverse-linked-list-ii/) |
| 25 | Reverse Nodes in k-Group | [Link](https://leetcode.com/problems/reverse-nodes-in-k-group/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/hard-25-reverse-nodes-in-k-group/) |
| 24 | Swap Nodes in Pairs | [Link](https://leetcode.com/problems/swap-nodes-in-pairs/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/24/medium-23-swap-nodes-in-pairs/) |

## Merge

**When to use:** The problem says "merge two sorted lists", "merge k sorted lists", or "add two numbers represented as lists". Compare heads, advance the smaller, and use a dummy node to collect the result.

### Merge Two Sorted Lists

```cpp
// Merge two sorted lists
ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    ListNode* dummy = new ListNode(0);
    ListNode* cur = dummy;
    
    while (list1 != nullptr && list2 != nullptr) {
        if (list1->val <= list2->val) {
            cur->next = list1;
            list1 = list1->next;
        } else {
            cur->next = list2;
            list2 = list2->next;
        }
        cur = cur->next;
    }
    
    cur->next = (list1 != nullptr) ? list1 : list2;
    return dummy->next;
}
```

### Merge K Sorted Lists

```cpp
// Merge k sorted lists using divide and conquer
ListNode* mergeKLists(vector<ListNode*>& lists) {
    if (lists.empty()) return nullptr;
    return mergeKListsHelper(lists, 0, lists.size() - 1);
}

ListNode* mergeKListsHelper(vector<ListNode*>& lists, int left, int right) {
    if (left == right) return lists[left];
    int mid = left + (right - left) / 2;
    ListNode* leftList = mergeKListsHelper(lists, left, mid);
    ListNode* rightList = mergeKListsHelper(lists, mid + 1, right);
    return mergeTwoLists(leftList, rightList);
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 21 | Merge Two Sorted Lists | [Link](https://leetcode.com/problems/merge-two-sorted-lists/) | - |
| 23 | Merge k Sorted Lists | [Link](https://leetcode.com/problems/merge-k-sorted-lists/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/02/15/hard-23-merge-k-sorted-lists/) |
| 2 | Add Two Numbers | [Link](https://leetcode.com/problems/add-two-numbers/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-18-medium-2-add-two-numbers/) |
| 1669 | Merge In Between Linked Lists | [Link](https://leetcode.com/problems/merge-in-between-linked-lists/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/15/medium-1669-merge-in-between-linked-lists/) |

## Cycle Detection

**When to use:** The problem asks "has cycle", "find cycle start", or "find the duplicate number" (which reduces to cycle detection). Floyd's algorithm: if fast and slow meet, there's a cycle.

### Detect Cycle (Floyd's Algorithm)

```cpp
// Detect cycle using Floyd's cycle detection
bool hasCycle(ListNode* head) {
    if (head == nullptr || head->next == nullptr) return false;
    
    ListNode* slow = head;
    ListNode* fast = head;
    
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    
    return false;
}

// Find cycle start node
ListNode* detectCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    
    // Find meeting point
    while (fast != nullptr && fast->next != nullptr) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) break;
    }
    
    if (fast == nullptr || fast->next == nullptr) return nullptr;
    
    // Find cycle start
    slow = head;
    while (slow != fast) {
        slow = slow->next;
        fast = fast->next;
    }
    
    return slow;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 141 | Linked List Cycle | [Link](https://leetcode.com/problems/linked-list-cycle/) | - |
| 142 | Linked List Cycle II | [Link](https://leetcode.com/problems/linked-list-cycle-ii/) | - |

## Circular Linked List

**When to use:** The problem mentions "circular linked list", "sorted circular list", or "rotate list". The key difference from normal lists: the tail's `next` points back to the head instead of `nullptr`.

### Insert into Sorted Circular List

```cpp
// Insert into sorted circular linked list
ListNode* insert(ListNode* head, int insertVal) {
    if (head == nullptr) {
        ListNode* newNode = new ListNode(insertVal);
        newNode->next = newNode;
        return newNode;
    }
    
    ListNode* prev = head;
    ListNode* cur = head->next;
    
    while (cur != head) {
        // Normal insertion point
        if (prev->val <= insertVal && insertVal <= cur->val) {
            break;
        }
        // At the boundary (largest to smallest)
        if (prev->val > cur->val && (insertVal >= prev->val || insertVal <= cur->val)) {
            break;
        }
        prev = cur;
        cur = cur->next;
    }
    
    prev->next = new ListNode(insertVal);
    prev->next->next = cur;
    return head;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 708 | Insert into a Sorted Circular Linked List | [Link](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-10-27-medium-708-insert-into-a-sorted-circular-linked-list/) |
| 382 | Linked List Random Node | [Link](https://leetcode.com/problems/linked-list-random-node/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/04/08/medium-382-linked-list-random-node/) |

## Quick-Reference Summary

| Pattern | Signal Phrases | Key Idea |
|---|---|---|
| Two Pointers | "middle", "kth from end", "intersection" | Fast moves 2x, slow moves 1x |
| Dummy Node | "delete head", "merge", "insert at front" | Avoids null-check edge cases |
| Reversal | "reverse list", "reverse between" | Rewire next pointers |
| Merge | "merge sorted", "merge k lists" | Compare heads, advance smaller |
| Cycle Detection | "has cycle", "cycle start" | Floyd's: fast meets slow = cycle |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures (pointers, recursion):** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/)
- **Graph, Search:** [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
{% endraw %}

