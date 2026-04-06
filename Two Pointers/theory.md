# Two Pointers Technique

## 🔹 What is Two Pointers?

Two Pointers is a technique where we use **two indices (pointers)** to traverse a data structure (mostly arrays or linked lists).

---

## 🔹 Where to Use?

- Arrays
- Linked Lists
- Mostly on **sorted data**

---

## 🔹 Common Problems

- Pair Sum (2 Sum in sorted array)
- Triplets / Quadruplets (3Sum, 4Sum)
- Remove Duplicates
- Merge Sorted Arrays
- Sorted / Sort
- Detech Cycle in Linkedlist
- Reverse Array / String

---

## 🔹 Types of Two Pointer Approach

### 1. Opposite Direction (Left & Right)

- One pointer at start (`left = 0`)
- One pointer at end (`right = n-1`)
- Move based on condition

#### Example: Pair Sum

```python
left = 0
right = n - 1

while left < right:
    if arr[left] + arr[right] == target:
        print("Found")
        break
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1