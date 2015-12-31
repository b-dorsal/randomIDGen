class Person(object):
	fName = ""	#first name, required for init
	lName = ""	#last name, required for init
	age = 0		#current age, required for init
	POB = "unknown"	#place of birth, optional
	job = "unemployed" #current job, optional
	fullName = ""

	#Initializer, learn the diff. between this and constructor soon.
	def __init__(self, f, l, a):
		self.fName = f
		self.lName = l
		self.age = a
		self.fullName = self.fName, self.lName

	def printName(self):
		print self.fName, " ", self.lName

	def printAge(self):
		print self.age

	def addAge(self): #A persons age cannot simply change, this prevents fraud in the Person storage system ;)
		self.age = self.age + 1

	def updatePOB(self, pob):
		old = self.POB
		self.POB = pob
		print "The POB of ", self.fullName, " has been changed from, ", old, " to, ", self.POB

	def printPOB(self):
		print self.POB
		
	def updateJob(self, job):
		old = self.job
		self.job = job
		print self.fullName, "s job has been changed from, ", old, " to, ", self.job

	def printJob(self):
		print self.job



first = Person("Steve", "DingDong", 45)

first.printName()	#output name
first.printAge()	#output age

first.addAge()		#increment age
first.printAge()	#output age

first.printPOB()	#output birthplace
first.updatePOB("New York, NY") #change birthplace
first.printPOB()	#output birthplace

first.printJob()	#output job
first.updateJob("pilot") #change job
first.printJob()	#output job



