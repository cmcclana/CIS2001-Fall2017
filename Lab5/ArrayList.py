import ctypes

class ArrayList(object):
    """Custom implemenation of an 'array' backed list"""

    def __init__(self, capacity=1):
        self._size = 0
        if capacity <= 0:
            capacity = 1
        self._capacity = capacity
        self._storage = self._make_array(self._capacity)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if not 0 <= index <= self._size:
            raise IndexError()
        return self._storage[index]
    
    def append(self, obj):
        self._ensure_capacity()
        self._storage[self._size] = obj
        self._size += 1

    def pop(self, index = None):
        if index == None:
            self._size -= 1
            temp = self._storage[ self._size ] 
            self._storage[ self._size ] = None
        else:
            pass

        return temp

    def remove(self, obj):
        item_was_at_index = -1
        for index in range(self._size):
            if self._storage[index] == obj:
                self._storage[index] = None
                item_was_at_index = index
                break
        if item_was_at_index != -1:
            for index in range(item_was_at_index, self._size - 1):
                self._storage[index] = self._storage[index + 1]
            self._storage[self._size - 1] = None
            self._size -= 1
        return item_was_at_index != -1

    def insert(self, index, obj):
        self._ensure_capacity()
        
        for position in range(self._size, index, -1):
            self._storage[position] = self._storage[position - 1]

        self._storage[index] = obj
        self._size += 1

    def _ensure_capacity(self):
        if self._size == self._capacity:
            self._resize( 2 * self._capacity )

    def _resize(self, new_capacity):
        new_storage = self._make_array(new_capacity)
        for index in range(self._size):
            new_storage[index] = self._storage[index]
        self._storage = new_storage
        self._capacity = new_capacity

    def _make_array(self, capacity):
        return ( capacity * ctypes.py_object)()