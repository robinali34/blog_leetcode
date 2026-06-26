---
layout: post
title: "[Easy] 1710. Maximum Units on a Truck"
date: 2026-01-04 00:00:00 -0700
categories: [leetcode, easy, array, greedy, sorting]
permalink: /2026/01/04/easy-1710-maximum-units-on-a-truck/
---
You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

- `numberOfBoxesi` is the number of boxes of type `i`.
- `numberOfUnitsPerBoxi` is the number of units in each box of the type `i`.

You are also given an integer `truckSize`, which is the **maximum number of boxes** that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return *the **maximum** total number of **units** that can be put on the truck*.

## Examples

**Example 1:**
```
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
```

**Example 2:**
```
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
Explanation: 
- Take 5 boxes of type 1 (5 * 10 = 50 units)
- Take 3 boxes of type 3 (3 * 9 = 27 units)
- Take 2 boxes of type 2 (2 * 5 = 10 units)
- Take 0 boxes of type 4
Total: 50 + 27 + 10 = 87... wait, let me recalculate.
Actually: Take boxes in order of units per box (descending):
- 5 boxes of type 1: 5 * 10 = 50
- 3 boxes of type 3: 3 * 9 = 27
- 2 boxes of type 2: 2 * 5 = 10
Total: 50 + 27 + 10 = 87, but we have 10 boxes, so we can take 2 more boxes of type 4: 2 * 7 = 14
Total: 50 + 27 + 10 + 14 = 101... Actually, let me verify with the algorithm.
```

## Constraints

- `1 <= boxTypes.length <= 1000`
- `1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000`
- `1 <= truckSize <= 10^6`

## Thinking Process

You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

- `numberOfBoxesi` is the number of boxes of type `i`.

- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 100" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Greedy choice</text>

  <line x1="30" y1="55" x2="250" y2="55" stroke="#D4D1CC" stroke-width="2"/>
  <rect x="60" y="43" width="40" height="22" rx="3" fill="#A8B5A2" stroke="#6B8B6B"/>
  <rect x="130" y="43" width="55" height="22" rx="3" fill="#D4D8E0" stroke="#8B8680"/>
  <rect x="200" y="43" width="35" height="22" rx="3" fill="#E8D5D0" stroke="#B8A5A0"/>
  <text x="140" y="90" text-anchor="middle" font-size="11" fill="#6B6560">pick locally best after sorting</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Sort + greedy** *(this problem)* | O(n log n) | O(1) | Interval scheduling, assignment |
| Local greedy choice | O(n) | O(1) | Jump game, gas station |
| Greedy + heap | O(n log n) | O(n) | Merge streams, room allocation |
| Exchange argument | O(n) | O(1) | Prove greedy choice is safe |

## Solution

### **Solution: Greedy with Sorting**

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [](auto& u, auto& v){
            return u[1] > v[1];
        });
        int remainSize = truckSize;
        int maximumUnits = 0;
        for(auto& boxType: boxTypes) {
            if(remainSize == 0) break;
            int cnt = min(remainSize, boxType[0]);
            maximumUnits += cnt * boxType[1];
            remainSize -= cnt;
        }
        return maximumUnits;
    }
};
```

### Solution Explanation

**Approach:** Sort + greedy (this problem)

**Key idea:** You are assigned to put some amount of boxes onto **one truck**. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`:

**How the code works:**
- `numberOfBoxesi` is the number of boxes of type `i`.
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.
- Prove or sanity-check: would swapping two choices ever help?

**Walkthrough** — input `boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4`, expected output `8`:

There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

**Time:** - **Sorting**: O(n log n) where n = `boxTypes.length` · **Space:** O(1)

### **Algorithm Explanation:**

1. **Sort by Units Per Box (Lines 4-6)**:
   - Sort `boxTypes` in descending order of `boxType[1]` (units per box)
   - This ensures we process boxes with highest units first
   - Custom comparator: `u[1] > v[1]` sorts by units per box (descending)

2. **Initialize Variables (Lines 7-8)**:
   - `remainSize`: Remaining truck capacity (starts at `truckSize`)
   - `maximumUnits`: Total units accumulated (starts at 0)

3. **Greedy Selection (Lines 9-14)**:
   - **For each box type** (in sorted order):
     - **Early termination**: If `remainSize == 0`, break (truck is full)
     - **Take boxes**: `cnt = min(remainSize, boxType[0])`
       - Take as many boxes as possible, limited by:
         - Remaining truck capacity (`remainSize`)
         - Available boxes of this type (`boxType[0]`)
     - **Add units**: `maximumUnits += cnt * boxType[1]`
     - **Update capacity**: `remainSize -= cnt`

4. **Return (Line 15)**:
   - Return the total units accumulated

### **Example Walkthrough:**

**Example 1: `boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4`**

**After sorting by units per box (descending):**
```
Original: [[1,3], [2,2], [3,1]]
Sorted:   [[1,3], [2,2], [3,1]]  (already in order: 3 > 2 > 1)
```

**Execution:**
```
Initial: remainSize = 4, maximumUnits = 0

Step 1: boxType = [1, 3]
  cnt = min(4, 1) = 1
  maximumUnits = 0 + 1 * 3 = 3
  remainSize = 4 - 1 = 3

Step 2: boxType = [2, 2]
  cnt = min(3, 2) = 2
  maximumUnits = 3 + 2 * 2 = 7
  remainSize = 3 - 2 = 1

Step 3: boxType = [3, 1]
  cnt = min(1, 3) = 1
  maximumUnits = 7 + 1 * 1 = 8
  remainSize = 1 - 1 = 0

Result: 8
```

