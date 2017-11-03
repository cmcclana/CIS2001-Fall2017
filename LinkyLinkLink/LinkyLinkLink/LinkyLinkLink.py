class LinkedList:
    class Position():
        def  __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.data

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not ( self == other )

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this list")
        if p._node is self.start_node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        if node is self.start_node:
            return None
        return self.Position(self, node)

    def first(self):
        return self._make_position(self.start_node.next)

    def last(self):
        return self._make_position(self.start_node.previous)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.previous)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
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
        return self._make_position(new_node)

    def add_back(self, item):
        new_node = Node(previous=self.start_node.previous, data=item, next=self.start_node)
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        self.size += 1
        return self._make_position(new_node)
    
    def add_before(self, p, item):
        node = self._validate(p)
        new_node = Node(node.previous, item, node)
        new_node.previous.next = new_node
        new_node.next.previous = new_node
        
    def add_before(self, p, item):
        node = self._validate(p)
        new_node = Node(node, item, node.next)
        new_node.previous.next = new_node
        new_node.next.previous = new_node

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
