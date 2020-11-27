# to extract min and max from an array sequence with min comparisons

class MinMax:
    def __init__(self):
        self.min = 0
        self.max = 0


# The program has the complexity of O(n) with this Brute force technique
def find_min_max(array_sequence):
    pair = MinMax()
    pair.min, pair.max = array_sequence[0], array_sequence[0]
    if len(array_sequence) == 1:
        return pair
    else:
        for element in array_sequence:
            if pair.min > element:
                pair.min = element
            elif pair.max < element:
                pair.max = element
        return pair


pa = MinMax
pa = find_min_max([1, 20, 10, 10000])
print("Min = {}, Max = {}".format(pa.min, pa.max))
