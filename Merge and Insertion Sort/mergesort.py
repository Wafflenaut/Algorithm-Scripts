def mergesort(thisList):
    if len(thisList) < 2:
        return thisList
    else:
        middle = int(len(thisList) / 2)
        left = mergesort(thisList[0:middle])
        right = mergesort(thisList[middle:])

        return merge(left, right)

def merge(leftList, rightList):
    #if not len(leftList):
     #   return rightList
   # if not len(rightList):
    #    return leftList

    leftCurrent = 0;
    rightCurrent = 0;
    fullSize = len(leftList) + len(leftList)
    mergedList = []

    while(len(mergedList) < fullSize):
        if(leftList[leftCurrent] < rightList[rightCurrent]):
            mergedList.append(leftList[leftCurrent])
            leftCurrent = leftCurrent + 1
        else:
            mergedList.append(rightList[rightCurrent])
            rightCurrent = rightCurrent + 1

        if(leftCurrent == len(leftList)):
            mergedList.extend(rightList[rightCurrent:])
            break
        elif(rightCurrent == len(rightList)):
            mergedList.extend(leftList[leftCurrent:])
            break

    return mergedList


filename="data.txt"
outfile="merge.out"
f = open(filename, 'r')
w = open(outfile, 'w')


for line in f:
    intList = list(map(int, line.split()))
    intList = mergesort(intList)
    printStr = " ".join(str(item) for item in intList) + "\n"
    w.write(printStr)

f.close()