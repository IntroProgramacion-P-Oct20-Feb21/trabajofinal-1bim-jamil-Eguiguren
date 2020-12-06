##Se utiliza acomulador de cadenas para poder presentar todas las variables
pais = "Ecuador"
ciudad = "Loja"
fechaIndependencia = "18 de noviembre"
cadenaAcumuladora = ""
cadenaAcumuladora = ("%s%s\n"% (cadenaAcumuladora, pais))
cadenaAcumuladora = ("%s%s\n"% (cadenaAcumuladora, ciudad))
cadenaAcumuladora = ("%s%s\n"% (cadenaAcumuladora, fechaIndependencia))
print("%s"% (cadenaAcumuladora))
