---
layout: post
title: "Algorithm Templates: Backtracking"
date: 2025-11-24 00:00:00 -0700
categories: leetcode templates backtracking
permalink: /posts/2025-11-24-leetcode-templates-backtracking/
tags: [leetcode, templates, backtracking, dfs]
---
Welcome to the backtracking templates! Backtracking is one of the most versatile problem-solving techniques in competitive programming—once you learn the core pattern, you can tackle a huge family of problems from permutations to Sudoku. This page gives you battle-tested C++ templates for every major backtracking pattern, ready to adapt and submit.

> **New to Backtracking?** Backtracking = DFS + undo. You try a choice, recurse deeper, and if it doesn't work out, you undo the choice and try the next one. It's how you systematically explore all possibilities without missing any.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 480" style="max-width:720px;width:100%;height:auto;display:block;margin:1.5em auto;">
  <style>
    .node { rx: 18; ry: 18; stroke-width: 2; }
    .label { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 13px; fill: #4a4a4a; text-anchor: middle; dominant-baseline: central; }
    .title { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 15px; fill: #5b5b5b; font-weight: 600; text-anchor: middle; }
    .edge-label { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 11px; fill: #7a8a7a; text-anchor: middle; }
    .edge { stroke-width: 1.8; fill: none; }
    .legend { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 11px; fill: #6b6b6b; }
  </style>
  <text x="360" y="22" class="title">Subsets of [1, 2, 3] — Backtracking Decision Tree</text>
  <!-- Level 0: root {} -->
  <rect x="325" y="40" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="360" y="56" class="label">{ }</text>
  <!-- Level 1 branches -->
  <line x1="345" y1="72" x2="180" y2="130" class="edge" stroke="#a3b5a0"/>
  <text x="255" y="95" class="edge-label">+1</text>
  <line x1="375" y1="72" x2="540" y2="130" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="465" y="95" class="edge-label">skip 1</text>
  <!-- Level 1 nodes -->
  <rect x="145" y="130" width="70" height="32" class="node" fill="#a3b5a0" stroke="#8a9f88"/>
  <text x="180" y="146" class="label">{1}</text>
  <rect x="505" y="130" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="540" y="146" class="label">{ }</text>
  <!-- Level 2 from {1} -->
  <line x1="160" y1="162" x2="90" y2="220" class="edge" stroke="#a3b5a0"/>
  <text x="118" y="185" class="edge-label">+2</text>
  <line x1="200" y1="162" x2="270" y2="220" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="242" y="185" class="edge-label">skip 2</text>
  <!-- Level 2 from skip-1 side -->
  <line x1="525" y1="162" x2="460" y2="220" class="edge" stroke="#a3b5a0"/>
  <text x="485" y="185" class="edge-label">+2</text>
  <line x1="555" y1="162" x2="630" y2="220" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="600" y="185" class="edge-label">skip 2</text>
  <!-- Level 2 nodes -->
  <rect x="55" y="220" width="70" height="32" class="node" fill="#a3b5a0" stroke="#8a9f88"/>
  <text x="90" y="236" class="label">{1,2}</text>
  <rect x="235" y="220" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="270" y="236" class="label">{1}</text>
  <rect x="425" y="220" width="70" height="32" class="node" fill="#a3b5a0" stroke="#8a9f88"/>
  <text x="460" y="236" class="label">{2}</text>
  <rect x="595" y="220" width="70" height="32" class="node" fill="#d4c5b0" stroke="#b8a994"/>
  <text x="630" y="236" class="label">{ }</text>
  <!-- Level 3 from {1,2} -->
  <line x1="75" y1="252" x2="35" y2="310" class="edge" stroke="#a3b5a0"/>
  <text x="48" y="275" class="edge-label">+3</text>
  <line x1="105" y1="252" x2="145" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="132" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 from {1} skip-2 -->
  <line x1="255" y1="252" x2="220" y2="310" class="edge" stroke="#a3b5a0"/>
  <text x="230" y="275" class="edge-label">+3</text>
  <line x1="285" y1="252" x2="320" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="310" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 from {2} -->
  <line x1="445" y1="252" x2="405" y2="310" class="edge" stroke="#a3b5a0"/>
  <text x="418" y="275" class="edge-label">+3</text>
  <line x1="475" y1="252" x2="515" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="502" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 from {} skip-all -->
  <line x1="630" y1="252" x2="630" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="645" y="275" class="edge-label">+3</text>
  <line x1="655" y1="252" x2="700" y2="310" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="690" y="275" class="edge-label">skip 3</text>
  <!-- Level 3 leaf nodes -->
  <rect x="5" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="40" y="326" class="label">{1,2,3}</text>
  <rect x="115" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="150" y="326" class="label">{1,2}</text>
  <rect x="190" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="225" y="326" class="label">{1,3}</text>
  <rect x="290" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="325" y="326" class="label">{1}</text>
  <rect x="375" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="410" y="326" class="label">{2,3}</text>
  <rect x="485" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="520" y="326" class="label">{2}</text>
  <rect x="600" y="310" width="70" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="635" y="326" class="label">{3}</text>
  <rect x="675" y="310" width="45" height="32" class="node" fill="#b0c4b0" stroke="#8aaa8a"/>
  <text x="697" y="326" class="label">{ }</text>
  <!-- Legend -->
  <line x1="200" y1="380" x2="240" y2="380" class="edge" stroke="#a3b5a0"/>
  <text x="300" y="383" class="legend">Include element</text>
  <line x1="380" y1="380" x2="420" y2="380" class="edge" stroke="#c4a7a0" stroke-dasharray="6,3"/>
  <text x="476" y="383" class="legend">Skip element</text>
  <rect x="236" y="400" width="16" height="16" rx="4" fill="#b0c4b0" stroke="#8aaa8a" stroke-width="1.5"/>
  <text x="310" y="411" class="legend">Leaf = final subset</text>
  <text x="360" y="445" class="legend" text-anchor="middle">Each root-to-leaf path is one subset · 2³ = 8 subsets total</text>
</svg>

## Contents

- [Permutations](#permutations-all-arrangements)
- [Combinations](#combinations-choose-k-from-n)
- [Subsets](#subsets-all-subsets)
- [Combination Sum](#combination-sum-unboundedreuse-elements)
- [Grid Backtracking](#grid-backtracking-word-search-path-finding)
- [Constraint Satisfaction](#constraint-satisfaction-n-queens-sudoku)
- [Palindrome Partitioning](#palindrome-partitioning)
- [General Backtracking Template](#general-backtracking-template)

## Introduction

Backtracking is a systematic way to explore all possible solutions by building candidates incrementally and abandoning ("backtracking") partial candidates that cannot lead to valid solutions. It's essentially a depth-first search with pruning.

**Key Characteristics:**
- Builds solutions incrementally
- Abandons partial solutions that cannot be completed (pruning)
- Uses recursion to explore the solution space
- Restores state after recursive calls (backtracking step)

**The Backtracking Template** — nearly every problem on this page follows this skeleton:

```
backtrack(current_state):
    if is_solution(current_state):
        record solution
        return
    for each choice in available_choices:
        if is_valid(choice):        ← pruning
            make_choice()
            backtrack(next_state)    ← recurse
            undo_choice()            ← backtrack
```

## Permutations (All Arrangements)

**When to use:** The problem asks for "all arrangements", "all orderings", "every possible order", or "rearrange".

Generate all permutations of distinct elements.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 340" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="20" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">Permutation Tree for [1, 2, 3] — pick one unused element per level</text>
  <!-- Edges Root to L1 -->
  <line x1="370" y1="56" x2="120" y2="106" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="56" x2="370" y2="106" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="56" x2="620" y2="106" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="232" y="74" text-anchor="middle" font-size="10" fill="#9A9792">pick 1</text>
  <text x="382" y="74" text-anchor="middle" font-size="10" fill="#9A9792">pick 2</text>
  <text x="508" y="74" text-anchor="middle" font-size="10" fill="#9A9792">pick 3</text>
  <!-- Edges L1 to L2 -->
  <line x1="120" y1="130" x2="60" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="120" y1="130" x2="180" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="130" x2="310" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="370" y1="130" x2="430" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="620" y1="130" x2="560" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <line x1="620" y1="130" x2="680" y2="178" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="82" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <text x="158" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="332" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <text x="408" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="582" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <text x="658" y="152" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <!-- Edges L2 to L3 (single child each) -->
  <line x1="60" y1="202" x2="60" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="180" y1="202" x2="180" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="310" y1="202" x2="310" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="430" y1="202" x2="430" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="560" y1="202" x2="560" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="680" y1="202" x2="680" y2="250" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="50" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="170" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <text x="300" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+3</text>
  <text x="420" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <text x="550" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+2</text>
  <text x="670" y="228" text-anchor="middle" font-size="10" fill="#9A9792">+1</text>
  <!-- Root node -->
  <rect x="340" y="36" width="60" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="51" text-anchor="middle" font-size="12" fill="#3A3530">[ ]</text>
  <!-- L1 nodes -->
  <rect x="90" y="110" width="60" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="120" y="125" text-anchor="middle" font-size="12" fill="#3A3530">[1]</text>
  <rect x="340" y="110" width="60" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="125" text-anchor="middle" font-size="12" fill="#3A3530">[2]</text>
  <rect x="590" y="110" width="60" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="620" y="125" text-anchor="middle" font-size="12" fill="#3A3530">[3]</text>
  <!-- L2 nodes -->
  <rect x="25" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="60" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[1,2]</text>
  <rect x="145" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="180" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[1,3]</text>
  <rect x="275" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="310" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[2,1]</text>
  <rect x="395" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="430" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[2,3]</text>
  <rect x="525" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="560" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[3,1]</text>
  <rect x="645" y="182" width="70" height="24" rx="12" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="680" y="197" text-anchor="middle" font-size="11" fill="#3A3530">[3,2]</text>
  <!-- L3 leaves (green-ish completed permutations) -->
  <rect x="15" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="60" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[1,2,3]</text>
  <rect x="135" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="180" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[1,3,2]</text>
  <rect x="265" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="310" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[2,1,3]</text>
  <rect x="385" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="430" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[2,3,1]</text>
  <rect x="515" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="560" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[3,1,2]</text>
  <rect x="635" y="254" width="90" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="680" y="269" text-anchor="middle" font-size="11" font-weight="600" fill="#3A3530">[3,2,1]</text>
  <!-- Legend -->
  <rect x="195" y="302" width="14" height="14" rx="4" fill="#D4D8E0" stroke="#B8B5B0" stroke-width="1"/>
  <text x="215" y="313" font-size="10" fill="#7A7772">Partial path</text>
  <rect x="320" y="302" width="14" height="14" rx="4" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1"/>
  <text x="340" y="313" font-size="10" fill="#7A7772">Complete permutation (leaf)</text>
  <text x="370" y="335" text-anchor="middle" font-size="10" fill="#9A9792">3! = 6 permutations · each root-to-leaf path is one arrangement</text>
</svg>

### Permutations without duplicates

```cpp
// Permutations without duplicates
void backtrack(vector<int>& nums, vector<int>& cur, vector<bool>& used, vector<vector<int>>& res){
    if (cur.size() == nums.size()){
        res.push_back(cur);
        return;
    }
    for (int i = 0; i < (int)nums.size(); ++i){
        if (used[i]) continue;
        used[i] = true;
        cur.push_back(nums[i]);
        backtrack(nums, cur, used, res);
        cur.pop_back();
        used[i] = false;
    }
}
```

### Permutations with duplicates

Avoid duplicates by sorting first, then skipping duplicates at the same level when the previous duplicate hasn't been used.

```cpp
// Permutations with duplicates (avoid duplicates by sorting + skip used duplicates)
void backtrack(vector<int>& nums, vector<int>& cur, vector<bool>& used, vector<vector<int>>& res){
    if (cur.size() == nums.size()){
        res.push_back(cur);
        return;
    }
    for (int i = 0; i < (int)nums.size(); ++i){
        // Skip if already used, or if duplicate and previous duplicate not used
        if (used[i] || (i > 0 && nums[i] == nums[i-1] && !used[i-1])) continue;
        used[i] = true;
        cur.push_back(nums[i]);
        backtrack(nums, cur, used, res);
        cur.pop_back();
        used[i] = false;
    }
}

// Call with sorted array
vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    vector<int> cur;
    vector<bool> used(nums.size(), false);
    backtrack(nums, cur, used, res);
    return res;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 46 | Permutations | [Link](https://leetcode.com/problems/permutations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-46-permutations/) |
| 47 | Permutations II | [Link](https://leetcode.com/problems/permutations-ii/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-47-permutations-ii/) |

## Combinations (Choose k from n)

**When to use:** The problem says "choose k from n", "select k items", or "all groups of size k" where order doesn't matter.

Generate all combinations of k elements from n elements. Order doesn't matter, so we use `start` index to avoid duplicates.

```cpp
// Combinations C(n, k)
void backtrack(int start, int n, int k, vector<int>& cur, vector<vector<int>>& res){
    if (cur.size() == k){
        res.push_back(cur);
        return;
    }
    // Only consider elements from start onwards to avoid duplicates
    for (int i = start; i <= n; ++i){
        cur.push_back(i);
        backtrack(i+1, n, k, cur, res);  // Next start is i+1
        cur.pop_back();
    }
}
```

**Key insight:** Use `start` parameter to ensure we only consider elements after the current position, preventing duplicate combinations.

| ID | Title | Link | Solution |
|---|---|---|---|
| 77 | Combinations | [Link](https://leetcode.com/problems/combinations/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/10/20/medium-77-combinations/) |
| 22 | Generate Parentheses | [Link](https://leetcode.com/problems/generate-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-22-generate-parentheses/) |

## Subsets (All Subsets)

**When to use:** The problem asks for "all subsets", "power set", "all subsequences", or "every possible selection".

Generate all subsets (power set) of an array. This includes the empty set and the set itself.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 740 330" style="max-width: 100%; height: auto; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
  <text x="370" y="18" text-anchor="middle" font-size="14" font-weight="600" fill="#3A3530">Subsets of [1, 2, 3] — Include / Exclude at Each Level</text>
  <!-- Edges Root to L1 -->
  <line x1="370" y1="50" x2="185" y2="98" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="370" y1="50" x2="555" y2="98" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="264" y="68" text-anchor="middle" font-size="10" fill="#8B9B86">incl 1</text>
  <text x="476" y="68" text-anchor="middle" font-size="10" fill="#B8A5A0">excl 1</text>
  <!-- Edges L1 to L2 -->
  <line x1="185" y1="122" x2="95" y2="170" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="185" y1="122" x2="275" y2="170" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="555" y1="122" x2="465" y2="170" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="555" y1="122" x2="645" y2="170" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="132" y="142" text-anchor="middle" font-size="10" fill="#8B9B86">+2</text>
  <text x="238" y="142" text-anchor="middle" font-size="10" fill="#B8A5A0">skip 2</text>
  <text x="502" y="142" text-anchor="middle" font-size="10" fill="#8B9B86">+2</text>
  <text x="608" y="142" text-anchor="middle" font-size="10" fill="#B8A5A0">skip 2</text>
  <!-- Edges L2 to L3 -->
  <line x1="95" y1="194" x2="55" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="95" y1="194" x2="135" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="275" y1="194" x2="235" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="275" y1="194" x2="315" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="465" y1="194" x2="425" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="465" y1="194" x2="505" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <line x1="645" y1="194" x2="605" y2="242" stroke="#8B9B86" stroke-width="1.5"/>
  <line x1="645" y1="194" x2="685" y2="242" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="68" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="122" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <text x="248" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="302" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <text x="438" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="492" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <text x="618" y="216" text-anchor="middle" font-size="9" fill="#8B9B86">+3</text>
  <text x="672" y="216" text-anchor="middle" font-size="9" fill="#B8A5A0">skip</text>
  <!-- Root node -->
  <rect x="342" y="30" width="56" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="370" y="45" text-anchor="middle" font-size="12" fill="#3A3530">{ }</text>
  <!-- L1 nodes -->
  <rect x="157" y="102" width="56" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="185" y="117" text-anchor="middle" font-size="12" fill="#3A3530">{1}</text>
  <rect x="527" y="102" width="56" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="555" y="117" text-anchor="middle" font-size="12" fill="#3A3530">{ }</text>
  <!-- L2 nodes -->
  <rect x="62" y="174" width="66" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="95" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{1,2}</text>
  <rect x="247" y="174" width="56" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="275" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{1}</text>
  <rect x="437" y="174" width="56" height="24" rx="12" fill="#D4D8D0" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="465" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{2}</text>
  <rect x="617" y="174" width="56" height="24" rx="12" fill="#E8E3D8" stroke="#B8B5B0" stroke-width="1.5"/>
  <text x="645" y="189" text-anchor="middle" font-size="11" fill="#3A3530">{ }</text>
  <!-- L3 leaf nodes (green-ish, all subsets) -->
  <rect x="14" y="246" width="82" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="55" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1,2,3}</text>
  <rect x="101" y="246" width="68" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="135" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1,2}</text>
  <rect x="201" y="246" width="68" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="235" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1,3}</text>
  <rect x="288" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="315" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{1}</text>
  <rect x="391" y="246" width="68" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="425" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{2,3}</text>
  <rect x="478" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="505" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{2}</text>
  <rect x="578" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="605" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{3}</text>
  <rect x="658" y="246" width="54" height="24" rx="12" fill="#C8D5C4" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="685" y="261" text-anchor="middle" font-size="10" font-weight="600" fill="#3A3530">{ }</text>
  <!-- Legend -->
  <line x1="190" y1="296" x2="225" y2="296" stroke="#8B9B86" stroke-width="1.5"/>
  <text x="235" y="300" font-size="10" fill="#7A7772">Include element</text>
  <line x1="350" y1="296" x2="385" y2="296" stroke="#B8A5A0" stroke-width="1.5" stroke-dasharray="5,3"/>
  <text x="395" y="300" font-size="10" fill="#7A7772">Exclude element</text>
  <text x="370" y="322" text-anchor="middle" font-size="10" fill="#9A9792">Each root-to-leaf path is one subset · 2³ = 8 subsets total</text>
</svg>

### Subsets without duplicates

```cpp
// Subsets without duplicates
void backtrack(int start, vector<int>& nums, vector<int>& cur, vector<vector<int>>& res){
    res.push_back(cur);  // Add current subset (including empty set)
    for (int i = start; i < (int)nums.size(); ++i){
        cur.push_back(nums[i]);
        backtrack(i+1, nums, cur, res);
        cur.pop_back();
    }
}
```

### Subsets with duplicates

Sort first, then skip duplicates at the same level.

```cpp
// Subsets with duplicates (sort first, skip duplicates at same level)
void backtrack(int start, vector<int>& nums, vector<int>& cur, vector<vector<int>>& res){
    res.push_back(cur);
    for (int i = start; i < (int)nums.size(); ++i){
        // Skip duplicates at the same level
        if (i > start && nums[i] == nums[i-1]) continue;
        cur.push_back(nums[i]);
        backtrack(i+1, nums, cur, res);
        cur.pop_back();
    }
}

// Call with sorted array
vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> res;
    vector<int> cur;
    backtrack(0, nums, cur, res);
    return res;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 78 | Subsets | [Link](https://leetcode.com/problems/subsets/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/05/medium-78-subsets/) |
| 90 | Subsets II | [Link](https://leetcode.com/problems/subsets-ii/) | - |

## Combination Sum (Unbounded/Reuse Elements)

**When to use:** The problem asks for "all combinations that sum to target", "target sum with reuse allowed", or "find numbers adding to k".

Find all combinations that sum to target. Elements can be reused or used once depending on the problem.

### Combination Sum (can reuse same element)

```cpp
// Combination Sum (can reuse same element)
void backtrack(int start, vector<int>& candidates, int target, vector<int>& cur, vector<vector<int>>& res){
    if (target == 0){
        res.push_back(cur);
        return;
    }
    if (target < 0) return;  // Pruning: target exceeded
    
    for (int i = start; i < (int)candidates.size(); ++i){
        cur.push_back(candidates[i]);
        // Can reuse: start=i (not i+1)
        backtrack(i, candidates, target - candidates[i], cur, res);
        cur.pop_back();
    }
}
```

### Combination Sum II (each element used once, duplicates exist)

```cpp
// Combination Sum II (each element used once, duplicates exist)
void backtrack(int start, vector<int>& candidates, int target, vector<int>& cur, vector<vector<int>>& res){
    if (target == 0){
        res.push_back(cur);
        return;
    }
    if (target < 0) return;
    
    for (int i = start; i < (int)candidates.size(); ++i){
        // Skip duplicates at the same level
        if (i > start && candidates[i] == candidates[i-1]) continue;
        cur.push_back(candidates[i]);
        // No reuse: start=i+1
        backtrack(i+1, candidates, target - candidates[i], cur, res);
        cur.pop_back();
    }
}

// Call with sorted array
vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> res;
    vector<int> cur;
    backtrack(0, candidates, target, cur, res);
    return res;
}
```

### Combination Sum III (choose k numbers from 1-9 that sum to n)

```cpp
// Combination Sum III: choose k numbers from 1-9 that sum to n
void backtrack(int start, int k, int n, vector<int>& cur, vector<vector<int>>& res){
    if (cur.size() == k && n == 0){
        res.push_back(cur);
        return;
    }
    if (cur.size() >= k || n < 0) return;
    
    for (int i = start; i <= 9; ++i){
        cur.push_back(i);
        backtrack(i+1, k, n-i, cur, res);
        cur.pop_back();
    }
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 39 | Combination Sum | [Link](https://leetcode.com/problems/combination-sum/) | - |
| 40 | Combination Sum II | [Link](https://leetcode.com/problems/combination-sum-ii/) | - |
| 216 | Combination Sum III | [Link](https://leetcode.com/problems/combination-sum-iii/) | - |

## Grid Backtracking (Word Search, Path Finding)

**When to use:** The problem says "find a path in a grid", "word search", "explore all directions", or involves marking/unmarking visited cells.

Backtrack on 2D grid with constraints. Mark cells as visited during exploration, then restore them.

### Word Search

```cpp
// Word Search: find if word exists in grid
bool dfs(vector<vector<char>>& board, int i, int j, string& word, int idx){
    if (idx == (int)word.size()) return true;
    if (i < 0 || i >= (int)board.size() || j < 0 || j >= (int)board[0].size()) return false;
    if (board[i][j] != word[idx]) return false;
    
    char temp = board[i][j];
    board[i][j] = '#';  // Mark as visited
    
    int dirs[4][2] = \{\{0,1\}, \{0,-1\}, \{1,0\}, \{-1,0\}\};
    for (auto& d : dirs){
        if (dfs(board, i+d[0], j+d[1], word, idx+1)) return true;
    }
    
    board[i][j] = temp;  // Backtrack: restore original value
    return false;
}

bool exist(vector<vector<char>>& board, string word) {
    for (int i = 0; i < (int)board.size(); ++i){
        for (int j = 0; j < (int)board[0].size(); ++j){
            if (dfs(board, i, j, word, 0)) return true;
        }
    }
    return false;
}
```

**Key points:**
- Mark cell as visited before recursion
- Restore cell value after recursion (backtracking)
- Check bounds and constraints before recursing

| ID | Title | Link | Solution |
|---|---|---|---|
| 79 | Word Search | [Link](https://leetcode.com/problems/word-search/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-79-word-search/) |
| 212 | Word Search II | [Link](https://leetcode.com/problems/word-search-ii/) | - |
| 351 | Android Unlock Patterns | [Link](https://leetcode.com/problems/android-unlock-patterns/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/02/medium-351-android-unlock-patterns/) |
| 425 | Word Squares | [Link](https://leetcode.com/problems/word-squares/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/12/31/hard-425-word-squares/) |
| 489 | Robot Room Cleaner | [Link](https://leetcode.com/problems/robot-room-cleaner/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-hard-489-robot-room-cleaner/) |

## Constraint Satisfaction (N-Queens, Sudoku)

**When to use:** The problem involves "placing items with constraints", "N-Queens", "Sudoku", or "valid placement" where each choice must satisfy multiple rules.

Backtracking with complex constraints. Validate each move before placing.

### N-Queens

```cpp
// N-Queens: place n queens on n×n board
void backtrack(int row, int n, vector<string>& board, vector<vector<string>>& res){
    if (row == n){
        res.push_back(board);
        return;
    }
    for (int col = 0; col < n; ++col){
        if (isValid(board, row, col, n)){
            board[row][col] = 'Q';
            backtrack(row+1, n, board, res);
            board[row][col] = '.';  // Backtrack
        }
    }
}

bool isValid(vector<string>& board, int row, int col, int n){
    // Check column above
    for (int i = 0; i < row; ++i) 
        if (board[i][col] == 'Q') return false;
    
    // Check diagonal \ (top-left to bottom-right)
    for (int i = row-1, j = col-1; i >= 0 && j >= 0; --i, --j)
        if (board[i][j] == 'Q') return false;
    
    // Check diagonal / (top-right to bottom-left)
    for (int i = row-1, j = col+1; i >= 0 && j < n; --i, ++j)
        if (board[i][j] == 'Q') return false;
    
    return true;
}
```

### Sudoku Solver

```cpp
// Sudoku Solver
bool solveSudoku(vector<vector<char>>& board){
    for (int i = 0; i < 9; ++i){
        for (int j = 0; j < 9; ++j){
            if (board[i][j] == '.'){
                for (char c = '1'; c <= '9'; ++c){
                    if (isValid(board, i, j, c)){
                        board[i][j] = c;
                        if (solveSudoku(board)) return true;
                        board[i][j] = '.';  // Backtrack
                    }
                }
                return false;  // No valid number found
            }
        }
    }
    return true;  // All cells filled
}

bool isValid(vector<vector<char>>& board, int row, int col, char c){
    for (int i = 0; i < 9; ++i){
        // Check row
        if (board[row][i] == c) return false;
        // Check column
        if (board[i][col] == c) return false;
        // Check 3x3 box
        if (board[3*(row/3) + i/3][3*(col/3) + i%3] == c) return false;
    }
    return true;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 51 | N-Queens | [Link](https://leetcode.com/problems/n-queens/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/hard-51-n-queens/) |
| 52 | N-Queens II | [Link](https://leetcode.com/problems/n-queens-ii/) | - |
| 37 | Sudoku Solver | [Link](https://leetcode.com/problems/sudoku-solver/) | - |

## Palindrome Partitioning

**When to use:** The problem asks to "partition a string into palindromes", "split into palindromic substrings", or "all ways to cut a string".

Partition string into palindromic substrings. Check if substring is palindrome before partitioning.

```cpp
// Palindrome Partitioning
void backtrack(int start, string& s, vector<string>& cur, vector<vector<string>>& res){
    if (start == (int)s.size()){
        res.push_back(cur);
        return;
    }
    for (int end = start; end < (int)s.size(); ++end){
        if (isPalindrome(s, start, end)){
            cur.push_back(s.substr(start, end-start+1));
            backtrack(end+1, s, cur, res);
            cur.pop_back();  // Backtrack
        }
    }
}

bool isPalindrome(string& s, int l, int r){
    while (l < r) {
        if (s[l++] != s[r--]) return false;
    }
    return true;
}
```

**Optimization:** Precompute palindrome table to avoid repeated checks.

```cpp
// Optimized: Precompute palindrome table
vector<vector<bool>> precomputePalindromes(string& s){
    int n = s.size();
    vector<vector<bool>> dp(n, vector<bool>(n, false));
    for (int i = n-1; i >= 0; --i){
        for (int j = i; j < n; ++j){
            if (i == j) dp[i][j] = true;
            else if (j == i+1) dp[i][j] = (s[i] == s[j]);
            else dp[i][j] = (s[i] == s[j] && dp[i+1][j-1]);
        }
    }
    return dp;
}
```

| ID | Title | Link | Solution |
|---|---|---|---|
| 131 | Palindrome Partitioning | [Link](https://leetcode.com/problems/palindrome-partitioning/) | [Solution](https://robinali34.github.io/blog_leetcode/2025/09/30/medium-131-palindrome-partitioning/) |
| 132 | Palindrome Partitioning II | [Link](https://leetcode.com/problems/palindrome-partitioning-ii/) | - |
| 5 | Longest Palindromic Substring | [Link](https://leetcode.com/problems/longest-palindromic-substring/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/08/medium-5-longest-palindromic-substring/) |
| 647 | Palindromic Substrings | [Link](https://leetcode.com/problems/palindromic-substrings/) | [Solution](https://robinali34.github.io/blog_leetcode/posts/2025-11-24-medium-647-palindromic-substrings/) |

## Parentheses Generation

Generate all valid parentheses combinations using backtracking.

```cpp
// Generate Parentheses: generate all valid n pairs
void backtrack(int n, int open, int close, string path, vector<string>& res){
    if(path.size() == 2 * n){
        res.push_back(path);
        return;
    }
    if(open < n){
        path.push_back('(');
        backtrack(n, open + 1, close, path, res);
        path.pop_back();
    }
    if(close < open){
        path.push_back(')');
        backtrack(n, open, close + 1, path, res);
        path.pop_back();
    }
}
```

**Key constraints:**
- `open < n`: Can add opening parenthesis if not all used
- `close < open`: Can add closing parenthesis if there are unmatched openings
- Base case: path length equals `2 * n`

| ID | Title | Link | Solution |
|---|---|---|---|
| 22 | Generate Parentheses | [Link](https://leetcode.com/problems/generate-parentheses/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/01/12/medium-22-generate-parentheses/) |
| 1087 | Brace Expansion | [Link](https://leetcode.com/problems/brace-expansion/) | [Solution](https://robinali34.github.io/blog_leetcode/2026/03/26/medium-1087-brace-expansion/) |

## General Backtracking Template

```cpp
void backtrack(state, constraints, current_solution, results){
    // Base case: solution is complete
    if (isComplete(current_solution)){
        results.add(current_solution);
        return;
    }
    
    // Generate candidates
    for (each candidate in candidates){
        // Pruning: skip invalid candidates early
        if (isValid(candidate, constraints)){
            // Make move: add candidate to solution
            makeMove(candidate, current_solution);
            
            // Recurse: explore further
            backtrack(updated_state, constraints, current_solution, results);
            
            // Backtrack: remove candidate to try next option
            undoMove(candidate, current_solution);
        }
    }
}
```

**Key Points:**
- **Base Case**: When solution is complete, add to results
- **Pruning**: Skip invalid candidates early to reduce search space
- **Make Move**: Add candidate to current solution and update state
- **Recurse**: Explore further with updated state
- **Backtrack**: Remove candidate and restore state to try next option

**Common Optimizations:**
1. **Early pruning**: Check constraints before recursing
2. **Memoization**: Cache results for repeated subproblems (if applicable)
3. **Sorting**: Sort input to handle duplicates efficiently
4. **Precomputation**: Precompute expensive checks (e.g., palindrome table)

**Time Complexity:** Typically exponential O(2^n) or O(n!) depending on problem
**Space Complexity:** O(depth) for recursion stack + O(solution_size) for current solution

## Quick Reference

| Pattern | Signal | # Solutions | Time |
|---|---|---|---|
| Permutations | "all arrangements", "ordering" | n! | O(n × n!) |
| Combinations | "choose k from n" | C(n,k) | O(C(n,k)) |
| Subsets | "all subsets", "power set" | 2^n | O(n × 2^n) |
| Combination Sum | "target sum with reuse" | varies | O(2^n) |
| Grid | "find path in grid" | varies | O(4^(m×n)) |
| Constraint | "N-Queens", "Sudoku" | varies | O(n!) |

## More templates

- **Beginner's Guide:** [LeetCode Beginner's Guide](/2026/06/25/leetcode-beginners-guide/)
- **Data structures, Graph, Search:** [Data Structures & Core Algorithms](/posts/2025-10-29-leetcode-templates-data-structures/), [Graph](/posts/2025-10-29-leetcode-templates-graph/), [Search](/posts/2026-01-20-leetcode-templates-search/)
- **Master index:** [Categories & Templates](/posts/2025-10-29-leetcode-categories-and-templates/)
