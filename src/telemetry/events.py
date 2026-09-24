"""Telemetry event schema for vending machines.

Uplink via MQTT or HTTPS. Offline queue recommended.
"""
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json

@dataclass
class TelemetryEvent:
    machine_id: str
    event_type: str  # sale, stock_change, fault, door, cash_level, heartbeat
    payload: dict
    ts: str

    @classmethod
    def now(cls, machine_id, event_type, payload):
        return cls(
            machine_id=machine_id,
            event_type=event_type,
            payload=payload,
            ts=datetime.now(timezone.utc).isoformat(),
        )

    def to_json(self):
        return json.dumps(asdict(self))


# Example
if __name__ == "__main__":
    e = TelemetryEvent.now("vm-001", "sale", {"slot": "A3", "amount": 150, "method": "cashless"})
    print(e.to_json())