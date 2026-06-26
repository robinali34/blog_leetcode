---
layout: post
title: "[Easy] 346. Moving Average from Data Stream"
date: 2025-12-14 00:00:00 -0800
categories: leetcode algorithm easy cpp queue sliding-window design problem-solving
---
{% raw %}

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:

- `MovingAverage(int size)` Initializes the object with the size of the window `size`.
- `double next(int val)` Returns the moving average of the last `size` values of the stream.

## Examples

**Example 1:**
```
Input
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

## Constraints

- `1 <= size <= 1000`
- `-10^5 <= val <= 10^5`
- At most `10^4` calls will be made to `next`.

## Thinking Process

1. **Sliding window pattern**: Queue naturally maintains FIFO order

- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.



<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Sliding window</text>

  <rect x="20" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="36" y="63" text-anchor="middle" font-size="11">a</text>
  <rect x="52" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="68" y="63" text-anchor="middle" font-size="11">b</text>
  <rect x="84" y="45" width="32" height="32" rx="3" fill="#D4D8E0" stroke="#8B8680"/><text x="100" y="63" text-anchor="middle" font-size="11">c</text>
  <rect x="116" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="132" y="63" text-anchor="middle" font-size="11">d</text>
  <rect x="148" y="45" width="32" height="32" rx="3" fill="#E8E3D8" stroke="#B8B5B0"/><text x="164" y="63" text-anchor="middle" font-size="11">e</text>
  <rect x="52" y="38" width="64" height="42" rx="4" fill="none" stroke="#C4956A" stroke-width="2" stroke-dasharray="4"/>
  <text x="84" y="32" text-anchor="middle" font-size="10" fill="#C4956A" font-weight="600">window</text>
  <text x="110" y="105" text-anchor="middle" font-size="11" fill="#6B6560">expand right, shrink left when invalid</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Fixed-size window** *(this problem)* | O(n) | O(1) | Window size known upfront |
| Variable-size window | O(n) | O(1) | Expand/shrink until valid |
| Window + hash map | O(n) | O(k) | Track character/count frequencies |
| Deque window max | O(n) | O(k) | Monotonic deque for max/min in window |

## Solution

**Time Complexity:** O(1) per `next()` call  
**Space Complexity:** O(size) - Queue stores at most `size` elements

This solution uses a queue to maintain the sliding window and a running sum to calculate the average efficiently.

```cpp
class MovingAverage {
private:
    queue<int> q;
    int windowSize;
    long long windowSum;
public:
    MovingAverage(int size) {
        windowSize = size;
        windowSum = 0;        
    }
    
