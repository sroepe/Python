class Animal(object):
  def __init__(self, name):

    self.name = name
    self.health = 0  #solution started with 100

  def displayHealth(self):
    print "Current Health = " + str(self.health)

  def walk(self):
    print self.name + " is walking!"
    self.health -=1
    print self.health
    return self

  def run(self):
    print self.name + " is running!"
    self.health -=5
    print self.health
    return self

animal1 = Animal("George")

#animal1.walk().walk().walk().run().run().displayHealth()

class Dog(Animal):
  def __init__(self, name):
    super(Dog, self).__init__(name)
    self.health = 150

  def pet(self):
    print d1.name + " is being petted by it's human!"
    self.health += 5
    print self.health
    return self

  def walk(self):
    super(Dog, self).walk()
    #return self
    #print self.health

  def run(self):
    super(Dog, self).run()
    #print self.health

  def displayHealth(self):
    super(Dog, self).displayHealth()
 

d1 = Dog("Fido")

'''
print d1.fly()
d1.walk()
d1.walk()
d1.walk()
d1.run()
d1.run()
d1.pet()
d1.displayHealth()
'''

class Dragon(Animal):
  def __init__(self, name):
    super(Dragon, self).__init__(name)
    self.health = 170

  def fly(self):
    print dr1.name + " is flying!"
    self.health -= 10
    print self.health

  def displayHealth(self):
    super(Dragon, self).displayHealth()
    print "I am a dragon!"
 

dr1 = Dragon("Drac")

#print dr1.fly()
#print dr1.fly()
#print dr1.displayHealth()


class Cat(Animal):
  def __init__(self, name):
    super(Cat, self).__init__(name)
    self.health = 120

  def clean(self):  
    print cat1.name + " is cleaning herself."
    self.health += 5
    print self.health
    return self

  def chase(self):
    print cat1.name + " is chasing a mouse!"
    self.health -= 2
    print self.health
    return self

  def purr(self):
    print cat1.name + " is purring:)"
    self.health +=10
    print self.health
    #return self

  def walk(self):
    super(Cat, self).walk()

  def run(self):
    super(Cat, self).run()

  def displayHealth(self):
    super(Cat, self).displayHealth()
 

cat1 = Cat("Whiskers")

print cat1.name
print cat1.clean().chase().purr()
print cat1.walk()
print cat1.run()
print cat1.displayHealth()


























