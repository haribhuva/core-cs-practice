# Add Two Fractions

- **Category:** Mathematics
- **Difficulty:** Core
- **Source:** [Add Two Fractions](https://takeuforward.org/practice/dsa/add-two-fractions)

## Hint
To add two fractions, use the cross-multiplication method. Multiply each numerator by the opposite denominator, add the results, and multiply both denominators to get the new denominator.

## My Approach
- Split both fraction strings using `/` and convert the numerator and denominator into integers.
- Store the values in separate variables (`a`, `b`, `c`, `d`).
- Check whether either denominator is zero to avoid division by zero.
- Calculate the numerator using the formula: `a*d + b*c`.
- Calculate the denominator using the formula: `b*d`.
- Divide the numerator by the denominator to get the result.
- Print the result.

## Key Insight
To add two fractions, we need a common denominator.

Formula:
(a/b) + (c/d) = (a*d + b*c) / (b*d)

For example:
1/2 + 1/3 = (1*3 + 2*1) / (2*3)
           = 5/6

## Complexity
- **Time:** O(1) – Only a fixed number of arithmetic operations are performed.
- **Space:** O(1) – Only a constant amount of extra space is used.

## Edge Cases
1. **Zero numerator:** Handles fractions such as 0/5.
2. **Zero denominator:** A denominator of 0 is invalid and should be handled to avoid division by zero.
3. **Same denominators:** For example, 1/4 + 2/4 = 3/4.
4. **Different denominators:** For example, 1/2 + 1/3 = 5/6.
5. **Negative fractions:** The calculation should also work with negative numerators.
6. **Result equal to a whole number:** For example, 1/2 + 1/2 = 1.

## My Experience

**Note:** I forgoted that how to use map function and take input in OOPs based class and functions, that's funny hehe! date: 14-11-2026.