import os
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

vector_layer = 'seismic_zones.shp'
vector_layer_path = os.path.join(data_dir, vector_layer)

raster_layer = 'srtm.tif'
raster_layer_path = os.path.join(data_dir, raster_layer)

# Input vector has invalid geometries
# Fix them first
results = processing.runAndLoadResults("native:fixgeometries", {
  'INPUT':vector_layer_path,
  'METHOD': 0,
  'OUTPUT':'TEMPORARY_OUTPUT'})

fixed_vector_layer = results['OUTPUT']

processing.runAndLoadResults("native:zonalstatisticsfb", {'INPUT':fixed_vector_layer,'INPUT_RASTER':'C:/Users/KNP/Downloads/pyqgis_masterclass/srtm.tif','RASTER_BAND':1,'COLUMN_PREFIX':'_','STATISTICS':[0,1,2],'OUTPUT':'TEMPORARY_OUTPUT'})