    double next(int val) {
        q.push(val);
        windowSum += val;
        if(q.size() > windowSize) {
            windowSum -= q.front();
            q.pop();
        }
        return (double) windowSum / q.size();
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
```

### Solution Explanation

**Approach:** Fixed-size window (this problem)

**Key idea:** 1. **Sliding window pattern**: Queue naturally maintains FIFO order

**How the code works:**
1. **Sliding window pattern**: Queue naturally maintains FIFO order
- Maintain a window `[left, right]` satisfying a constraint.
- Expand `right` to grow; shrink `left` when invalid.
- Fixed window: slide both pointers together.

| Operation | Time | Space |
|-----------|------|-------|
| Constructor | O(1) | O(1) |
| next() | O(1) | O(size) |
| **Overall** | **O(1) per call** | **O(size)** |

### How Solution 1 Works

1. **Initialization**: 
   - Store `windowSize` to know the maximum window size
   - Initialize `windowSum` to 0

2. **Adding new value**:
   - Push new value to queue
   - Add value to running sum

3. **Maintaining window size**:
   - If queue size exceeds `windowSize`, remove oldest element
   - Subtract removed element from running sum

4. **Calculate average**:
   - Return `windowSum / q.size()`
   - Note: `q.size()` may be less than `windowSize` initially

### Key Insight

- **Running sum**: Maintain sum of current window elements
- **Queue**: Automatically maintains FIFO order for sliding window
- **O(1) average calculation**: No need to sum all elements each time
## Example Walkthrough

**Input:** `size = 3`, calls: `next(1)`, `next(10)`, `next(3)`, `next(5)`

### Solution 1 (Queue):
```
Initial: q = [], windowSum = 0

next(1):
  q.push(1) → q = [1]
  windowSum = 0 + 1 = 1
  q.size() = 1
  return 1.0 / 1 = 1.0

next(10):
  q.push(10) → q = [1, 10]
  windowSum = 1 + 10 = 11
  q.size() = 2
  return 11.0 / 2 = 5.5

next(3):
  q.push(3) → q = [1, 10, 3]
  windowSum = 11 + 3 = 14
  q.size() = 3 (equals windowSize)
  return 14.0 / 3 = 4.66667

next(5):
  q.push(5) → q = [1, 10, 3, 5]
  windowSum = 14 + 5 = 19
  q.size() = 4 > windowSize
  Remove q.front() = 1
  windowSum = 19 - 1 = 18
  q.pop() → q = [10, 3, 5]
  return 18.0 / 3 = 6.0
```

### Complexity
| Operation | Time | Space |
|-----------|------|-------|
| Constructor | O(1) | O(1) |
| next() | O(1) | O(size) |
| **Overall** | **O(1) per call** | **O(size)** |

## Common Mistakes

1. **Window not full**: First few calls when `q.size() < windowSize`
2. **Single element window**: `size = 1`
3. **Large window size**: `size = 1000`
4. **Negative values**: `val = -10^5`
5. **Many calls**: Up to 10^4 calls

1. **Integer overflow**: Using `int` for `windowSum` instead of `long long`
2. **Division by zero**: Not handling case when queue is empty (shouldn't happen per constraints)
3. **Wrong average**: Using `windowSize` instead of `q.size()` when window not full
4. **Not removing old elements**: Forgetting to pop when window is full
5. **Type conversion**: Not casting to `double` before division

## Optimization Tips

1. **Use `long long`**: Prevents overflow when summing many values
2. **Queue vs Array**: Queue is simpler, array is faster for fixed-size windows
3. **Early return**: Can optimize for `size = 1` case separately

## Related Problems

- [239. Sliding Window Maximum](https://www.leetcode.com/problems/sliding-window-maximum/) - Find maximum in sliding window
- [480. Sliding Window Median](https://www.leetcode.com/problems/sliding-window-median/) - Find median in sliding window
- [643. Maximum Average Subarray I](https://www.leetcode.com/problems/maximum-average-subarray-i/) - Maximum average in fixed window
- [1423. Maximum Points You Can Obtain from Cards](https://www.leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) - Sliding window variant

## Pattern Recognition

This problem demonstrates the **"Sliding Window with Running Sum"** pattern:

```
1. Use queue/array to maintain window
2. Maintain running sum of window elements
3. Add new element, update sum
4. Remove old element when window exceeds size
5. Calculate result from running sum
```

Similar problems:
- Sliding Window Maximum
- Sliding Window Median
- Maximum Average Subarray
- Subarray Sum Equals K

## Real-World Applications

1. **Stock Price Analysis**: Calculate moving average of stock prices
2. **Network Monitoring**: Average network latency over time window
3. **Sensor Data**: Smooth sensor readings over time
4. **Performance Metrics**: Average response time in sliding window
5. **Signal Processing**: Moving average filter for noise reduction

{% endraw %}

## References

- [LC 346: Moving Average from Data Stream on LeetCode](https://www.leetcode.com/problems/moving-average-from-data-stream/)
- [LeetCode Discuss — LC 346: Moving Average from Data Stream](https://www.leetcode.com/problems/moving-average-from-data-stream/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/moving-average-from-data-stream/editorial/) *(may require premium)*

## Key Takeaways

1. **Sliding window pattern**: Queue naturally maintains FIFO order
2. **Running sum optimization**: Avoid recalculating sum each time
3. **Window size management**: Check size before removing elements
4. **Type safety**: Use `long long` to prevent overflow with large sums
