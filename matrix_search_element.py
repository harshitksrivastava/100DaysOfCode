# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#     Integers in each row are sorted from left to right.
#     The first integer of each row is greater than the last integer of the previous row.

def search_matrix(matrix, target):
    columns = len(matrix[0]) - 1
    rows = len(matrix) - 1
    i = 0
    while i < rows:
        if target <= matrix[i][columns]:
            break
        i += 1
    while columns >= 0:
        if target == matrix[i][columns]:
            return True
        columns -= 1
    return False


if __name__ == "__main__":
    ele, tar = [[1], [3]], 1
    ans = search_matrix(ele, tar)
    print(ans)


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
