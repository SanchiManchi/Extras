class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    # Function to insert in BST
    def insert(self, DataToInsert):
        # if value is lesser than the value of the parent node
        if DataToInsert < self.data:
            if self.leftChild is not None:
                # if we still need to move towards the left subtree
                self.leftChild.insert(DataToInsert)
            else:
                self.leftChild = Node(DataToInsert)
                return
        # if value is greater than the value of the parent node
        else:
            if self.rightChild is not None:
                # if we still need to move towards the right subtree
                self.rightChild.insert(DataToInsert)
            else:
                self.rightChild = Node(DataToInsert)
                return

    # Function to search in BST
    def search(self, tofind):
        # if value to be searched is found
        if tofind == self.data:
            return str(tofind) + " is found in the BST"
        # if value is lesser than the value of the parent node
        elif tofind < self.data:
            # if we still need to move towards the left subtree
            if self.leftChild is not None:
                return self.leftChild.search(tofind)
            else:
                return str(tofind) + " is not found in the BST"
        # if value is greater than the value of the parent node
        else:
            # if we still need to move towards the right subtree
            if self.rightChild is not None:
                return self.rightChild.search(tofind)
            else:
                return str(tofind) + " is not found in the BST"

    # function to print a BST
    def PrintTree(self):
        if self.leftChild is not None:
            self.leftChild.PrintTree()
        print(self.data)
        if self.rightChild is not None:
            self.rightChild.PrintTree()

# Creating root node
root = Node(27)
# Inserting values in BST
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.PrintTree()
# searching the values
print(root.search(7))
print(root.search(14))

