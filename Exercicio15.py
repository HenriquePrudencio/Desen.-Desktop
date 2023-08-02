frutas = {
    "jaboticaba": 123123,
    "melancia": 1,
    "kiwi": 32,
    "pitaya": 18,
    "uva":108
}
qtd = frutas.get("jaboticaba")
print(f"Exitem {qtd} jaboticabas")
print(frutas)

for f in frutas.keys():
    print(f)