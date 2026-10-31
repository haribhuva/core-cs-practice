"""
Problem: Pattern 4
Difficulty: Basic
Category: Pattern Printing
Source: https://takeuforward.org/practice/dsa/pattern-4
"""


class Solution:
    def pattern4(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end="")
            print()
        return i

        #comprehension method
# class Solution:
#     def pattern4(self, n):
        # return "\n".join(str(i) * i for i in range(1, n+1))


if __name__ == "__main__":
    solution = Solution()
    print(solution.pattern4(5))