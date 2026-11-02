"""
Problem: Pattern 6
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-6
"""


class Solution:
    def pattern6(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i + 1):
                print(j, end="")
            print()


if __name__ == "__main__":
    solution = Solution()
    solution.pattern6(5)
