vlan = int(input("Ingrese el numerode VLAN:  "))
if 1 <= vlan <= 1005:
    print("VLAN es rango normal")
elif 1006 <= vlan <= 4094:
    print("VLAN es rango extendido")
else:
    print("VLAN no valida")