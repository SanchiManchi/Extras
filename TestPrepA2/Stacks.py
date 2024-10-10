def CreateStack():
    global Stack, TopOfStack
    Stack = [None for i in range(3)]
    TopOfStack = -1


def Push(value):
    global Stack, TopOfStack
    if TopOfStack == -1:
        Stack[0] = value
        TopOfStack = 0
    elif TopOfStack + 1 == len(Stack):
        print("Stack is full, cannot add value.")
    else:
        Stack[TopOfStack + 1] = value
        TopOfStack += 1


def Pop():
    global Stack, TopOfStack
    if TopOfStack == -1:
        print("Stack is empty, cannot pop value.")
    else:
        value = Stack[TopOfStack]
        Stack[TopOfStack] = None
        TopOfStack -= 1
        return value


def DisplayStack():
    print(Stack)


CreateStack()
Push("Boothill")
DisplayStack()
Push("Aventurine")
DisplayStack()
Push("Argenti")
DisplayStack()
Push("Sunday")
DisplayStack()
Pop()
DisplayStack()
Pop()
DisplayStack()
Pop()
DisplayStack()
Pop()
DisplayStack()
Pop()
DisplayStack()
