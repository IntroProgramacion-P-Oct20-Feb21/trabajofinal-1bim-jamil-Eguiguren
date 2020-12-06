##Se crea una cadena de repetiion que presenta una tabla con las variables ingresadas
cadenaFinal = ""
bandera = True
contador = 0
promedio = 0
sumaNotas = 0
while (bandera):
    nota = float(input("Ingrese calificaciónes: "))
    cadenaFinal = f"{cadenaFinal}{nota:.2f}\n"
    sumaNotas = sumaNotas + nota
    salida = input("Ingrese (si) si desea salir del ciclo: ")
    salida = salida.lower()
    contador = contador + 1
    if (salida == "si"):
        bandera = False
promedio = sumaNotas / contador
cadenaFinal = f"Listado de Notas\n{cadenaFinal}Promedio: {promedio:.2f}\n"
print(cadenaFinal)