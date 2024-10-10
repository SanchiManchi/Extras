class Node:
    def __init__(self):
        self.Data = ""
        self.LeftChild = None
        self.RightChild = None


def InitialiseTree():
    global Tree, FreePointer, RootPointer

    Tree = [Node() for i in range(5)]

    for i in range(len(Tree)-1):
        Tree[i].LeftChild = i+1  # The starting position of a Binary Tree is actually a Linked List
        # Right nodes of each tree connected to nothing
    FreePointer = 0
    RootPointer = None


def FindInsertionPoint(NewData):
    global Tree, FreePointer, RootPointer

    Pointer = RootPointer

    while Pointer is not None:
        LastPointer = Pointer
        current = Tree[Pointer].Data

        if current < NewData:
            Direction = "Right"
            Pointer = Tree[Pointer].RightChild
        else:
            Direction = "Left"
            Pointer = Tree[Pointer].LeftChild

    return LastPointer, Direction


def AddNode(NewData):
    global Tree, FreePointer, RootPointer
    if FreePointer is None:
        print("Tree is full. Value cannot be added")

    else:
        NewPointer = FreePointer
        Tree[NewPointer].Data = NewData
        FreePointer = Tree[NewPointer].LeftChild
        Tree[NewPointer].LeftChild = None

        if RootPointer is None:
            RootPointer = NewPointer
        else:
            Pointer, Direction = FindInsertionPoint(NewData)
            if Direction == "Left":
                Tree[Pointer].LeftChild = NewPointer
            else:
                Tree[Pointer].RightChild = NewPointer
    print(f"{NewData} added into Tree")


def SearchTree(Data):
    global Tree, FreePointer, RootPointer

    Pointer = RootPointer

    while True:

        if Pointer is None:
            print(f"{Data} was not found.")
            break
        else:
            current = Tree[Pointer].Data

            if current == Data:
                print(f"{Data} was found at position {Pointer}")
                break

            elif current < Data:
                Direction = "Right"
                Pointer = Tree[Pointer].RightChild

            else:
                Direction = "Left"
                Pointer = Tree[Pointer].LeftChild





def TraverseTree(Pointer = None):
    global Tree, FreePointer, RootPointer

    if RootPointer is None:
        print("Cannot Traverse tree, tree is empty")
        return

    if Pointer is None:
        Pointer = RootPointer

    Left = Tree[Pointer].LeftChild
    Right = Tree[Pointer].RightChild
    Data = Tree[Pointer].Data

    if Left is not None:
        TraverseTree(Left)
    print(Data)
    if Right is not None:
        TraverseTree(Right)


def Test():
    global Tree, FreePointer, RootPointer

    InitialiseTree()

    AddNode("Boothill")
    AddNode("Aventurine")
    AddNode("Sunday")
    AddNode("Kaeya")
    AddNode("Diluc")
    TraverseTree()
    SearchTree("Sunday")
    SearchTree("Albedo")

Test()
