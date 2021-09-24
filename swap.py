def swap(firstNumber, secondNumber):
    temporary = firstNumber
    firstNumber = secondNumber


def editList(inputList):
    inputList[0] = 1


first = 1
second = 2
swap(first, second)
print(f"first {first}\nsecond {second}")

someList = [0, 0]
print(someList)
editList(someList)
print("after editList: ", someList)
