---
layout: post
title: "[Easy] 346. Moving Average from Data Stream"
date: 2025-12-14 00:00:00 -0800
categories: leetcode algorithm easy cpp queue sliding-window design problem-solving
---

{% raw %}
# [Easy] 346. Moving Average from Data Stream

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

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Moving average definition**: What is a moving average? (Assumption: Average of the last size elements - sliding window average)

2. **Window size**: What is the window size? (Assumption: Fixed size specified in constructor - only consider last size elements)

3. **New values**: What happens when we add a new value? (Assumption: Oldest value is removed if window is full, new value is added)

4. **Return value**: What should next() return? (Assumption: Double - average of current window of size elements)

5. **Initial window**: What if we have fewer than size elements? (Assumption: Average all available elements until window is full)

## Interview Deduction Process (10 minutes)

**Step 1: Brute-Force Approach (2 minutes)**

Maintain an array or list of all values. For each next() call, calculate the sum of the last size elements and divide by the count. This requires O(size) time per call to sum the elements, which is acceptable for small sizes but not optimal. The space complexity is O(n) where n is the total number of calls, which grows unbounded.

**Step 2: Semi-Optimized Approach (3 minutes)**

Use a fixed-size circular array to maintain only the last size elements. When adding a new value, overwrite the oldest value using modulo arithmetic. For each next() call, sum all elements in the array and divide. This reduces space to O(size) but still requires O(size) time per call to calculate the sum, which can be optimized further.

**Step 3: Optimized Solution (5 minutes)**

Use a queue to maintain the sliding window and a running sum variable. When adding a new value, add it to the queue and the sum. If the queue size exceeds the window size, remove the oldest element from both the queue and subtract it from the sum. The average is simply sum / queue.size(). This achieves O(1) time per operation: adding/removing from queue is O(1), updating sum is O(1), and calculating average is O(1). The space complexity is O(size) for the queue, which is optimal.

## Solution 1: Queue with Running Sum (Recommended)

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

## Solution 2: Circular Array

**Time Complexity:** O(1) per `next()` call  
**Space Complexity:** O(size)

Use a circular array to store window elements, avoiding queue overhead.

```cpp
class MovingAverage {
private:
    vector<int> window;
    int windowSize;
    int count;
    int head;
    long long windowSum;
public:
    MovingAverage(int size) {
        windowSize = size;
        window.resize(size);
        count = 0;
        head = 0;
        windowSum = 0;
    }
    
    double next(int val) {
        if(count < windowSize) {
            window[count] = val;
            windowSum += val;
            count++;
        } else {
            windowSum -= window[head];
            window[head] = val;
            windowSum += val;
            head = (head + 1) % windowSize;
        }
        return (double) windowSum / count;
    }
};
```

### How Solution 2 Works

1. **Circular buffer**: Use array with modulo indexing
2. **Track position**: `head` points to oldest element
3. **Count tracking**: `count` tracks number of elements (up to `windowSize`)
4. **Update sum**: Subtract old value, add new value

### Advantages

- **No dynamic allocation**: Fixed-size array
- **Cache-friendly**: Array access is faster than queue
- **Memory efficient**: No extra pointers per element

## Solution 3: Deque (Alternative)

**Time Complexity:** O(1) per `next()` call  
**Space Complexity:** O(size)

Similar to Solution 1 but using deque for potential future extensions.

```cpp
class MovingAverage {
private:
    deque<int> dq;
    int windowSize;
    long long windowSum;
public:
    MovingAverage(int size) {
        windowSize = size;
        windowSum = 0;
    }
    
    double next(int val) {
        dq.push_back(val);
        windowSum += val;
        if(dq.size() > windowSize) {
            windowSum -= dq.front();
            dq.pop_front();
        }
        return (double) windowSum / dq.size();
    }
};
```

## Comparison of Approaches

| Aspect | Queue | Circular Array | Deque |
|--------|-------|----------------|-------|
| **Time Complexity** | O(1) | O(1) | O(1) |
| **Space Complexity** | O(size) | O(size) | O(size) |
| **Code Simplicity** | Excellent | Good | Excellent |
| **Memory Overhead** | Higher | Lower | Higher |
| **Cache Performance** | Good | Excellent | Good |
| **Flexibility** | High | Low | High |

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

## Complexity Analysis

| Operation | Time | Space |
|-----------|------|-------|
| Constructor | O(1) | O(1) |
| next() | O(1) | O(size) |
| **Overall** | **O(1) per call** | **O(size)** |

## Edge Cases

1. **Window not full**: First few calls when `q.size() < windowSize`
2. **Single element window**: `size = 1`
3. **Large window size**: `size = 1000`
4. **Negative values**: `val = -10^5`
5. **Many calls**: Up to 10^4 calls

## Common Mistakes

1. **Integer overflow**: Using `int` for `windowSum` instead of `long long`
2. **Division by zero**: Not handling case when queue is empty (shouldn't happen per constraints)
3. **Wrong average**: Using `windowSize` instead of `q.size()` when window not full
4. **Not removing old elements**: Forgetting to pop when window is full
5. **Type conversion**: Not casting to `double` before division

## Key Insights

1. **Sliding window pattern**: Queue naturally maintains FIFO order
2. **Running sum optimization**: Avoid recalculating sum each time
3. **Window size management**: Check size before removing elements
4. **Type safety**: Use `long long` to prevent overflow with large sums

## Optimization Tips

1. **Use `long long`**: Prevents overflow when summing many values
2. **Queue vs Array**: Queue is simpler, array is faster for fixed-size windows
3. **Early return**: Can optimize for `size = 1` case separately

## Related Problems

- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) - Find maximum in sliding window
- [480. Sliding Window Median](https://leetcode.com/problems/sliding-window-median/) - Find median in sliding window
- [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) - Maximum average in fixed window
- [1423. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/) - Sliding window variant

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

