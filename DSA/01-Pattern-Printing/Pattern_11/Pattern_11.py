"""
Problem: Pattern 11
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-11
"""


class Solution:
    def pattern11(self, n):
        for i in range(1, n+1):
            for j in range(i):
                print((i + j) % 2, end="")
            print()

if __name__ == "__main__":
    solution = Solution()
    solution.pattern11(5)