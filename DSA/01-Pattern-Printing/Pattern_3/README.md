# Pattern 3

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 3](https://takeuforward.org/practice/dsa/pattern-3)

### Hint
Use nested loops to print numbers in increasing order. The outer loop controls the rows, and the inner loop prints numbers from 1 to the current row number.

### My Approach
- Used an outer loop to iterate through each row from `1` to `n`.
- Used an inner loop to print numbers from `1` to `i`.
- After printing each row, used `print()` to move to the next line.
- Each row contains numbers equal to its row number.

### Key Insight
The number of elements in each row is equal to the current row number. Therefore, we print numbers from `1` to `i` in every row.

### Complexity
- **Time Complexity:** O(n²) – Nested loops execute a total of n(n+1)/2 iterations.
- **Space Complexity:** O(1) – No extra data structures are used.

### Edge Cases
- **n = 0:** No pattern is printed.
- **n = 1:** Prints a single row containing `1`.
- **n > 1:** Prints the complete number pattern with `n` rows.

## My Experience

**Note:** Not that much hard as first, but also I forgot how to write code in optimum solution and also as much as less lines like sometimes single line code instead of bunch of lines. date 31-10-2026.