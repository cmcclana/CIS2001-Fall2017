from PriorityQueueADT import *

class HeapPriorityQueue(PriorityQueueADT):

    class _Item:

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def _parent(self, index):
        return ( index-1 ) // 2

    def _left(self, index):
        return 2*index + 1

    def _right(self, index):
        return 2*index + 2

    def _has_left(self, index):
        return self._left(index) < len(self._data)

    def _has_right(self, index):
        return self._right(index) < len(self._data)

    def _swap(self, first_index, second_index):
        temp = self._data[first_index]
        self._data[first_index] = self._data[second_index]
        self._data[second_index] = temp

    def _upheap(self, index):
        parent = self._parent(index)
        if index > 0 and self._data[index] < self._data[parent]:
            self._swap(index, parent)
            self._upheap(parent)

    def _downheap(self, index):
        if self._has_left(index):
            left = self._left(index)
            small_child = left
            if self._has_right(index):
                right = self._right(index)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[index]:
                self._swap(small_child, index)
                self._downheap(small_child)

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def add(self, key, value = None):
        item = self._Item(key, value)
        self._data.append(item)
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise IndexError
        item = self._data[0]
        return ( item._key, item._value )

    def remove_min(self):
        if self.is_empty():
            raise IndexError
        self._swap(0, len(self._data) - 1 )
        item = self._data.pop()
        self._downheap(0)
        return ( item._key, item._value )