**Visual Representation:**
```
Box Types (sorted by units):
Type 1: [1 box, 3 units/box] → Take 1 box → 3 units
Type 2: [2 boxes, 2 units/box] → Take 2 boxes → 4 units
Type 3: [3 boxes, 1 unit/box] → Take 1 box → 1 unit
Total: 3 + 4 + 1 = 8 units
```

**Example 2: `boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10`**

**After sorting by units per box (descending):**
```
Original: [[5,10], [2,5], [4,7], [3,9]]
Sorted:   [[5,10], [3,9], [4,7], [2,5]]  (10 > 9 > 7 > 5)
```

**Execution:**
```
Initial: remainSize = 10, maximumUnits = 0

Step 1: boxType = [5, 10]
  cnt = min(10, 5) = 5
  maximumUnits = 0 + 5 * 10 = 50
  remainSize = 10 - 5 = 5

Step 2: boxType = [3, 9]
  cnt = min(5, 3) = 3
  maximumUnits = 50 + 3 * 9 = 77
  remainSize = 5 - 3 = 2

Step 3: boxType = [4, 7]
  cnt = min(2, 4) = 2
  maximumUnits = 77 + 2 * 7 = 91
  remainSize = 2 - 2 = 0

Step 4: boxType = [2, 5]
  remainSize == 0, break

Result: 91
```

## Algorithm Breakdown

### **Why Greedy Works**

The greedy strategy is optimal because:
1. **Highest Units First**: Taking boxes with highest units per box maximizes units per box slot
2. **No Regret**: If we skip a high-unit box, we can't use that capacity later
3. **Optimal Substructure**: After taking boxes, the remaining problem is independent
4. **Mathematical Proof**: Any other ordering would result in fewer total units

**Intuition:**
- If we have 1 box slot and two options:
  - Box A: 10 units
  - Box B: 5 units
- We should take Box A (greedy choice)
- This applies recursively: always take the best available option

### **Why Sorting is Necessary**

Without sorting, we might:
- Take low-unit boxes first, wasting capacity
- Miss opportunities to maximize units
- Need to check all combinations (exponential)

With sorting:
- Process boxes in order of value (units per box)
- Greedy choice is optimal
- Linear time after sorting

### **Key Insight: Units Per Box**

The critical metric is **units per box**, not total units:
- Box type [100, 1]: 100 boxes, 1 unit each = 100 total units, but 1 unit/box
- Box type [1, 100]: 1 box, 100 units = 100 total units, but 100 units/box
- If truckSize = 1, we should take the second type (100 units vs 1 unit)

## Time & Space Complexity

- **Time Complexity**: 
  - **Sorting**: O(n log n) where n = `boxTypes.length`
  - **Greedy Selection**: O(n) - single pass through sorted array
  - **Total**: O(n log n)
- **Space Complexity**: O(1)
  - Only using a few variables (`remainSize`, `maximumUnits`, `cnt`)
  - Sorting is typically in-place (O(1) extra space)

## Key Points

1. **Greedy Algorithm**: Always make locally optimal choice (highest units per box)
2. **Sorting**: Essential for greedy approach to work correctly
3. **Units Per Box**: The key metric, not total units
4. **Optimal**: Greedy strategy finds maximum units
5. **Simple**: Straightforward implementation after sorting

## Common Mistakes

1. **Truck size equals total boxes**: `truckSize = sum(boxTypes[i][0])` → take all boxes
2. **Truck size is 1**: Take one box with highest units per box
3. **All boxes have same units per box**: Order doesn't matter, take until full
4. **Single box type**: Take `min(truckSize, boxTypes[0][0])` boxes
5. **Truck size larger than all boxes**: Take all boxes, return sum of all units

1. **Not sorting**: Trying to select boxes without sorting by units per box
2. **Wrong metric**: Sorting by total units instead of units per box
3. **Wrong order**: Sorting in ascending instead of descending order
4. **Not tracking remaining**: Forgetting to update `remainSize`
5. **Off-by-one errors**: Incorrect calculation of boxes to take

## Related Problems

- [455. Assign Cookies](https://www.leetcode.com/problems/assign-cookies/) - Greedy matching
- [435. Non-overlapping Intervals](https://www.leetcode.com/problems/non-overlapping-intervals/) - Greedy interval selection
- [452. Minimum Number of Arrows to Burst Balloons](https://www.leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/) - Greedy with sorting
- [322. Coin Change](https://www.leetcode.com/problems/coin-change/) - Similar greedy concept (though DP is better)
- [860. Lemonade Change](https://www.leetcode.com/problems/lemonade-change/) - Greedy change giving

## Tags

`Array`, `Greedy`, `Sorting`, `Easy`

## Key Takeaways

- `numberOfBoxesi` is the number of boxes of type `i`.
- Greedy works when local optimal choices lead to global optimum.
- Often sort first to make the greedy choice obvious.

## References

- [LC 1710: Maximum Units on a Truck on LeetCode](https://www.leetcode.com/problems/maximum-units-on-a-truck/)
- [LeetCode Discuss — LC 1710: Maximum Units on a Truck](https://www.leetcode.com/problems/maximum-units-on-a-truck/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/maximum-units-on-a-truck/editorial/) *(may require premium)*

## Template Reference

- [Array & Matrix](/blog_leetcode/posts/2025-11-24-leetcode-templates-array-matrix/)
