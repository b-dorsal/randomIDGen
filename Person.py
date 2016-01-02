# Operation Description
#	Creates a person object with the fields...
#		First Name
#		Last Name
#		Age
#		Home US-state
#		Job
#----------------------------------------------------------------

class Person(object):
	fName = ""	#first name, required for init
	lName = ""	#last name, required for init
	age = 0		#current age, required for init
	homeState = "unknown"	#home US-state, optional
	job = "unemployed" #current job, optional
	fullName = ""

	#Initializer, learn the diff. between this and constructor soon.
	def __init__(self, f, l, a, g):
		self.fName = f
		self.lName = l
		self.age = a
		self.gender = g

	def getName(self):
		return self.fName + " " + self.lName

	def getAge(self):
		return self.age

	def addAge(self): #A persons age cannot simply change, this prevents fraud in the Person storage system ;)
		self.age = self.age + 1

	def updateHomeState(self, homeSt):
		old = self.homeState
		self.homeState = homeSt
		#print "The home state of ", self.fullName, " has been changed from, ", old, " to, ", self.homeState

	def getHomeState(self):
		return self.homeState
		
	def updateJob(self, job):
		old = self.job
		self.job = job
		#print self.fullName, "s job has been changed from, ", old, " to, ", self.job

	def getJob(self):
		return self.job

	def getGender(self):
		return self.gender



