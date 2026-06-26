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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 300" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="fsp-arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#B8B5B0"/>
    </marker>
  </defs>
  <text x="320" y="14" font-size="11.5" fill="#7A7772" text-anchor="middle" font-style="italic">slow moves 1 step · fast moves 2 steps</text>
  <!-- Row 0: Initial — slow & fast both at node 1 -->
  <text x="12" y="63" font-size="12" font-weight="600" fill="#5A5752">Initial</text>
  <text x="137" y="28" font-size="11" fill="#6B8B6B" text-anchor="middle" font-weight="600">slow</text>
  <path d="M133,33 L137,41 L141,33 Z" fill="#6B8B6B"/>
  <path d="M133,91 L137,83 L141,91 Z" fill="#6B7B9B"/>
  <text x="137" y="104" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">fast</text>
  <rect x="110" y="48" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="137" y="62" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="165" y1="62" x2="200" y2="62" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="200" y="48" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="227" y="62" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="255" y1="62" x2="290" y2="62" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="290" y="48" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="317" y="62" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="345" y1="62" x2="380" y2="62" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="380" y="48" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="407" y="62" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="435" y1="62" x2="470" y2="62" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="470" y="48" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="497" y="62" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
  <!-- Row 1: Step 1 — slow at node 2, fast at node 3 -->
  <text x="12" y="157" font-size="12" font-weight="600" fill="#5A5752">Step 1</text>
  <text x="227" y="122" font-size="11" fill="#6B8B6B" text-anchor="middle" font-weight="600">slow</text>
  <path d="M223,127 L227,135 L231,127 Z" fill="#6B8B6B"/>
  <path d="M313,183 L317,175 L321,183 Z" fill="#6B7B9B"/>
  <text x="317" y="196" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">fast</text>
  <rect x="110" y="142" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="137" y="156" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="165" y1="156" x2="200" y2="156" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="200" y="142" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="227" y="156" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="255" y1="156" x2="290" y2="156" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="290" y="142" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="317" y="156" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="345" y1="156" x2="380" y2="156" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="380" y="142" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="407" y="156" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="435" y1="156" x2="470" y2="156" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="470" y="142" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="497" y="156" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
  <!-- Row 2: Step 2 — slow at middle (node 3), fast at end (node 5) -->
  <text x="12" y="251" font-size="12" font-weight="600" fill="#5A5752">Step 2</text>
  <text x="317" y="216" font-size="11" fill="#6B8B6B" text-anchor="middle" font-weight="600">slow</text>
  <path d="M313,221 L317,229 L321,221 Z" fill="#6B8B6B"/>
  <path d="M493,277 L497,269 L501,277 Z" fill="#6B7B9B"/>
  <text x="497" y="290" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">fast</text>
  <rect x="110" y="236" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="137" y="250" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="165" y1="250" x2="200" y2="250" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="200" y="236" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="227" y="250" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="255" y1="250" x2="290" y2="250" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="290" y="236" width="55" height="28" rx="6" fill="#D4D8D0" stroke="#8B8680" stroke-width="2"/>
  <text x="317" y="250" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <text x="317" y="278" font-size="10" fill="#6B8B6B" text-anchor="middle" font-style="italic">middle</text>
  <line x1="345" y1="250" x2="380" y2="250" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="380" y="236" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="407" y="250" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="435" y1="250" x2="470" y2="250" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#fsp-arr)"/>
  <rect x="470" y="236" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="497" y="250" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
