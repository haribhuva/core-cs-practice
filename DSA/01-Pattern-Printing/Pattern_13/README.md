# Pattern 13

- **Category:** Pattern Printing
- **Difficulty:** Basic
- **Source:** [Pattern 13](https://takeuforward.org/practice/dsa/pattern-13)

## Hint
Think about using a variable `num` that starts at 1 and increments after every printed number. Use nested loops to print numbers in increasing order, where each row contains one more number than the previous row.

## My Approach
- Initialize `num = 1` before starting the loops.
- Use an outer loop to control the number of rows (1 to n).
- Use an inner loop to print `i` numbers in each row.
- After printing each number, increment `num` by 1.
- Use `print()` after the inner loop to move to the next line.

## Key Insight
The main idea is to maintain a single counter (`num`) throughout the pattern instead of resetting it for every row. Each row contains an increasing number of consecutive integers.

**Output for n = 4:**
1
2 3
4 5 6
7 8 9 10

## Complexity
- **Time:** O(n²) – The total number of printed elements is 1 + 2 + 3 + ... + n = n(n+1)/2.
- **Space:** O(1) – Only a constant amount of extra space is used.

## Edge Cases
1. **n = 1:** Prints a single number: 1.
2. **n = 2:** Prints:
   1
   2 3
3. **n = 0:** No pattern is printed because the outer loop does not execute.
4. **Larger values of n:** The pattern continues with consecutive numbers, increasing the number of elements in each row.

## My Experience

**Note: ** I stuck for whole two days but didn't get logic and write the code blindly. that was mistake because i didn't even try to understand question and try and error again and again for print focused results instead of thinking the core problem. date: 13-11-2026.