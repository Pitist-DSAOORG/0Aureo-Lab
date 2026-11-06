import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "docs/architecture/status.json"

data = json.loads(STATUS.read_text(encoding="utf-8"))

errors = []

allowed = {
    "DESIGNED",
    "IMPLEMENTED",
    "INTEGRATED",
    "VERIFIED",
    "BLOCKED"
}

for component in data["components"]:
    name = component["name"]
    state = component["status"]

    if state not in allowed:
        errors.append(f"{name}: estado desconocido {state}")
        continue

    if state == "DESIGNED":
        print(f"PASS {name}: diseñado, no implementado")
        continue

    if state in ("IMPLEMENTED", "INTEGRATED", "VERIFIED"):
        errors.append(
            f"{name}: requiere evidencia verificable antes de aceptar {state}"
        )

if data["overall_status"] != "SPECIFICATION_ONLY":
    errors.append("Estado global incorrecto")

if data["implemented"] or data["integrated"] or data["verified"]:
    errors.append("El registro global afirma capacidades no demostradas")

if errors:
    for error in errors:
        print("FAIL:", error)
    sys.exit(1)

print("ARCHITECTURE_AUDIT=PASS")
print("IMPLEMENTED_COMPONENTS=0")
print("INTEGRATED_COMPONENTS=0")
print("VERIFIED_COMPONENTS=0")
