---
layout: post
title: "LeetCode Beginner's Guide: From Zero to Competitive Programming"
date: 2026-06-25
categories: [guide, leetcode]
tags: [guide, leetcode, beginner, competitive-programming, interview-prep]
permalink: /2026/06/25/leetcode-beginners-guide/
---

So you've heard about LeetCode but aren't sure where to start? Or maybe you've opened a problem, stared at it for 30 minutes, and closed the tab? You're not alone -- everyone starts there.

This guide walks you through everything step by step: what LeetCode actually is, how to use it, what the difficulty levels mean, and exactly which problems to solve first. No prior algorithm experience required.

> **New to C++?** Check out the [C++ Guide](/blog_leetcode/cpp-guide/) to learn the language alongside this guide.

## What Is LeetCode?

[LeetCode](https://leetcode.com/) is a website with **3000+** coding puzzles. Each puzzle gives you a problem, and you write code to solve it. Think of it like a gym for your brain -- instead of lifting weights, you're training your problem-solving muscles.

**People use LeetCode for:**

- **Getting a tech job** -- companies like Google, Meta, Amazon, and Microsoft ask LeetCode-style questions in interviews. It's the standard.
- **Learning algorithms** -- the problems teach you patterns (sorting, searching, graph traversal) that come up everywhere in real software.
- **Competitive programming** -- if you want to compete in ICPC, Codeforces, or AtCoder, LeetCode is a great starting point.

**What makes it different from tutorials?** LeetCode doesn't teach you theory then quiz you. It throws you into a problem, and you figure out which technique applies. That's exactly what interviews and real engineering feel like.

## How the Platform Works

### What a Problem Looks Like

Every LeetCode problem has four parts:

| Part | What It Tells You | Why It Matters |
|---|---|---|
| **Description** | The problem statement | Read carefully -- every word matters |
| **Examples** | Sample input → expected output | Work through these by hand before coding |
| **Constraints** | How large the input can be | Tells you which approaches are fast enough |
| **Follow-up** | An optional harder challenge | Ignore this at first, come back later |

### Your First Submission

Here's exactly what happens when you solve a problem:

1. **Pick a language** -- C++, Python, Java, or others (new to C++? See the [C++ Guide](/blog_leetcode/cpp-guide/))
2. **Write your code** in the browser editor
3. **Click "Run"** -- tests your code against the visible examples
4. **Click "Submit"** -- tests against hundreds of hidden test cases
5. **Get a verdict:**

| Verdict | What It Means | What to Do |
|---|---|---|
| **Accepted (AC)** | Your code is correct and fast enough | Celebrate, then read other solutions |
| **Wrong Answer (WA)** | Incorrect output on some test case | Check edge cases and logic |
| **Time Limit Exceeded (TLE)** | Too slow | You need a faster algorithm |
| **Memory Limit Exceeded (MLE)** | Uses too much memory | Optimize your data structures |
| **Runtime Error (RE)** | Crash (null pointer, out of bounds, etc.) | Check array bounds and null checks |

Don't be discouraged by WA or TLE -- they're normal, even for experienced programmers. Each failed submission teaches you something.

### The Secret Cheat Sheet: Reading Constraints

Here's something most beginners miss: **the constraints section tells you which algorithm to use.** The input size directly determines what time complexity is acceptable:

| Input size `n` | Target Complexity | What This Means | Typical Approaches |
|---|---|---|---|
| $n \le 10$ | $O(n!)$ or $O(2^n)$ | Try everything | Brute force, backtracking |
| $n \le 20$ | $O(2^n)$ | Subsets / states | Bitmask DP |
| $n \le 500$ | $O(n^3)$ | Triple loop is OK | Floyd-Warshall, matrix DP |
| $n \le 5{,}000$ | $O(n^2)$ | Double loop is OK | DP, two pointers |
| $n \le 10^5$ | $O(n \log n)$ | Sort + scan | Sorting, binary search |
| $n \le 10^6$ | $O(n)$ | Single pass | Hash map, sliding window |
| $n \le 10^9$ | $O(\log n)$ | No array at all | Binary search on answer, math |

**Example:** If a problem says $1 \le n \le 10^5$, an $O(n^2)$ solution will be too slow ($10^{10}$ operations). You need $O(n \log n)$ or better -- think sorting or binary search.

## Difficulty Levels Explained

LeetCode marks every problem as Easy, Medium, or Hard. Here's what that actually means in practice:

### Easy -- "Learn the building blocks"

You need **one** technique and the path is usually obvious. If you know the right data structure, the code writes itself.

**You'll use:** Arrays, hash maps, basic string operations, simple loops.

**Examples (try these first!):**
- [1. Two Sum](https://leetcode.com/problems/two-sum/) -- "Can I look up values instantly?" Yes: use a hash map.
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) -- Pure pointer manipulation, no tricks.
- [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) -- Your first recursion problem.

**Benchmark:** Can you solve a new Easy in 10-15 minutes? If not, keep practicing at this level. There's no shame in it -- foundations matter.

### Medium -- "This is where interviews live"

You need to **recognize a pattern** and sometimes combine two techniques. The approach isn't always obvious -- that's the challenge.

**You'll use:** BFS/DFS, dynamic programming, sliding window, binary search, graphs.

**Examples:**
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) -- "I see a grid, I need to explore connected regions." DFS or BFS.
- [322. Coin Change](https://leetcode.com/problems/coin-change/) -- "Minimize something with choices at each step." Classic DP.
- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) -- Combine a hash map with a linked list. Design problems test your ability to compose data structures.

