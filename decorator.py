def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def sleep(func):

    sleeping = func("i am sleeping, don't shout plz !!!")

    print(sleeping)

sleep(shout)
sleep(whisper)