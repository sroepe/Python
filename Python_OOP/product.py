class Product(object):
  def __init__(self, price, name, weight, brand):
    self.price = price
    self.name = name   
    self.weight = weight
    self.brand = brand
    self.status = "for sale"
    self.tax = 0

  def displayinfo(self):
    print "Price ($):" + str(self.price)
    print "Item Name:" + self.name
    print "Weight:" + str(self.weight)
    print "Brand:" + self.brand
    print "Status:" + self.status
    return self


  def sell(self):
    self.status = "sold"
    return "sold"


  def addtax(self, t):
    self.tax += t    
    self.price += self.tax
    return "Total price with tax is $" + str(self.price)

  def retprod(self, r):
    
    if r == "defective":
      self.status = "defective"
      self.price = 0

    elif r == "like new":
      self.status = "for sale"

    elif r == "open box":
      self.status = "used"
      self.price *= .80

    print self.status
    print self.price


bev1 = Product(3, "cola", 1, "Coca-Cola")
bev2 = Product(2, "water", 2, "Arrowhead")
bev3 = Product(10, "wine", 1, "Charles Shaw")
bev4 = Product(8, "beer", 3, "Budweiser")

print bev2.sell()
print bev1.addtax(.08)
print bev3.retprod("open box")

bev1.displayinfo()
bev2.displayinfo()
bev3.displayinfo()
bev4.displayinfo()












