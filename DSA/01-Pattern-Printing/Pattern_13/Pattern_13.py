"""
Problem: Pattern 13
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-13
"""


class Solution:
    def pattern13(self, n):
        num = 1
        for i in range(1, n+1):
            for j in range(i):
                print(num, end=" ")
                num += 1
            print()


if __name__ == "__main__":
    solution = Solution()
    solution.pattern13(4)