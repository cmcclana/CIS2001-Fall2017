from LInkedBinaryTrree import *


def print_position(tree, position):
    print( position.element() )
    for child in tree.children(position):
        print_position(tree, child)

def print_tree(tree):
    print_position(tree, tree.root())




bTree = LinkedBinaryTree()

position = bTree.add_root(50)
left = bTree.add_left(position, 40)
right = bTree.add_right(position, 60)
bTree.add_right(right, 20)
bTree.add_left(left, 100)

print_tree(bTree)
