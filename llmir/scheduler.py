from __future__ import annotations

from threading import Thread
from typing import Callable, List


class Scheduler:
    """Very simple scheduler for running tasks sequentially."""

    def __init__(self) -> None:
        self.tasks: List[Callable[[], None]] = []

    def schedule(self, task: Callable[[], None]) -> None:
        self.tasks.append(task)

    def run(self) -> None:
        for task in self.tasks:
            t = Thread(target=task)
            t.start()
            t.join()
