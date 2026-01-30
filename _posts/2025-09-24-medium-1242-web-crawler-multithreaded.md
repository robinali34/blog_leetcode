---
layout: post
title: "[Medium] 1242. Web Crawler Multithreaded"
date: 2025-09-24 18:00:00 -0000
categories: leetcode algorithm multithreading concurrency data-structures synchronization medium cpp web-crawler concurrent-programming problem-solving
---

# [Medium] 1242. Web Crawler Multithreaded

This is a multithreading problem that requires implementing a concurrent web crawler. The key insight is using proper synchronization mechanisms to avoid race conditions while crawling URLs from the same domain concurrently.

## Problem Description

Given a start URL and an HTML parser, implement a multithreaded web crawler that:
1. Crawls all URLs from the same domain as the start URL
2. Uses multiple threads for concurrent crawling
3. Avoids visiting the same URL multiple times
4. Returns all discovered URLs

### Examples

**Example 1:**
```
Input: 
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
startUrl = "http://news.yahoo.com/news/topics/"
Output: [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/"
]
```

**Example 2:**
```
Input:
urls = [
  "http://news.yahoo.com",
  "http://news.yahoo.com/news",
  "http://news.yahoo.com/news/topics/",
  "http://news.google.com"
]
startUrl = "http://news.google.com"
Output: ["http://news.google.com"]
```

### Constraints
- 1 <= urls.length <= 1000
- 1 <= urls[i].length <= 300
- startUrl is one of the urls
- All URLs have the same hostname

## Clarification Questions

Before diving into the solution, here are 5 important clarifications and assumptions to discuss during an interview:

1. **Crawling scope**: What URLs should we crawl? (Assumption: Only URLs with the same hostname as startUrl - per constraints, all URLs have same hostname)

2. **Thread safety**: Do we need thread-safe operations? (Assumption: Yes - multithreaded environment, need synchronization for shared state)

3. **URL format**: What constitutes a valid URL? (Assumption: Standard URL format, startUrl is guaranteed to be in urls list)

4. **Duplicate handling**: How should we handle duplicate URLs? (Assumption: Each URL should be crawled only once - need to track visited URLs)

5. **Return format**: What should we return? (Assumption: List of all URLs that can be reached from startUrl with same hostname)

## Interview Deduction Process (20 minutes)

### Step 1: Brute-Force Approach (5 minutes)
**Initial Thought**: "I need to crawl web pages. Let me start from startUrl and follow links sequentially."

**Naive Solution**: Start from startUrl, fetch HTML, extract URLs, filter by hostname, recursively crawl each URL sequentially.

**Complexity**: O(n) time where n is number of URLs, O(n) space

**Issues**:
- Sequential crawling is slow
- Doesn't leverage multithreading
- Not optimal for concurrent operations
- Can be optimized

### Step 2: Semi-Optimized Approach (7 minutes)
**Insight**: "I can use BFS/DFS with thread pool to crawl URLs concurrently."

**Improved Solution**: Use BFS/DFS with thread pool. Maintain queue of URLs to crawl. Use multiple threads to fetch URLs concurrently. Track visited URLs to avoid duplicates.

**Complexity**: O(n) time with better concurrency, O(n) space

**Improvements**:
- Concurrent crawling is faster
- Thread pool manages threads efficiently
- Handles visited URLs correctly
- Better utilizes resources

### Step 3: Optimized Solution (8 minutes)
**Final Optimization**: "BFS with thread pool and proper synchronization is optimal."

**Best Solution**: BFS with thread pool. Use queue for URLs to crawl, visited set for tracking. Use thread pool to fetch URLs concurrently. Synchronize access to shared data structures.

**Complexity**: O(n) time with concurrency, O(n) space

**Key Realizations**:
1. BFS is natural for web crawling
2. Thread pool enables concurrent fetching
3. Synchronization is crucial for thread safety
4. Visited tracking prevents infinite loops

## Approach

The solution involves:

1. **Domain Extraction**: Extract the base domain from the start URL
2. **Thread Pool**: Use multiple threads for concurrent crawling
3. **Synchronization**: Use locks to prevent race conditions
4. **URL Filtering**: Only crawl URLs from the same domain
5. **Visited Tracking**: Avoid revisiting the same URL

## Solution in C++

**Time Complexity:** O(n) where n is the number of URLs in the same domain  
**Space Complexity:** O(n) for storing visited URLs and results

