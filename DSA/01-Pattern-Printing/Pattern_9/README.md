# Pattern 9

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 9](https://takeuforward.org/practice/dsa/pattern-9)

## Hint
Use two loops to print the upper and lower parts of the pattern. The first loop increases the number of stars by 2, while the second loop decreases it by 2. Adjust the spaces before the stars to keep the pattern centered.

## My Approach
I used two separate loops to print the pattern.

- **First loop:** Starts from 1 and increases the number of stars by 2 in each iteration. This prints the upper part of the pattern.
- **Second loop:** Starts from `n` and decreases the number of stars by 2. This prints the lower part of the pattern.
- In both loops, spaces are printed before the stars to maintain alignment and create the pattern shape.

I chose this approach because separating the upper and lower parts makes the pattern easier to understand and implement.

## Key Insight
The main observation is that the number of stars changes by 2 in each row.

- The upper part increases the number of stars.
- The lower part decreases the number of stars.
- Spaces are adjusted according to the number of stars to maintain the pattern's alignment.

Using two loops makes it simple to control the increasing and decreasing star sequences.

## Complexity

- **Time:** O(n²) — The outer loops execute O(n) times, and printing stars and spaces in each row takes up to O(n) time. Therefore, the total time complexity is O(n²).
- **Space:** O(n) — Each row creates a string containing spaces and stars, with a maximum length proportional to n. The auxiliary space required for each row is O(n).

## Edge Cases
- **n = 1:** The loops execute and print a single row containing one star.
- **n = 0:** Both loops are skipped, so no pattern is printed.
- **Even n:** The first loop prints odd numbers of stars, while the second loop prints even numbers of stars. This may produce a different pattern shape than expected.
- **Odd n:** The pattern follows the intended increasing and decreasing sequence of odd numbers.
- **Negative n:** Both loops are skipped, so no pattern is printed.

## My Experience

**note:** I stuck for few minutes around 30 and then i found that i'm printing wrong variable i instead of j. date: 5-11-2026.