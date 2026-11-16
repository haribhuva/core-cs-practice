# Automorphic Number

- **Category:** Mathematics
- **Difficulty:** Basic
- **Source:** [Automorphic Number](https://takeuforward.org/practice/dsa/automorphic-number)

## Hint
- An automorphic number is a number whose square ends with the number itself.
- Use the modulo (%) operator to extract the last digits of the square.
- The number of digits determines the power of 10 required.

## My Approach
- Calculate the square of the given number.
- Find the number of digits using len(str(n)).
- Calculate 10 ** len(str(n)) to determine the last digits.
- Use the modulo operator (%) to check whether the last digits of the square match the original number.
- Return True if they match; otherwise, return False.

## Key Insight
The key observation is that an automorphic number's square ends with the number itself.

For example:
- 25² = 625
- 625 % 100 = 25
- Since the result equals 25, it is an automorphic number.

## Complexity
- Time: O(d), where d is the number of digits in n.
- Space: O(d), due to string conversion.

## Edge Cases
- Single-digit automorphic numbers (1, 5, 6).
- Zero (0 is an automorphic number).
- Numbers ending with zero.
- Non-automorphic numbers (e.g., 7).

## My Experience

**Note:** I found a solution after some struggle but after that i did chat GPT and get better solution with the maths, so I approach it. Date: 16-11-2026
