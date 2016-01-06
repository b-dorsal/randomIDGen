#Random Identity Creator - Brian Dorsey - 2016
#	Simply outputs a random first and last name, age, home US-state and gender that matched the name.
#	Random.py: loads all data from files, formats data to look clean/uniform, chooses random data.
#	Person.py: creates a Person object that stores that persons identity, used to easily create and manage many persons.
#
#	Purpose/Usage:
#		None other than for learning experience.
#	
#	This file creates 100 random 'Person' objects using data loaded from Random object 'rand'.
#	After creation the identities are printed to the console.
#
#	Known Issues:
#		The male first names database file is currently 
#
#
#-----------------------------------------------------------------------------------------------------------------------
import os.path		#for file existence checking.

from Person import Person
from Random import listsLoader

rand = listsLoader('Data_Files/female_first_names.dat', 'Data_Files/male_first_names.dat', 'Data_Files/last_names.dat', 'Data_Files/home.dat')

people = []


def savePerson(pers, directory):
	print "Saving ", pers.getName(), "'s data to ", directory
	if os.path.isfile(directory): #if the file is found
		print "File already exists, overwriting..."

	files = open(directory, 'w')

	text = "Name: " + pers.getName() + "\n"
	temp = str(text)
	files.write(temp)

	text = "Gender: " + pers.getGender() + "\n"
	temp = str(text)
	files.write(temp)

	text = "Age: " + pers.getGender() + "\n"
	temp = str(text)
	files.write(temp)

	text = "Home: " + pers.getHomeState() + "\n"
	temp = str(text)
	files.write(temp)

	files.close()


#Creates 100 random Persons.
for x in range(0, 100):
	people.append(Person(rand.getRandomFirstName(), rand.getRandomLastName(), rand.getRandomAge(), rand.getGender()))

	people[x].updateHomeState(rand.getRandomHomeState())
#Prints each Person's info to the console.
for y in range(0, 100):
	print
	print "Person #", y + 1
	print "Name: ", people[y].getName()
	print "Gender: ", people[y].getGender()
	print "Age: ", people[y].getAge()
	print "Home: ", people[y].getHomeState()
	print

savePerson(people[99], "/Users/admin/Desktop/person.txt")

