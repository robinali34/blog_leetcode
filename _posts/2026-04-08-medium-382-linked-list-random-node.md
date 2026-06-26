---
layout: post
title: "[Medium] 382. Linked List Random Node"
date: 2026-04-08
categories: [leetcode, medium, linked-list, randomized]
tags: [leetcode, medium, linked-list, randomized, reservoir-sampling]
permalink: /2026/04/08/medium-382-linked-list-random-node/
---
Given a singly linked list, return a **random** node's value. Each node must have an **equal probability** of being chosen.

**Follow-up**: What if the linked list is extremely large and its length is unknown? Can you solve this without using extra space?

## Examples

**Example 1:**

```
Input: head = [1,2,3]
  getRandom() → 1
  getRandom() → 3
  getRandom() → 2
  getRandom() → 2
  getRandom() → 3
Each call returns 1, 2, or 3 with probability 1/3.
```

## Constraints

- Number of nodes in the list is in the range `[1, 10^4]`
- `-10^4 <= Node.val <= 10^4`
- At most `10^4` calls to `getRandom`

## Thinking Process

### Approach 1: Flatten to Array

Copy all values into a vector in the constructor. `getRandom` picks a random index. Simple but uses O(n) extra space.

### Approach 2: Reservoir Sampling

For the follow-up (unknown length, no extra space), use **Reservoir Sampling (k=1)**:

Walk through the list. At the i-th node (1-indexed), replace the current pick with this node's value with probability frac{1}{i}.

**Why this gives uniform probability**:

The probability that node j is the final pick:

$P(text{picked at } j) × P(text{not replaced at } j{+}1) × ldots × P(text{not replaced at } n)

= frac{1}{j} × frac{j}{j+1} × frac{j+1}{j+2} × ldots × frac{n-1}{n} = frac{1}{n}

The fractions telescope, giving exactly \frac{1}{n} for every node.

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

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Iterative pointer walk | O(n) | O(1) | Traversal, insertion |
| **Dummy head node** *(this problem)* | O(n) | O(1) | Simplify head-edge cases |
| Reversal (3-pointer) | O(n) | O(1) | Reverse sublist or full list |
| Slow/fast pointers | O(n) | O(1) | Middle, cycle, merge lists |

## Solution
```cpp
class Solution {
public:
    Solution(ListNode* head) {
        while (head) {
            v.push_back(head->val);
            head = head->next;
        }
    }

    int getRandom() {
        return v[rand() % v.size()];
    }

private:
    vector<int> v;
};
```

### Solution Explanation

**Approach:** Dummy head node (this problem)

**Key idea:** ### Approach 1: Flatten to Array

**How the code works:**
**Why this gives uniform probability**:

**Walkthrough** — input `head = [1,2,3]`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Starting the index counter at 1 instead of 2 in reservoir sampling (node 1 is always picked initially)
- Using `rand() % i == 0` with `i` starting at 0 (division by zero)
- Assuming `rand()` is perfectly uniform -- for production code, use `<random>` with `uniform_int_distribution`

## Key Takeaways

- **Reservoir Sampling** solves "pick k items uniformly at random from a stream of unknown length" in O(1)$ space
- The telescoping probability proof is elegant and worth understanding
- This is a classic interview follow-up: "What if you can't store the data?"

## Related Problems

- [398. Random Pick Index](https://www.leetcode.com/problems/random-pick-index/) -- reservoir sampling with target value
- [528. Random Pick with Weight](https://www.leetcode.com/problems/random-pick-with-weight/) -- weighted random selection
- [876. Middle of the Linked List](https://www.leetcode.com/problems/middle-of-the-linked-list/) -- linked list traversal

## References

- [LC 382: Linked List Random Node on LeetCode](https://www.leetcode.com/problems/linked-list-random-node/)
- [LeetCode Discuss — LC 382: Linked List Random Node](https://www.leetcode.com/problems/linked-list-random-node/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/linked-list-random-node/editorial/) *(may require premium)*

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
