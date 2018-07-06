class Car(object):

  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    if self.price > 10000:
      self.tax = 0.15
    elif self.price < 10000:
      self.tax = 0.12

  def display_all(self):
    print self.price, self.speed, self.fuel, self.mileage, self.tax

Car1 = Car(2000, "35mph", "Full", "15mpg")
Car2 = Car(2000, "5mph", "Not Full", "105mph")
Car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
Car4 = Car(2000, "25mph", "Full", "25mpg")
Car5 = Car(2000, "45mph", "Empty", "25mpg")
Car6 = Car(20000000, "35mph", "Empty", "15mpg")

Car1.display_all()
Car2.display_all()
Car3.display_all()
Car4.display_all()
Car5.display_all()
Car6.display_all()



