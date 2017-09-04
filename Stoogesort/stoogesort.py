import math

def stoogeSort(thisList):

    if(len(thisList) == 2 and thisList[0] > thisList[1]):
        thisList[0], thisList[1] = thisList[1], thisList[0]
        return thisList
    elif(len(thisList) > 2):
        tempList = []
        ceiling = math.ceil((len(thisList) * 2) / 3)
        tempList = stoogeSort(thisList[0:ceiling])
        tempList.extend(thisList[ceiling:])
        thisList = tempList[0:]
        tempList = stoogeSort(thisList[len(thisList) - (ceiling):])
        thisList = thisList[0:len(thisList) - ceiling]
        thisList.extend(tempList)
        tempList = stoogeSort(thisList[0:ceiling])
        tempList.extend(thisList[ceiling:])
        return tempList

    return thisList


filename="data.txt"
outfile="stooge.out"
f = open(filename, 'r')
w = open(outfile, 'w')

for line in f:
    stoogeList = list(map(int, line.split()))
    stoogeList = stoogeSort(stoogeList)
    printStr = " ".join(str(item) for item in stoogeList) + "\n"
    w.write(printStr)





f.close()
w.close()