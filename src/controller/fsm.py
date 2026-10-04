"""Primer intento de estados de la maquina.

Vi esto en un video: idle, hay plata, vende, error.
Guardo el estado en un json para no perderlo si cierro el programa.
"""
from enum import Enum, auto
import json
import os

STATE_FILE = "machine_state.json"
PRICES_FILE = "prices.json"

class State(Enum):
    IDLE = auto()
    CREDIT = auto()
    VEND = auto()
    ERROR = auto()
    OUT_OF_SERVICE = auto()

def precios_validos(data):
    """Solo dejo slots con precio entero > 0. Si el json trae basura, no la uso."""
    limpios = {}
    if not isinstance(data, dict):
        return limpios
    for slot, precio in data.items():
        if isinstance(precio, bool) or not isinstance(precio, int):
            continue
        if precio <= 0:
            continue
        limpios[str(slot)] = precio
    return limpios

class VendingMachine:
    def __init__(self):
        self.state = State.IDLE
        self.credit = 0
        self.inventory = {}  # slot -> cantidad
        # precios: si hay prices.json lo uso, si no quedan los fijos de prueba
        self.prices = {"A1": 100, "A2": 150, "B1": 200}
        self._load_prices()
        self._load()

    def _load_prices(self):
        if os.path.exists(PRICES_FILE):
            with open(PRICES_FILE) as f:
                data = json.load(f)
            limpios = precios_validos(data)
            if limpios:
                self.prices = limpios

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
        # si esta rota no acepto plata
        if self.state == State.OUT_OF_SERVICE:
            return False
        # 0, negativo o texto no son un billete: antes restaba credito
        if isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0:
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
        price = self.prices.get(slot_id)
        # sin precio (o precio 0) no vendo: antes salia gratis
        if price is None or price <= 0:
            return False, "no price"
        if self.credit < price:
            return False, "insufficient credit"
        self.inventory[slot_id] = qty - 1
        self.credit -= price
        if self.credit == 0:
            self.state = State.IDLE
        self._save()
        return True, "vended"

    def fault(self, reason):
        self.state = State.ERROR
        self._save()


if __name__ == "__main__":
    vm = VendingMachine()
    print(vm.state, vm.credit, vm.prices)
