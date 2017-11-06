from BinarySearchTree import *


def print_position(tree, position):
    print( position.element() )
    for child in tree.children(position):
        print_position(tree, child)

def print_tree(tree):
    print_position(tree, tree.root())




bTree = BinarySearchTree()

position = bTree.add(50)
bTree.add(40)
bTree.add( 60)
bTree.add(20)
bTree.add(100)

print_tree(bTree)
