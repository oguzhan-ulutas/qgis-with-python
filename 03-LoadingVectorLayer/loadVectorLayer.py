if not vLayer.isValid():
    print("Layer failed to load")
else:
    QgsProject.instance().addMapLayer(vLayer)