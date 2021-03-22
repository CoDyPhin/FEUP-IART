import time

class Stats:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.moves = 0
        self.timestring = "{hours:02d}:{minutes:02d}:{seconds:02d}".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds)
        self.starttime = None

    def start_timer(self):
        self.starttime = int(time.time())

    def update_timer(self):
        timer = int(time.time())-self.starttime
        self.seconds = timer % 60
        self.minutes = timer // 60 % 60
        self.hours = timer // 3600
        self.timestring = "{hours:02d}:{minutes:02d}:{seconds:02d}".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds)

def timer():
    while True:
        stats.update_timer()
        print(stats.timestring)
