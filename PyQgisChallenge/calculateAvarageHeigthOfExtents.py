import os

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')
icon = "kordilLogo.png"
iconPath = os.path.join(data_dir, icon)

rasterPath = os.path.join(data_dir, "srtm.tif")
def calculateAverage():
    rlayer = QgsRasterLayer(rasterPath, "MyRaster")
    provider = rlayer.dataProvider()
    
    mc = iface.mapCanvas()
    extent = QgsRectangle(mc.extent())
    
    stats = provider.bandStatistics(1, stats=QgsRasterBandStats.All, extent=extent)
    
    iface.messageBar().pushInfo("Average Height", f"{stats.mean}")
    

action = QAction("Calculate Average")
action.triggered.connect(calculateAverage)
action.setIcon(QIcon(iconPath))
iface.addToolBarIcon(action)