```cpp
/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */
class Solution {
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        StUrl = getStartUrl(startUrl);
        q.push(startUrl);
        auto eUrl = [&]() {
            while(true) {
                mtxq.lock();
                if(!q.size()) {
                    mtxq.unlock();
                    this_thread::sleep_for(chrono::milliseconds(20));
                    mtxq.lock();
                    if(!q.size()) {mtxq.unlock(); return;}
                }
                string t=q.front();
                q.pop();
                if(getStartUrl(t)!=StUrl) {mtxq.unlock(); continue;}
                mtxm.lock();
                if(m.count(t)) {mtxm.unlock();mtxq.unlock(); continue;}
                m[t] = true;
                mtxa.lock();
                rtn.emplace_back(t);
                mtxa.unlock();
                mtxm.unlock();
                mtxq.unlock();
                vector<string> vec(htmlParser.getUrls(t));
                mtxq.lock();
                for(auto& s:vec) {q.push(s);}
                mtxq.unlock();
            }
            return;
        };
        while(n--) pool.emplace_back(thread(eUrl));
        for(auto& t:pool) t.join();
        return rtn;
    }
private:
    vector<string> rtn;
    unordered_map<string, bool> m;
    mutex mtxq, mtxm, mtxa;
    string StUrl;
    int n = thread::hardware_concurrency();
    vector<thread> pool;
    queue<string> q;

    string getStartUrl(string& s){
        int t = 3;
        string rtn="";
        for (char& c: s){
            if(c== '/') t--;
            if(!t) return rtn;
            rtn.push_back(c);
        }
        return rtn;
    }
};
```

## Solution in Python

**Time Complexity:** O(n) where n is the number of URLs in the same domain  
**Space Complexity:** O(n) for storing visited URLs and results

```python
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def host(u: str) -> str:
            return u.split('/')[2]
        
        base = host(startUrl)
        visited = set([startUrl])
        lock = Lock()

        def worker(url: str) -> List[str]:
            next_urls = []
            for u in htmlParser.getUrls(url):
                if host(u) == base:
                    with lock:
                        if u in visited:
                            continue
                        visited.add(u)
                    next_urls.append(u)
            return next_urls
        
        with ThreadPoolExecutor(max_workers=32) as ex:
            pending = {ex.submit(worker, startUrl)}
            while pending:
                done, pending = wait(pending, return_when=FIRST_COMPLETED)
                for fut in done:
                    for nxt in fut.result():
                        pending.add(ex.submit(worker, nxt))
        
        return list(visited)
```

## Step-by-Step Example

Let's trace through the Python solution with startUrl = "http://news.yahoo.com/news/topics/":

**Step 1:** Extract base domain
- `host("http://news.yahoo.com/news/topics/")` → "news.yahoo.com"
- `visited = {"http://news.yahoo.com/news/topics/"}`

**Step 2:** Start worker thread
- Submit initial URL to thread pool
- Worker calls `htmlParser.getUrls()` on startUrl

**Step 3:** Process discovered URLs
- For each URL from parser:
  - Check if host matches base domain
  - If yes, add to visited set (with lock)
  - Add to next_urls for further processing

**Step 4:** Continue until no more URLs
- Submit new URLs to thread pool
- Wait for completion and process results
- Repeat until all URLs are processed

## Key Insights

1. **Thread Safety**: Use locks to protect shared data structures
2. **Domain Filtering**: Only process URLs from the same domain
3. **Concurrent Processing**: Use thread pools for parallel execution
4. **Deadlock Prevention**: Careful lock ordering and timeout handling
5. **Memory Management**: Proper cleanup of thread resources

## Synchronization Patterns

### C++ Approach:
- **Multiple Mutexes**: Separate locks for queue, map, and results
- **Manual Thread Management**: Create and join threads manually
- **Polling**: Sleep and check for work periodically

### Python Approach:
- **Single Lock**: One lock for the visited set
- **ThreadPoolExecutor**: Automatic thread management
- **Future-based**: Use futures for asynchronous execution

## Common Mistakes

- **Race Conditions**: Not properly synchronizing access to shared data
- **Deadlocks**: Incorrect lock ordering or holding multiple locks
- **Memory Leaks**: Not properly cleaning up thread resources
- **Infinite Loops**: Not handling empty queue conditions correctly
- **Domain Mismatch**: Processing URLs from different domains

---
