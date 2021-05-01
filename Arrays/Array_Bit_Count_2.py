class BitCount:

    def solve(self, A):
        setbit = 0
        j = 0
        bit = 0
        while j < len(A):
            bit = bin(A[j][0] ^ A[j][1]).count("1")
            if bit % 2 == 0:
                setbit += 1
            j += 1
        return setbit


if __name__ == '__main__':
    N = int(input())
    array_list_one = list(map(int, input().split()))
    Q = int(input())
    # N=3
    # array_list_one=[2,2,3]
    # Q=2
    for j in range(0, Q):
        index, value = map(int, input().split())
        Am = BitCount()
        temp = array_list_one[index]
        array_list_one[index] = value
        res = [(a, b) for idx, a in enumerate(array_list_one) for b in array_list_one[idx + 1:]]
        fact = Am.solve(res)
        array_list_one[index] = temp
        print(fact)
