def descuento(precio, porcentaje):
    """
    Aplica descuento.

    Args:
        precio (float)
        porcentaje (float)

    Returns:
        float
    """
    return precio - (precio * porcentaje/100)

print(descuento(100,10))