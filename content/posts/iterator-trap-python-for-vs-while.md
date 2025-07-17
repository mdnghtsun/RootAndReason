---
title: "For vs While Loops in Python: The Iterator Trap Explained"
date: '2025-07-16T16:00:00-07:00'
draft: false
tags: ["python", "loops", "coding", "iterator", "while-vs-for"]
description: "Why Python's for loops don't behave like C or Java and when to use while instead."
---

---

## 0. Problem

I tried to implement a **counter-driven** loop in Python, similar to how you'd do it in C or Java. My goal was to modify the loop variable inside the loop body to reset the index when a certain condition was met.

Here’s what I initially wrote:

```python
for i in range(len(integer_list)):
    if integer_list[i] == 0:
        integer_list = integer_list[:i] + integer_list[i+1:]
        i = 0  # I thought this would reset the loop
        ...
```

I expected that setting i = 0 would restart the iteration. Instead, it had no effect—the loop ignored my assignment completely. Why?

## 1. Explanation 

The core issue is that `range(len(integer_list))` creates a **range object**, which is an **iterator** that generates a sequence of values `(0, 1, 2, … len(list)`. On each iteration, Python assigns the next value from this iterator to `i`.

This means:
- Any assignment to `i` inside the loop is immediately overwritten by the next value from the iterator.
- Changing `i` in the middle of the loop has no effect.

While debugging, I realized the value I was assigning to `i` never persisted. The iterator controlled by `range()` always overrode it on the next iteration. This behavior is by design—Python’s `for` loops are **iterator-driven**, not **counter-driven**.


### Iterators vs Counters
Coming from C background, I used to treat iterators and counters as the same thing. But in Python, they’re very different.

#### **Iterators**
- Abstractions that represent a position within a sequence.
- Provide movement through an API (like `next()` or `__next__()`).
- In Python, all `for` loops are iterator-driven by design.
- In C, traditional `for` loops are counter-based unless you explicitly use iterators (via pointers for example)

#### **Counters**
- Simple integers you manage manually.
- Can be reset, incremented, or decremented as needed.
- Logic is explicit and under your direct control.

### While vs For Loops In Python

**C `for` loops** are counter-based, so changing `i` works as expected because it’s simply a variable under your control managed by the loop

```c
// C
for (int i = 0; i < 10; i++) {
    if (i == 5) {
        i = 0;  // resets at the end of the current iteration
    }
}
```

In contrast, **Python `for` loops** are iterator-based. Modifying `i` inside the loop has no effect because `i` gets its value from the iterator object created by the `for` statement.
```python
# Python
for i in range(10):
    if i == 5:
        i = 0  # does nothing because i gets its value from the iterator created by range(10) (0, 1, 2, 3, ...)
```

Note: It is possible to mimic a C-style `for` loop in Python though its rather unpythonic:

```python
from itertools import count

for i in count(0):  # start counting from 0
    if i >= 10:  # stop condition
        break
    print(i)
```


## 2. Solution

To gain full control, I switched from a `for` loop to a `while` loop. A `while` loop allows explicit management of the counter, which is exactly what I needed for operations like resetting or adjusting `i`.

While it’s possible to mimic a counter-based `for` loop in Python using `itertools.count()`, this approach is considered unpythonic because:
- It requires importing an extra module.
- The loop’s exit condition must be set explicitly with an `if` statement, rather than being built into the loop header.

### An Unpythonic Way To Implement A C-like For Loop
```python
from itertools import count

def shift_list_left(integer_list):
    for i in count(0):  # start counting from 0
        if i >= len(integer_list):
            break  # stop when we've checked everything
        if integer_list[i] == 0:
            print("Removing zero at index:" + str(i))
            integer_list.pop(i)  # modify list in place
            i -= 1  # has no real effect because the iterator controls i
        ...
```

### Full Code Using A While Loop (And The Pythonic way)
```python
def shift_list_left(integer_list):
    index = 0
    DEBUG = True

    # base case
    if 0 not in integer_list:
        print("not shifting: " + str(integer_list))
        print("no zeroes found to shift over") if DEBUG else None
        return integer_list
    else: 
        print("shifting:" + str(integer_list)) if DEBUG else None


    # 0s present -> work to do
    while index < len(integer_list):
        # 0 found
        if integer_list[index] == 0:
            print("before:" + str(integer_list)) if DEBUG else None
            integer_list.pop(index)
            index-=1
            print("after:" + str(integer_list)) if DEBUG else None
        # double integer found
        elif index!= 0 and integer_list[index-1] == integer_list[index]:
            print("before:" + str(integer_list)) if DEBUG else None
            integer_list[index-1] = integer_list[index-1] + integer_list[index]
            integer_list.pop(index)
            index-=1
            print("after:" + str(integer_list)) if DEBUG else None

        index+=1
    
    # pad 0s to fill list of length 4 to be returned
    integer_list += [0] * (4 - len(integer_list))
    print("final:" + str(integer_list)) if DEBUG else None
    print("done\n") if DEBUG else None

    return integer_list
```

## TL;DR/Conclusion
- Counters are simple numbers you manage; iterators are tied to sequences and yield elements one at a time.
- I assumed Python’s `for` loop was **counter-driven** like in C, where changing `i` inside the loop would affect iteration.
- In reality, Python’s `for` loop is **iterator-driven**: any reassignment to `i` is ignored because the next value comes from the iterator.
- **C:** `for` loops → counter-based  
- **Python:** `for` loops → iterator-based  
- **Rule of thumb:**  
  - Use `for` for straightforward iteration over a sequence.  
  - Use `while` with a manual counter when you need more control (resetting, skipping, restarting).  

