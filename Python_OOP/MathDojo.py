class MathDojo(object):
  def __init__(self):
    self.x = 0  
    self.y = 0
    self.sum = 0
    
  def add(self, x, y):  #trouble with just getting output if only 1 integer is entered below
    self.sum += x + y
    print self.sum
    return self

  def subtract(self, x, y):
    self.sum -= x + y
    print self.sum
    return self

  def result(self):
    print "The final value is " + str(self.sum)
    return self

md = MathDojo()
print md.add(2, 4).add(6, 10).subtract(5, 2).result()

#use *args for completing part 2 of this assignment (see Multiple Arguments section)








  

