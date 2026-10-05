def buscar_multiplo(actual, fin, paso, resultado=None):
    # Caso base:
    if (paso == 1 and actual > fin) or (paso == -1 and actual < fin):
        return resultado
    # Si es múltiplo de 3, actualizamos el resultado
    if actual % 3 == 0:
        if resultado is None:
            resultado = actual
        elif paso == 1:
            resultado = max(resultado, actual)   # adelante: el máximo
        else:
            resultado = min(resultado, actual)   # atrás: el mínimo

    return buscar_multiplo(actual + paso, fin, paso, resultado)

def main():
    numero_inicio=int(input("Ingrese el número de inicio: "))
    numero_fin=int(input("Ingrese el número de fin: "))

    if numero_inicio <= numero_fin:
        paso = 1
    else:
        paso = -1
    resultado = buscar_multiplo(numero_inicio, numero_fin, paso)

    if resultado is None:
        print("No hay múltiplos de 3 en ese rango.")
    elif paso == 1:
        print("Máximo múltiplo de 3 (hacia adelante):", resultado)
    else:
        print("Mínimo múltiplo de 3 (hacia atrás):", resultado)
main()