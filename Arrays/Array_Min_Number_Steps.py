# Problem Description
# You are in an infinite 2D grid where you can move in any of the 8 directions
#  (x,y) to
#     (x+1, y),
#     (x - 1, y),
#     (x, y+1),
#     (x, y-1),
#     (x-1, y-1),
#     (x+1,y+1),
#     (x-1,y+1),
#     (x+1,y-1)
#
# You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of
# steps in which you can achieve it. You start from the first point.
# NOTE: This question is intentionally left
# slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.

# Input Format
# Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.
# Output Format
# Return an Integer, i.e minimum number of steps.


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, a, b) -> int:
        steps = 0
        for i in range(0, len(a) - 1):
            steps += abs(a[i + 1] - a[i]) + abs(b[i + 1] - b[i]) - min(abs((a[i + 1] - a[i])), abs(b[i + 1] - b[i]))

        return steps

    # This approach is more simple as it calculates the absolute difference between two points x and y and adds max
    # of the two to the steps
    # def coverPoints(self, A, B):
    #     steps = 0
    #     for i in range(0, len(A) - 1):
    #         steps +=  max( abs(A[i + 1] - A[i]) , abs(B[i + 1] - B[i]) )
    #
    #     return steps


if __name__ == "__main__":
    A1 = [4, 8, -7, -5, -13, 9, -7, 8]
    B1 = [4, -15, -10, -3, -13, 12, 8, -8]          # output wil be 108
    Am = Solution()
    fact = Am.coverPoints(A1, B1)
    print("factorial is", fact)

# Input
# A = [0, 1, 1]
# B = [0, 1, 2]
# Example Output
# 2

# Example Explanation
# Given three points are: (0, 0), (1, 1) and (1, 2). It takes 1 step to move from (0, 0) to (1, 1)
# .It takes one more step to move from (1, 1) to(1, 2).
