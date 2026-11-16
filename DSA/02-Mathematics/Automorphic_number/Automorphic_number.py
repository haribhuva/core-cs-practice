"""
Problem: Automorphic Number
Difficulty: Basic
Category: Mathematics
Source: https://takeuforward.org/practice/dsa/automorphic-number
"""


class Solution:
    def isAutomorphic(self, n: int) -> bool:
        return (n ** 2) % (10 ** len(str(n))) == n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    solution = Solution()
    print(solution.isAutomorphic(n))
