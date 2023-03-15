macas = float(input("Quantas macas foram compradas? "))

if (macas < 12):
    valor = macas + 1.30
else:
    valor = macas * 1.00

print(f"Voce comprou: {macas} por {valor:.2f}")