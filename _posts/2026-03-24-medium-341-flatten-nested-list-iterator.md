---
layout: post
title: "[Medium] 341. Flatten Nested List Iterator"
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

We could recursively flatten the entire list in the constructor and iterate over the result. That works, but uses O(n) extra space upfront and doesn't take advantage of **lazy evaluation** -- we might not need all elements.

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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 125" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Stack</text>

  <rect x="100" y="30" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="46" text-anchor="middle" font-size="10">top</text>
  <rect x="100" y="54" width="80" height="24" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/>
  <rect x="100" y="78" width="80" height="24" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <text x="200" y="70" font-size="11" fill="#6B6560">push / pop</text>
  <path d="M90 42v60" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="115" text-anchor="middle" font-size="11" fill="#6B6560">LIFO — monotonic stack scans array</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Monotonic stack** *(this problem)* | O(n) | O(n) | Next greater/smaller element |
| Parentheses matching | O(n) | O(n) | Push open, pop on close |
| Expression evaluation | O(n) | O(n) | Operand + operator stacks |
| Stack simulation | O(n) | O(n) | Process in LIFO order |

## Solution
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

### Solution Explanation

**Approach:** Monotonic stack (this problem)

**Key idea:** ### The Problem with Pre-flattening

**How the code works:**
1. **Constructor**: push elements onto the stack **in reverse order** (so the first element is on top)
2. **`hasNext`**: peek at the top -- if it's a list, expand it (pop, push children in reverse). Repeat until the top is an integer or the stack is empty
3. **`next`**: the top is guaranteed to be an integer (since `hasNext` was called first) -- pop and return it

**Walkthrough** — input `nestedList = [[1,1],2,[1,1]]`, expected output `[1,1,2,1,1]`:

Flattening gives [1,1,2,1,1].
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

- [385. Mini Parser](https://www.leetcode.com/problems/mini-parser/) -- building nested structures
- [339. Nested List Weight Sum](https://www.leetcode.com/problems/nested-list-weight-sum/) -- DFS on nested lists
- [173. Binary Search Tree Iterator](https://www.leetcode.com/problems/binary-search-tree-iterator/) -- stack-based tree iterator
- [281. Zigzag Iterator](https://www.leetcode.com/problems/zigzag-iterator/) -- iterator design

## References

- [LC 341: Flatten Nested List Iterator on LeetCode](https://www.leetcode.com/problems/flatten-nested-list-iterator/)
- [LeetCode Discuss — LC 341: Flatten Nested List Iterator](https://www.leetcode.com/problems/flatten-nested-list-iterator/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/flatten-nested-list-iterator/editorial/) *(may require premium)*

## Template Reference

- [Data Structure Design](/blog_leetcode/posts/2025-11-24-leetcode-templates-data-structure-design/)
- [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/)