</svg>

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 295" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="rv-fwd" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#B8B5B0"/>
    </marker>
    <marker id="rv-rev" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#B07878"/>
    </marker>
  </defs>
  <!-- Step 1: prev=null, curr=1, next=2 — all forward links -->
  <text x="12" y="66" font-size="12" font-weight="600" fill="#5A5752">Step 1</text>
  <text x="125" y="30" font-size="11" fill="#9A7E5A" text-anchor="middle" font-weight="600">prev</text>
  <path d="M121,35 L125,43 L129,35 Z" fill="#9A7E5A"/>
  <text x="200" y="30" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">curr</text>
  <path d="M196,35 L200,43 L204,35 Z" fill="#6B7B9B"/>
  <text x="285" y="30" font-size="11" fill="#8B8680" text-anchor="middle" font-weight="600">next</text>
  <path d="M281,35 L285,43 L289,35 Z" fill="#8B8680"/>
  <rect x="105" y="50" width="40" height="28" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="125" y="64" font-size="11" fill="#7A7772" text-anchor="middle" dominant-baseline="central">null</text>
  <rect x="175" y="50" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="200" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="225" y1="64" x2="260" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#rv-fwd)"/>
  <rect x="260" y="50" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="285" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="310" y1="64" x2="345" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#rv-fwd)"/>
  <rect x="345" y="50" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="395" y1="64" x2="430" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#rv-fwd)"/>
  <rect x="430" y="50" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="455" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <!-- Step 2: prev=1, curr=2, next=3 — node 1 reversed to null -->
  <text x="12" y="162" font-size="12" font-weight="600" fill="#5A5752">Step 2</text>
  <text x="200" y="126" font-size="11" fill="#9A7E5A" text-anchor="middle" font-weight="600">prev</text>
  <path d="M196,131 L200,139 L204,131 Z" fill="#9A7E5A"/>
  <text x="285" y="126" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">curr</text>
  <path d="M281,131 L285,139 L289,131 Z" fill="#6B7B9B"/>
  <text x="370" y="126" font-size="11" fill="#8B8680" text-anchor="middle" font-weight="600">next</text>
  <path d="M366,131 L370,139 L374,131 Z" fill="#8B8680"/>
  <rect x="105" y="146" width="40" height="28" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="125" y="160" font-size="11" fill="#7A7772" text-anchor="middle" dominant-baseline="central">null</text>
  <rect x="175" y="146" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B07878" stroke-width="1.5"/>
  <text x="200" y="160" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="175" y1="160" x2="145" y2="160" stroke="#B07878" stroke-width="1.5" marker-end="url(#rv-rev)"/>
  <rect x="260" y="146" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="285" y="160" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="310" y1="160" x2="345" y2="160" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#rv-fwd)"/>
  <rect x="345" y="146" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="160" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="395" y1="160" x2="430" y2="160" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#rv-fwd)"/>
  <rect x="430" y="146" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="455" y="160" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <!-- Step 3: prev=2, curr=3, next=4 — nodes 1,2 reversed -->
  <text x="12" y="258" font-size="12" font-weight="600" fill="#5A5752">Step 3</text>
  <text x="285" y="222" font-size="11" fill="#9A7E5A" text-anchor="middle" font-weight="600">prev</text>
  <path d="M281,227 L285,235 L289,227 Z" fill="#9A7E5A"/>
  <text x="370" y="222" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">curr</text>
  <path d="M366,227 L370,235 L374,227 Z" fill="#6B7B9B"/>
  <text x="455" y="222" font-size="11" fill="#8B8680" text-anchor="middle" font-weight="600">next</text>
  <path d="M451,227 L455,235 L459,227 Z" fill="#8B8680"/>
  <rect x="105" y="242" width="40" height="28" rx="6" fill="#F0EBE6" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="125" y="256" font-size="11" fill="#7A7772" text-anchor="middle" dominant-baseline="central">null</text>
  <rect x="175" y="242" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B07878" stroke-width="1.5"/>
  <text x="200" y="256" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="175" y1="256" x2="145" y2="256" stroke="#B07878" stroke-width="1.5" marker-end="url(#rv-rev)"/>
  <rect x="260" y="242" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B07878" stroke-width="1.5"/>
  <text x="285" y="256" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="260" y1="256" x2="225" y2="256" stroke="#B07878" stroke-width="1.5" marker-end="url(#rv-rev)"/>
  <rect x="345" y="242" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="256" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="395" y1="256" x2="430" y2="256" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#rv-fwd)"/>
  <rect x="430" y="242" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="455" y="256" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <!-- Legend -->
  <text x="540" y="258" font-size="10" fill="#B07878">← reversed</text>
  <text x="540" y="272" font-size="10" fill="#B8B5B0">→ original</text>
