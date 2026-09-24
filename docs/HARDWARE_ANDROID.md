# Hardware — Android como base

Repo: open-vending (core). Los demas repos son distintos. No mezclar codigo.

## Idea

Android es la pantalla y el kiosco. No es el motor.
Tres cajas: cerebro Android, I/O de maquina, pago/edad.

El FSM de este repo (`src/controller/fsm.py`) habla por UART o HTTP local.
No manejar relés desde un Activity.

## Etapas

0. Banco — tablet Android 10" en modo kiosco, o Pi + Linux. USB-serial al FSM.
1. Prototipo — panel PC Android industrial 7–10", 12–24 V, sin bateria, UART x2, GPIO/RS485. Relés optoaislados.
2. Calle — IP65, −10 a 60 °C. Pago en terminal PCI aparte (PAX/Nayax). No PCI en el mismo SoC que los relés.

Android Things no existe mas. Usar Android 11+ industrial + lock task (Device Owner).

## Encaje con este repo

```
[kiosco Android]
    -> puente UART/HTTP
    -> fsm.py + telemetry/events.py
    -> relés / MDB / sensores
```

Watchdog: si el Python se cae, no vende.
Hora por NTP. eMMC, no solo microSD.

## Que no hacer

- Celular de consumo 24/7 a la intemperie.
- Unificar este repo con snacks/frozen/tcg/tobacco/seedbank.
- Cobrar solo con un browser abierto.

Licencia MIT. Lee `/LEEME_LICENCIA.md`. Sin garantia.
