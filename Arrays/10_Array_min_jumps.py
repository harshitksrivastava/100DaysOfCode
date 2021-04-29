# to calculate the minimum jumps to reach the end of the array

def min_jump(arr, n):
    if n - 1 == 0:
        return 0
    if arr[0] == 0:
        return float('inf')
    jump = 0
    maxi = 0
    total = arr[0]
    for i in range(0, n - 1):
        maxi = 0
        for j in range(1, arr[i] + 1):
            a = arr[i + j]
            if maxi < a:
                maxi = a
                temp = j
        if maxi == 0:
            return float('inf')
        jump += 1
        print(total, maxi)
        total += maxi
        print(total)
        if i+temp == n-1:
            return jump
        if total > n - 1:
            return jump+1
        i += temp


if __name__ == "__main__":
    input_array = [1, 4, 3, 2, 6, 7, 1, 2]
    # input_array = [1, 1, 1, 1, 1, 1, 1]
    # input_array = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    minimum = min_jump(input_array, len(input_array))
    print(minimum)
