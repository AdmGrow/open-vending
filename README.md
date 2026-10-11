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
- `prices.example.json` — ejemplo de precios por slot

## como lo corro

Python 3 en Linux:

```
# copiá el ejemplo de precios (opcional, si no usa los fijos de prueba)
cp prices.example.json prices.json

python src/controller/fsm.py
python src/telemetry/events.py
```

Si existe `prices.json` en la carpeta, lo carga y usa esos precios. Si no, quedan los de prueba (A1=100, A2=150, B1=200).

En Android: la UI en kiosco habla con este proceso por UART o HTTP local. Ver `docs/HARDWARE_ANDROID.md`.

## otros repos

snacks, tcg, frozen, tobacco, vivero-seedbank — misma licencia. Repos distintos.
