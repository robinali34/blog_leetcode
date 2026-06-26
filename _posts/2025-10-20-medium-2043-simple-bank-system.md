---
layout: post
title: "[Medium] 2043. Simple Bank System"
date: 2025-10-20 13:50:00 -0700
categories: leetcode algorithm medium design data-structure
permalink: /2025/10/20/medium-2043-simple-bank-system/
---
**Difficulty:** Medium  
**Category:** Design, Data Structure

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has `n` accounts numbered from `1` to `n`. The initial balance of each account is stored in a **0-indexed** integer array `balance`, with the `(i + 1)th` account having an initial balance of `balance[i]`.

Execute all the **valid** transactions. A transaction is **valid** if:

- The given account number(s) are between `1` and `n`, and
- The amount of money withdrawn or transferred from is less than or equal to the balance of the account.

Implement the `Bank` class:

- `Bank(long[] balance)` Initializes the object with the 0-indexed integer array `balance`.
- `boolean transfer(int account1, int account2, long money)` Transfers `money` dollars from the account numbered `account1` to the account numbered `account2`. Returns `true` if the transaction was successful, `false` otherwise.
- `boolean deposit(int account, long money)` Deposits `money` dollars to the account numbered `account`. Returns `true` if the transaction was successful, `false` otherwise.
- `boolean withdraw(int account, long money)` Withdraws `money` dollars from the account numbered `account`. Returns `true` if the transaction was successful, `false` otherwise.

## Examples

### Example 1:
```
Input
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]

Output
[null, true, true, true, false, false]

Explanation
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has a balance of 20, so it is valid to withdraw 10.
                         // Account 3 has 20 - 10 = 10 after the transaction.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of 30, so it is valid to transfer 20.
                         // Account 5 has 30 - 20 = 10 after the transaction.
                         // Account 1 has 10 + 20 = 30 after the transaction.
bank.deposit(5, 20);     // return true, it is valid to deposit 20 to account 5.
                         // Account 5 has 10 + 20 = 30 after the transaction.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is 10,
                         // so it is invalid to transfer 15 from it.
bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.
```

## Constraints

- `n == balance.length`
- `1 <= n, account, account1, account2 <= 10^5`
- `0 <= balance[i] <= 10^12`
- `1 <= money <= 10^12`
- At most `10^4` calls will be made to each function `transfer`, `deposit`, and `withdraw`.

## Thinking Process

This is a **Data Structure Design** problem that simulates a simple bank system. The key requirements are:

1. **Account Validation:** Ensure account numbers are valid (1 to n)
2. **Balance Checking:** Ensure sufficient funds for withdrawals and transfers
3. **Atomic Operations:** Each transaction should be atomic (all-or-nothing)
4. **Efficient Operations:** All operations should be O(1) time complexity

### Algorithm:
1. **Store balances** in a vector/array for O(1) access
2. **Validate accounts** before any operation
3. **Check sufficient funds** before withdrawals and transfers
4. **Perform operations** atomically (check first, then modify)
5. **Return success/failure** based on validation results

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 115" style="max-width:100%;height:auto;display:block;margin:1.5em auto;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif">
<text x="50%" y="18" text-anchor="middle" font-size="13" font-weight="600" fill="#5A5752">Design pattern</text>

  <rect x="40" y="45" width="70" height="36" rx="4" fill="#D4D8E0" stroke="#8B8680"/><text x="75" y="67" text-anchor="middle" font-size="10">API</text>
  <rect x="150" y="45" width="90" height="36" rx="4" fill="#E0D8E4" stroke="#A098A8"/><text x="195" y="67" text-anchor="middle" font-size="10">hash + list</text>
  <path d="M110 63h36" stroke="#8B8680" stroke-width="2" marker-end="url(#arr2)"/>
  <defs><marker id="arr2" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="#8B8680"/></marker></defs>
  <text x="140" y="105" text-anchor="middle" font-size="11" fill="#6B6560">compose data structures for operations</text>

</svg>

## Common Approaches

Typical techniques for this pattern:

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| **Hash map + list** *(this problem)* | O(1) avg | O(n) | LRU cache pattern |
| Heap + hash map | O(\log n) | O(n) | LFU, time-based store |
| Trie (prefix tree) | O(m) | O(nm) | Word search, autocomplete |
| Deque / circular buffer | O(1) | O(n) | Queue with fixed capacity |

## Solution

