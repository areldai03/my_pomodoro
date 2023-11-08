import time


class PomodoroTimer:
    def __init__(self, work_time=25, break_time=5, track=4):
        self.work_time = work_time * 60
        self.break_time = break_time * 60
        self.current_time = self.work_time
        self.timer_status = False
        self.break_status = False
        self.current_track = 0
        self.track = track

    def timer(self):
        while self.current_track < self.track:
            while self.current_time > 0 and self.timer_status:
                time.sleep(1)
                self.current_time -= 1
            if self.timer_status:
                self.count_track()
                self.switch_timer()

    def start_timer(self):
        self.timer_status = True

    def stop_timer(self):
        self.timer_status = False

    def reset(self):
        self.break_status = False
        self.current_time = self.work_time
        self.current_track = 0

    def switch_timer(self):
        if self.break_status:
            self.break_status = False
            self.current_time = self.work_time
        else:
            self.break_status = True
            self.current_time = self.break_time

    def count_track(self):
        if not self.break_status:
            self.current_track += 1

    def get_timer_status(self):
        return {
            "current_track": self.current_track,
            "current_time": self.current_time,
            "timer_status": self.timer_status,
            "break_status": self.break_status
        }

    def set_work_time(self, work_time):
        self.work_time = work_time * 60


    def set_break_time(self, break_time):
        self.break_time = break_time * 60


