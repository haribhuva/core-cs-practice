"""
Problem: Pattern 1
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-1
"""


class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()


if __name__ == "__main__":
    solution = Solution()
    solution.pattern1(4)
