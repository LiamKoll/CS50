# Code um Name ordentlich zu ordnen
import re

name = input("Was ist dein Name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)

# Wenn User schreibt: "lastname, firstname" soll es "firstname lastname" sein
if matches:
    name = matches.group(2) + " " + matches.group(1)
# Ausführen des Programms
print(f"Hallo, {name}!")