import random

def generar_lista_aleatoria(tamaño: int):
    if tamaño <= 0:
        return []
    return [random.randint(10, 99)] + generar_lista_aleatoria(tamaño - 1)

def Suma_Multiplo_tres( lista : list, indice : int = 0 ) -> int:
    if indice == len(lista):
        return 0
    if lista[indice] % 3 == 0:
        return lista[indice] + Suma_Multiplo_tres(lista, indice + 1)
    return Suma_Multiplo_tres(lista, indice + 1)

def main():
    tamaño = int(input("Ingrese la cantidad de elementos para la lista:"))
    if tamaño <= 0:
        print("El tamaño de la lista debe ser un número positivo.")
        return
    lista_aleatoria = generar_lista_aleatoria(tamaño)
    print("Lista generada:", lista_aleatoria)
    suma = Suma_Multiplo_tres(lista_aleatoria)
    print("La suma de los múltiplos de 3 en la lista es:", suma)
main()