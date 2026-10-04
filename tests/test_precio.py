"""Test chico: sin precio no vende, y el credito basura no entra.

Correr desde la raiz del repo:
  python tests/test_precio.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src", "controller"))
from fsm import VendingMachine, State, precios_validos


def test_sin_precio_no_vende():
    vm = VendingMachine()
    vm.inventory = {"C9": 2}
    vm.prices = {"A1": 100}
    vm.state = State.CREDIT
    vm.credit = 500
    ok, msg = vm.select("C9")
    assert ok is False and msg == "no price"
    assert vm.inventory["C9"] == 2 and vm.credit == 500


def test_precio_conocido_descuenta():
    vm = VendingMachine()
    vm.inventory = {"A1": 1}
    vm.prices = {"A1": 100}
    vm.state = State.CREDIT
    vm.credit = 150
    ok, msg = vm.select("A1")
    assert ok is True and msg == "vended"
    assert vm.credit == 50 and vm.inventory["A1"] == 0


def test_precio_negativo_no_entra():
    limpios = precios_validos({"A1": 100, "A2": -5, "B1": 0, "C1": "barato"})
    assert limpios == {"A1": 100}


def test_credito_cero_o_negativo_no_entra():
    vm = VendingMachine()
    vm.credit = 100
    vm.state = State.IDLE
    assert vm.insert_credit(0) is False
    assert vm.insert_credit(-20) is False
    assert vm.credit == 100 and vm.state == State.IDLE
    assert vm.insert_credit(50) is True
    assert vm.credit == 150 and vm.state == State.CREDIT


if __name__ == "__main__":
    test_sin_precio_no_vende()
    test_precio_conocido_descuenta()
    test_precio_negativo_no_entra()
    test_credito_cero_o_negativo_no_entra()
    print("ok")
