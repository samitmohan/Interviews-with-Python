> python lang specific questions, dsa implementation, along with neetcode150 and striver sheet solutions while preparing for interviews.

**Data Structures and Algorithms** for technical interviews!

---

## 📁 Directory Structure

```bash
.
.
├── CompanyQuestions/           → Company-specific DSA questions (Amazon, Google, etc.)
│   ├── Epifi/
│   ├── Data Insights/
│
├── DSAPython/                  → Core DSA algorithm implementations in Python
│   ├── Algorithms/
│   ├── Graphs/
│   ├── HashTables/
│   ├── Heap/
│   ├── LinkedLists/
│   ├── SearchingSorting/
│   ├── StackQueue/
│   ├── Trees/
│   ├── Trie/
│
├── Neetcode150/                → Solutions and patterns from the Neetcode 150 list
│   ├── Arrays & Hashing/
│   ├── AdvancedGraphs
│   ├── Backtracking
│   ├── Binary Search/
│   ├── BitManipulation
│   ├── DP
│   ├── Graphs
│   ├── Greedy
│   ├── Heap
│   ├── Intervals
│   ├── LinkedList
│   ├── Math
│   ├── Sliding Window/
│   ├── Trees/
│   ├── Tries/
│   └── Two Pointers
│
├── OS/                         → Operating System fundamentals and notes
│   ├── deadlocks
│   ├── scheduler
│   ├── synchronisation
│   └── system calls
│
├── Problems/                   → Solved problems, often LeetCode/InterviewBit style
│   ├── Array/
│   ├── DesignDSA/
│   ├── DP/
│   └── Graphs/
│   └── Hashing/
│   └── Heaps/
│   └── LinkedList/
│   └── Math/
│   └── Queues/
│   └── Recursion/
│   └── Searching & Sorting/
│   └── Sliding/
│   └── Stack/
│   └── Trees/
│   └── UnionFind/

│── PythonLanguageSpecific/     → Python tricks, language-specific interview Qs
│   ├── PythonTips.md
│   ├── InterviewQuestions.pdf
│
├── StriverSheet/               → Striver’s DSA Sheet solutions & notes
│   ├── Arrays/
│   ├── Backtracking/
│   ├── BinarySearch/
│   ├── BinaryTree/
│   └── DP/
│   └── Graph/
│   └── Greedy/
│   └── Heaps/
│   ├── LinkedLists/
│   ├── Recursion/
│   ├── SQ/
│   ├── String/
│   ├── Trees/
│   ├── Trie/
│
├── Time Complexity                   → CheatSheet
├── README.md                   → Entry point to the repository with all documentation
│

```

---

## 📄 `cheatsheets/time_complexity.md`

```markdown
# ⏱️ Time & Space Complexity Cheatsheet

## Common Complexities

| Complexity | Description   | Examples                          |
| ---------- | ------------- | --------------------------------- |
| O(1)       | Constant time | Hash table lookup                 |
| O(log n)   | Logarithmic   | Binary search                     |
| O(n)       | Linear        | Single for-loop over array        |
| O(n log n) | Linearithmic  | Merge sort, quicksort (avg)       |
| O(n²)      | Quadratic     | Nested loops, Bubble sort         |
| O(2^n)     | Exponential   | Recursive Fibonacci               |
| O(n!)      | Factorial     | Travelling salesman, permutations |

---

## Time Complexities of Common Operations

### Arrays

- Access: `O(1)`
- Search: `O(n)`
- Insert/Delete (end): `O(1)`
- Insert/Delete (start or middle): `O(n)`

### Hash Tables (Dict)

- Insert: `O(1)`
- Search: `O(1)` average
- Delete: `O(1)`

### Linked Lists

- Access: `O(n)`
- Insert/Delete (head): `O(1)`
- Search: `O(n)`

### Binary Search Tree (Balanced)

- Insert/Search/Delete: `O(log n)`

### Heaps

- Insert/Delete: `O(log n)`
- Peek Max/Min: `O(1)`

### Graph Traversal

- BFS/DFS: `O(V + E)` (vertices + edges)

---

## Space Complexity Tips

- Extra arrays = +O(n)
- Recursion depth = +O(stack depth)
- Hash sets/maps = O(n) for `n` elements stored
```
