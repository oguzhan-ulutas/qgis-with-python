pathToFile = "D:/MBES_Trackline/all/example/KORDIL_NISA_SSS_TRACKLINES.shp"

vlayer = iface.addVectorLayer(pathToFile, "", "ogr")
if not vlayer:
    print("Layer Failed to load!!!")