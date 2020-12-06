##Se realiza una opracion gracias a los valores ingresados para que luego esa operacion sea presentada
costoporminuto = float(input("Ingrese el costo por minutos ")) 
minutosconsumidos = float(input("Ingrese el numero de minutos consumidos en el mes ")) 
resultado = costoporminuto * minutosconsumidos
print ("minutosconsumidos: %.2f\n"%(resultado))