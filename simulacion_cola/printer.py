class Printer:

    def __init__(self, pages_per_minute):

        self.pages_per_minute = pages_per_minute

        self.current_task = None

        self.time_remaining = 0

    def is_busy(self):

        return self.current_task is not None

    def assign_task(self, task, current_time):

        self.current_task = task

        task.start_time = current_time

        self.time_remaining = task.pages * 2

    def tick(self):

        finished_task = None

        if self.current_task:

            self.time_remaining -= 1

            if self.time_remaining <= 0:

                finished_task = self.current_task

                self.current_task = None

        return finished_task