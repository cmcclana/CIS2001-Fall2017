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
        if p._node.parent is p._node
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
        pass

    def add_left(self, p, data):
        pass

    def add_right(self, p, data):
        pass

    def replace(self, p, data):
        pass

    def delete(self, p):
        pass

    def attach(self, t1, t2):
        pass
