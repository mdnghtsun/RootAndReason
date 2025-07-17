---
title: "For vs While Loops in Python: The Iterator Trap Explained"
date: '2025-07-16T16:00:00-07:00'
draft: false
topics: ["Coding"]
tags: ["python", "loops", "coding", "iterators-vs-counters", "while-vs-for"]
description: "Why Python's for loops don't behave like C or Java and when to use while instead."
---

I had a technical interview today with a company I’ve been eager to join. The coding challenge was engaging, but I made one incorrect assumption about how Python’s `for` loop works because it behaves very differently from C. In this post, I’ll explain the misunderstanding, why it happened, and how I could have approached the problem correctly.

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
- Advance through elements using an API such as `next()` (or `__next__()` under the hood in Python’s `for` loops).
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

In contrast, **Python `for` loops** are iterator-based. Modifying `i` inside the loop has no effect because `i` gets its value from the iterator object created by the `for` statement. Any manual assignment to `i` is immediately overridden by the next value pulled from this iterator.
```python
# Python
for i in range(10):
    if i == 5:
        i = 0  # does nothing because i gets its value from the iterator created by range(10) (0, 1, 2, 3, ...)
```

Note: You can mimic a C-style `for` loop in Python using `itertools.count()`, but it’s considered unpythonic because the loop doesn’t have an implicit exit condition. Instead, you must break out manually with an `if` statement—much like a `while` loop.

```python
from itertools import count

for i in count(0):  # start counting from 0
    if i >= 10:  # stop condition
        break
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

list_a = [0, 4, 2, 4]
list_b = [4, 0, 4, 2]
list_c = [4, 4, 0, 2]
list_d = [0, 0, 4, 2]
list_e = [0, 4, 4, 4]
list_f = [0, 4, 4, 8]
list_g = [4, 4, 4, 8]
list_x = [0, 0, 0, 0, 4, 4, 7, 8, 0, 16]
list_y = [0, 4, 0, 4, 0, 8, 16, 8]
list_z = [0, 4, 0, 4, 0, 8, 16, 32]

shift_list_left(list_a)
shift_list_left(list_b)
shift_list_left(list_c)
shift_list_left(list_d)
shift_list_left(list_e)
shift_list_left(list_g)
shift_list_left(list_x)
shift_list_left(list_y)
shift_list_left(list_z)
```

Output
```
➜  Code  python3 2028.py
shifting:[0, 4, 2, 4]
before:[0, 4, 2, 4]
after:[4, 2, 4]
final:[4, 2, 4, 0]
done

shifting:[4, 0, 4, 2]
before:[4, 0, 4, 2]
after:[4, 4, 2]
before:[4, 4, 2]
after:[8, 2]
final:[8, 2, 0, 0]
done

shifting:[4, 4, 0, 2]
before:[4, 4, 0, 2]
after:[8, 0, 2]
before:[8, 0, 2]
after:[8, 2]
final:[8, 2, 0, 0]
done

shifting:[0, 0, 4, 2]
before:[0, 0, 4, 2]
after:[0, 4, 2]
before:[0, 4, 2]
after:[4, 2]
final:[4, 2, 0, 0]
done

shifting:[0, 4, 4, 4]
before:[0, 4, 4, 4]
after:[4, 4, 4]
before:[4, 4, 4]
after:[8, 4]
final:[8, 4, 0, 0]
done

not shifting: [4, 4, 4, 8]
no zeroes found to shift over

shifting:[0, 0, 0, 0, 4, 4, 7, 8, 0, 16]
before:[0, 0, 0, 0, 4, 4, 7, 8, 0, 16]
after:[0, 0, 0, 4, 4, 7, 8, 0, 16]
before:[0, 0, 0, 4, 4, 7, 8, 0, 16]
after:[0, 0, 4, 4, 7, 8, 0, 16]
before:[0, 0, 4, 4, 7, 8, 0, 16]
after:[0, 4, 4, 7, 8, 0, 16]
before:[0, 4, 4, 7, 8, 0, 16]
after:[4, 4, 7, 8, 0, 16]
before:[4, 4, 7, 8, 0, 16]
after:[8, 7, 8, 0, 16]
before:[8, 7, 8, 0, 16]
after:[8, 7, 8, 16]
final:[8, 7, 8, 16, 0, 0, 0, 0, 0, 0]
done

shifting:[0, 4, 0, 4, 0, 8, 16, 8]
before:[0, 4, 0, 4, 0, 8, 16, 8]
after:[4, 0, 4, 0, 8, 16, 8]
before:[4, 0, 4, 0, 8, 16, 8]
after:[4, 4, 0, 8, 16, 8]
before:[4, 4, 0, 8, 16, 8]
after:[8, 0, 8, 16, 8]
before:[8, 0, 8, 16, 8]
after:[8, 8, 16, 8]
before:[8, 8, 16, 8]
after:[16, 16, 8]
before:[16, 16, 8]
after:[32, 8]
final:[32, 8, 0, 0, 0, 0, 0, 0]
done

shifting:[0, 4, 0, 4, 0, 8, 16, 32]
before:[0, 4, 0, 4, 0, 8, 16, 32]
after:[4, 0, 4, 0, 8, 16, 32]
before:[4, 0, 4, 0, 8, 16, 32]
after:[4, 4, 0, 8, 16, 32]
before:[4, 4, 0, 8, 16, 32]
after:[8, 0, 8, 16, 32]
before:[8, 0, 8, 16, 32]
after:[8, 8, 16, 32]
before:[8, 8, 16, 32]
after:[16, 16, 32]
before:[16, 16, 32]
after:[32, 32]
before:[32, 32]
after:[64]
final:[64, 0, 0, 0, 0, 0, 0, 0]
done
```

## TL;DR/Conclusion
- Counters are simple variables you manage; iterators are tied to sequences and yield elements one at a time.
- I assumed Python’s `for` loop was **counter-driven** like in C, where changing `i` inside the loop would affect iteration.
- In reality, Python’s `for` loop is **iterator-driven**: any reassignment to `i` is ignored because the next value comes from the iterator.
- **C:** `for` loops → counter-based  
- **Python:** `for` loops → iterator-based  
- **Rule of thumb:**  
  - Use `for` for straightforward iteration over a sequence.  
  - Use `while` with a manual counter when you need more control (resetting, skipping, restarting).  

