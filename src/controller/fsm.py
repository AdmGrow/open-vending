"""Vending machine controller — finite state machine scaffold.

States: IDLE, CREDIT, VEND, ERROR, OUT_OF_SERVICE.
Offline-first. Persists state to a local file.
"""
from enum import Enum, auto
import json
import os

STATE_FILE = "machine_state.json"

class State(Enum):
    IDLE = auto()
    CREDIT = auto()
    VEND = auto()
    ERROR = auto()
    OUT_OF_SERVICE = auto()

class VendingMachine:
    def __init__(self):
        self.state = State.IDLE
        self.credit = 0
        self.inventory = {}  # slot_id -> qty
        self._load()

    def _load(self):
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE) as f:
                data = json.load(f)
            self.state = State[data.get("state", "IDLE")]
            self.credit = data.get("credit", 0)
            self.inventory = data.get("inventory", {})

    def _save(self):
        with open(STATE_FILE, "w") as f:
            json.dump({
                "state": self.state.name,
                "credit": self.credit,
                "inventory": self.inventory,
            }, f)

    def insert_credit(self, amount):
        if self.state == State.OUT_OF_SERVICE:
            return False
        self.credit += amount
        self.state = State.CREDIT
        self._save()
        return True

    def select(self, slot_id):
        if self.state != State.CREDIT:
            return False, "no credit"
        qty = self.inventory.get(slot_id, 0)
        if qty <= 0:
            return False, "out of stock"
        # price lookup omitted in scaffold
        self.inventory[slot_id] = qty - 1
        self.credit = 0
        self.state = State.IDLE
        self._save()
        return True, "vended"

    def fault(self, reason):
        self.state = State.ERROR
        self._save()


if __name__ == "__main__":
    vm = VendingMachine()
    print(vm.state, vm.credit)