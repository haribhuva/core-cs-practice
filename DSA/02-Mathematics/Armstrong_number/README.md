# Armstrong Number

- **Category:** Mathematics
- **Difficulty:** Basic
- **Source:** [Armstrong Number](https://takeuforward.org/practice/dsa/armstrong-number)

## Hint

- Convert the number into a string to count its digits.
- An Armstrong number is a number equal to the sum of its digits, each raised to the power of the total number of digits.
- Use a loop to calculate the sum and compare it with the original number.

## My Approach

1. Convert the input number into a list of digits using `str(N)`.
2. Initialize a variable `armstrong = 0` to store the sum.
3. Iterate through each digit:
   - Convert the digit into an integer.
   - Raise it to the power of the total number of digits.
   - Add the result to `armstrong`.
4. Compare the calculated sum with the original number.
5. Return `True` if both are equal; otherwise, return `False`.

I chose this approach because converting the number into a string makes it easy to access individual digits and calculate their powers.

## Key Insight

The key observation is that the power of each digit depends on the total number of digits in the original number, not on its position.

Example:

153 has 3 digits.

1³ + 5³ + 3³ = 1 + 125 + 27 = 153

Since the sum equals the original number, 153 is an Armstrong number.

## Complexity

- **Time:** O(d), where d is the number of digits. Each digit is processed once.
- **Space:** O(d), because the number is converted into a list of its digits.

## Edge Cases

- **Single-digit numbers:** Every single-digit non-negative number (0–9) is an Armstrong number.
- **Zero:** 0 is an Armstrong number.
- **Armstrong numbers:** 153, 370, 371, and 407 should return True.
- **Non-Armstrong numbers:** 123 and 100 should return False.
- **Large numbers:** The approach works for larger integers as well.
- **Negative numbers:** The current implementation returns False for negative numbers.

## My Experience

**Note:** I did this easily, because understand the question properly with calculations. Face some struggle in printing the output and calculation but it was ok not much hard. Date: 16-11-2026
