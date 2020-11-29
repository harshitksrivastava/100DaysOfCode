# rotate the array elements circularly

def circular_shift(array):
    last_element = array[len(array) - 1]
    for i in range(len(array)-2, -1,-1):
        array[i + 1] = array[i]
    array[0] = last_element


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        length_one = input().split()
        array_list_one = list(map(int, input().split()))
        circular_shift(array_list_one)
        for i in array_list_one:
            print(i,end=" ")
        print()

# Input
# 1 no of test cases(T)
# 5   no of elements for array
# 1 2 3 4 5  array
# 5 1 2 3 4  output
