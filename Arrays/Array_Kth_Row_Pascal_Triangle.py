from typing import List


class PascalTriangle:
    # @param integer representing kth row
    # return list of integers

    # def solve_using_recursion(self, k):
    #     if k == 0:
    #         return [1]
    #     nth_row: List[int] = [1]
    #     curr = self.solve_using_recursion(k - 1)
    #     for i in range(1, k):
    #         value = curr[i] + curr[i - 1]
    #         nth_row.append(value)
    #     nth_row.append(1)
    #     return nth_row
    def non_recursive_solution(self, k):
        if k == 0:
            return [1]
        nth_row = [[1], [1, 1]]

        for j in range(1, k-1):
            val = [1]
            for i in range(1, len(nth_row[j])):
                value = nth_row[j][i] + nth_row[j][i - 1]
                val.append(value)
            val.append(1)
            nth_row.append(val)
        return nth_row

    def solve(self, A):
        if A == 0:
            return []
        nth_row = [[1]]
        for j in range(1, A):
            val = [1]
            prev = 1
            curr = 0
            for i in range(1, j):
                curr = (prev * (j - i + 1)) // i
                val.append(curr)
                prev = curr
            val.append(1)
            nth_row.append(val)
        return nth_row


if __name__ == "__main__":
    pascal = PascalTriangle()
    ans = pascal.solve(3)
    print(ans)
