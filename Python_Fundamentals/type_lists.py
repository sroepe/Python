list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [1,2,3,4,5]
list3 = ["Spiff", "Moon", "Robot"]

def typeList(myList):

  newstr = ""
  totalint = 0

  for value in myList:
    if isinstance(value, int) or isinstance(value, float):
      totalint += value
    elif isinstance(value, str):
      newstr += value
    
  if newstr and totalint:
    print "The list you entered is of MIXED type."
    print "String:", newstr
    print "Sum:", totalint

  elif newstr:
    print "The list you entered is of STRING type."
    print "String:", newstr

  else:
    print "The list you entered is of INTEGER type."
    print "Sum:", totalint  
    
print typeList(list1)
print typeList(list2)
print typeList(list3)

    




