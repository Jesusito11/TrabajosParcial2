d=int(input("ingresa la distancia"))
t=int(input("ingresa el tiempo"))
v=d/t
if t == 0:
    print ('operacion no valida, division entre 0')
else:
    print ("velocidad es igual",v,)
    