from qgis.core import *

# Supply path to qgis install location
QgsApplication.setPrefixPath("C:\Program Files\QGIS 3.34.12\bin\qgis-ltr-bin.exe", True)

# Create a reference to the QgsApplication.  Setting the

# second argument to False disables the GUI.

qgs = QgsApplication([], False)


# Load providers

qgs.initQgis()


# Write your code here to load some layers, use processing

# algorithms, etc.


# Finally, exitQgis() is called to remove the

# provider and layer registries from memory

qgs.exitQgis()
