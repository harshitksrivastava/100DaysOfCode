# union of two sorted arrays

def union_of_sorted_array(array_one, array_two):
    unified_array = []
    length_array_one = len(array_one)
    length_array_two = len(array_two)
    i = 0
    j = 0
    while i < length_array_one and j < length_array_two:
        if array_one[i] < array_two[j]:
            if array_one[i] not in unified_array:
                unified_array.append(array_one[i])
            i += 1
        elif array_two[j] < array_one[i]:
            if array_two[j] not in unified_array:
                unified_array.append(array_two[j])
            j += 1
        elif array_two[j] == array_one[i]:
            if array_one[i] not in unified_array:
                unified_array.append(array_one[i])
            i += 1
            j += 1
    while i < length_array_one:
        if array_one[i] not in unified_array:
            unified_array.append(array_one[i])
        i += 1
    while j < length_array_two:
        if array_two[j] not in unified_array:
            unified_array.append(array_two[j])
        j += 1
    return len(unified_array)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        length_one, length_two = input().split()
        array_list_one = list(map(int, input().split()))
        array_list_two = list(map(int, input().split()))
        union_number = union_of_sorted_array(array_list_one, array_list_two)
        print(union_number)

# Input
# 1 no of test cases(T)
# 6 5   no of elements for first and second array
# 1 1 2 2 3 3   first array
# 8 9 7 6 5     second array
# 8             output
