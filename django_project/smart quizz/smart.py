import os
import pyttsx3 
import pyfiglet
from colorama import init
init()
from colorama import Fore, Back, Style
  
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices") 
engine.setProperty("voice", voices[1].id)

def smart(value):
	print(value)


def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def ques1():
	print(Fore.YELLOW + "Question 1: What is E-Kaksha?" + Fore.WHITE)
	speak("Question 1: What is E-Kaksha?")
	print(Fore.BLUE + "(a): A platform to provide virtual education")
	speak("(a): A platform to provide virtual education")
	print("(b): A platform to provide virtual entertainment")
	speak("(b): A platform to provide virtual entertainment")
	print("(c): A platform to have chat among your friends")
	speak("(c): A platform to have chat among your friends")
	print("(d): A platform to provide virtual singing" + Fore.WHITE)
	speak("(d): A platform to provide virtual singing")

def answer1(ans):
	if( ans == "a"):
		print(Fore.GREEN + "Correct Answer")
		speak("Correct Answer")
	elif( ans == "b" or ans == "c" or ans == "d" ):
		print(Fore.RED + "Incorrect Answer")
		speak("Incorrect Answer")

def ques2():
	print("\n")
	print(Fore.YELLOW + "Question 2: What are features of E-Kaksha?")
	speak("Question 2: What are features of E-Kaksha?")
	print(Fore.BLUE + "(a): Smart Quiz/Test")
	speak("(a): Smart Quiz/Test")
	print("(b): Discipline Monitor and Smart WhiteBoard")
	speak("(b): Discipline Monitor and Smart WhiteBoard")
	print("(c): Automatic Attendance and Fixed Window")
	speak("(c): Automatic Attendance and Fixed Window")
	print("(d): All of the above" + Fore.WHITE)
	speak("(d): All of the above")	
		
def answer2(ans):
	if( ans == "d"):
		print(Fore.GREEN + "Correct Answer")
		speak("Correct Answer")
	elif( ans == "b" or ans == "c" or ans == "a" ):
		print(Fore.RED + "Incorrect Answer")
		speak("Incorrect Answer")

def ques3():
	print("\n")
	print(Fore.YELLOW + "Question 3: What is HopHacks?")
	speak("Question 3: What is HopHacks?")
	print(Fore.BLUE + "(a): HopHacks is the bi-annual gaming event hosted at Johns Hopkins University in Baltimore, Maryland.")
	speak("(a): HopHacks is the bi-annual gaming event hosted at Johns Hopkins University in Baltimore, Maryland.")
	print("(b): HopHacks is the bi-annual hackathon hosted at Johns Hopkins University in Baltimore, Maryland.")
	speak("(b): HopHacks is the bi-annual hackathon hosted at Johns Hopkins University in Baltimore, Maryland.")
	print("(c): HopHacks is the bi-annual webinar on tech hosted at Johns Hopkins University in Baltimore, Maryland.")
	speak("(c): HopHacks is the bi-annual webinar on tech hosted at Johns Hopkins University in Baltimore, Maryland.")
	print("(d): None of the above" + Fore.WHITE)
	speak("(d): None of the above")	
		
def answer3(ans):
	if( ans == "b"):
		print(Fore.GREEN + "Correct Answer")
		speak("Correct Answer")
	elif( ans == "a" or ans == "c" or ans == "d" ):
		print(Fore.RED + "Incorrect Answer")
		speak("Incorrect Answer")


if __name__ == "__main__":
	os.system('cls')
	smart(pyfiglet.figlet_format("                          Smart Quiz"))
	speak("Welcome to Smart Quiz")
	ques1()
	answer1(input("Enter the answer: "))
	ques2()
	answer2(input("Enter the answer: "))
	ques3()
	answer3(input("Enter the answer: "))
	print("\n")
	print("Final Score is  2 point")
	speak("Final Score is 2 point" )
	

