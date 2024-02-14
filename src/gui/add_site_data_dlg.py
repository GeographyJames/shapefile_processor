from .qt_designer.qt_add_site_data_dlg import Ui_AddSiteDataDlg
from PyQt5.QtWidgets import QDialog

class AddSiteDataDlg(QDialog, Ui_AddSiteDataDlg):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    app = QApplication([])
    window = AddSiteDataDlg()
    window.show()
    app.exec()