import pyttsx3
import os
pyttsx3.speak("Welcome to my tools")
while True:
	print("Chat with me about your requirements:", end='')
	p= input()
 
	if(("run" in p)or ("execute" in p)) and ("chrome" in p):
		os.system("chrome")
	elif(("run" in p) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
		os.system("notepad")
	elif ("exit" in p) or ("stop" in p):
		break
	
	else:
		print("Dont support")
