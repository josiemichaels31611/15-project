import random
import time
messages = ["Someone is watching you.", "I know what you did yesterday", "Your webcam is already on", "Don't turn around", "6767676767"]
i = 0
while i < 10:
    try:
        num = random.randint(0, 5)
        print(messages[num])
    except IndexError:
        print("ERROR: Something is trying to communicate.....")
    finally:
        print("The computer is watching you")
        i +=1
        time.sleep(1)
