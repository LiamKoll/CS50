import re

email = input("Whats your Email?\n").strip()

if re.search(r"^(\w | \.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")