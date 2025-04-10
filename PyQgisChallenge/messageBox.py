mb = QMessageBox()
mb.setText("Click OK to confirm.")
mb.setIcon(QMessageBox.Warning)
mb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
returnValue = mb.exec()

print(returnValue)

if returnValue == QMessageBox.Ok:
    print("You pressed ok.")
elif returnValue == QMessageBox.Cancel:
    print("You pressed cancel. ")