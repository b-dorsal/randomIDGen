# Operation Description - Brian Dorsey - 2016
#	Loads files from directories.
#	Formats each files data to appear clean and uniform.
#	Produces a random value from each list.
#----------------------------------------------------------------
import random 		#for random number generation.
import os.path		#for file existence checking.

class listsLoader(object):

	#Set directories for each list
	def __init__(self, femaleList, maleList, lastList, homeList):
		#prevents directory changes after object creation

		self.femaleNameList =	self.loadList(femaleList)
		self.maleNameList 	=	self.loadList(maleList)
		self.lastNameList 	=	self.loadList(lastList)
		self.homeStateList 	=	self.loadList(homeList)

		self.formatList(self.femaleNameList)
		self.formatList(self.maleNameList)
		self.formatList(self.lastNameList)

		self.formatListST(self.homeStateList)

		self.gender = "Female" #default, can be changed using functions

	#open file, add each line to each nameList[] directory
	def loadList(self, directory):
		itemList = [] #list... array
		print "Opening File: ", directory

		if os.path.isfile(directory): #if the file is found
			print "Open Successful!"

			with open(directory, 'r') as files:
				print "Loading..."
				itemList = files.readlines()

			if not itemList: #if the list is empty after loading.
				print "Error: File at", directory, "EMPTY, continuing with no data!"
			else: #if it has any data.
				print "Loading Complete."

		else: # if the file is not found
			print "Error: File at", directory, "NOT found, continuing with no data!"

		print ""


		return itemList

	#Removes extra chars from list items, formats as lowercase with uppercase first letter
	def formatList(self, editList):
		for x in range(0, len(editList)):
			editList[x] = editList[x].strip()
			editList[x] = editList[x].lower()
			editList[x] = editList[x].capitalize()
			#print editList[x] #for debug

	#Special format function for the homeState list, States are all caps.
	def formatListST(self, editList):
		for x in range(0, len(editList)):
			editList[x] = editList[x].strip()
			editList[x] = editList[x].upper()

	def getRandomFirstName(self):
		if self.gender == 'Male':
			return self.maleNameList[random.randint(0, len(self.maleNameList) - 1)]

		if self.gender == 'Female':	
			return self.femaleNameList[random.randint(0, len(self.femaleNameList) - 1)]

	def setGender(self, gen):
		self.gender = gen

	def getGender(self):
		return self.gender
	# def setRandomGender(self):
	# 	choice = random.randint(0,1)
	# 	print choice
	# 	if choice == "0":
	# 		self.gender == "male"
	# 	if choice == "1":
	# 		self.gender == "Male"

	def getRandomLastName(self):
		return self.lastNameList[random.randint(0, len(self.lastNameList) - 1)]

	def getRandomHomeState(self):
		return self.homeStateList[random.randint(0, len(self.homeStateList) - 1)]

	def getRandomAge(self):
		return random.randint(1,85)



# TO-DO:
	#1) Find out wtf is wrong with the male list
	#2) fix random gender selector to add male personas