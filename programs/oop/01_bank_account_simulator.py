"""
Bank Account Simulator.

Demonstrates OOP encapsulation, validation, and transaction tracking.
"""

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class Transaction:
    type: str
    amount: float
    timestamp: str


class BankAccount:
    """Represents a bank account with safety checks and ledger history."""

    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self._balance = initial_balance
        self._transactions: list[Transaction] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount
        self._record_transaction("DEPOSIT", amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._balance:
            raise ValueError(f"Insufficient funds: available {self._balance:.2f}, requested {amount:.2f}")
        self._balance -= amount
        self._record_transaction("WITHDRAWAL", amount)

    def _record_transaction(self, tx_type: str, amount: float) -> None:
        tx = Transaction(type=tx_type, amount=amount, timestamp=datetime.now(timezone.utc).isoformat())
        self._transactions.append(tx)

    def print_statement(self) -> None:
        print(f"--- Statement for {self.owner} ---")
        for tx in self._transactions:
            print(f"[{tx.timestamp[:19]}] {tx.type:10s}: ${tx.amount:.2f}")
        print(f"Current Balance: ${self._balance:.2f}")


if __name__ == "__main__":
    print("=== Bank Account Simulation ===")
    acc = BankAccount("Dhanyasree", 500.0)
    acc.deposit(250.0)
    acc.withdraw(100.0)
    acc.print_statement()
