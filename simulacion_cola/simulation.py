import random

from queue_custom import Queue
from print_task import PrintTask
from printer import Printer


class Simulation:

    def __init__(self, duration, ppm):

        self.duration = duration

        self.printer = Printer(ppm)

        self.queue = Queue()

        self.completed_tasks = []

        self.max_queue_size = 0

    def new_task_arrives(self):

        return random.randint(1, 10) == 1

    def run(self):

        task_id = 1

        for current_time in range(self.duration):

            # Llegan trabajos nuevos
            if self.new_task_arrives():

                pages = random.randint(1, 20)

                task = PrintTask(
                    task_id,
                    pages,
                    current_time
                )

                self.queue.enqueue(task)

                task_id += 1

            # Tamaño máximo cola
            if self.queue.size() > self.max_queue_size:

                self.max_queue_size = self.queue.size()

            # Asignar tarea a impresora
            if not self.printer.is_busy():

                if not self.queue.is_empty():

                    next_task = self.queue.dequeue()

                    self.printer.assign_task(
                        next_task,
                        current_time
                    )

            # Avanzar impresión
            finished = self.printer.tick()

            if finished:

                self.completed_tasks.append(finished)

        return self.calculate_metrics()

    def calculate_metrics(self):

        if len(self.completed_tasks) == 0:

            return {
                "total": 0,
                "average_wait": 0,
                "max_wait_task": None,
                "max_queue_size": self.max_queue_size
            }

        waits = []

        for task in self.completed_tasks:

            waits.append(task.waiting_time())

        average_wait = sum(waits) / len(waits)

        max_task = max(
            self.completed_tasks,
            key=lambda t: t.waiting_time()
        )

        return {
            "total": len(self.completed_tasks),
            "average_wait": average_wait,
            "max_wait_task": max_task,
            "max_queue_size": self.max_queue_size
        }