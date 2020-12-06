##Se pide que ingrese variables para callulcular una medida la cual sera presentada despues
largo = float(input("Ingrese el largo del terreno"))
ancho = float(input("Ingrese el ancho del terreno"))
costoMetro = float(input("Ingrese el costo del m2 del terreno"))
nombreComprador = input("Ingrese el su nombre")
area = largo * ancho
costoTerreno = area * costoMetro;
print ("El costo del terreno es : %.2f\n"%(costoTerreno))