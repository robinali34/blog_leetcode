---
layout: post
title: "LeetCode 341. Flatten Nested List Iterator"
date: 2026-03-24
categories: [leetcode, medium, design, stack, iterator]
tags: [leetcode, medium, design, stack, iterator]
permalink: /2026/03/24/medium-341-flatten-nested-list-iterator/
---

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement `NestedIterator`:
- `NestedIterator(vector<NestedInteger> &nestedList)` -- initializes the iterator
- `int next()` -- returns the next integer in the flattened list
- `bool hasNext()` -- returns `true` if there are still integers to iterate

## Examples

**Example 1:**

```
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: Flattening gives [1,1,2,1,1].
```

**Example 2:**

```
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
```

## Constraints

- `1 <= nestedList.length <= 500`
- Values are in the range `[-10^6, 10^6]`
- At most `10^5` calls to `next` and `hasNext`

## Thinking Process

### The Problem with Pre-flattening

We could recursively flatten the entire list in the constructor and iterate over the result. That works, but uses $O(n)$ extra space upfront and doesn't take advantage of **lazy evaluation** -- we might not need all elements.

### Stack-Based Lazy Approach

Use a stack to simulate the recursive flattening on demand:

1. **Constructor**: push elements onto the stack **in reverse order** (so the first element is on top)
2. **`hasNext`**: peek at the top -- if it's a list, expand it (pop, push children in reverse). Repeat until the top is an integer or the stack is empty
3. **`next`**: the top is guaranteed to be an integer (since `hasNext` was called first) -- pop and return it

### Why Push in Reverse?

A stack is LIFO. To process elements left-to-right, we push them right-to-left:

```
nestedList = [A, B, C]
Push: C, B, A  →  stack top = A  ✓
```

### Walk-through

```
Input: [[1,1], 2, [1,1]]

Constructor: push [1,1], 2, [1,1] in reverse
  stack: [1,1] | 2 | [1,1]  (top → [1,1])

hasNext(): top = [1,1] → list, expand: push 1, 1
  stack: [1,1] | 2 | 1 | 1  (top → 1, integer ✓)
next(): return 1

hasNext(): top = 1 (integer ✓)
next(): return 1

hasNext(): top = 2 (integer ✓)
next(): return 2

hasNext(): top = [1,1] → list, expand: push 1, 1
  stack: 1 | 1  (top → 1 ✓)
next(): return 1

hasNext(): top = 1 (integer ✓)
next(): return 1

hasNext(): stack empty → false
```

## Solution: Stack-Based Lazy Iterator -- $O(1)$ amortized

{% raw %}
```cpp
class NestedIterator {
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i = nestedList.size() - 1; i >= 0; --i) {
            stk.push(nestedList[i]);
        }
    }

    int next() {
        int val = stk.top().getInteger();
        stk.pop();
        return val;
    }

    bool hasNext() {
        while (!stk.empty()) {
            NestedInteger curr = stk.top();
            if (curr.isInteger()) {
                return true;
            }
            stk.pop();
            auto& lst = curr.getList();
            for (int i = lst.size() - 1; i >= 0; --i) {
                stk.push(lst[i]);
            }
        }
        return false;
    }

private:
    stack<NestedInteger> stk;
};
```
{% endraw %}

**Time**: $O(1)$ amortized per `next`/`hasNext` call -- each element is pushed and popped exactly once across all calls
**Space**: $O(D)$ where $D$ = maximum nesting depth (stack holds at most one "path" through the nesting)

## Key Details

**Why does `hasNext` do the flattening, not `next`?**
The iterator contract requires `hasNext` to correctly report whether more elements exist. If the top of the stack is a nested list (possibly empty), `hasNext` must drill down to find the next actual integer -- or determine there are none.

**What about empty nested lists like `[[], [1]]`?**
The `while` loop in `hasNext` handles this: `[]` gets popped and expanded to nothing, then the loop continues to process `[1]`.

## Common Mistakes

- Pushing elements in forward order (reverses the iteration order)
- Flattening in `next` instead of `hasNext` (breaks the contract when checking for empty nested lists)
- Not handling deeply nested empty lists like `[[[[]]]]`

## Key Takeaways

- **"Flatten a recursive structure lazily"** = stack-based iterator
- Push in reverse order to maintain left-to-right traversal with a LIFO stack
- Doing the expansion in `hasNext` rather than `next` correctly handles empty nested lists and satisfies the iterator contract

## Related Problems

- [385. Mini Parser](https://leetcode.com/problems/mini-parser/) -- building nested structures
- [339. Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/) -- DFS on nested lists
- [173. Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator/) -- stack-based tree iterator
- [281. Zigzag Iterator](https://leetcode.com/problems/zigzag-iterator/) -- iterator design

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
- [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/)
