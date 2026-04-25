"""Resultado: Clasifica fruta."""
fruta = "manzana"
match fruta:
    case "manzana":
        print("Manzana")
    case _:
        print("Otra fruta")