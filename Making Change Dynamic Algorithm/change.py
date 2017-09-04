def makeChange(amount, denominations):
    money = [None] * (amount + 1)
    money[0] = 0
    trace = [-1] * (amount + 1)
    coins = [0]*(len(denominations))

    #Build an array representing min coins for each amount 0 to Amount
    for i in range(0, len(denominations)):
        for j in range(1, len(money)):
            if(money[j] == None or money[j] > 1 + money[j - denominations[i]]):
                money[j] = 1 + money[j - denominations[i]]
                trace[j] = i

    #Build the list of number of coins by denomination
    k = amount
    while(k > 0):
        coins[trace[k]] += 1
        k -= denominations[trace[k]]

    results = []
    results.append(money[amount])
    results.append(coins)

    return results






filename="amount.txt"
outfile="change.txt"
f = open(filename, 'r')
w = open(outfile, 'w')

for line in f:
    denomList = list(map(int, line.split()))
    amount = int(f.readline())

    #write the denominations and amount to a file
    printDenom= " ".join(str(item) for item in denomList) + "\n"
    w.write(printDenom)
    w.write(str(amount) + "\n")
    results = makeChange(amount, denomList)

    printList = results[1]
    #write the
    printStr = " ".join(str(item) for item in printList) + "\n"
    w.write(printStr)
    w.write(str(results[0]) + "\n")





f.close()
w.close()