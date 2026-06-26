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

This is structurally identical to [LC 127 Word Ladder](https://www.leetcode.com/problems/word-ladder/), just with a 4-letter alphabet (`ACGT`) and fixed length 8.

### Algorithm

1. Put the bank into a set for O(1) lookup
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

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 135" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Graph BFS layers</text>

  <circle cx="60" cy="70" r="16" fill="#D4D8E0" stroke="#8B8680"/><text x="60" y="74" text-anchor="middle" font-size="11">S</text>
  <circle cx="140" cy="45" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="49" text-anchor="middle" font-size="10">a</text>
  <circle cx="140" cy="95" r="14" fill="#E8E3D8" stroke="#B8B5B0"/><text x="140" y="99" text-anchor="middle" font-size="10">b</text>
  <circle cx="210" cy="70" r="14" fill="#E8D5D0" stroke="#B8A5A0"/><text x="210" y="74" text-anchor="middle" font-size="10">t</text>
  <line x1="74" y1="65" x2="126" y2="50" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="74" y1="75" x2="126" y2="95" stroke="#9A9792" stroke-width="1.5"/>
  <line x1="154" y1="50" x2="196" y2="65" stroke="#9A9792" stroke-width="1.5"/>
  <text x="140" y="125" text-anchor="middle" font-size="11" fill="#6B6560">BFS: expand by layers (queue)</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Queue BFS** *(this problem)* | O(n) | O(n) | Shortest path in unweighted graphs |
| Multi-source BFS | O(n) | O(n) | Start from all sources simultaneously |
| 0-1 BFS / deque | O(n) | O(n) | Weights 0 or 1 |
| Level-order BFS | O(n) | O(w) | Process by depth/layer |

## Solution
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

### Solution Explanation

**Approach:** Queue BFS (this problem)

**Key idea:** ### Why BFS?

**How the code works:**
1. Put the bank into a set for O(1) lookup
2. Early exit if `endGene` is not in the bank
3. BFS level by level: for each gene, try all single-character mutations (`A`, `C`, `G`, `T`)
4. If a mutation is in the bank, enqueue it and **remove it from the bank set** (acts as visited)
5. When we dequeue `endGene`, return the current step count

**Walkthrough** — input `startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]`, expected output `1`:

1. Initialize variables from the problem setup.
2. Apply the main loop / recursion until the condition is met.
3. Confirm the result matches the expected output.
## Common Mistakes

- Forgetting the early exit when `endGene` is not in the bank
- Using a separate visited set but forgetting to mark `startGene` as visited
- Not restoring `curr[j] = org` after trying all mutations at position `j`

## Key Takeaways

- **"Minimum transformations with single-step changes"** = BFS shortest path
- Erasing from the bank set doubles as visited tracking -- a clean pattern for word/gene ladder problems
- Structurally identical to LC 127 Word Ladder

## Related Problems

- [127. Word Ladder](https://www.leetcode.com/problems/word-ladder/) -- same pattern, 26-letter alphabet
- [841. Keys and Rooms](https://www.leetcode.com/problems/keys-and-rooms/) -- BFS reachability
- [1091. Shortest Path in Binary Matrix](https://www.leetcode.com/problems/shortest-path-in-binary-matrix/) -- BFS shortest path on grid

## References

- [LC 433: Minimum Genetic Mutation on LeetCode](https://www.leetcode.com/problems/minimum-genetic-mutation/)
- [LeetCode Discuss — LC 433: Minimum Genetic Mutation](https://www.leetcode.com/problems/minimum-genetic-mutation/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/minimum-genetic-mutation/editorial/) *(may require premium)*

## Template Reference

- [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/)
