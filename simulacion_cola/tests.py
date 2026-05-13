from queue_custom import Queue
from print_task import PrintTask
from printer import Printer


def test_queue():
    q = Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3

    print("Queue FIFO: OK")


def test_print_task():
    task = PrintTask(1, 10, 5)

    assert task.task_id == 1
    assert task.pages == 10
    assert task.arrival_time == 5

    print("PrintTask: OK")


def test_printer():
    printer = Printer(10)

    task = PrintTask(1, 5, 0)

    printer.assign_task(task, 0)

    assert printer.is_busy() is True

    while printer.is_busy():
        printer.tick()

    assert printer.is_busy() is False

    print("Printer: OK")


if __name__ == "__main__":
    test_queue()
    test_print_task()
    test_printer()