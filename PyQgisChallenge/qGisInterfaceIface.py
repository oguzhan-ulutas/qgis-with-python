"""title = iface.mainWindow().windowTitle()
print(title)
newTitle = title.replace("QGIS", "KordilGIS")
iface.mainWindow().setWindowTitle(newTitle)"""

"""import os

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')
print(data_dir)
icon_path = os.path.join(data_dir, "kordilLogo.png")
print(icon_path)
icon = QIcon(icon_path)
iface.mainWindow().setWindowIcon(icon)"""

vectorMenu = iface.vectorMenu()
rasterMenu = iface.rasterMenu()