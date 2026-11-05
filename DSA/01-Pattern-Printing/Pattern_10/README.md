# Pattern 10

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 10](https://takeuforward.org/practice/dsa/pattern-10)

## Hint
Use two separate loops:
- The first loop prints stars in increasing order from 1 to `n - 1`.
- The second loop prints stars in decreasing order from `n` to 1.

## My Approach
I used two `for` loops to print the pattern.

1. The first loop runs from `1` to `n - 1` and prints an increasing number of stars in each row.
2. The second loop runs from `n` down to `1` and prints a decreasing number of stars in each row.

I chose this approach because separating the increasing and decreasing parts makes the pattern easy to understand and implement.

## Key Insight
The pattern consists of two parts:
- An increasing sequence of stars.
- A decreasing sequence of stars.

Using `i * "*"` or `j * "*"` allows us to print the required number of stars in each row without using an inner loop.

## Complexity
- **Time:** O(n) — Two loops run approximately `n` times each. The total number of stars printed is O(n²), so the actual time complexity including printing is **O(n²)**.
- **Space:** O(n) — Each printed row contains at most `n` stars. If considering only auxiliary space excluding the output, it is **O(1)**.

## Edge Cases
- **n = 1:** Prints one row containing a single star.
- **n = 0:** Both loops are skipped, so nothing is printed.
- **n > 1:** Prints the increasing and decreasing star pattern.
- **Negative n:** Both loops are skipped, so nothing is printed.

## My Experience

**note:** solve in minutes, because it was easy. Date: 5-11-2026.