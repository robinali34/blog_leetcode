---
layout: post
title: "[Medium] 433. Minimum Genetic Mutation"
date: 2026-03-15
categories: [leetcode, medium, bfs, string]
tags: [leetcode, medium, bfs, string, shortest-path]
permalink: /2026/03/15/medium-433-minimum-genetic-mutation/
---

A gene string is represented by an 8-character string of `'A'`, `'C'`, `'G'`, and `'T'`. Given `startGene`, `endGene`, and a `bank` of valid gene strings, return the **minimum number of mutations** needed to mutate from `startGene` to `endGene`. Each mutation changes exactly one character and the result must be in the bank. Return `-1` if no such mutation sequence exists.

## Examples

**Example 1:**

```
Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
```

**Example 2:**

```
Input: startGene = "AACCGGTT", endGene = "AAACGGTA",
       bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
```

**Example 3:**

```
Input: startGene = "AAAAACCC", endGene = "AACCCCCC",
       bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3
```

## Constraints

- `startGene.length == endGene.length == 8`
- `startGene` and `endGene` consist of `'A'`, `'C'`, `'G'`, `'T'`
- `0 <= bank.length <= 10`
- `bank[i].length == 8`
- All strings in `bank` are unique

## Thinking Process

### Why BFS?

Each gene string is a **node**. Two nodes are connected if they differ by exactly one character **and** the target is in the bank. We need the **minimum number of steps** from start to end -- classic BFS shortest path on an unweighted graph.

This is structurally identical to [LC 127 Word Ladder](https://leetcode.com/problems/word-ladder/), just with a 4-letter alphabet (`ACGT`) and fixed length 8.

### Algorithm

1. Put the bank into a set for $O(1)$ lookup
2. Early exit if `endGene` is not in the bank
3. BFS level by level: for each gene, try all single-character mutations (`A`, `C`, `G`, `T`)
4. If a mutation is in the bank, enqueue it and **remove it from the bank set** (acts as visited)
5. When we dequeue `endGene`, return the current step count

### Walk-through

```
startGene = "AACCGGTT", endGene = "AAACGGTA"
bank = {"AACCGGTA", "AACCGCTA", "AAACGGTA"}

Step 0: queue = ["AACCGGTT"]
  Try all mutations of "AACCGGTT"
  "AACCGGTA" ∈ bank → enqueue, remove from bank

Step 1: queue = ["AACCGGTA"]
  Try all mutations of "AACCGGTA"
  "AAACGGTA" ∈ bank → enqueue, remove from bank

Step 2: queue = ["AAACGGTA"]
  Dequeue "AAACGGTA" == endGene → return 2
```

## Solution: BFS -- $O(n \cdot L \cdot 4)$

{% raw %}
```cpp
class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> bankSet(bank.begin(), bank.end());
        if (!bankSet.contains(endGene)) return -1;

        queue<string> q;
        q.push(startGene);
        int steps = 0;
        vector<char> genes = {'A', 'C', 'G', 'T'};

        while (!q.empty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                string curr = q.front();
                q.pop();
                if (curr == endGene) return steps;

                for (int j = 0; j < curr.size(); j++) {
                    char org = curr[j];
                    for (char g : genes) {
                        if (org == g) continue;
                        curr[j] = g;
                        if (bankSet.contains(curr)) {
                            q.push(curr);
                            bankSet.erase(curr);
                        }
                    }
                    curr[j] = org;
                }
            }
            steps++;
        }
        return -1;
    }
};
```
{% endraw %}

**Time**: $O(n \cdot L \cdot 4)$ where $n$ = bank size, $L$ = gene length (8)
**Space**: $O(n)$ for the bank set and queue

## Key Details

**Why erase from `bankSet` instead of a separate `visited` set?**
Removing a gene from the bank once enqueued guarantees we never revisit it -- functionally identical to a visited set but saves space.

**Why check `curr == endGene` at dequeue, not when generating?**
Either works. Checking at dequeue is cleaner for level-by-level BFS since `steps` is already correct at that point. Checking when generating would also work and would short-circuit slightly earlier.

## Common Mistakes

- Forgetting the early exit when `endGene` is not in the bank
- Using a separate visited set but forgetting to mark `startGene` as visited
- Not restoring `curr[j] = org` after trying all mutations at position `j`

## Key Takeaways

- **"Minimum transformations with single-step changes"** = BFS shortest path
- Erasing from the bank set doubles as visited tracking -- a clean pattern for word/gene ladder problems
- Structurally identical to LC 127 Word Ladder

## Related Problems

- [127. Word Ladder](https://leetcode.com/problems/word-ladder/) -- same pattern, 26-letter alphabet
- [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/) -- BFS reachability
- [1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/) -- BFS shortest path on grid

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
