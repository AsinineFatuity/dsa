class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
       self.insert_recursively(current_node=self.root,value_to_insert=new_val)

    def insert_recursively(self,current_node,value_to_insert):
        if value_to_insert > current_node.value:
            if current_node.right:
                self.insert_recursively(current_node=current_node.right,value_to_insert=value_to_insert)
            else:
                current_node.right = Node(value_to_insert)
        else:
            if current_node.left:
                self.insert_recursively(current_node=current_node.left,value_to_insert=value_to_insert)
            else:
                current_node.left = Node(value_to_insert)

    def search(self, find_val):
        return self.search_recursively(current_node=self.root,value_to_search=find_val)
    def search_recursively(self,current_node,value_to_search):
        if value_to_search == current_node.value:
            return True
        elif value_to_search > current_node.value:
            if current_node.right:
               return self.search_recursively(current_node=current_node.right,value_to_search=value_to_search)
            else:
                return False
        elif value_to_search < current_node.value:
            if current_node.left:
               return self.search_recursively(current_node=current_node.left,value_to_search=value_to_search)
            else:
                return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))