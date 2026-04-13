---
layout: post
title: "LeetCode 382. Linked List Random Node"
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

Copy all values into a vector in the constructor. `getRandom` picks a random index. Simple but uses $O(n)$ extra space.

### Approach 2: Reservoir Sampling

For the follow-up (unknown length, no extra space), use **Reservoir Sampling (k=1)**:

Walk through the list. At the $i$-th node (1-indexed), replace the current pick with this node's value with probability $\frac{1}{i}$.

**Why this gives uniform probability**:

The probability that node $j$ is the final pick:

$$P(\text{picked at } j) \times P(\text{not replaced at } j{+}1) \times \ldots \times P(\text{not replaced at } n)$$

$$= \frac{1}{j} \times \frac{j}{j+1} \times \frac{j+1}{j+2} \times \ldots \times \frac{n-1}{n} = \frac{1}{n}$$

The fractions telescope, giving exactly $\frac{1}{n}$ for every node.

## Solution 1: Flatten to Array -- $O(1)$ per query

{% raw %}
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
{% endraw %}

| Operation | Time | Space |
|---|---|---|
| Constructor | $O(n)$ | $O(n)$ |
| `getRandom` | $O(1)$ | -- |

## Solution 2: Reservoir Sampling -- $O(n)$ per query, $O(1)$ space

{% raw %}
```cpp
class Solution {
public:
    Solution(ListNode* head) {
        this->head = head;
    }

    int getRandom() {
        int rtn = head->val;
        ListNode* curr = head->next;
        int i = 2;
        while (curr) {
            if (rand() % i == 0) {
                rtn = curr->val;
            }
            curr = curr->next;
            i++;
        }
        return rtn;
    }

private:
    ListNode* head;
};
```
{% endraw %}

| Operation | Time | Space |
|---|---|---|
| Constructor | $O(1)$ | $O(1)$ |
| `getRandom` | $O(n)$ | $O(1)$ |

## Comparison

| Approach | Constructor | `getRandom` | Extra Space | Unknown Length? |
|---|---|---|---|---|
| Array | $O(n)$ | $O(1)$ | $O(n)$ | No (must traverse first) |
| Reservoir Sampling | $O(1)$ | $O(n)$ | $O(1)$ | Yes |

**Trade-off**: Array is better when `getRandom` is called many times (amortized). Reservoir Sampling is better when memory is constrained or the list length is unknown/changing.

## Common Mistakes

- Starting the index counter at 1 instead of 2 in reservoir sampling (node 1 is always picked initially)
- Using `rand() % i == 0` with `i` starting at 0 (division by zero)
- Assuming `rand()` is perfectly uniform -- for production code, use `<random>` with `uniform_int_distribution`

## Key Takeaways

- **Reservoir Sampling** solves "pick k items uniformly at random from a stream of unknown length" in $O(1)$ space
- The telescoping probability proof is elegant and worth understanding
- This is a classic interview follow-up: "What if you can't store the data?"

## Related Problems

- [398. Random Pick Index](https://leetcode.com/problems/random-pick-index/) -- reservoir sampling with target value
- [528. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/) -- weighted random selection
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) -- linked list traversal

## Template Reference

- [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/)
