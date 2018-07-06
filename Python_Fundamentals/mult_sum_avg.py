#Multiples - Part 1 : prints odd number -> 1000
def printrange():
    for count in range (1, 1000, 2):
        print count
printrange()

#Multiples - Part 2 : print mult of 5 from 5 -> 1,000,000
def mult5():
for count in range (5, 1000001, 5):
    print count
mult5()

#Sum List - Prints sum of all values in a list
def sumlist():
    sumList = [1, 2, 5, 10, 255, 3]
    sum = 0
    for i in sumList:
        sum += i
    print sum
sumlist()

#Average List - Prints average of the values in a list
def myAvg():
    myAvg = [1, 2, 5, 10, 255, 3]
    sum = 0
    for i in myAvg:
        sum += i
        avg = sum/len(myAvg)
    print avg
myAvg()



