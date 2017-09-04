filename="data.txt"
outfile="insert.out"
f = open(filename, 'r')
w = open(outfile, 'w')

for line in f:
    intList = list(map(int, line.split()))
    for i in range(1, len(intList)):
        j=i
        while( intList[j] < intList[j - 1] and j >= 1):
            #swap(intList[j], intList[j - 1])
            temp = intList[j]
            intList[j] = intList[j -1]
            intList[j-1] = temp
            j = j - 1
    printStr = " ".join(str(item) for item in intList) + "\n"
    w.write(printStr)

f.close()




