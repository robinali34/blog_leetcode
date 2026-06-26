---
layout: post
title: "[Hard] 23. Merge k Sorted Lists"
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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Iterative pointer walk** *(this problem)* | O(n) | O(1) | Traversal, insertion |
| Dummy head node | O(n) | O(1) | Simplify head-edge cases |
| Reversal (3-pointer) | O(n) | O(1) | Reverse sublist or full list |
| Slow/fast pointers | O(n) | O(1) | Middle, cycle, merge lists |

## Thinking Process

Let `k` = number of lists, `N` = total number of nodes.

**Lower bound**: We must touch every node, so Omega(N).

### Why Sequential Merge Is Bad

If you merge one-by-one:

```
res = merge(lists[0], lists[1])
res = merge(res, lists[2])
res = merge(res, lists[3])
...
```

Worst case time is roughly N + 2N + 3N + ·s approx O(kN). This TLEs when `k` is large because earlier merged results keep getting re-traversed.

### Balanced Merging

This is exactly like merge sort -- tree height is log k. Each level processes all N nodes once, so:

$text{Time} = O(N log k)

### Why This Is \log k

Each round halves the number of lists:

```
k → k/2 → k/4 → k/8 → ... → 1
```

Number of rounds: \log_2 k. Each round processes all nodes once. Total: N \cdot \log k.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Linked list: pointer walk</text>

  <rect x="30" y="50" width="44" height="32" rx="4" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="52" y="68" text-anchor="middle" font-size="12">1</text>
  <path d="M74 66h16" stroke="#8B8680" stroke-width="2" marker-end="url(#arr)"/>
  <rect x="90" y="50" width="44" height="32" rx="4" fill="#E0D8E4" stroke="#A098A8"/>
  <text x="112" y="68" text-anchor="middle" font-size="12">2</text>
  <path d="M134 66h16" stroke="#8B8680" stroke-width="2"/>
  <rect x="150" y="50" width="44" height="32" rx="4" fill="#E8E3D8" stroke="#B8B5B0"/>
  <text x="172" y="68" text-anchor="middle" font-size="12">3</text>
  <text x="130" y="105" text-anchor="middle" font-size="11" fill="#6B6560">slow → → fast (2x speed)</text>
  <defs><marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>

</svg>

## Approach: Divide & Conquer -- O(N \log k)

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

### Solution Explanation

**Approach:** Iterative pointer walk (this problem)

**Key idea:** Let `k` = number of lists, `N` = total number of nodes.

**How the code works:**
**Lower bound**: We must touch every node, so \Omega(N).

**Walkthrough** — input `lists = [[1,4,5],[1,3,4],[2,6]]`, expected output `[1,1,2,3,4,4,5,6]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Alternative: Min Heap (Priority Queue) -- O(N \log k)

Also optimal at O(N \log k), but with O(k) extra space for the heap.

**How it works:**

1. **Initialize** -- push the head of each non-empty list into a min-heap (size at most `k`)
2. **Pop** the smallest node from the heap and append it to the result
3. **Push** that node's `next` into the heap (if it exists)
4. Repeat until the heap is empty

The heap always holds at most one node per list, so each push/pop is O(\log k). Over all N nodes, total time is O(N \log k).

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

**Time**: O(N \log k) -- each of N nodes is pushed/popped once, each operation O(\log k)
**Space**: O(k) for the heap

## What Strong Candidates Notice

- `k` may be large with small lists, or `k` small with very large lists -- balanced merging handles both
- Divide & conquer uses O(1) extra space vs O(k) for the heap
- Sequential merge degrades to O(kN) -- always avoid it

## Edge Cases

- `k = 0` -- return `nullptr`
- Some lists are empty -- skip them
- All lists are empty -- return `nullptr`
- Single list -- return it directly

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.


## Key Takeaways

When you see **"merge k sorted ..."**, immediately think:
- **Multi-way merge** via min heap
- **Divide & conquer** tree merging

This is a pattern problem. Balanced merging prevents repeated long traversals, bringing complexity from O(kN) down to O(N \log k)$.

## Related Problems

- [21. Merge Two Sorted Lists](https://www.leetcode.com/problems/merge-two-sorted-lists/) -- base case for this problem
- [148. Sort List](https://www.leetcode.com/problems/sort-list/) -- merge sort on linked list
- [378. Kth Smallest Element in a Sorted Matrix](https://www.leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/) -- multi-way merge variant

## References

- [LC 23: Merge k Sorted Lists on LeetCode](https://www.leetcode.com/problems/merge-k-sorted-lists/)
- [LeetCode Discuss — LC 23: Merge k Sorted Lists](https://www.leetcode.com/problems/merge-k-sorted-lists/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/merge-k-sorted-lists/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
- [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/)
