# the objective to extract the Kth smallest element from the given array sequence
import math


class Heap:
    def __init__(self, array):
        self.A = array
        self.heapSize = len(array) - 1

    def build_min_heap(self):
        for i in range(math.floor(len(self.A)/2), -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        smallest = i
        if left <= self.heapSize and self.A[i] >= self.A[left]:
            smallest = left
        if right <= self.heapSize and self.A[right] <= self.A[smallest]:
            smallest = right
        if smallest != i:
            self.A[smallest], self.A[i] = self.A[i], self.A[smallest]
            self.min_heapify(smallest)

    def smallest_kth_element(self, k):
        self.build_min_heap()
        for i in range(k):
            minimum = self.A[0]
            self.A[0] = self.A[self.heapSize]
            self.heapSize -= 1
            self.min_heapify(0)
        return minimum


if __name__ == "__main__":
    input_array = [7, 10, 4, 3, 20, 15]
    heap = Heap(input_array)
    small = heap.smallest_kth_element(4)
    print(small)
