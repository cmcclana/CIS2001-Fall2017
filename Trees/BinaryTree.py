from Tree import *

class BinaryTree(Tree):

    def right(self, p):
        #return Tree to the right of the current position
        raise NotImplementedError

    def left(self, p):
        # return Tree to the left of the current position
        raise NotImplementedError

    def sibling(self, p):
        # parents other child, or None\
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)