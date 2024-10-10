class Node:  # Every node has what? That's right. Data and a Pointer.
    def __init__(self):
        self.Data = ""  # Don't use private attributes for Linked Lists
        self.Pointer = None


def CreateList():
    global LinkedList, HeadPointer, FreePointer

    LinkedList = [Node() for i in range(10)]  # Creates 10 Node Objects in linked list

    FreePointer = 0  # Nothing in the list so first node free
    HeadPointer = None  # Nothing in the list so no 'start' node (Start node has some value in it)

    for i in range(10 - 1):
        LinkedList[i].Pointer = i + 1  # Pointer is an index value. NOT the actual node value.


def Append(NewData):
    global LinkedList, HeadPointer, FreePointer

    if FreePointer == None:  # LL fixed size! FP must be pointing to Null Node as final Node points to Null.
        print(f"list is full, cannot append {NewData}")
    else:
        NewNodeIndex = FreePointer
        FreePointer = LinkedList[NewNodeIndex].Pointer
        LinkedList[NewNodeIndex].Data = NewData
        LinkedList[NewNodeIndex].Pointer = None

        if HeadPointer is None:  # Basically if LL has no nodes, No HP. This appended node must be first node, thus new HP.
            HeadPointer = NewNodeIndex
        else:
            SearchPointer = HeadPointer

            while SearchPointer is not None:
                LastPointer = SearchPointer
                SearchPointer = LinkedList[SearchPointer].Pointer

            LinkedList[LastPointer].Pointer = NewNodeIndex
        print(f"Data {NewData} added.")


def Prepend(NewData):
    global LinkedList, HeadPointer, FreePointer

    if FreePointer is None:  # LL fixed size! FP must be pointing to Null Node as final Node points to Null.
        print("list is full, cannot append")
    else:
        NewNodeIndex = FreePointer
        FreePointer = LinkedList[NewNodeIndex].Pointer
        LinkedList[NewNodeIndex].Data = NewData
        LinkedList[NewNodeIndex].Pointer = None

        if HeadPointer is None:
            HeadPointer = NewNodeIndex
        else:
            LinkedList[NewNodeIndex].Pointer = HeadPointer
            HeadPointer = NewNodeIndex
    print(f"Prepended {NewData}.")


def Insert(NewData, After):  # Inserts after node After
    global LinkedList, HeadPointer, FreePointer

    if FreePointer is None:  # LL fixed size! FP must be pointing to Null Node as final Node points to Null.
        print("list is full, cannot append")
    elif HeadPointer is None:
        print("No items in Linked List thus cannot insert value.")
    else:
        SearchPointer = HeadPointer
        swap = False
        while SearchPointer is not None:
            if LinkedList[SearchPointer].Data == After:
                swap = True
                break
            SearchPointer = LinkedList[SearchPointer].Pointer
        if swap == False:
            print(f"{After} Node does not exist. Thus cannot insert value")
        else:
            NewNodeIndex = FreePointer
            FreePointer = LinkedList[NewNodeIndex].Pointer
            LinkedList[NewNodeIndex].Data = NewData
            LinkedList[NewNodeIndex].Pointer = LinkedList[SearchPointer].Pointer
            LinkedList[SearchPointer].Pointer = NewNodeIndex

        print("Value has been inserted")


def Delete(DataToDelete):
    global LinkedList, HeadPointer, FreePointer

    if HeadPointer is None:
        print("Linked List is empty thus node cannot be deleted.")
    else:
        SearchPointer = HeadPointer
        swap = False
        while SearchPointer is not None:
            if LinkedList[SearchPointer].Data == DataToDelete:
                swap = True
                break
            LastPointer = SearchPointer
            SearchPointer = LinkedList[SearchPointer].Pointer
        if swap == False:
            print(f"{DataToDelete} Node does not exist. Thus cannot delete value")
        elif SearchPointer == HeadPointer:
            HeadPointer = LinkedList[SearchPointer].Pointer
            LinkedList[SearchPointer].Data = None
            LinkedList[SearchPointer].Pointer = FreePointer
            FreePointer = SearchPointer
        else:
            LinkedList[LastPointer].Pointer = LinkedList[SearchPointer].Pointer
            LinkedList[SearchPointer].Data = None
            LinkedList[SearchPointer].Pointer = FreePointer
            FreePointer = SearchPointer
        print(f"{DataToDelete} has been deleted from linked list.")


def DisplayList():
    SearchPointer = HeadPointer
    while SearchPointer is not None:
        print(LinkedList[SearchPointer].Data)
        SearchPointer = LinkedList[SearchPointer].Pointer


# LINKED LIST IN REVERSE ORDER


def Test():
    CreateList()
    Append("Boothill")
    DisplayList()
    Append("Argenti")
    DisplayList()
    Insert("Aventurine", "Boothill")
    DisplayList()
    Delete("Aventurine")
    DisplayList()


Test()
