# Pattern 4

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 4](https://takeuforward.org/practice/dsa/pattern-4)

### Hint
- Use nested loops to print the pattern.
- The outer loop controls the rows.
- The inner loop prints the current row number repeatedly.
- The number of repetitions increases with each row.

### My Approach
1. The outer loop iterates from `1` to `n`, representing the rows.
2. The inner loop iterates from `1` to `i`, printing the current row number (`i`) without moving to a new line.
3. After the inner loop finishes, `print()` moves the cursor to the next line.

### Key Insight
The current row number (`i`) determines both:
- **Which number to print:** `i`
- **How many times to print it:** `i`

### Complexity
- **Time:** O(n²) – The inner loop executes a total of 1 + 2 + 3 + ... + n times.
- **Space:** O(1) – Only loop variables are used; no additional data structures are created.

### Edge Cases
- **n = 1:** Prints a single row containing `1`.
- **n = 0:** Prints nothing.
- **n < 0:** Prints nothing.
- **n > 1:** Prints the increasing number triangle as expected.

## My Experience

**Note:** Not that much hard. the consistancy is effective, and this is being fun again for me! date 31-10-2026.