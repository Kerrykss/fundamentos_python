def pago(horas, tarifa=10):
    """Calcula pago total."""
    return horas * tarifa

print(pago(5))
print(pago(5, 20))

# Resultado:
# 50 y 100