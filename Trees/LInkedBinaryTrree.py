from BinaryTree import *

class LinkedBinaryTree(BinaryTree):

    class Node():
        def __init__(self, data, parent=None, left=None, right=None):
            self.data = data
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.data

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this list")
        if p._node.parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        #return self.Position(self, node) if node is not None else None
        if node is None:
            return None
        else:
            return self.Position(self, node)

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node.left is not None:
            count += 1
        if node.right is not None:
            count += 1
        return count

    def add_root(self, data):
        if self._root is not None:
            raise ValueError
        self._size = 1
        self._root = self.Node(data)
        return self._make_position(self._root)

    def add_left(self, p, data):
        node = self._validate(p)
        if node.left is not None:
            raise ValueError
        self._size += 1
        node.left = self.Node(data, node)
        return self._make_position(node.left)

    def add_right(self, p, data):
        node = self._validate(p)
        if node.right is not None:
            raise ValueError
        self._size += 1
        node.right = self.Node(data, node)
        return self._make_position(node.right)

    def replace(self, p, data):
        node = self._validate(p)
        old = node.data
        node.data = data
        return old

    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError
        child = node.left if node.left else node.right

        if child is not None:
            child.parent = node.parent
        if node is self._root:
            self._root = child
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        node.parent = node
        return node.data

    def attach(self, p, t1, t2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError
        if not type(self) is type(t1) is type(t2):
            raise TypeError
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root.parent = node
            node.left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root.parent = node
            node.right = t1._root
            t2._root = None
            t2._size = 0
