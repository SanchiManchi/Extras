from random import randint


# RECURSIVE BINARY TREE
def binary_search(array, low, high, tofind):
    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if array[mid] == tofind:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif array[mid] > tofind:
            return binary_search(array, low, mid - 1, tofind)

        # Else the element can only be present in right subarray
        else:
            return binary_search(array, mid + 1, high, tofind)

    else:
        # Element is not present in the array
        return -1


array = [randint(1, 20) for i in range(10)]
array.sort()
print(array)

result = binary_search(array, 0, len(array) - 1, 6)

if result == -1:
    print("Element not in array")
else:
    print(f"Element is present at {result}")


# FACTORIAL
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)


# FIBONACCI
def fibonacci(nth):
    if nth == 0:
        return 0
    if nth == 1:
        return 1
    return fibonacci(nth - 1) + fibonacci(nth - 2)


# LARGEST COMMON MULTIPLE
def LCM(x, y):
    if y == 0:
        return x
    return LCM(y, x % y)


# TOWERS OF HANOI
def TOH(n, source, dest, aux):
    if n == 1:
        print(f"Disk 1: {source} --> {dest}")
        return
    TOH(n - 1, source, aux, dest)
    print(f"Disk {n}: {source} --> {dest} ")
    TOH(n - 1, aux, dest, source)


n = int(input("How many blocks are on the stack?"))
TOH(n, 'A', 'B', 'C')


# GREY CODE
def GrayCode(n):
    def get_gray_codes(n):
        """Return n-bit Gray code in a list."""
        if n == 0:
            return ['']
        first_half = get_gray_codes(n - 1)
        second_half = first_half.copy()

        first_half = ['0' + code for code in first_half]
        second_half = ['1' + code for code in reversed(second_half)]

        return first_half + second_half

    n = int(input('Enter the number of bits: '))
    codes = get_gray_codes(n)
    print('All {}-bit Gray Codes:'.format(n))
    print(codes)


# RPN CALCULATOR
print("yo")


# COMPUTE THE SUM
def SumRecursive(array, num):
    if num <= 0:
        return 0
    else:
        return SumRecursive(array, num - 1) + array[num - 1]
