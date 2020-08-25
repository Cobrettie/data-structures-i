"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if BST empty: self.value = value 
        if self.value is None:
            self.value = value

        if value >= self.value: # if passed in value is greater than current checked value
            if self.right is None: # if right side is available
                self.right = BSTNode(value) # number is greater, we add number to the right
            else: # if right side is not available
                self.right.insert(value) # recursive function, basically repeating the above steps

        if value <= self.value: # if passed in value is less than current checked value
            if self.left is None: # if left side is available
                self.left = BSTNode(value) # number is less, we add number to the left
            else: # if left side is not available
                self.left.insert(value) # recursive function, basically repeating the above steps


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if one node in tree, check to see if passed in value equals the only node
        if target == self.value:
            return True

        # if multiple nodes in tree, compare target with root node, then go left or right
        if target > self.value:
            # go right, if self.right == None, we have traversed the list, return false
            if self.right is None:
                return False
            else:
                return self.right.contains(target) # why did returning this statement work, but without the 'return' it does not work??????? o.O

        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        

    # Return the maximum value found in the tree
    def get_max(self):
        # in a BST, the maximum value will always be the bottom-most right value
        current = self
        while (current.right):
            current = current.right        
        return current.value
    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
