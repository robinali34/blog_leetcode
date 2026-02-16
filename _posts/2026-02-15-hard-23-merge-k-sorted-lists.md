---
layout: post
title: "LeetCode 23. Merge k Sorted Lists"
date: 2026-02-15
categories: [leetcode, hard, linked-list, divide-and-conquer, heap]
tags: [leetcode, hard, linked-list, divide-and-conquer, heap, merge]
permalink: /2026/02/15/hard-23-merge-k-sorted-lists/
---

You are given an array of `k` linked lists, each sorted in ascending order. Merge all the linked lists into one sorted linked list and return it.

## Examples

**Example 1:**

```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

**Example 2:**

```
Input: lists = []
Output: []
```

**Example 3:**

```
Input: lists = [[]]
Output: []
```

## Constraints

- `k == lists.length`
- `0 <= k <= 10^4`
- `0 <= lists[i].length <= 500`
- `-10^4 <= lists[i][j] <= 10^4`
- `lists[i]` is sorted in ascending order
- The sum of `lists[i].length` will not exceed `10^4`

## Thinking Process

Let `k` = number of lists, `N` = total number of nodes.

**Lower bound**: We must touch every node, so $\Omega(N)$.

### Why Sequential Merge Is Bad

If you merge one-by-one:

```
res = merge(lists[0], lists[1])
res = merge(res, lists[2])
res = merge(res, lists[3])
...
```

Worst case time is roughly $N + 2N + 3N + \cdots \approx O(kN)$. This TLEs when `k` is large because earlier merged results keep getting re-traversed.

### Balanced Merging

This is exactly like merge sort -- tree height is $\log k$. Each level processes all $N$ nodes once, so:

$$\text{Time} = O(N \log k)$$

### Why This Is $\log k$

Each round halves the number of lists:

```
k → k/2 → k/4 → k/8 → ... → 1
```

Number of rounds: $\log_2 k$. Each round processes all nodes once. Total: $N \cdot \log k$.

## Approach: Divide & Conquer -- $O(N \log k)$

Pair lists and merge them in rounds, halving the count each time. This avoids the repeated long traversals of sequential merging.

{% raw %}
```cpp
class Solution {
public:
    ListNode* mergeTwo(ListNode* a, ListNode* b) {
        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (a && b) {
            if (a->val < b->val) {
                tail->next = a;
                a = a->next;
            } else {
                tail->next = b;
                b = b->next;
            }
            tail = tail->next;
        }

        tail->next = a ? a : b;
        return dummy.next;
    }

    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        int n = lists.size();
        int step = 1;

        while (step < n) {
            for (int i = 0; i + step < n; i += step * 2) {
                lists[i] = mergeTwo(lists[i], lists[i + step]);
            }
            step *= 2;
        }

        return lists[0];
    }
};
```
{% endraw %}

**Time**: $O(N \log k)$
**Space**: $O(1)$ extra (iterative, in-place pointer rewiring)

## Alternative: Min Heap (Priority Queue) -- $O(N \log k)$

Also optimal at $O(N \log k)$, but with $O(k)$ extra space for the heap.

**How it works:**

1. **Initialize** -- push the head of each non-empty list into a min-heap (size at most `k`)
2. **Pop** the smallest node from the heap and append it to the result
3. **Push** that node's `next` into the heap (if it exists)
4. Repeat until the heap is empty

The heap always holds at most one node per list, so each push/pop is $O(\log k)$. Over all $N$ nodes, total time is $O(N \log k)$.

**Why use a custom comparator struct?** Defining `Compare` as a struct makes the comparator reusable and avoids lambda overhead. The `priority_queue` in C++ is a max-heap by default, so we reverse the comparison (`a->val > b->val`) to get min-heap behavior.

{% raw %}
```cpp
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        priority_queue<ListNode*, vector<ListNode*>, Compare> pq;

        for (auto l : lists) {
            if (l) pq.push(l);
        }

        while (!pq.empty()) {
            ListNode* cur = pq.top();
            pq.pop();
            tail->next = cur;
            tail = tail->next;
            if (cur->next) pq.push(cur->next);
        }

        return dummy.next;
    }

private:
    struct Compare {
        bool operator()(ListNode* a, ListNode* b) const {
            return a->val > b->val;
        }
    };
};
```
{% endraw %}

**Time**: $O(N \log k)$ -- each of $N$ nodes is pushed/popped once, each operation $O(\log k)$
**Space**: $O(k)$ for the heap

## What Strong Candidates Notice

- `k` may be large with small lists, or `k` small with very large lists -- balanced merging handles both
- Divide & conquer uses $O(1)$ extra space vs $O(k)$ for the heap
- Sequential merge degrades to $O(kN)$ -- always avoid it

## Edge Cases

- `k = 0` -- return `nullptr`
- Some lists are empty -- skip them
- All lists are empty -- return `nullptr`
- Single list -- return it directly

## Key Takeaways

When you see **"merge k sorted ..."**, immediately think:
- **Multi-way merge** via min heap
- **Divide & conquer** tree merging

This is a pattern problem. Balanced merging prevents repeated long traversals, bringing complexity from $O(kN)$ down to $O(N \log k)$.

## Related Problems

- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) -- base case for this problem
- [148. Sort List](https://leetcode.com/problems/sort-list/) -- merge sort on linked list
- [378. Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) -- multi-way merge variant

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
