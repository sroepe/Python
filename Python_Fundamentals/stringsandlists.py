words = "It's Thanksgiving Day.  It's my birthday, too!"
print words 
print words.split()
print words.find("Day")
print words.replace("Day.", "month.")

x = []
print x
x = 2,5,-2,-15,10,100
print x
print min(x)
print max(x)

My_Nums = []
print My_Nums
My_Nums = 5,1,2,3,4,5,6,7,8,9,45
print My_Nums
print My_Nums[0]
print My_Nums[len(My_Nums)-1]
MyNewNums = [My_Nums[0], My_Nums[len(My_Nums)-1]]
print MyNewNums

newList = []
print newList
newList = 19,2,54,-2,7,12,98,32,10,-3,6
print newList
newList = sorted(newList)
print newList
list1 = newList[:len(newList)/2]
list2 = newList[len(newList)/2:]
print newList, list1, list2
newsplitList = [list1]
newsplitList.extend(list2)
print newsplitList



  






