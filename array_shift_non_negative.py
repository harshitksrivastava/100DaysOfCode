# to shift all non negative numbers to the front of the array and order is not important

def shift_non_negative(arr, n):
    j = n - 1
    for i in range(n):
        if arr[i] > 0:
            while arr[j] > 0:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                print(i)
                break


# input_arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
input_arr = [-12, 11, -13, -5, 6, -7, 5, -3, 11]
shift_non_negative(input_arr, len(input_arr))
print(input_arr)
