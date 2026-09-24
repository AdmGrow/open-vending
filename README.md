# open-vending

Proyecto público. Software libre para máquina expendedora (todavía no es hardware real).

Licencia MIT. Lee `LEEME_LICENCIA.md` y `LICENSE`.
Hacé tu versión. Podés usarlo, copiarlo y ganar dinero con lo que armes.
Sin garantía: cada quien responde por lo que construye.

## que hay

- `src/controller/fsm.py` — estados simples (idle, credito, vender, error)
- `src/telemetry/events.py` — eventos
- `docs/` — apuntes

## como lo corro

Python 3.

```
python src/controller/fsm.py
python src/telemetry/events.py
```

## otros repos

snacks, tcg, frozen, tobacco, vivero-seedbank — misma licencia.
