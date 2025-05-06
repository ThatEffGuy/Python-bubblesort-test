def bubbleSort(myList):
    moreSwaps = True
    while moreSwaps:
        moreSwaps = False
        for element in range(len(myList) -1):
            if myList[element] > myList[element + 1]:
                moreSwaps = True
                temp = myList[element]
                myList[element]= myList[element + 1]
                myList[element + 1] = temp
        return myList

def testBubbleSort():
    myList = [1, 4, 65, 13, 62, 69, 800, 75, 96]
    print("This is the original list: ", myList)
    sortedList = bubbleSort(myList)
    print("This is the sorted list: ", sortedList)
    print("This is the sorted list: ", sortedList)
    print("This is a test edit via github")

testBubbleSort()

