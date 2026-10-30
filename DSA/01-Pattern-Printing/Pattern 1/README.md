# Pattern 1

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 1](https://takeuforward.org/practice/dsa/pattern-1)

## Hint

Can use Nested loops.

## My Approach

I used nested for loops with the print() function instead of returning a value.

Outer loop (i) controls the number of rows.

Inner loop (j) controls the number of stars in each row.

print("*", end=" ") prints stars on the same line.

print() moves the cursor to the next line after completing each row.

## Key Insight

For an N × N square pattern:

Number of rows = N.

Number of columns = N.

Every row contains exactly N stars.

The inner loop always runs N times, independent of the outer loop's current iteration.

Core logic: Both loops iterate N times, resulting in N × N = N² stars.

## Complexity

- **Time:** O(N²) – The outer loop executes N times, and for every iteration, the inner loop executes N times. 
- **Space:** O(1) – Only loop variables are used. No additional data structure is required because the pattern is printed directly.

## Edge Cases

N = 1: Prints only one star.

N = 2: Prints a 2 × 2 square.

N = 100: Prints a 100 × 100 square.

N = 0: Prints nothing (although the given problem constraint is N ≥ 1).

Ensure the newline is printed after each completed row.

## My Experience

**Note:** I skipped my practice from previous 5 months, because **I shifted on vibe coding and prompt base coding, because of job's deadline pressure. So I forgot that how to write code manual.** This is the first day 30-10-2026, I'm facing so much struggle into understanding the problem. My brain don't want to think anything.

**Lesson:** I don't care how much I struggle, I will do practice again.