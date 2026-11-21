"""
Custom Logger Utility.

Formats log events with ISO UTC timestamps and severity labels.
"""

from datetime import datetime, timezone


class SimpleLogger:
    LEVELS = {"DEBUG": 10, "INFO": 20, "WARNING": 30, "ERROR": 40}

    def __init__(self, min_level: str = "INFO"):
        self.min_level_val = self.LEVELS.get(min_level.upper(), 20)

    def _log(self, level: str, message: str) -> None:
        if self.LEVELS.get(level, 0) >= self.min_level_val:
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
            print(f"[{ts}] [{level:7s}] {message}")

    def info(self, msg: str) -> None:
        self._log("INFO", msg)

    def warning(self, msg: str) -> None:
        self._log("WARNING", msg)

    def error(self, msg: str) -> None:
        self._log("ERROR", msg)


if __name__ == "__main__":
    print("=== Simple Logger ===")
    logger = SimpleLogger(min_level="INFO")
    logger.info("Bot workflow started.")
    logger.warning("Network latency detected: retrying.")
    logger.error("Failed to fetch remote asset.")
