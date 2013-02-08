from Question import *
import random
random.seed()

print ("This is the Italian Test!!\n")

Q1 = Question("What does this mean? 'Come si puo vivere con te stesso?'", "1. What do you want?", "2. How can you live with yourself?", "3. Are you okay?", "2")
Q2 = Question("How do you say 'SHUT UP'?", "1. Sta' Zitto", "2. Callar", "3. Silentu", "1")
Q3 = Question("What Language is this in? 'Ich bin genial'", "1. German", "2. Esperanto", "3. Russian", "1")
Q4 = Question("What does this mean? 'Ego sum angelus mortis'", "1. I am EPIC", "2. I can do anything", "3. I am the angel of death", "3")
Q5 = Question("How do you say 'ILIKEPIE' in LATIN?", "1. Ego quasi pastillus", "2. Ich mag pie", "3. Mi Sastas kukajo", "1")

QuestionInt = random.randint(0, 4)


Q1.ask()

QuestionInt = random.randint(0, 4)

if Q1.correct == 0:
	Q2.ask()
	
QuestionInt = random.randint(0, 4)
	
if Q2.correct == 0:
	Q3.ask()
	
QuestionInt = random.randint(0, 4)
	
if Q3.correct == 0:
	Q4.ask()
	
if Q4.correct == 0:
	Q5.ask()
QuestionInt = random.randint(0, 4)