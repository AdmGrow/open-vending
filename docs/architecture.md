# Architecture

## Layers
1. **Hardware / Edge**: ESP32 or Raspberry Pi. MDB master or slave. Local SQLite for inventory and transaction log. Offline-first.
2. **Controller**: Finite state machine. States: idle, credit, vend, error, out-of-service. Watchdog + self-test.
3. **Telemetry**: MQTT or HTTPS uplink. Events: sale, stock change, fault, door, cash level, heartbeat. EVA DEX export.
4. **Compliance**: fail-closed. Age gate, temperature lockout, expiry. One age check per vend.
5. **Cloud**: Inventory, fleet dashboard, alerts, restock routes, pricing. REST + WebSocket. Not a SaaS bill in v0.1.
6. **Ops**: GitHub issues + Drive sheet + daily job 09:00 America/Argentina/Buenos_Aires.

## Data model (v0.1)
- Product: id, name, price, sku, category
- Slot: id, product_id, capacity, current_qty, par_level
- Machine: id, location, status, last_seen
- Transaction: id, machine_id, slot_id, amount, method, ts
- Alert: id, machine_id, type, severity, ts
- TelemetryEvent: machine_id, event_type, payload, ts

Vertical extras live in sibling repos (expiry, sealed pack, cabinet, age check, seed lot).

## Contracts
- Edge can vend offline.
- Tobacco never vends without a passed age check.
- TCG catalog stores no official marks.
- Frozen blocks vend if door open or temp out of range.
- Nursery software does not speak MDB.

## Non-goals for v0.1
- No AI recommendations yet.
- No multi-tenant SaaS billing.
- No proprietary hardware lock-in.