**Benchmark:** Solve in 20-30 minutes. Most of your practice time should be here.

### Hard -- "Come back later"

Multiple techniques, tricky edge cases, or a key insight that's genuinely difficult to find. These test mastery, not learning.

**Examples:**
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) -- Two pointers or monotonic stack
- [295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) -- Two heaps working together
- [329. Longest Increasing Path in a Matrix](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) -- DFS + memoization on a grid

**Don't start here.** Seriously. Come back after you're comfortable solving Medium problems. Hard problems build on patterns you learn from Medium.

## Your Roadmap: From Zero to Interview-Ready

Don't try to learn everything at once. Follow these phases in order -- each one builds on the last.

### Phase 1: Foundations (Weeks 1-4) -- "Get comfortable"

**Goal:** Solve Easy problems without getting stuck. Build muscle memory with basic data structures.

**What to learn:**
- **Arrays and strings** -- looping, indexing, basic manipulation
- **Hash maps** -- the single most useful data structure in interviews (instant lookup)
- **Linked lists** -- pointer manipulation (this feels weird at first, that's normal)
- **Stacks and queues** -- LIFO vs FIFO, when to use each
- **Basic recursion** -- "solve a smaller version of the same problem"

> **Learning C++ alongside?** Work through Stages 1-2 of the [C++ Guide](/blog_leetcode/cpp-guide/) in parallel.

**Start with these 10 problems (in order):**

| # | Problem | Topic |
|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Hash Map |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Hash Set |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Hash Map / Sorting |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Stack |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Linked List |
| 21 | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Linked List |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Array / Greedy |
| 70 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Basic DP |
| 104 | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Tree / Recursion |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Tree / Recursion |

### Phase 2: Core Patterns (Weeks 5-12) -- "Learn to recognize"

**Goal:** When you see a new problem, you can say "This looks like a sliding window problem" or "This is DFS on a grid." Pattern recognition is the core skill.

**The 9 patterns that cover 90% of interview questions:**

| Pattern | Key Problems | Template |
|---|---|---|
| Sliding Window | 3, 76, 424, 567 | [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/) |
| Two Pointers | 15, 11, 167, 42 | [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/) |
| Binary Search | 33, 34, 153, 875 | [Search](/blog_leetcode/posts/2026-01-20-leetcode-templates-search/) |
| BFS / DFS | 200, 133, 695, 994 | [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/), [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/) |
| Dynamic Programming | 70, 198, 322, 300 | [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/) |
| Backtracking | 46, 78, 39, 79 | [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/) |
| Graphs | 207, 210, 743, 261 | [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/) |
| Heap / Priority Queue | 215, 347, 295 | [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/) |
| Monotonic Stack | 84, 739, 496 | [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/) |

**How to study each pattern:**
1. Read the template page linked above -- understand the general approach
2. Solve 3-5 problems in that category
3. **Stuck for 20+ minutes?** That's OK. Read the editorial, understand it, then **re-solve from scratch the next day** without looking. This is where real learning happens.
4. Move to the next pattern once you can solve new problems in the category without hints

### Phase 3: Competition Readiness (Weeks 13+) -- "Get fast"

**Goal:** Solve 2-3 Medium problems in 60 minutes under time pressure.

**How to practice:**
- **Timed sessions** -- set a 60-minute timer, pick 2 random Medium problems
- **Weekly contests** -- LeetCode runs one every Sunday (4 problems, 90 minutes). Just try it -- you'll probably only solve 1-2 at first, and that's fine.
- **Retry list** -- every problem you couldn't solve goes on a list. Revisit it weekly.
- **Codeforces Div 2** -- problems A and B are comparable to LeetCode Easy/Medium, but with a competitive twist

**Advanced topics (when you're ready):**

| Topic | What It's For | Template |
|---|---|---|
| Segment Tree / BIT | Range queries and updates | [Data Structures](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/) |
| Topological Sort | Ordering tasks with dependencies | [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/) |
| Union Find (DSU) | Grouping connected components | [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/) |
| Bit Manipulation | Power-of-2 tricks, subset enumeration | [Math & Bit](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/) |
| Advanced DP | Bitmask DP, digit DP, tree DP | [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/) |

## The Must-Know Problem Lists

Don't try to do all 3000+ LeetCode problems. These curated lists are the most efficient paths to interview readiness — start with **Blind 75** for the core, then **NeetCode 150** for full pattern coverage.

| List | Problems | Best For |
|---|---|---|
| [Blind 75](https://leetcode.com/problem-list/79h8rn6/) | 75 | First pass — covers every major category |
| [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) | 150 | Blind 75 + 75 more — deeper practice per pattern |
| [NeetCode 250](https://neetcode.io/practice/practice/neetcode250) | 250 | After 150 — extra hard problems and company tags |

### Blind 75 -- The Essential Core

The original "must-do" list. 75 problems that cover every major category with no fluff. If you deeply understand each solution (not just memorize it), you're ready for most interviews.

| Category | Count | Problem Numbers |
|---|---|---|
| Array & Hashing | 9 | 1, 49, 238, 128, 217, 242, 347, 271, 659 |
| Two Pointers | 3 | 15, 11, 125 |
| Sliding Window | 4 | 3, 424, 76, 567 |
| Stack | 1 | 20 |
| Binary Search | 2 | 153, 33 |
| Linked List | 6 | 206, 21, 141, 143, 19, 23 |
| Trees | 11 | 226, 104, 100, 572, 102, 297, 230, 98, 235, 105, 124 |
| Heap | 1 | 295 |
| Backtracking | 2 | 39, 79 |
| Graphs | 6 | 200, 133, 417, 207, 323, 261 |
| 1-D DP | 10 | 70, 198, 213, 5, 647, 91, 322, 139, 300, 152 |
| 2-D DP | 2 | 62, 1143 |
| Greedy | 2 | 53, 55 |
| Intervals | 4 | 57, 56, 435, 252 |
| Math & Bit | 3 | 191, 338, 268 |

### NeetCode 150 -- The Full Interview Roadmap

[NeetCode 150](https://neetcode.io/practice/practice/neetcode150) is **Blind 75 plus 75 more problems** in the same pattern-based structure. On the official site it is described as *"the perfect list for people already familiar with basic algorithms & data structures."*

**Practice on NeetCode:** [neetcode.io/practice/neetcode150](https://neetcode.io/practice/practice/neetcode150) · **LeetCode list:** [problem-list/ebdgnf5s](https://leetcode.com/problem-list/ebdgnf5s/)

#### Why NeetCode 150?

| Value | What You Get |
|---|---|
| **Curated roadmap** | 18 categories in a logical study order — not a random grab bag |
| **Pattern-first** | Each section drills one technique (sliding window, topo sort, interval DP, etc.) |
| **Efficient scope** | 150 problems vs. 3000+ on LeetCode — quality over quantity |
| **Progress tracking** | Track Easy / Medium / Hard completion on [NeetCode](https://neetcode.io/practice/practice/neetcode150) |
| **Video walkthroughs** | Free video solutions for every problem on the [NeetCode YouTube channel](https://www.youtube.com/@neetcode) |
| **Maps to this blog** | Most categories link directly to our [algorithm templates](/blog_leetcode/leetcode-templates/) |

**Difficulty split:** 28 Easy · 101 Medium · 21 Hard (**150 total**)

#### Recommended study order

Follow the [NeetCode Roadmap](https://neetcode.io/roadmap) — work through categories top to bottom:

1. **Foundations** — Arrays & Hashing → Two Pointers → Sliding Window → Stack → Binary Search
2. **Core structures** — Linked List → Trees → Tries → Heap / Priority Queue
3. **Search & graphs** — Backtracking → Graphs → Advanced Graphs
4. **Optimization** — 1-D DP → 2-D DP → Greedy → Intervals → Math & Geometry → Bit Manipulation

> **When to start:** Finish Phase 1–2 of the roadmap above (or complete Blind 75) before diving into NeetCode 150. You should already be comfortable with hash maps, basic recursion, and at least one traversal (BFS or DFS).

#### Category overview

| Category | Count | Template on this blog |
|---|---|---|
| Arrays & Hashing | 9 | [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/) |
| Two Pointers | 5 | [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/) |
| Sliding Window | 6 | [Arrays & Strings](/blog_leetcode/posts/2025-10-29-leetcode-templates-arrays-strings/) |
| Stack | 6 | [Stack](/blog_leetcode/posts/2025-11-13-leetcode-templates-stack/) |
| Binary Search | 7 | [Search](/blog_leetcode/posts/2026-01-20-leetcode-templates-search/) |
| Linked List | 11 | [Linked List](/blog_leetcode/posts/2025-11-24-leetcode-templates-linked-list/) |
| Trees | 15 | [Trees](/blog_leetcode/posts/2025-10-29-leetcode-templates-trees/) |
| Heap / Priority Queue | 7 | [Heap](/blog_leetcode/posts/2026-01-05-leetcode-templates-heap/) |
| Backtracking | 10 | [Backtracking](/blog_leetcode/posts/2025-11-24-leetcode-templates-backtracking/) |
| Tries | 3 | [Data Structures](/blog_leetcode/posts/2025-10-29-leetcode-templates-data-structures/) |
| Graphs | 13 | [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/), [BFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-bfs/), [DFS](/blog_leetcode/posts/2025-11-24-leetcode-templates-dfs/) |
| Advanced Graphs | 6 | [Graph](/blog_leetcode/posts/2025-10-29-leetcode-templates-graph/) |
| 1-D Dynamic Programming | 12 | [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/) |
| 2-D Dynamic Programming | 11 | [DP](/blog_leetcode/posts/2025-10-29-leetcode-templates-dp/) |
| Greedy | 8 | [Greedy](/blog_leetcode/posts/2025-12-14-leetcode-templates-greedy/) |
| Intervals | 6 | [Greedy](/blog_leetcode/posts/2025-12-14-leetcode-templates-greedy/) |
| Math & Geometry | 8 | [Math & Geometry](/blog_leetcode/posts/2025-10-29-leetcode-templates-math-geometry/), [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/) |
| Bit Manipulation | 7 | [Math & Bit](/blog_leetcode/posts/2025-11-24-leetcode-templates-math-bit-manipulation/) |

#### Complete problem list (150)

Problems are listed in NeetCode roadmap order. Premium problems are marked with †.

**Arrays & Hashing (9)**

| LC | Problem |
|---|---|
| [217](https://leetcode.com/problems/contains-duplicate/) | Contains Duplicate |
| [242](https://leetcode.com/problems/valid-anagram/) | Valid Anagram |
| [1](https://leetcode.com/problems/two-sum/) | Two Sum |
| [349](https://leetcode.com/problems/intersection-of-two-arrays/) | Intersection of Two Arrays |
| [128](https://leetcode.com/problems/longest-consecutive-sequence/) | Longest Consecutive Sequence |
| [238](https://leetcode.com/problems/product-of-array-except-self/) | Product of Array Except Self |
| [271](https://leetcode.com/problems/encode-and-decode-strings/)† | Encode and Decode Strings |
| [49](https://leetcode.com/problems/group-anagrams/) | Group Anagrams |
| [347](https://leetcode.com/problems/top-k-frequent-elements/) | Top K Frequent Elements |

**Two Pointers (5)**

| LC | Problem |
|---|---|
| [125](https://leetcode.com/problems/valid-palindrome/) | Valid Palindrome |
| [167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Two Sum II |
| [15](https://leetcode.com/problems/3sum/) | 3Sum |
| [11](https://leetcode.com/problems/container-with-most-water/) | Container With Most Water |
| [42](https://leetcode.com/problems/trapping-rain-water/) | Trapping Rain Water |

**Sliding Window (6)**

| LC | Problem |
|---|---|
| [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Best Time to Buy and Sell Stock |
| [3](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Longest Substring Without Repeating Characters |
| [424](https://leetcode.com/problems/longest-repeating-character-replacement/) | Longest Repeating Character Replacement |
| [567](https://leetcode.com/problems/permutation-in-string/) | Permutation in String |
| [76](https://leetcode.com/problems/minimum-window-substring/) | Minimum Window Substring |
| [239](https://leetcode.com/problems/sliding-window-maximum/) | Sliding Window Maximum |

**Stack (6)**

| LC | Problem |
|---|---|
| [20](https://leetcode.com/problems/valid-parentheses/) | Valid Parentheses |
| [155](https://leetcode.com/problems/min-stack/) | Min Stack |
| [150](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Evaluate Reverse Polish Notation |
| [739](https://leetcode.com/problems/daily-temperatures/) | Daily Temperatures |
| [394](https://leetcode.com/problems/decode-string/) | Decode String |
| [853](https://leetcode.com/problems/car-fleet/) | Car Fleet |

**Binary Search (7)**

| LC | Problem |
|---|---|
| [704](https://leetcode.com/problems/binary-search/) | Binary Search |
| [74](https://leetcode.com/problems/search-a-2d-matrix/) | Search a 2D Matrix |
| [875](https://leetcode.com/problems/koko-eating-bananas/) | Koko Eating Bananas |
| [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Find Minimum in Rotated Sorted Array |
| [33](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Search in Rotated Sorted Array |
| [981](https://leetcode.com/problems/time-based-key-value-store/) | Time Based Key-Value Store |
| [4](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Median of Two Sorted Arrays |

**Linked List (11)**

| LC | Problem |
|---|---|
| [206](https://leetcode.com/problems/reverse-linked-list/) | Reverse Linked List |
| [21](https://leetcode.com/problems/merge-two-sorted-lists/) | Merge Two Sorted Lists |
| [143](https://leetcode.com/problems/reorder-list/) | Reorder List |
| [19](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Remove Nth Node From End of List |
| [138](https://leetcode.com/problems/copy-list-with-random-pointer/) | Copy List with Random Pointer |
| [2](https://leetcode.com/problems/add-two-numbers/) | Add Two Numbers |
| [141](https://leetcode.com/problems/linked-list-cycle/) | Linked List Cycle |
| [287](https://leetcode.com/problems/find-the-duplicate-number/) | Find the Duplicate Number |
| [146](https://leetcode.com/problems/lru-cache/) | LRU Cache |
| [23](https://leetcode.com/problems/merge-k-sorted-lists/) | Merge k Sorted Lists |
| [25](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Reverse Nodes in k-Group |

**Trees (15)**

| LC | Problem |
|---|---|
| [226](https://leetcode.com/problems/invert-binary-tree/) | Invert Binary Tree |
| [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Maximum Depth of Binary Tree |
| [543](https://leetcode.com/problems/diameter-of-binary-tree/) | Diameter of Binary Tree |
| [110](https://leetcode.com/problems/balanced-binary-tree/) | Balanced Binary Tree |
| [100](https://leetcode.com/problems/same-tree/) | Same Tree |
| [572](https://leetcode.com/problems/subtree-of-another-tree/) | Subtree of Another Tree |
| [235](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Lowest Common Ancestor of a BST |
| [102](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Binary Tree Level Order Traversal |
| [199](https://leetcode.com/problems/binary-tree-right-side-view/) | Binary Tree Right Side View |
| [1448](https://leetcode.com/problems/count-good-nodes-in-binary-tree/) | Count Good Nodes in Binary Tree |
| [98](https://leetcode.com/problems/validate-binary-search-tree/) | Validate Binary Search Tree |
| [230](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | Kth Smallest Element in a BST |
| [105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Construct Binary Tree from Preorder and Inorder |
| [124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Maximum Path Sum |
| [297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Serialize and Deserialize Binary Tree |

**Tries (3)**

| LC | Problem |
|---|---|
| [208](https://leetcode.com/problems/implement-trie-prefix-tree/) | Implement Trie (Prefix Tree) |
| [211](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | Design Add and Search Words Data Structure |
| [212](https://leetcode.com/problems/word-search-ii/) | Word Search II |

**Heap / Priority Queue (7)**

| LC | Problem |
|---|---|
| [703](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Kth Largest Element in a Stream |
| [1046](https://leetcode.com/problems/last-stone-weight/) | Last Stone Weight |
| [973](https://leetcode.com/problems/k-closest-points-to-origin/) | K Closest Points to Origin |
| [215](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Kth Largest Element in an Array |
| [621](https://leetcode.com/problems/task-scheduler/) | Task Scheduler |
| [355](https://leetcode.com/problems/design-twitter/) | Design Twitter |
| [295](https://leetcode.com/problems/find-median-from-data-stream/) | Find Median from Data Stream |

**Backtracking (10)**

| LC | Problem |
|---|---|
| [78](https://leetcode.com/problems/subsets/) | Subsets |
| [39](https://leetcode.com/problems/combination-sum/) | Combination Sum |
| [46](https://leetcode.com/problems/permutations/) | Permutations |
| [90](https://leetcode.com/problems/subsets-ii/) | Subsets II |
| [40](https://leetcode.com/problems/combination-sum-ii/) | Combination Sum II |
| [79](https://leetcode.com/problems/word-search/) | Word Search |
| [131](https://leetcode.com/problems/palindrome-partitioning/) | Palindrome Partitioning |
| [17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) | Letter Combinations of a Phone Number |
| [51](https://leetcode.com/problems/n-queens/) | N-Queens |
| [22](https://leetcode.com/problems/generate-parentheses/) | Generate Parentheses |

**Graphs (13)**

| LC | Problem |
|---|---|
| [200](https://leetcode.com/problems/number-of-islands/) | Number of Islands |
| [133](https://leetcode.com/problems/clone-graph/) | Clone Graph |
| [695](https://leetcode.com/problems/max-area-of-island/) | Max Area of Island |
| [417](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Pacific Atlantic Water Flow |
| [130](https://leetcode.com/problems/surrounded-regions/) | Surrounded Regions |
| [994](https://leetcode.com/problems/rotting-oranges/) | Rotting Oranges |
| [286](https://leetcode.com/problems/walls-and-gates/)† | Walls and Gates |
| [207](https://leetcode.com/problems/course-schedule/) | Course Schedule |
| [210](https://leetcode.com/problems/course-schedule-ii/) | Course Schedule II |
| [684](https://leetcode.com/problems/redundant-connection/) | Redundant Connection |
| [323](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/) | Number of Connected Components |
| [261](https://leetcode.com/problems/graph-valid-tree/) | Graph Valid Tree |
| [127](https://leetcode.com/problems/word-ladder/) | Word Ladder |

**Advanced Graphs (6)**

| LC | Problem |
|---|---|
| [332](https://leetcode.com/problems/reconstruct-itinerary/) | Reconstruct Itinerary |
| [1584](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Min Cost to Connect All Points |
| [743](https://leetcode.com/problems/network-delay-time/) | Network Delay Time |
| [778](https://leetcode.com/problems/swim-in-rising-water/) | Swim in Rising Water |
| [269](https://leetcode.com/problems/alien-dictionary/)† | Alien Dictionary |
| [787](https://leetcode.com/problems/cheapest-flights-within-k-stops/) | Cheapest Flights Within K Stops |

**1-D Dynamic Programming (12)**

| LC | Problem |
|---|---|
| [70](https://leetcode.com/problems/climbing-stairs/) | Climbing Stairs |
| [746](https://leetcode.com/problems/min-cost-climbing-stairs/) | Min Cost Climbing Stairs |
| [198](https://leetcode.com/problems/house-robber/) | House Robber |
| [213](https://leetcode.com/problems/house-robber-ii/) | House Robber II |
| [5](https://leetcode.com/problems/longest-palindromic-substring/) | Longest Palindromic Substring |
| [647](https://leetcode.com/problems/palindromic-substrings/) | Palindromic Substrings |
| [91](https://leetcode.com/problems/decode-ways/) | Decode Ways |
| [322](https://leetcode.com/problems/coin-change/) | Coin Change |
| [152](https://leetcode.com/problems/maximum-product-subarray/) | Maximum Product Subarray |
| [139](https://leetcode.com/problems/word-break/) | Word Break |
| [300](https://leetcode.com/problems/longest-increasing-subsequence/) | Longest Increasing Subsequence |
| [416](https://leetcode.com/problems/partition-equal-subset-sum/) | Partition Equal Subset Sum |

**2-D Dynamic Programming (11)**

| LC | Problem |
|---|---|
| [62](https://leetcode.com/problems/unique-paths/) | Unique Paths |
| [1143](https://leetcode.com/problems/longest-common-subsequence/) | Longest Common Subsequence |
| [309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Best Time to Buy and Sell Stock with Cooldown |
| [518](https://leetcode.com/problems/coin-change-ii/) | Coin Change 2 |
| [494](https://leetcode.com/problems/target-sum/) | Target Sum |
| [97](https://leetcode.com/problems/interleaving-string/) | Interleaving String |
| [329](https://leetcode.com/problems/longest-increasing-path-in-a-matrix/) | Longest Increasing Path in a Matrix |
| [115](https://leetcode.com/problems/distinct-subsequences/) | Distinct Subsequences |
| [72](https://leetcode.com/problems/edit-distance/) | Edit Distance |
| [312](https://leetcode.com/problems/burst-balloons/) | Burst Balloons |
| [10](https://leetcode.com/problems/regular-expression-matching/) | Regular Expression Matching |

**Greedy (8)**

| LC | Problem |
|---|---|
| [53](https://leetcode.com/problems/maximum-subarray/) | Maximum Subarray |
| [55](https://leetcode.com/problems/jump-game/) | Jump Game |
| [45](https://leetcode.com/problems/jump-game-ii/) | Jump Game II |
| [134](https://leetcode.com/problems/gas-station/) | Gas Station |
| [846](https://leetcode.com/problems/hand-of-straights/) | Hand of Straights |
| [1899](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/) | Merge Triplets to Form Target Triplet |
| [763](https://leetcode.com/problems/partition-labels/) | Partition Labels |
| [678](https://leetcode.com/problems/valid-parenthesis-string/) | Valid Parenthesis String |

**Intervals (6)**

| LC | Problem |
|---|---|
| [57](https://leetcode.com/problems/insert-interval/) | Insert Interval |
| [56](https://leetcode.com/problems/merge-intervals/) | Merge Intervals |
| [435](https://leetcode.com/problems/non-overlapping-intervals/) | Non-overlapping Intervals |
| [252](https://leetcode.com/problems/meeting-rooms/)† | Meeting Rooms |
| [253](https://leetcode.com/problems/meeting-rooms-ii/)† | Meeting Rooms II |
| [2402](https://leetcode.com/problems/meeting-rooms-iii/) | Meeting Rooms III |

**Math & Geometry (8)**

| LC | Problem |
|---|---|
| [48](https://leetcode.com/problems/rotate-image/) | Rotate Image |
| [54](https://leetcode.com/problems/spiral-matrix/) | Spiral Matrix |
| [73](https://leetcode.com/problems/set-matrix-zeroes/) | Set Matrix Zeroes |
| [202](https://leetcode.com/problems/happy-number/) | Happy Number |
| [66](https://leetcode.com/problems/plus-one/) | Plus One |
| [50](https://leetcode.com/problems/powx-n/) | Pow(x, n) |
| [43](https://leetcode.com/problems/multiply-strings/) | Multiply Strings |
| [2013](https://leetcode.com/problems/detect-squares/)† | Detect Squares |

**Bit Manipulation (7)**

| LC | Problem |
|---|---|
| [136](https://leetcode.com/problems/single-number/) | Single Number |
| [191](https://leetcode.com/problems/number-of-1-bits/) | Number of 1 Bits |
| [338](https://leetcode.com/problems/counting-bits/) | Counting Bits |
| [190](https://leetcode.com/problems/reverse-bits/) | Reverse Bits |
| [268](https://leetcode.com/problems/missing-number/) | Missing Number |
| [371](https://leetcode.com/problems/sum-of-two-integers/) | Sum of Two Integers |
| [7](https://leetcode.com/problems/reverse-integer/) | Reverse Integer |

#### How to use NeetCode 150 effectively

1. **Follow the roadmap order** — don't skip ahead to DP before you can do trees comfortably.
2. **Pair with templates** — read the matching [template page](/blog_leetcode/leetcode-templates/) before each category.
3. **Watch the video after you try** — attempt the problem for 20–25 minutes first, then watch the NeetCode explanation.
4. **Track on NeetCode** — the [practice page](https://neetcode.io/practice/practice/neetcode150) shows your Easy/Medium/Hard progress bar.
5. **Revisit weak categories** — if Graphs feels hard, loop back to BFS/DFS templates before Advanced Graphs.

**More lists on NeetCode:** [Blind 75](https://neetcode.io/practice/practice/blind75) · [NeetCode 250](https://neetcode.io/practice/practice/neetcode250) · [How to use NeetCode effectively](https://neetcode.io/)

## Practical Tips That Actually Help

### When You're Stuck (This Will Happen a Lot)

Getting stuck is **normal** and **part of the process.** Here's a concrete checklist:

1. **Re-read the constraints** -- they tell you which algorithm to use (see the cheat sheet above)
2. **Draw it out** -- literally use pen and paper. Trace through the example step by step.
3. **Ask yourself: "What data structure would make this easier?"**
   - "I need instant lookup" → hash map
   - "I need sorted order" → heap, BST, or `set`
   - "I need to undo / go back" → stack
   - "I need to process in order" → queue
4. **After 25 minutes, read the editorial.** Don't waste 2 hours staring. Learning from solutions is still learning.
5. **The crucial step:** Re-solve the problem the next day **without looking at the solution.** This is where the learning actually sticks.

### The 5 Most Common Beginner Mistakes

| Mistake | Why It Hurts | The Fix |
|---|---|---|
| Jumping to Hard problems | You lack the patterns that Hard problems build on | Complete Phase 1 and 2 first |
| Memorizing code | You can reproduce one solution but can't adapt to variants | Focus on **why** the approach works, not the exact code |
| Never timing yourself | Interviews have time limits; untimed practice doesn't prepare you | Set a timer. Every time. |
| Only solving comfortable categories | Your weak areas stay weak | Track which categories you struggle with and prioritize them |
| Ignoring edge cases | Costs you "Accepted" on problems you otherwise solved | Always test: empty input, single element, all same values, maximum input size |

### Which Language Should I Use?

| Language | Best For | Trade-offs | Guide |
|---|---|---|---|
| **C++** | Competitive programming, maximum speed | More verbose, but STL is incredibly powerful | [C++ Guide](/blog_leetcode/cpp-guide/) |
| **Python** | Interviews, rapid prototyping | Slower runtime, may TLE on tight constraints | -- |
| **Java** | Enterprise interviews, strong typing | Verbose, slower than C++ | -- |

**Bottom line:** For competitive programming, use **C++** -- it's the industry standard. For interviews, use whatever language you're most comfortable with. The algorithm matters more than the language.

## Getting the Most Out of LeetCode

| Feature | What It Does | When to Use It |
|---|---|---|
| **Study Plans** | Daily curated problem sets | Great for building consistency — or use [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) |
| **Weekly Contests** | 4 problems, 90 min, every Sunday | Start joining once you can solve Medium problems |
| **Discussion Tab** | Other people's solutions | Read after every problem -- even ones you solved |
| **Company Tags** (Premium) | Which companies ask which problems | Useful when preparing for a specific interview |
| **Playground** | Quick code sandbox | Test snippets without creating a submission |

## What Comes After LeetCode?

Once you can consistently solve 2-3 Medium problems in a timed session:

1. **LeetCode Weekly Contests** -- measure yourself against others
2. **Codeforces Div 2** -- problems A and B are similar difficulty, but the contest format is different
3. **AtCoder** -- exceptional problem quality, especially for dynamic programming
4. **Books to level up:**
   - *Competitive Programming 3* by Steven Halim
   - *Guide to Competitive Programming* by Antti Laaksonen

Remember: the goal isn't to solve every problem. It's to **recognize patterns quickly** and **write correct solutions under pressure.**

---

## Quick Links

| Resource | Description |
|---|---|
| [LeetCode Templates Index](/blog_leetcode/leetcode-templates/) | All algorithm pattern templates on this blog |
| [NeetCode 150 (official)](https://neetcode.io/practice/practice/neetcode150) | Curated 150-problem interview roadmap with progress tracking |
| [All Solved Problems](/blog_leetcode/leetcode-questions-list.html) | Every problem solved on this blog, with links |
| [C++ Guide](/blog_leetcode/cpp-guide/) | Learn C++ for competitive programming |
