from pygame import *

class Question:
	def __init__(self, Text, Answer1, Answer2, Answer3, correctAnswer):
		self.Text = Text
		self.Answer1 = Answer1
		self.Answer2 = Answer2
		self.Answer3 = Answer3
		self.correctAnswer = correctAnswer
		self.correct = 1
	def ask(self):
		fullQuestion = self.Text + "\n" + self.Answer1 + "\n" + self.Answer2 + "\n" + self.Answer3 + "\n"
		
		if (self.correct == 1):
			enteredAnswer = raw_input(fullQuestion)
			if enteredAnswer == self.correctAnswer:
				print ("Zat's Correct!")
				self.correct = 0
			else:
				print ("Incorrect")		
				self.correct = 1