</svg>

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 220" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="mg-arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#B8B5B0"/>
    </marker>
    <marker id="mg-warm" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <path d="M0,0 L6,2.5 L0,5 Z" fill="#B07878"/>
    </marker>
    <marker id="mg-cool" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
      <path d="M0,0 L6,2.5 L0,5 Z" fill="#7A8A9A"/>
    </marker>
  </defs>
  <!-- Source lists -->
  <text x="22" y="42" font-size="12" font-weight="600" fill="#5A5752">list1</text>
  <rect x="70" y="28" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="95" y="42" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="120" y1="42" x2="155" y2="42" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="155" y="28" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="180" y="42" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="205" y1="42" x2="240" y2="42" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="240" y="28" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="265" y="42" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
  <text x="380" y="42" font-size="12" font-weight="600" fill="#5A5752">list2</text>
  <rect x="420" y="28" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="445" y="42" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="470" y1="42" x2="505" y2="42" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="505" y="28" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="530" y="42" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="555" y1="42" x2="590" y2="42" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="590" y="28" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="615" y="42" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">6</text>
  <!-- Dashed arrows from source to result -->
  <line x1="95" y1="56" x2="55" y2="148" stroke="#B07878" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#mg-warm)"/>
  <line x1="180" y1="56" x2="225" y2="148" stroke="#B07878" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#mg-warm)"/>
  <line x1="265" y1="56" x2="395" y2="148" stroke="#B07878" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#mg-warm)"/>
  <line x1="445" y1="56" x2="140" y2="148" stroke="#7A8A9A" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#mg-cool)"/>
  <line x1="530" y1="56" x2="310" y2="148" stroke="#7A8A9A" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#mg-cool)"/>
  <line x1="615" y1="56" x2="480" y2="148" stroke="#7A8A9A" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#mg-cool)"/>
  <!-- Merged result -->
  <text x="10" y="168" font-size="12" font-weight="600" fill="#5A5752">result</text>
  <rect x="30" y="155" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="55" y="169" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="80" y1="169" x2="115" y2="169" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="115" y="155" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="140" y="169" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="165" y1="169" x2="200" y2="169" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="200" y="155" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="225" y="169" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="250" y1="169" x2="285" y2="169" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="285" y="155" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="310" y="169" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="335" y1="169" x2="370" y2="169" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="370" y="155" width="50" height="28" rx="6" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="395" y="169" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
  <line x1="420" y1="169" x2="455" y2="169" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#mg-arr)"/>
  <rect x="455" y="155" width="50" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="480" y="169" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">6</text>
  <!-- Legend -->
  <rect x="530" y="155" width="12" height="12" rx="2" fill="#E8D5D0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="548" y="165" font-size="10" fill="#7A7772">from list1</text>
  <rect x="530" y="173" width="12" height="12" rx="2" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="548" y="183" font-size="10" fill="#7A7772">from list2</text>
