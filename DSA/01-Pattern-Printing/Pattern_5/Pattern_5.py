"""
Problem: Pattern 5
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-5
"""


class Solution:
    def pattern5(self, n):
        for i in range(n, 0, -1):
            print(i * "*")

if __name__ == "__main__":
    solution = Solution()
    solution.pattern5(5)
