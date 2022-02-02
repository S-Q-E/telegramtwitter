import schedule
import time
from threading import Thread

# Код ...

def geeks():
    print("Get ready")

def run():
    schedule.every(3).seconds.do(geeks)

    while True:
        schedule.run_pending()
        time.sleep(1)

thread = Thread(target=run)
thread.start()