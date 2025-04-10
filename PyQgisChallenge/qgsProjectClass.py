import os

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

project = QgsProject.instance()
project_name = "sf.qgz"
project_path = os.path.join(data_dir, project_name)
print(project_path)
project.read(project_path)