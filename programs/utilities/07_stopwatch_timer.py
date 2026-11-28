"""
Precision Stopwatch and Lap Timer.

High precision timer using time.perf_counter().
"""

import time


class Stopwatch:
    def __init__(self):
        self._start_time: float | None = None
        self._laps: list[float] = []

    def start(self) -> None:
        self._start_time = time.perf_counter()
        self._laps.clear()

    def lap(self) -> float:
        if self._start_time is None:
            raise RuntimeError("Stopwatch has not been started.")
        current = time.perf_counter()
        elapsed = current - self._start_time
        self._laps.append(elapsed)
        return elapsed

    def get_laps(self) -> list[float]:
        return self._laps.copy()


if __name__ == "__main__":
    print("=== Stopwatch Simulation ===")
    sw = Stopwatch()
    sw.start()
    time.sleep(0.02)
    lap1 = sw.lap()
    time.sleep(0.03)
    lap2 = sw.lap()
    print(f"Lap 1: {lap1 * 1000:.2f} ms")
    print(f"Lap 2: {lap2 * 1000:.2f} ms")
