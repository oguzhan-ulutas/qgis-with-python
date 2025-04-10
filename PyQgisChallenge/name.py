layer = iface.activeLayer()
print(layer.name())

name =layer.name()

if name == "zoning":
    iface.messageBar().pushSuccess("Rigth Layer","You chose the correct layer.")
else:
    iface.messageBar().pushCritical("Wrong Layer","You choose wrong layer!!!")