san_francisco = (37.7749, -122.4194)
new_york = (40.661, -73.944)
las_vegas = (36.1699, -115.1398)

d = QgsDistanceArea()
d.setEllipsoid("WGS84")

# Prints if ellipsoid will be use or not
print(d.willUseEllipsoid())

point1 = QgsPointXY(san_francisco[1],san_francisco[0])
point2 = QgsPointXY(new_york[1], new_york[0])
point3 = QgsPointXY(las_vegas[1], las_vegas[0])

distance = d.measureLine([point1, point3, point2])
print(distance)

distInMeters = d.convertLengthMeasurement(distance, Qgis.DistanceUnit.DistanceMeters)
print(distInMeters)