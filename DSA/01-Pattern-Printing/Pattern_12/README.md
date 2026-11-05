# Pattern 12

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 12](https://takeuforward.org/practice/dsa/pattern-12)

Hint:
Use three nested loops to print increasing numbers, spaces, and decreasing numbers in each row.

My Approach:
I used nested for loops to print the pattern row by row.
1. The outer loop runs from 1 to n.
2. The first inner loop prints numbers in increasing order (1 to i).
3. The second inner loop prints spaces using 2 * (n-i).
4. The third inner loop prints numbers in decreasing order (i to 1).
5. After each row, print() moves to the next line.

Key Insight:
The number of digits increases with each row, while the number of spaces decreases.
- Increasing sequence: 1 to i
- Spaces: 2 * (n-i)
- Decreasing sequence: i to 1

Complexity:
Time: O(n²) – Nested loops iterate over the rows and columns.
Space: O(1) – No extra data structures are used.

Edge Cases:
1. n = 1: Prints a single row (11).
2. n = 2: Prints two rows with decreasing spaces.
3. n = 0: No output.
4. Larger n: The pattern continues symmetrically.

## My Experience

**note:** Too much hard. i'm still trying to understanding the code and logic. date: 5-11-2026.
