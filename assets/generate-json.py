"""
Generar JSON para ejercicio de años bisiestos
"""

import json
import random
from datetime import date
from datetime import timedelta

FILENAME = ".github/classroom/autograding.json"
PROG_FILE = "dia_anterior.py"


anho = date.today().year
cases = []
for mes in range(1, 13):
    # Primer día del mes
    cases.append((1, mes, anho))
    # Día a medio mes
    dia = random.randint(2, 27)
    cases.append((dia, mes, anho))
    # Último día del mes
    dia = date(anho, mes % 12 + 1, 1) - timedelta(days=1)
    dia = dia.day
    cases.append((dia, mes, anho))
# Año bisiesto secular
cases.append((1, 3, 2000))
# Año bisiesto no secular
cases.append((1, 3, 2016))
# Año secular no bisiesto
cases.append((1, 3, 2100))
# Año no secular y no bisiesto
cases.append((1, 3, 2015))

output = {}
tests = []

for i, case in enumerate(cases, start=1):
    inp = f"{case[0]}\r\n{case[1]}\r\n{case[2]}"
    outp = date(*case[::-1]) - timedelta(days=1)
    outp = (outp.day, outp.month, outp.year)
    #outp = f"{outp[0]}\r\n{outp[1]}\r\n{outp[2]}"
    outp = "(\n|.)*".join(str(i) for i in outp)
    name = f"Test{i:02d}"
    entry = {
        "name": name,
        "setup": "",
        "run": "LANG=en_US.utf8 timeout 3m python3 " + PROG_FILE,
        "input": inp,
        "output": outp,
        "comparison": "regex",
        "timeout": 1,
        "points": 1
        }
    tests.append(entry)
tests = {"tests": tests}

with open(FILENAME, "w") as f:
    json.dump(tests, f, indent=2)
