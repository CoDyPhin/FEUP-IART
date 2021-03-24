from datetime import datetime

class Stats:
    def __init__(self):
        self.ms = 0
        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.moves = 0
        self.operations = 0
        self.memoryused = 0
        self.timestring = "{hours:02d}h {minutes:02d}m {seconds:02d}s {milliseconds:03d}ms".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds,  milliseconds=self.ms)
        self.starttime = None

    def start_timer(self):
        self.starttime = datetime.now()

    def update_timer(self):
        timer = datetime.now()-self.starttime
        self.ms = timer.microseconds // 1000
        self.seconds = timer.seconds % 60
        self.minutes = timer.seconds // 60 % 60
        self.hours = timer.seconds // 3600
        self.timestring = "{hours:02d}h {minutes:02d}m {seconds:02d}s {milliseconds:03d}ms".format(hours=self.hours, minutes=self.minutes, seconds=self.seconds, milliseconds=self.ms)

