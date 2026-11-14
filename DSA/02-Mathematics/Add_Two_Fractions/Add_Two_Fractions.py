"""
Problem: Add Two Fractions
Difficulty: Core
Category: Mathematics
Source: https://takeuforward.org/practice/dsa/add-two-fractions
"""

from math import gcd


class Solution:
    def addFractions(self, frac1: str, frac2: str) -> str:
        a, b = map(int, frac1.split("/"))
        c, d = map(int, frac2.split("/"))

        if b == 0 or d == 0:
            return "Invalid denominator"

        fraction_up = a * d + b * c
        fraction_down = b * d

        common = gcd(fraction_up, fraction_down)

        fraction_up //= common
        fraction_down //= common

        return f"{fraction_up}/{fraction_down}"


if __name__ == "__main__":
    frac1 = input("Enter the first fraction: ")
    frac2 = input("Enter the second fraction: ")

    solution = Solution()
    print(solution.addFractions(frac1, frac2))