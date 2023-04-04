import pyttsx3 as tts
#Initializing the pyttsx3 library
engine = tts.init()

user_input = input("Enter the sentence you want to convert in speech:")
engine.say(user_input)
engine.runAndWait()



