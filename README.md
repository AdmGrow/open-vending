# open-vending

Proyecto público. Software libre para máquina expendedora (todavía no es hardware real).

**Código para Linux y Android.** Python 3 en Linux. Android = kiosco / pantalla.

Licencia MIT. Lee `LEEME_LICENCIA.md` y `LICENSE`.
Hacé tu versión. Podés usarlo, copiarlo y ganar dinero con lo que armes.
Sin garantía: cada quien responde por lo que construye.

## que hay

- `src/controller/fsm.py` — estados simples (idle, credito, vender, error)
- `src/telemetry/events.py` — eventos
- `docs/` — apuntes y hardware Android

## como lo corro

Python 3 en Linux:

```
python src/controller/fsm.py
python src/telemetry/events.py
```

En Android: la UI en kiosco habla con este proceso por UART o HTTP local. Ver `docs/HARDWARE_ANDROID.md`.

## otros repos

snacks, tcg, frozen, tobacco, vivero-seedbank — misma licencia. Repos distintos.
