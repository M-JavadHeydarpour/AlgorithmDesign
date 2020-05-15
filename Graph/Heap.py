class PriorityQueue:
    def __init__(self, size):
        self.heap = [[None, None] for i in range(size)]  # [priority, data]
        self.size = size
        self.count = -1

    def parent(self, i):
        return i // 2 if i // 2 > -1 else 0

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def isFull(self):
        return self.count == self.size - 1

    def isEmpty(self):
        return self.count == 0

    def expand(self, count):
        if self.isFull():
            self.heap += [[None, None] for i in range(count)]
            self.size += count

    def insert(self, data, index):
        if not self.isFull():
            self.count += 1
            self.heap[self.count][0] = data
            self.heap[self.count][1] = index


        elif self.isFull():
            self.expand(1)
            self.count += 1
            self.heap[self.count][0] = data
            self.heap[self.count][1] = index
        self.reheap(1, self.count)

    def reheap(self, status, data_index):
        if status == -1:  # delete data from heap tree

            root = data_index
            smallest = root
            if (self.left(root) < self.count) or (self.right(root) < self.count):
                if self.heap[self.left(root)][0] < self.heap[smallest][0]:
                    smallest = self.left(root)
                if self.heap[self.right(root)][0] < self.heap[smallest][0]:
                    smallest = self.right(root)
                if smallest != self.heap[root][0]:
                    self.heap[root], self.heap[smallest] = self.heap[smallest], self.heap[root]
                    data_index += 1
                    self.reheap(-1, data_index)

        elif status == 1:  # insert data in heap tree
            if self.heap[data_index][0] < self.heap[self.parent(data_index)][0]:
                # self.heap[data_index][0], self.heap[self.parent(data_index)][0] = self.heap[self.parent(data_index)][0], \
                # self.heap[data_index][0]
                self.heap[data_index], self.heap[self.parent(data_index)] = self.heap[self.parent(data_index)], \
                                                                            self.heap[data_index]
                # index = self.heap.index(self.heap[self.parent(data_index)][0])
                index = self.parent(data_index)
                self.reheap(1, index)

    def delete(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.count]
        self.heap[self.count] = [None, None]
        self.count -= 1
        self.reheap(-1, 0)
        return result


# [priority, data]

# h = PriorityQueue(5)
# h.insert(4, 7)
# h.insert(1, 5)
# h.insert(9, 3)
# h.insert(5, 3)
# h.insert(3, 1)
# h.insert(3, 1)
# h.insert(2, 2)
# h.insert(7, 4)
# h.insert(5, 6)
#
# print(h.heap)
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.delete())
# print(h.delete())


# class Heap:
#     def __init__(self, size):
#         self.heap = [None for i in range(size)]
#         self.size = size
#         self.count = -1
#
#     def parent(self, i):
#         return i // 2 if i // 2 > -1 else 0
#
#     def left(self, i):
#         return 2 * i
#
#     def right(self, i):
#         return 2 * i + 1
#
#     def isFull(self):
#         return self.count == self.size - 1
#
#     def isEmpty(self):
#         return self.count == 0
#
#     def expand(self, count):
#         if self.isFull():
#             self.heap += [None for i in range(count)]
#             self.size += count
#
#     def insert(self, data):
#         if not self.isFull():
#             self.count += 1
#             self.heap[self.count] = data
#
#         elif self.isFull():
#             self.expand(1)
#             self.count += 1
#             self.heap[self.count] = data
#         self.reheap(1, self.count)
#
#     def reheap(self, status, data_index):
#         if status == -1:  # delete data from heap tree
#
#             root = data_index
#             smallest = root
#             if (self.left(root) < self.count) or (self.right(root) < self.count):
#                 if self.heap[self.left(root)] < self.heap[smallest]:
#                     smallest = self.left(root)
#                 if self.heap[self.right(root)] < self.heap[smallest]:
#                     smallest = self.right(root)
#                 if smallest != self.heap[root]:
#                     self.heap[root], self.heap[smallest] = self.heap[smallest], self.heap[root]
#                     data_index += 1
#                     self.reheap(-1, data_index)
#
#         elif status == 1:  # insert data in heap tree
#             if self.heap[data_index] < self.heap[self.parent(data_index)]:
#                 self.heap[data_index], self.heap[self.parent(data_index)] = self.heap[self.parent(data_index)], \
#                                                                             self.heap[data_index]
#                 # index = self.heap.index(self.heap[self.parent(data_index)])
#                 index = self.parent(data_index)
#                 self.reheap(1, index)
#
#     def delete(self):
#         result = self.heap[0]
#         self.heap[0] = self.heap[self.count]
#         self.heap[self.count] = None
#         self.count -= 1
#         self.reheap(-1, 0)
#         return result
#
# # f = Heap(4)
# # f.insert(9)
# # f.insert(7)
# # f.insert(2)
# # f.insert(3)
# #
# # print(f.delete())
# # print(f.delete())
# # print(f.delete())
# # print(f.delete())