```cpp
class Bank {
private:
    vector<long long> balance;
    bool isValid(int account) {
        return account >= 1 && account <= balance.size();
    }
public:
    Bank(vector<long long>& balance) {
        this->balance = balance;
    }
    
    bool transfer(int account1, int account2, long long money) {
        if(isValid(account1) && isValid(account2) && balance[account1 - 1] >= money) {
            balance[account1 - 1] -= money;
            balance[account2 - 1] += money;
            return true;
        }
        return false;
    }
    
    bool deposit(int account, long long money) {
        if(isValid(account)) {
            balance[account - 1] += money;
            return true;
        }
        return false;
    }
    
    bool withdraw(int account, long long money) {
        if(isValid(account) && balance[account - 1] >= money) {
            balance[account - 1] -= money;
            return true;
        }
        return false;
    }
};

/**
 * Your Bank object will be instantiated and called as such:
 * Bank* obj = new Bank(balance);
 * bool param_1 = obj->transfer(account1,account2,money);
 * bool param_2 = obj->deposit(account,money);
 * bool param_3 = obj->withdraw(account,money);
 */
```

### Solution Explanation

**Approach:** Hash map + list (this problem)

**Key idea:** This is a **Data Structure Design** problem that simulates a simple bank system. The key requirements are:

**How the code works:**
1. **Account Validation:** Ensure account numbers are valid (1 to n)
2. **Balance Checking:** Ensure sufficient funds for withdrawals and transfers
3. **Atomic Operations:** Each transaction should be atomic (all-or-nothing)
4. **Efficient Operations:** All operations should be O(1) time complexity
1. **Store balances** in a vector/array for O(1) access
2. **Validate accounts** before any operation

**Time Complexity:** O(1) for all operations
- **Constructor:** O(n) where n is number of accounts
- **transfer():** O(1) - constant time validation and operations
- **deposit():** O(1) - constant time validation and operations
- **withdraw():** O(1) - constant time validation and operations

**Space Complexity:** O(n) where n is the number of accounts
- **Storage:** Vector to store account balances
- **Auxiliary:** O(1) for validation and operations
## Explanation

### Class Design:

**Private Members:**
- `vector<long long> balance`: Stores account balances (0-indexed)
- `bool isValid(int account)`: Helper function to validate account numbers

**Public Methods:**
1. **Constructor:** Initialize with given balance array
2. **transfer():** Move money between accounts
3. **deposit():** Add money to an account
4. **withdraw():** Remove money from an account

### Step-by-Step Process:

**Transfer Operation:**
1. **Validate both accounts** exist (1 to n)
2. **Check sufficient funds** in source account
3. **Perform atomic transfer** (subtract from source, add to destination)
4. **Return success/failure**

**Deposit Operation:**
1. **Validate account** exists
2. **Add money** to account balance
3. **Return success/failure**

**Withdraw Operation:**
1. **Validate account** exists
2. **Check sufficient funds** available
3. **Subtract money** from account balance
4. **Return success/failure**

### Example Walkthrough:
For `balance = [10, 100, 20, 50, 30]` (5 accounts):

- **withdraw(3, 10):** Account 3 has 20, withdraw 10 → Success, balance = 10
- **transfer(5, 1, 20):** Account 5 has 30, transfer 20 to account 1 → Success
- **deposit(5, 20):** Add 20 to account 5 → Success, balance = 30
- **transfer(3, 4, 15):** Account 3 has 10, insufficient for 15 → Failure
- **withdraw(10, 50):** Account 10 doesn't exist → Failure

### Complexity
**Time Complexity:** O(1) for all operations
- **Constructor:** O(n) where n is number of accounts
- **transfer():** O(1) - constant time validation and operations
- **deposit():** O(1) - constant time validation and operations
- **withdraw():** O(1) - constant time validation and operations

**Space Complexity:** O(n) where n is the number of accounts
- **Storage:** Vector to store account balances
- **Auxiliary:** O(1) for validation and operations

## Design Patterns

### Data Structure Design:
- **Encapsulation:** Private data members with public interface
- **Validation:** Centralized validation logic
- **Atomic Operations:** All-or-nothing transaction semantics

### Error Handling:
- **Graceful Degradation:** Return false instead of crashing
- **Input Validation:** Check all preconditions before operations
- **Consistent Interface:** All methods return boolean success status

## References

- [LC 2043: Simple Bank System on LeetCode](https://www.leetcode.com/problems/simple-bank-system/)
- [LeetCode Discuss — LC 2043: Simple Bank System](https://www.leetcode.com/problems/simple-bank-system/discuss/)
- [LeetCode Editorial](https://www.leetcode.com/problems/simple-bank-system/editorial/) *(may require premium)*

## Common Mistakes

- Skipping edge cases (empty input, single element, boundaries).
- Off-by-one errors in loops and index ranges.
- Forgetting to handle the case when no valid answer exists.

## Key Takeaways

1. **Account Indexing:** Accounts are 1-indexed but stored in 0-indexed array
2. **Validation First:** Always validate accounts before performing operations
3. **Atomic Operations:** Check conditions before modifying balances
4. **Efficient Design:** O(1) operations for all transactions
5. **Error Handling:** Return false for invalid operations instead of throwing exceptions
