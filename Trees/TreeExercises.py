from BinarySearchTree import *


def print_pre_order_position(tree, position):
    print( position.element() )
    for child in tree.children(position):
        print_pre_order_position(tree, child)

def print_post_order_position(tree, position):
    for child in tree.children(position):
        print_post_order_position(tree, child)
    print(position.element())

def is_bst(tree, position):
    left = tree.left(position)
    right = tree.right(position)
    if left is not None:
        if left.element() > position.element():
            return False
        if not is_bst(tree, left):
            return False
    if right is not None:
        if right.element < position.element():
            return False
        if not is_bst(tree, right):
            return False
    return True

def print_tree(tree):
    print_position(tree, tree.root())

def _print_bst_in_order(list, tree, position):
    left = tree.left(position)
    if left is not None:
        _print_bst_in_order(in_order_list, tree, left)
    list.append(position.element())
    right = tree.right(position)
    if right is not None:
        _print_bst_in_order(in_order_list, tree, right)

def print_bst_in_order(in_order_list, tree):
    _print_bst_in_order(in_order_list, tree, tree.root())

bTree = BinarySearchTree()

position = bTree.add(15)
bTree.add(12)
bTree.add(16)
bTree.add(14)
bTree.add(10)
bTree.add(11)
bTree.add(13)
bTree.add(18)
bTree.add(17)

linkedTree = LinkedBinaryTree()
linkedTree.add_root(15)
root = linkedTree.root()
linkedTree.add_left(root, 13)

left = linkedTree.left(root)
linkedTree.add_right(left, 14)
right = linkedTree.right(left)
linkedTree.add_left(right, 12)


in_order_list = []
print_bst_in_order(in_order_list, linkedTree)
current = in_order_list[0]
for index in range(1, len(in_order_list)):
    if current > in_order_list[index]:
        print("NOT BST")
    current = in_order_list[index]


#print_pre_order_position(bTree, bTree.root())
#print()
#print_post_order_position(bTree, bTree.root())


for item in bTree._in_order():
    print(item)
