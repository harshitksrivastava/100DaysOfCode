# 1
# abcdefghijklmnopqrstuvwxyz
# cba


class RajAndCards:

    def solve(self, A, string):
        dict1 = {}
        i = 0
        c = 0
        sum=0
        while i < len(A):
            dict1[A[i]] = i
            i += 1
        print(dict1)
        for j in range(0, len(string)):
            diff = abs(c - dict1[string[j]])
            sum += diff
            c = dict1[string[j]]
        return sum


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        array_list_one = list(input())
        string = input()
        Am = RajAndCards()
        fact = Am.solve(array_list_one, string)
        print(fact)
