"""
Problem: Pattern 10
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-10
"""


class Solution:
    def pattern10(self, n):
        for i in range(1, n):
            print(i * "*")
        for j in range(n, 0, -1):
            print(j * "*")

if __name__ == "__main__":
    solution = Solution()
    solution.pattern10(5)