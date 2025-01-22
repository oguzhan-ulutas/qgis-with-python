pathToTif = "D:/MBES_Trackline/all/example/NISA_BOUNDARY_1m_B_05.tif"

rLayer = QgsRasterLayer(pathToTif, "test")
if not rLayer.isValid():
    print("Layer failed to load!!!")

iface.addRasterLayer(pathToTif, "NISA-test")