"""
Problem: Armstrong Number
Difficulty: Basic
Category: Mathematics
Source: https://takeuforward.org/practice/dsa/armstrong-number
"""


class Solution:
    def isArmstrong(self, N: int) -> bool:
        n = list(str(N))
        armstrong =  0

        for i in n:
            armstrong += int(i)**len(n)

        return True if armstrong == N else False
        
if __name__ == "__main__":
    solution = Solution()
    n = int(input("Enter number: "))
    print(solution.isArmstrong(n))