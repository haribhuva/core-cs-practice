"""
Problem: Pattern 2
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-2
"""


class Solution:
    def pattern2(self, n):
        for i in range(0,n):
            for j in range(0,n):
                # i+=1
                j+=1
                # print(i*"*"\nj*"*", end="")
                # print(f"{i*"*"}\n{j*"*"}", end="")
                print(j*"*")
            print(i*"*")
            return i, j

if __name__ == "__main__":
    solution = Solution()
    solution.pattern2(4)