def CreateQueue():
    global Queue, HeadPointer, TailPointer
    Queue = [None for i in range(3)]
    HeadPointer = 0
    TailPointer = 0


def EnQueue(value):
    global Queue, HeadPointer, TailPointer

    if HeadPointer == TailPointer and Queue[HeadPointer] is not None:
        print("Queue is full. Cannot Enqueue new value.")
    else:
        if TailPointer == 0:
            Queue[TailPointer] = value
            TailPointer = len(Queue) - 1
        else:
            Queue[TailPointer] = value
            TailPointer -= 1
        print(f"{value} queued")


def DeQueue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == TailPointer and Queue[HeadPointer] is None:
        print("Queue is empty. Cannot Dequeue value.")
    else:
        value = Queue[HeadPointer]
        Queue[HeadPointer] = None
        if HeadPointer == 0:
            HeadPointer = len(Queue) - 1
        else:
            HeadPointer -= 1
        print(f"{value} dequeued")
    return value


def DisplayQueue():
    global Queue, HeadPointer, TailPointer
    print(Queue)

CreateQueue()
EnQueue("Boothill")
DisplayQueue()
EnQueue("Aventurine")
DisplayQueue()
EnQueue("Argenti")
DisplayQueue()
EnQueue("Sunday")
DisplayQueue()
DeQueue()
DisplayQueue()
DeQueue()
DisplayQueue()
DeQueue()
DisplayQueue()
DeQueue()
DisplayQueue()
