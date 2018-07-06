class Bike(object):
  def __init__(self, price, max_speed):
    self.price = price
    self.max_speed = max_speed
    self.miles = 0

#print Schwinn.price
#print Huffy.max_speed
#print Diamondback.price
  def displayinfo(self):
    print "Price ($):" + str(self.price)
    print "Maximum Speed:" + str(self.max_speed)
    print "Total Miles:" + str(self.miles)
    return self

  def ride(self):
    print "Riding"
    self.miles += 10
    print "Total Miles:" + str(self.miles)
    return self

  def reverse(self):
    print "Reversing"
    if self.miles < 0:
      print "You cannot reverse! You are out of miles!"
    else:
      self.miles -= 5
      print "Total Miles:" + str(self.miles)
    return self
 
Schwinn = Bike(150, 20)
Huffy = Bike(75, 15)
Diamondback = Bike(250, 30)

Schwinn.ride().ride().ride().reverse().displayinfo()
Huffy.ride().ride().reverse().reverse().displayinfo()
Diamondback.reverse().reverse().reverse().displayinfo()


























  









  