class Person(object):

	def __init__(self, f, l, age):
		self.fName = f
		self.lName = l


	def printName():
		print self.fName, " ", self.lName


first = Person("Steve", "DingDong", 45)

print "First:", first.fName
print "Last:", first.lName