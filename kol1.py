###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck

#!/usr/bin/env python2.7
import random
import time

class Plane:
	def __init__(self,orien):
		self.orientation=orien

	def turbulation(self):
		self.orientation=random.randrange(0,50)

	def correction(self):
		self.orientation-=0+(self.orientation/2)
				


plane_1=Plane(10)

print(plane_1.orientation)

while(1):
	plane_1.turbulation()
	print('Orientation of plane_1= ', plane_1.orientation)
	plane_1.correction()
	print('After correction, orientation=' , plane_1.orientation)
	time.sleep(3)
	

