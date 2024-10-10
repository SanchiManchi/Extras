from random import randint

ArrayToSort = [randint(1, 20) for x in range(10)]


def BubbleSort(array):
    top = len(array)
    for i in range(0, len(array)):  # Outer loop. Dictates how many 'loops' will be made
        swap = False
        for j in range(0, top - 1):  # Inner loop. Dictates how many comparisons will be made and till where
            if array[j + 1] < array[j]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swap = True
        top -= 1  # Top decremented outside of Inner loop.
        if swap == False:
            break
    print(array)


def InsertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while key < array[j] and j >= 0:
            array[j + 1] = array[j]  # Value's moving up so that bottom 2 values duplicated
            j -= 1
        array[j + 1] = key  # This was the value at the top, now she's at the bottom.
    print(array)  # j+1 outside the loop is actually at the same value as j bcus it's been subtracted by one
    # more time


def BinarySeachAsc(array, tofind):
    low = 0
    top = len(array)

    while True:
        current = (top + low) // 2      # 1. Find value for current
        if low >= top:                  # 2. Check if value in list w/ low >= top. If yes, break.
            print("Value not in list")
            break
        elif array[current] == tofind:  # 3. Check is value to find == current. If yes, break.
            print(f"Found {tofind} at index {array.index(tofind)} in array")
            break
        elif tofind < array[current]:  # 4. Check is value to find < current
            top = current - 1
        elif tofind > array[current]:  # 3. Check is value to find > current
            low = current + 1


BubbleSort(ArrayToSort)
InsertionSort(ArrayToSort)
BinarySeachAsc(ArrayToSort, 3)
