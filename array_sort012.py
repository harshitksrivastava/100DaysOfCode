# to sort the array containing only 0,1,2 

def sort012(arr):
    dict_012 = {}
    for i in arr:
        if i not in dict_012:
            dict_012[i] = 1
        else:
            dict_012[i] += 1
    k = 0
    for i in range(3):
        j = dict_012.get(i)
        while j:
            arr[k] = i
            k += 1
            j -= 1
    print(arr)


input_array = [0, 2, 1, 2, 0]
sort012(input_array)
