# https://leetcode.com/problems/rotate-image/
# Problem No: 48
# Time Complexity: O(M)


class Solution:

    def rotate(self, matrix):
        n = len(matrix)

        # for transposing
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for reversing/reflecting
        for i in range(n // 2):
            for j in range(0, n):
                matrix[j][i], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[j][i]


if __name__ == "__main__":
    sol = Solution()
    # mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    sol.rotate(mat)
    print(mat)

#
#  clockwise rotate
#  first transpose, then reflection
#  1 2 3     1 4 7     7 4 1
#  4 5 6  => 2 5 8  => 8 5 2
#  7 8 9     3 8 3     3 6 3
#

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
