class PrintTask:

    def __init__(self, task_id, pages, arrival_time):

        if pages <= 0:
            raise ValueError("Cantidad de páginas inválida")

        self.task_id = task_id
        self.pages = pages
        self.arrival_time = arrival_time

        self.start_time = None

    def waiting_time(self):

        if self.start_time is None:
            return 0

        return self.start_time - self.arrival_time