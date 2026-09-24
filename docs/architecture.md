# Architecture

## Layers
1. **Hardware / Edge**: ESP32 or Raspberry Pi. MDB master or slave. Local SQLite for inventory and transaction log. Offline-first.
2. **Controller**: Finite state machine. States: idle, credit, vend, error, out-of-service. Watchdog + self-test.
3. **Telemetry**: MQTT or HTTPS uplink. Events: sale, stock change, fault, door, cash level. EVA DEX export.
4. **Cloud**: Inventory, fleet dashboard, alerts, restock routes, pricing. REST + WebSocket.
5. **Payments**: MDB cashless reader, QR, NFC. Remote credit support.

## Data model (v0.1)
- Product: id, name, price, sku, category
- Slot: id, product_id, capacity, current_qty, par_level
- Machine: id, location, status, last_seen
- Transaction: id, machine_id, slot_id, amount, method, ts
- Alert: id, machine_id, type, severity, ts

## Non-goals for v0.1
- No AI recommendations yet.
- No multi-tenant SaaS billing.
- No proprietary hardware lock-in.