"""Resultado: Clasifica edad."""
edad = 20
match edad:
    case edad if edad < 18:
        print("Menor")
    case _:
        print("Adulto")