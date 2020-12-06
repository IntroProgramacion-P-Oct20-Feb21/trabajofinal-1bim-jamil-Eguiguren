##Se genera ciclo en cual se vera un descuento dependiendo de la variable ingresada pra luego ser presentado 
porcentaje1 = 10
porcentaje2 = 15
porcentaje3 = 20
numeroDias = int(input("Ingrese el número de días que se hospedará: "))
precioHabitacion = float(input("Ingrese el valor diario de la habitación: "))
if ((numeroDias > 5) and (numeroDias <= 10)):
	subtotal = numeroDias * precioHabitacion
	descuento = (porcentaje1 * subtotal) / 100
	valorTotal = subtotal - descuento
else:
	if ((numeroDias > 10) and (numeroDias <= 15)):
		subtotal = numeroDias * precioHabitacion
		descuento = (porcentaje2 * subtotal) / 100
		valorTotal = subtotal - descuento
	else:
		if (numeroDias > 15):
			subtotal = numeroDias * precioHabitacion
			descuento = (porcentaje3 * subtotal) / 100
			valorTotal = subtotal - descuento
		else:
			subtotal = numeroDias * precioHabitacion
			descuento = 0
			valorTotal = subtotal - descuento
print("El valor subtotal es: %.2f\nEl descuento es: %.2f\n"\
	"El valor total a pagar es: %.2f\n"%(\
		subtotal,\
		descuento,\
		valorTotal))