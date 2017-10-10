import ctypes

class Queue():
    
    def __init__(self, capacity=1):
        self._size = 0
        self._queue_front = 0
        if capacity <= 0:
            capacity = 1
        self._capacity = capacity
        self._storage = self._make_array(self._capacity)

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def enqueue(self, obj):
        self._ensure_capacity()
        self._storage[( self._size + self._queue_front ) % self._capacity ] = obj
        self._size += 1

    def dequeue(self):
        self._size -= 1
        temp = self._storage[ self._queue_front ] 
        self._storage[ self._queue_front ] = None
        self._queue_front += 1
        self._queue_front %= self._capacity

        # maybe check to see if size is less than 1/2 of the capacity shrink?
        return temp

    def _ensure_capacity(self):
        if self._size == self._capacity:
            self._resize( 2 * self._capacity )

    def _resize(self, new_capacity):
        new_storage = self._make_array(new_capacity)
        for index in range(self._queue_front, self._size):
            new_storage[index] = self._storage[index]
        for index in range(0, self._queue_front):
            new_storage[index] = self._storage[index]
        self._queue_front = 0
        self._storage = new_storage
        self._capacity = new_capacity

    def _make_array(self, capacity):
        return ( capacity * ctypes.py_object)()