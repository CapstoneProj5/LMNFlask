from utils.scheduler.scheduler import scheduler
import datetime


@scheduler.scheduled_job(trigger="interval", seconds=5)
def say_hi():
    now = datetime.datetime.now().time()
    print("Hi, it is {hour:0>2d}:{min:0>2d}:{sec:0>2d}! I run every {interval} seconds!".format(
        hour=now.hour, min=now.minute, sec=now.second, interval=5))
