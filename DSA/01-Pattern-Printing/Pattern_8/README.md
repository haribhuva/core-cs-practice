# Pattern 8

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 8](https://takeuforward.org/practice/dsa/pattern-8)

## Hint

- focus on loop's parameter like *(start, stop, limit)*

- try to understand the operations what will be the requirement to print, star or space

## My Approach

- I use a for loop to iterate from n to 1 in decreasing order.

- In each iteration, I calculate the number of spaces using n - i to align the pattern properly.

- I calculate the number of stars using the formula 2 * i - 1 to print an odd number of stars in each row.

- I concatenate the spaces and stars and print them in each iteration.

- As the loop progresses, the spaces increase by 1 and the stars decrease by 2, forming a reverse pyramid pattern.

## Key Insight

- The outer loop runs from n to 1 in decreasing order.

- The number of spaces increases by 1 in each row.

- The number of stars decreases by 2 in each row.

- The formula n - i determines the number of leading spaces.

- The formula 2 * i - 1 ensures that the number of stars is always odd.

- String multiplication (" " * count and "*" * count) makes pattern printing easier.

- The overall pattern forms an inverted pyramid shape.

## Complexity

- **Time:** O(n²)
- **Space:** O(n) (Auxiliary Space)

## Edge Cases

- n = 1: Prints a single star (*).

- n = 0: The loop does not execute, so no pattern is printed.

- n < 0: The loop does not execute, so no pattern is printed.

- n = 5: Prints the expected reverse pyramid pattern with 5 rows.

## My Experience

**note:** it's little bit tough because I'm still trying to understand the logic of the print function with different operations. date: 5-11-2026.