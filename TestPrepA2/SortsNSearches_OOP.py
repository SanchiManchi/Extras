from random import randint


class LinearSearch:
    def __init__(self):
        self._list = []
        self._element = 0

    def Constructor(self, array, tofind):
        self._list = array
        self._element = tofind

    def Search(self):
        found = False
        for i in self._list:
            if self._element == i:
                print(f"Found value {self._element} at index {self._list.index(self._element)}")
                found = True
                break
        if found == False:
            print(f"Value {self._element} not found.")


ArrayToSort = [randint(1, 20) for x in range(10)]
print(ArrayToSort)

value_finder = LinearSearch()
value_finder.Constructor(ArrayToSort, 3)
value_finder.Search()


class BubbleSort:
    def __init__(self):
        self._list = []

    def Constructor(self, array):
        self._list = array

    def Sort(self):
        top = len(self._list)
        for i in range(0, len(self._list)):  # Outer loop. Dictates how many 'loops' will be made
            swap = False
            for j in range(0, top - 1):  # Inner loop. Dictates how many comparisons will be made and till where
                if self._list[j + 1] < self._list[j]:
                    temp = self._list[j]
                    self._list[j] = self._list[j + 1]
                    self._list[j + 1] = temp
                    swap = True
            top -= 1  # Top decremented outside of Inner loop.
            if swap == False:
                break
        print(self._list)


value_finder = BubbleSort()
value_finder.Constructor(ArrayToSort)
value_finder.Sort()
