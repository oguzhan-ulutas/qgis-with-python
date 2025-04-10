result = processing.runAndLoadResults("gdal:cliprasterbymasklayer", {
    'INPUT': 'C:/Users/KNP/Downloads/pyqgis_masterclass/srtm.tif',
    'MASK': 'C:/Users/KNP/Downloads/pyqgis_masterclass/shoreline.shp',
    'SOURCE_CRS': None,
    'TARGET_CRS': None,
    'TARGET_EXTENT': None,
    'NODATA': None,
    'ALPHA_BAND': False,
    'CROP_TO_CUTLINE': True,
    'KEEP_RESOLUTION': False,
    'SET_RESOLUTION': False,
    'X_RESOLUTION': None,
    'Y_RESOLUTION': None,
    'MULTITHREADING': False,
    'OPTIONS': '',
    'DATA_TYPE': 0,
    'EXTRA': '',
    'OUTPUT': 'TEMPORARY_OUTPUT'
})

clippedDem = result["OUTPUT"]

processing.runAndLoadResults("native:hillshade", {'INPUT': clippedDem,'Z_FACTOR':1,'AZIMUTH':300,'V_ANGLE':40,'OUTPUT':'TEMPORARY_OUTPUT'})