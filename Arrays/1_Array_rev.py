import math


# using a python inbuilt way
def array_reverse_python(array_sequence):
    print(array_sequence[::-1])


# In this approach we change the first with last and so on, the changes made here are in-place(i.e effects original
# array sequence
def array_reverse(array_sequence):
    length = len(array_sequence)
    for i in range(math.ceil(length / 2)):
        array_sequence[i], array_sequence[length - (i + 1)] = array_sequence[length - (i + 1)], array_sequence[i]
    print("array_reverse", array_sequence)


# the function defines a recursive approach to reverse an array, the changes made here are in-place(i.e effects original
# array sequence
def array_reverse_recursive(array_sequence, start, end):
    if start >= end:
        return
    array_sequence[start], array_sequence[end] = array_sequence[end], array_sequence[start]
    array_reverse_recursive(array_sequence, start + 1, end - 1)


arr = [1, 2, 3, 4, 5, 6]
# array_reverse_python(arr)
# print(arr)

# array_reverse(arr)
# print(arr)
array_reverse_recursive(arr, 0, len(arr) - 1)
print(arr)


# all the above programs have complexity of O(n)
