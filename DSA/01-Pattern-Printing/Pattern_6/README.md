# Pattern 6

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 6](https://takeuforward.org/practice/dsa/pattern-6)

### Hint
- Use nested loops to print the pattern.
- The outer loop controls the rows from `n` down to `1`.
- The inner loop prints numbers from `1` to the current row value.
- The number of printed values decreases as the row number decreases.

### My Approach
1. The outer loop iterates from `n` to `1`, representing the rows from the top to the bottom.
2. The inner loop iterates from `1` to `i`, printing each number without moving to a new line.
3. After finishing a row, `print()` moves the cursor to the next line.

### Key Insight
The current row number (`i`) determines both:
- **How many numbers to print:** `i`
- **The value range for each row:** `1` through `i`

### Complexity
- **Time:** O(n²) – The inner loop executes a total of 1 + 2 + 3 + ... + n times.
- **Space:** O(1) – Only loop variables are used; no additional data structures are created.

### Edge Cases
- **n = 1:** Prints a single row containing `1`.
- **n = 0:** Prints nothing.
- **n < 0:** Prints nothing.
- **n > 1:** Prints the descending number triangle as expected.

## My Experience

**Note:** Quite impressive and thoughfull process with different approach. date 02-11-2026.
