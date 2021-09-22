# https://leetcode.com/problems/pascals-triangle/
# Problem Link: 118
# Time Complexity: O(N^2)


class Solution:

    def generate_nrow_pascal_triangle(self, num_rows):
        final_triangle = [[1]]
        for index_i in range(1, num_rows):
            nth_row = [1]
            for index_j in range(len(final_triangle[index_i-1]) - 1):
                nth_row.append(final_triangle[index_i-1][index_j]+final_triangle[index_i-1][index_j+1])
            nth_row.append(1)
            final_triangle.append(nth_row)
        return final_triangle


if __name__ == "__main__":
    sol = Solution()
    ans = sol.generate_nrow_pascal_triangle(5)
    print(ans)


# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
