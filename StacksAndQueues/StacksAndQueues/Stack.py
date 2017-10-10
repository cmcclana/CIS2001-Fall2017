class Stack():
    def __init__(self):
        self._data = []
    
    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def peek(self):
        return self._data[ len(self._data) - 1]

    def pop(self):
       return self._data.pop()

    def __len__(self):
       return len(self._data)


