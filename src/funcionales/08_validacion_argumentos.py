def validar(numero):
    """Valida si el número es positivo."""
    if numero < 0:
        return "Número inválido"
    return "Número válido"

print(validar(10))
print(validar(-5))

# Resultado:
# Validación básica