def mostrar(**datos):
    """Muestra datos clave-valor."""
    for k, v in datos.items():
        print(k, v)

mostrar(nombre="Kerry", edad=20)

# Resultado:
# Imprime claves y valores