</svg>

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 280" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <defs>
    <marker id="cd-arr" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#B8B5B0"/>
    </marker>
    <marker id="cd-cyc" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <path d="M0,0 L8,3 L0,6 Z" fill="#9A9792"/>
    </marker>
  </defs>
  <!-- Phase 1: fast & slow meet -->
  <text x="350" y="16" font-size="12" fill="#5A5752" text-anchor="middle" font-weight="600">Phase 1 — fast and slow meet</text>
  <!-- Nodes: 1→2→3→4→5, with 5→3 cycle -->
  <rect x="55" y="50" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="82" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="110" y1="64" x2="145" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="145" y="50" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="172" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="200" y1="64" x2="245" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="245" y="50" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="272" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <text x="272" y="44" font-size="9" fill="#9A9792" text-anchor="middle" font-style="italic">cycle start</text>
  <line x1="300" y1="64" x2="345" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="345" y="50" width="55" height="28" rx="6" fill="#E8D5D0" stroke="#B07878" stroke-width="2"/>
  <text x="372" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="400" y1="64" x2="445" y2="64" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="445" y="50" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="472" y="64" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
  <!-- Cycle arrow: 5 → 3 (curved underneath) -->
  <path d="M472,78 C472,112 272,112 272,78" stroke="#9A9792" stroke-width="1.5" fill="none" stroke-dasharray="5,3" marker-end="url(#cd-cyc)"/>
  <text x="372" y="108" font-size="9" fill="#9A9792" text-anchor="middle" font-style="italic">cycle</text>
  <!-- Meeting point labels -->
  <text x="362" y="36" font-size="11" fill="#6B8B6B" text-anchor="middle" font-weight="600">slow</text>
  <path d="M358,40 L362,47 L366,40 Z" fill="#6B8B6B"/>
  <text x="392" y="36" font-size="11" fill="#6B7B9B" text-anchor="middle" font-weight="600">fast</text>
  <path d="M388,40 L392,47 L396,40 Z" fill="#6B7B9B"/>
  <text x="540" y="60" font-size="10" fill="#B07878" font-weight="600">meet here!</text>
  <line x1="530" y1="62" x2="502" y2="64" stroke="#B07878" stroke-width="1" stroke-dasharray="3,2"/>
  <!-- Phase 2: find cycle start -->
  <text x="350" y="148" font-size="12" fill="#5A5752" text-anchor="middle" font-weight="600">Phase 2 — reset slow to head, both advance ×1</text>
  <!-- Same node layout -->
  <rect x="55" y="178" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="82" y="192" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">1</text>
  <line x1="110" y1="192" x2="145" y2="192" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="145" y="178" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="172" y="192" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">2</text>
  <line x1="200" y1="192" x2="245" y2="192" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="245" y="178" width="55" height="28" rx="6" fill="#D4D8D0" stroke="#8B8680" stroke-width="2"/>
  <text x="272" y="192" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">3</text>
  <line x1="300" y1="192" x2="345" y2="192" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="345" y="178" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="372" y="192" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">4</text>
  <line x1="400" y1="192" x2="445" y2="192" stroke="#B8B5B0" stroke-width="1.5" marker-end="url(#cd-arr)"/>
  <rect x="445" y="178" width="55" height="28" rx="6" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="472" y="192" font-size="13" fill="#3A3530" text-anchor="middle" dominant-baseline="central">5</text>
  <!-- Cycle arrow -->
  <path d="M472,206 C472,240 272,240 272,206" stroke="#9A9792" stroke-width="1.5" fill="none" stroke-dasharray="5,3" marker-end="url(#cd-cyc)"/>
  <!-- Slow starts at node 1, fast stays at node 4 -->
  <text x="82" y="166" font-size="10" fill="#6B8B6B" text-anchor="middle" font-weight="600">slow (reset)</text>
  <path d="M78,170 L82,176 L86,170 Z" fill="#6B8B6B"/>
  <text x="372" y="166" font-size="10" fill="#6B7B9B" text-anchor="middle" font-weight="600">fast</text>
  <path d="M368,170 L372,176 L376,170 Z" fill="#6B7B9B"/>
  <!-- Dashed path showing slow: 1→2→3 -->
  <path d="M100,175 Q100,158 172,158 Q245,158 255,175" stroke="#6B8B6B" stroke-width="1.2" fill="none" stroke-dasharray="4,3" marker-end="url(#cd-arr)"/>
  <!-- Dashed path showing fast: 4→5→3 -->
  <path d="M390,210 Q390,225 472,225 Q540,225 540,218 Q540,210 472,210 Q390,250 272,210" stroke="#6B7B9B" stroke-width="1.2" fill="none" stroke-dasharray="4,3"/>
  <!-- Cycle start annotation -->
  <text x="272" y="268" font-size="11" fill="#8B8680" text-anchor="middle" font-weight="600">↑ cycle start — both meet here</text>
</svg>

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

