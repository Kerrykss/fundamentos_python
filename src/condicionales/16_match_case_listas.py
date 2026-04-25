"""Resultado: Evalúa lista."""
lista = [1,2,3]
match lista:
    case [x,*resto]:
        print("Primero:",x)