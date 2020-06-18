from datetime import datetime

def process(input):
    if input == 'bla bla':
        return "i can't heart you"
    if input == 'hello' or input == 'hi':
        return  'hello , I am javis '
    if input == 'bye' or input== 'goodbye':
        return 'bye'
    if input == "what's your name":
        return 'my name is Javis'
    if input == 'what is the time':
        return getTime()
    return 'I am fine thank you'


def getTime():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return "Current Time is " +  current_time



