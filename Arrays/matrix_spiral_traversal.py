# Given a matrix of size R*C. Traverse the matrix in spiral form.

def spiral_traversal(matrix, r, c):
    i = 0
    p = 0
    l = r
    m = c
    mat = []
    while i < l and p < m:
        for j in range(p, m):
            mat.append(matrix[i][j])
        i = i + 1
        for k in range(i, l):
            mat.append(matrix[k][m - 1])
        m = m - 1
        if i < l:
            for t in range(m - 1, p - 1, -1):
                mat.append(matrix[l - 1][t])
            l = l - 1
        if p < m:
            for q in range(l - 1, i - 1, -1):
                mat.append(matrix[q][p])
            p = p + 1
    return mat


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        r, c = map(int, input().split())
        array_list_one = list(map(int, input().split()))
        matrix = []
        k = 0
        for i in range(r):
            row = []
            for j in range(c):
                row.append(array_list_one[k])
                k += 1
            matrix.append(row)
        print(matrix)
        ans = spiral_traversal(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()


# Input
# 1 no of test cases(T)
# 3 5   no of rows and column for matrix
# 6 6 2 28 2 12 26 3 28 7 22 25 3 4 23 matrix as input
# 6 6 2 28 2 7 23 4 3 25 22 12 26 3 28 output

#
# Expected Time Complexity: O(R*C)
# Expected Auxiliary Space: O(R*C)        Can be O(1) by directly printing
