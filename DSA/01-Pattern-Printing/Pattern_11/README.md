# Pattern 11

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 11](https://takeuforward.org/practice/dsa/pattern-11)

## Hint
Use nested loops to print the pattern. The outer loop controls the rows, and the inner loop prints numbers in each row. Use `(i + j) % 2` to alternate between 0 and 1.

## My Approach
I used two nested loops to print the pattern.

- The outer loop runs from 1 to n and controls the number of rows.
- The inner loop runs from 0 to i-1 and prints i numbers in each row.
- I used `(i + j) % 2` to generate alternating 0s and 1s.
- `end=" "` prints numbers on the same line with spaces.
- `print()` moves to the next line after each row.

## Key Insight
The main observation is that `(i + j) % 2` generates an alternating binary pattern.

- If `i + j` is even, it prints 0.
- If `i + j` is odd, it prints 1.

The number of elements in each row is equal to the row number.

## Complexity
- **Time:** O(n²) – The nested loops execute a total of n(n+1)/2 times.
- **Space:** O(1) – Only a constant amount of extra space is used.

## Edge Cases
- **n = 1:** Prints a single 1.
- **n = 0:** Prints nothing.
- **n < 0:** Prints nothing because the outer loop does not execute.
- **n > 1:** Prints n rows with alternating 0s and 1s.

## My Experience

**note:** it was little bit twisted because i didn't think about maths. it was so easy to write the code. date: 5-11-2026.