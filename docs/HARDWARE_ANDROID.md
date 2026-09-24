# Hardware — Linux y Android

Repo: open-vending (core). Los demas repos son distintos. No mezclar codigo.

## Idea

El codigo de este proyecto esta hecho para Linux y Android.

- Linux: corre el Python (FSM, telemetria). Banco, Raspberry Pi, panel industrial con Linux.
- Android: pantalla y kiosco. No es el motor.

Tres cajas: cerebro (Linux o servicio local), UI Android, I/O de maquina.

El FSM (`src/controller/fsm.py`) habla por UART o HTTP local.
No manejar reles desde un Activity.

## Etapas

0. Banco — Linux (PC o Pi) + tablet Android 10" en modo kiosco. USB-serial al FSM.
1. Prototipo — panel PC Android industrial 7–10", 12–24 V, sin bateria, UART x2, GPIO/RS485. Reles optoaislados. O Linux embebido + pantalla Android.
2. Calle — IP65, -10 a 60 C. Pago en terminal PCI aparte (PAX/Nayax). No PCI en el mismo SoC que los reles.

Android Things no existe mas. Usar Android 11+ industrial + lock task (Device Owner).

## Encaje

```
[kiosco Android]     [Linux: fsm.py + events.py]
        \                    /
         \                  /
          UART / HTTP local
                 |
          reles / MDB / sensores
```

Watchdog: si el Python se cae, no vende.
Hora por NTP. eMMC, no solo microSD.

## Que no hacer

- Celular de consumo 24/7 a la intemperie.
- Unificar este repo con snacks/frozen/tcg/tobacco/seedbank.
- Cobrar solo con un browser abierto.

Licencia MIT. Lee `/LEEME_LICENCIA.md`. Sin garantia.
