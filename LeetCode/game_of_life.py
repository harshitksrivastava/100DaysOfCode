# https://leetcode.com/problems/game-of-life/
# Problem No: 289
# Time Complexity:

# Table utilized to maintain state
#   Initial state |  New state |  Substituted value
#          0      |      0     |        0           value fewer than 2
#          1      |      0     |        1           value fewer than 2 or more than 3
#          0      |      1     |        2           value exactly equal to 3 (means cell initially dead is now live)
#          1      |      1     |        3           value in range [2,3]

# we notice that 1 and 2 are interchanged


class Solution:

    # takes a matrix and returns new state of the matrix with in-place changes
    def game_of_life(self, board):
        row, col = len(board), len(board[0])

        # this function adds up the value for surrounding valid locations if they were 1
        def helper_function(row_num, col_num):
            value = 0

            # max and min are used to remove the invalid indexes for corner as now it always remain in valid indexes and
            # adds up their value if previously they were 1 and if the current location is 1 then we sub it later
            for i in range(max(row_num - 1, 0), min(row_num + 2, len(board))):
                for j in range(max(0, col_num - 1), min(len(board[i]), col_num + 2)):

                    # we only add if the value of the location is 1 or 3 because
                    # if 1 or 3 are encountered we add it as their initial value was 1
                    # if 0 or 2 are encountered we ignore it as their initial value was 0
                    if board[i][j] in [1, 3]:
                        value += 1

            # while adding we don't filter the value of current location, hence we sub it from our final value
            return value-board[row_num][col_num]

        for row_index in range(row):
            for col_index in range(col):

                # calling helper function to compute sum of 8 surrounding elements for every element of matrix
                new_state = helper_function(row_index, col_index)

                # if the initial value of element is 1 then
                if board[row_index][col_index]:

                    # if the sum of elements in all 8 direction has value 2 or 3 then we assign 3 to it
                    if new_state in [2, 3]:
                        board[row_index][col_index] = 3

                # if the initial value was 0, and the sum is exactly 3 then we assign it 2 (cell is now live)
                elif new_state == 3:
                    board[row_index][col_index] = 2

        # Substituting
        # 0 for 1
        # 1 for 2 or 3
        for i in range(row):
            for j in range(col):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] in [2, 3]:
                    board[i][j] = 1


if __name__ == "__main__":
    sol = Solution()
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    sol.game_of_life(board)
    for index in range(len(board)):
        print(board[index])


# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#
# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
