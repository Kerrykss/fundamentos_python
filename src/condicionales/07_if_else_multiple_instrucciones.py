"""Resultado: Simula operación bancaria."""
saldo = 300
retiro = 200
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso", saldo)
else:
    print("Fondos insuficientes")