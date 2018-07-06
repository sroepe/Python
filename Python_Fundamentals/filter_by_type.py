# ----  Testing integer, string and list values for type.  ------

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


#Integers - Prints a different message depending on if integer is > or < 100.

def int100(x):
  curr_type = type(x)
  if curr_type is int:
    if x < 100:
      print "That's a small number!"
    else:
      print "That's a large number!"

#Strings - Prints a different message depending on if characters in string are > or < 50.

def str50(x):
  curr_type = type(x)
  if curr_type is str:
    y = len(x)
    print y
    if y < 50:
      print "Short sentence"
    else:
      print "Long sentence"

#Lists - Prints a different message depending on if the number of items in the list is > or < 10.

def list10(x):
  if isinstance(x, list):
    y = len(x)
    print y
    if y < 10:
      print "Short list."
    else: 
      print "Big list!"


#int100()
#str50()
list10(spL)
