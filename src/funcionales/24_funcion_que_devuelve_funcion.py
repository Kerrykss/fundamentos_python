def crear():
    def interno():
        return "Hola"
    return interno

f = crear()
print(f())

# Resultado:
# Función dentro de función