class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(tree.root, find_val)


    def print_tree(self,order):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        print_order_choices = {"in":self.inorder_print(start=tree.root,traversal="")[:-1],"pre":self.preorder_print(start=tree.root,traversal="")[:-1],
        "post":self.postorder_print(start=tree.root,traversal="")[:-1]}
        #remove the last trailing - by slicing
        return print_order_choices.get(order)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if find_val == start.value:
                return True
            else:
                return self.preorder_search(start=start.left,find_val=find_val) or self.preorder_search(start=start.right,find_val=find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start=start.left,traversal=traversal)
            traversal = self.preorder_print(start=start.right,traversal=traversal)
        return traversal
    def inorder_print(self,start,traversal):
        if start:
            traversal = self.inorder_print(start=start.left,traversal=traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_print(start=start.right,traversal=traversal)
        return traversal
    def postorder_print(self,start,traversal):
        if start:
            traversal = self.postorder_print(start=start.left,traversal=traversal)
            traversal = self.postorder_print(start=start.right,traversal=traversal)
            traversal += str(start.value) + "-"
        return traversal
    



# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3 (pre order)
print ("Pre Order: "+tree.print_tree(order="pre"))
# Should be 4-2-5-1-3 (in order)
print ("In Order: "+tree.print_tree(order="in"))
# Should be 4-5-2-3-1 (post order)
print ("Post Order: "+tree.print_tree(order="post"))