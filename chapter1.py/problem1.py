import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Optional: Adjust speed and volume
engine.setProperty('rate', 150)    # Speed (words per minute)
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Speak text
engine.say("Hello, this is an offline text to speech example.")
engine.runAndWait()