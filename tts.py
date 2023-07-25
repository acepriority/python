import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

text = "My name is Sudaice and I am a Software Engineer."
engine.say(text)

engine.runAndWait()
