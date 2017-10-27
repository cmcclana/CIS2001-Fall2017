class LinkedList:
    def __init__(self):
        self.start_node = Node()
        self.start_node.previous = self.start_node
        self.start_node.next = self.start_node
        self.size = 0

    def add_front(self, item):
        new_node = Node(previous=self.start_node, data=item, next=self.start_node.next)
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self.size += 1

    def add_back(self, item):
        new_node = Node(previous=self.start_node.previous, data=item, next=self.start_node)
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self.size += 1

    def peek_front(self):
        return self.start_node.next.data
    
    def peek_back(self):
        return self.start_node.previous.data

    def remove_front(self):
        item = self.start_node.next.data
        self.start_node.next = self.start_node.next.next
        self.start_node.next.previous = self.start_node
        self.size -= 1
        return item

    def remove_back(self):
        item = self.start_node.previous.data
        self.start_node.previous = self.start_node.previous.previous
        self.start_node.previous.next = self.start_node
        self.size -= 1
        return item

    def __getitem__(self, index):
        return self._get_node_at_index(index).data

    def remove_at(self, index):
        if index >= self.size:
            raise IndexError

        # the get_node_at_index method works for front and back almost just as quick
        #if index == 0:
        #    return self.remove_front()
        #elif index == self.size - 1:
        #    return self.remove_back()
        #else:
        current_node = self._get_node_at_index(index)

        item = current_node.data
        current_node.previous.next = current_node.next
        current_node.next.previous = current_node.previous

        return item

    def _get_node_at_index(self, index):
        if index < self.size / 2:
                current_node = self.head
                for current_index in range(index):
                    current_node = current_node.next
        else:
            current_node = self.tail
            for current_index in range(self.size - 1 - index):
                current_node = current_node.previous

        return current_node
        
    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    class Node:
        def __init__(self, previous = None, data = None, next = None ):
            self.previous = previous
            self.data = data
            self.next = next
