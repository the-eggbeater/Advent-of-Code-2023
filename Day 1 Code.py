f = open("input.txt","r")
wordlist = []

for line in f:
    wordlist.append(line)

summ = 0
first = 0
last = 0

for word in wordlist:
    count1 = 0
    count2 = 0

    while count1<1:
        for char in word:
            if char in ["0","1","2","3","4","5","6","7","8","9"]:
                first = char
                count1 = count1+1

    rword = word[::-1]

    while count2<1:
        for char in rword:
            if char in ["0","1","2","3","4","5","6","7","8","9"]:
                last = char
                count2 = count2+1
    

    summ = summ + int(last+first)
    

print(summ)
