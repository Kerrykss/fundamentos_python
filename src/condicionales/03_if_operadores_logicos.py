"""Descripción: Uso de and, or, not.
Resultado: Evalúa múltiples condiciones."""
edad = 25
ingresos = 30000
llueve = False
if edad >= 18 and ingresos > 20000:
    print("Aprobado")
if not llueve:
    print("No llueve")