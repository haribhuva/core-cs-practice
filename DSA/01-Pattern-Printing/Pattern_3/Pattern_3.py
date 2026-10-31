"""
Problem: Pattern 3
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-3
"""

class Solution:
    def pattern3(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
        return i


if __name__ == "__main__":
    solution = Solution()
    solution.pattern3(4)
