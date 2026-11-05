"""
Problem: Pattern 9
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-9
"""


class Solution:
    def pattern9(self, n):
        for i in range(1, n, 2):
            print(" " * (n-i//2) + (i * "*"))
        for j in range(n, 0, -2):
            print(" " * (n-j//2) + (j * "*"))

if __name__ == "__main__":
    solution = Solution()
    solution.pattern9(9)
