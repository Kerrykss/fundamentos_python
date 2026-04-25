"""Resultado: Evalúa rol."""
usuario = {"rol":"admin"}
match usuario:
    case {"rol":"admin"}:
        print("Admin")