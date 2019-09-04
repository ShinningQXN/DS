# class Element:
# 	def accept(IVisitor visitor):
# 		pass
# 	def printName():
# 		pass

# class ComputerMouse(Element):
# 	def accept(Mouse):


# class IVisitor:
# 	def __visit__()
import random

class Flower(object):
	def accept(self, visitor):
		visitor.visit(self)
	def pollinate(self, pollinator):
		print(self, "pollinated by", pollinator)
	def eat(self, eater):
		print(self, "eaten by", eater)
	def __str__(self):
		return self.__class__.__name__


class Gladiolus(Flower): pass
class Runuculus(Flower): pass
class Chrysanthemum(Flower): pass

class Visitor:
	def __str__(self):
		return self.__class__.__name__


class Bug(Visitor): pass
class Pollinator(Bug): pass
class Predator(Bug): pass

class Bee(Pollinator):
	def visit(self, flower):
		flower.pollinate(self)

class Worm(Predator):
	def visit(self, flower):
		flower.eat(self)

class Fly(Predator):
	def visit(self, flower):
		flower.pollinate(self)

def FlowerGen(n):
	flowers = Flower.__subclasses__()
	for i in range(n):
		yield random.choice(flowers)()

bee = Bee()
worm = Worm()
fly = Fly()

for flower in FlowerGen(10):
	flower.accept(bee)
	flower.accept(fly)
	flower.accept(worm)
