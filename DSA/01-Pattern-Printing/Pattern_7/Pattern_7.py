"""
Problem: Pattern 7
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-7
"""


class Solution:
    def pattern7(self, n):
        for i in range(1, n*2, 2):
            print(" " * (n - (i // 2)) + i * "*")

if __name__ == "__main__":
    solution = Solution()
    solution.pattern7(5)
