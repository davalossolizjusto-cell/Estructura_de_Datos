def calculate_area(base, height):
    """Calculate the area of a rectangle.
      result devuelve el área total
      Parameters:
        base (int or float)
        height (int or float)
    """
    result = base * height
    return result


if __name__ == "__main__":
    # Llamada al metodo calculate_area()
    area = calculate_area(10, 3)
    print(area)