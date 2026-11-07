"""
JSON Configuration Manager.

Allows reading and writing nested JSON configurations using dot notation (e.g. 'server.port').
"""

import json
from typing import Any


class ConfigManager:
    def __init__(self, data: dict[str, Any]):
        self._data = data

    def get(self, path: str, default: Any = None) -> Any:
        keys = path.split(".")
        current = self._data
        for k in keys:
            if isinstance(current, dict) and k in current:
                current = current[k]
            else:
                return default
        return current

    def set(self, path: str, value: Any) -> None:
        keys = path.split(".")
        current = self._data
        for k in keys[:-1]:
            current = current.setdefault(k, {})
        current[keys[-1]] = value

    def to_json(self) -> str:
        return json.dumps(self._data, indent=2)


if __name__ == "__main__":
    print("=== Config Manager ===")
    cfg = ConfigManager({"database": {"host": "localhost", "port": 5432}})
    print(f"Port: {cfg.get('database.port')}")
    cfg.set("database.port", 5433)
    print(f"Updated JSON:\n{cfg.to_json()}")
