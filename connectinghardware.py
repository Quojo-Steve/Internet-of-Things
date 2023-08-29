from gpiozero import Button
from signal import pause
from sendmessage import Iftttnotify

def hello():
    print("hello world")
    notify = Iftttnotify('event_name',"nd55SJlD3exO3aqvyplDRkw8SZuYDy4uS1jiHeW8jBN")
    notify.notify()
    
def text():
    print("text")
    notifytext = Iftttnotify('text_name',"nd55SJlD3exO3aqvyplDRkw8SZuYDy4uS1jiHeW8jBN")
    notifytext.notify(json_data={"Ahmed":1})




button = Button(17)
buzz = Button(26)
button.when_pressed = hello
buzz.when_pressed = text
pause()
# sendmail()