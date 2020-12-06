## Se raliza una operacion  con las variables ingresadas para luego presentarlas
prestamo = float(input("Ingrese el valor del prestamo"))
interes = float(input("Ingrese el valor del interes"))
tiempo = float(input("Ingrese el tiempo del prestamo"))
multiplicacion = prestamo * tiempo
suma = multiplicacion + interes
print ("el pago mensual de del préstamo es: %.2f\n"%(suma))