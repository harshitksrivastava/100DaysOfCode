# Common elements

def common_elements(array1, array2, array3):
    dict1 = {}
    dict2 = {}
    dict3 = {}
    common = []
    for i in array1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for i in array2:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] += 1
    for i in array3:
        if i not in dict3:
            dict3[i] = 1
        else:
            dict3[i] += 1
    for i in array1:
        if dict2.get(i) and dict3.get(i):
            common.append(i)

    return common


if __name__ == "__main__":
    input_array1 = list(map(int, input().split()))
    input_array2 = list(map(int, input().split()))
    input_array3 = list(map(int, input().split()))
    arr = common_elements(input_array1, input_array2, input_array3)
    print(arr)


# Input:
# n1 = 6; A = {1, 5, 10, 20, 40, 80}
# n2 = 5; B = {6, 7, 20, 80, 100}
# n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
# Output: 20 80
# Explanation: 20 and 80 are the only
# common elements in A, B and C.
