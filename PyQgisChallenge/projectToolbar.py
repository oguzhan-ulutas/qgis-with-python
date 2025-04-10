import os

data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

projectToolBar = iface.addToolBar("Project Selector")

label = QLabel("Select a project to load", parent=projectToolBar)
projectSelector = QComboBox(parent=projectToolBar)

projectSelector.addItem("sf.qgz")
projectSelector.addItem("places.qgz")

def loadProject(projectName):
    print("You select", projectName)
    projectPath = os.path.join(data_dir, projectName)
    project = QgsProject.instance()
    project.read(projectPath)

projectSelector.currentTextChanged.connect(loadProject)

projectToolBar.addWidget(label)
projectToolBar.addWidget(projectSelector)