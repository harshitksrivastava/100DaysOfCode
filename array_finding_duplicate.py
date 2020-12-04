# to find the duplicate in an array of N+1 integer

def finding_duplicate(arr):
    dict_dup = {}
    for i in arr:
        if i not in dict_dup:
            dict_dup[i] = 1
        else:
            return i
