# Pattern 5

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 5](https://takeuforward.org/practice/dsa/pattern-5)

### Hint
- Use nested loops to print the pattern.
- The outer loop controls the rows from `n` down to `1`.
- The inner loop prints the current row value as stars.
- The number of stars decreases as the row number decreases.

### My Approach
1. The outer loop iterates from `n` to `1`, representing the rows from the top to the bottom.
2. The inner loop iterates from `1` to `i`, printing `*` each time without moving to a new line.
3. After the inner loop finishes, `print()` moves the cursor to the next line.

### Key Insight
The current row number (`i`) determines both:
- **How many stars to print:** `i`
- **How many rows remain in the pattern:** the outer loop counts downward from `n` to `1`

### Complexity
- **Time:** O(n²) – The inner loop executes a total of 1 + 2 + 3 + ... + n times.
- **Space:** O(1) – Only loop variables are used; no additional data structures are created.

### Edge Cases
- **n = 1:** Prints a single row containing one star.
- **n = 0:** Prints nothing.
- **n < 0:** Prints nothing.
- **n > 1:** Prints the descending star triangle as expected.

## My Experience

**Note:** This pattern was simple but satisfying. date 31-10-2026.
