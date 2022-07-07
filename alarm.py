import datetime
import playsound 
file = "ceza.mp3"
alarmhour = int(input("hour"))
alarmmin = int(input("minute"))
alarmam = input("am/pm")

if alarmam == "am":
    alarmhour +=12

while True:
    if alarmhour == datetime.datetime.now().hour and alarmmin == datetime.datetime.now().minute:
        print("playing")
        playsound.playsound(file)
        break
