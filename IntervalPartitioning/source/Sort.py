from source.Heap import Heap


class HeapSort:
    def __init__(self, size=10, array=None):
        self.heapSize = size
        self.array = array

    def sort(self):

        if self.array is None:
            return 'The value of array is None.'
        heappop = Heap(self.heapSize)

        dataCount = 0
        while self.array:
            heappop.insert(self.array[0])
            del self.array[0]
            dataCount += 1

        for item in range(dataCount):
            self.array.append(heappop.delete())

        return self.array, dataCount

