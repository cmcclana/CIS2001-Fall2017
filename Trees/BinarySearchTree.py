from LInkedBinaryTrree import *

class BinarySearchTree(LinkedBinaryTree):

    def __init__(self):
        super().__init__()

    def __iter__(self):
        for item in self._in_order():
            yield item

    def _in_order(self, position = None):
        if position is None:
            position = self.root()
        left = self.left(position)
        if left is not None:
            yield self._in_order( left )
        yield position.element()
        right = self.right(position)
        if right is not None:
            yield self._in_order( right )

    def add( self, item ):
        if self._root is None:
            self._root = self.Node(item)
            return True

        else:
            return self._add(item, self._root)

    def _add(self, item, node):
        if item < node.data:
            if node.left is None:
                node.left = self.Node(item, node)
                return True
            else:
                return self._add(item, node.left)
        elif item > node.data:
            if node.right is None:
                node.right = self.Node(item, node)
                return True
            else:
                return self._add(item, node.right)
        else:
            return False

    def remove( self, item ):
        if self._root is None:
            return False
        else:
            return self._remove(item, self.root)

    def _remove(self, item, node):
        if item == node.data:
            p = self.Position(self, node)
            self.delete(p)
            return True
        else:
            if item < node.data:
                if node.left is None:
                    return False
                else:
                    return self._remove(item, node.left)
            elif item > node.data:
                if node.right is None:
                    return False
                else:
                    return self._remove(item, node.right)

bst = BinarySearchTree()
for n in range(50):
    bst.add(n)
