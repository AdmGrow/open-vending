# Research — Day 1

## Market
- ~14 million vending machines worldwide; ~8.1 million connected in 2025.
- Connected machines growing at 7.6% CAGR to ~11.7 million by 2030.
- Cashless is the main driver; 71% of US transactions are cashless.
- Intelligent vending market projected to reach $96B by 2033.

## Open-source landscape
- vend.io (Node.js framework, MIT, low activity)
- temoto/vender (Go VMC firmware, CC0, 91 stars, MDB adapter works)
- nodestark/mdb-esp32-cashless / VMflow (ESP32, MDB, DEX/DDCMP, MQTT, MIT)
- gorodulin/vendingmachine (Python, Docker, Raspberry Pi, FSM)
- morzan1001/Kiosk (Python, NFC + barcode, communal fridge)
- Catfeeds/vmbm (PHP/Laravel backend management)
- foswvs (archived, wifi vending on RPi)

## Key protocols
- MDB (Multi-Drop Bus): standard bus between VMC and peripherals (coin, bill, cashless).
- DEX / EVA DTS / DDCMP: data transfer standard for sales and inventory audit.
- ccTalk: common for coin acceptors over USB/serial.

## Architecture direction
1. Edge controller (ESP32 or Raspberry Pi) speaking MDB.
2. Local state machine for vend logic + inventory.
3. Telemetry uplink via MQTT or cellular.
4. Cloud backend: inventory, sales, alerts, route planning.
5. Cashless via MDB cashless reader or QR/NFC.

## Next steps
- Pick hardware target and protocol scope for v0.1.
- Define data model for products, slots, transactions.
- Scaffold controller + simulator.