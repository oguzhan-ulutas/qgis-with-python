import os

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

for angle in range(0,100,10):
    outputFileName = f"hillside{angle}.tif"
    print(outputFileName)
    outputPath = os.path.join(data_dir, f"hillOutput\{outputFileName}")
    
    result =  processing.runAndLoadResults(
        "native:hillshade", {
        'INPUT':'C:/Users/KNP/Downloads/pyqgis_masterclass/srtm.tif',
        'Z_FACTOR':1,
        'AZIMUTH':300,
        'V_ANGLE':angle,
        'OUTPUT':outputPath
    })
    print(result)



