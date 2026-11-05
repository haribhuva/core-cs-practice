"""
Problem: Pattern 12
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-12
"""


class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            
            for j in range(1, i+1):
                print(j, end="")

            for j in range(2 * (n-i)):
                print(" ", end="")

            for j in range(i, 0, -1):
                print(j, end="")
            print()
        

if __name__ == "__main__":
    solution = Solution()
    solution.pattern12(5)