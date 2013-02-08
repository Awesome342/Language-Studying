from pygame import *
from Question import *

class Quiz:
	def __init__(self, name, Q1, Q2):
		self.name = name
		self.Q1 = Q1
		self.Q2 = Q2
	def run(self):
		Name = self.name
		print("This is the " + Name + " Test")
		
		Q1.ask()
		