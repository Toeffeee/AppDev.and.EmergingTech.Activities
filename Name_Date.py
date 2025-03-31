from datetime import datetime

time = datetime.now()
currentTime = time.strftime("%H:%M")

name = input("What is your name? ")
print("Hello,", name)
print("The current time is", currentTime)