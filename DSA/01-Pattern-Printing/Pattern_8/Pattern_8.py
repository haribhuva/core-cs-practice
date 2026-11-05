"""
Problem: Pattern 8
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-8
"""


class Solution:
    def pattern8(self, n):
        for i in range(n, 0, -1):
            print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    solution = Solution()
    solution.pattern8(5)