from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from monitoring import *





class Marker(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        
        self.show_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.show_animation.setDuration(300)
        self.show_animation.setStartValue(0)
        self.show_animation.setEndValue(1)
        
        self.hide_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.hide_animation.setDuration(300)
        self.hide_animation.setStartValue(1)
        self.hide_animation.setEndValue(0)
        self.hide_animation.finished.connect(self.hide)
    

        
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint);
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.clicked = False
        self.resize(0, 0)

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(int(self.pos().x() - dx), int(self.pos().y() - dy))
        self.old_pos = event.screenPos()
        self.clicked = True

        return QtWidgets.QWidget.mouseMoveEvent(self, event)
    
    def showEvent(self, event):
        self.setWindowOpacity(0)
        self.show_animation.start()
        super().showEvent(event)
    
    def hider(self):
        self.hide_animation.start()

    def closeEvent(self, event):
        event.ignore()
        self.hide_animation.start()

class onscreenMarker(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        
        self.show_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.show_animation.setDuration(300)
        self.show_animation.setStartValue(0)
        self.show_animation.setEndValue(1)
        
        self.hide_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.hide_animation.setDuration(300)
        self.hide_animation.setStartValue(1)
        self.hide_animation.setEndValue(0)
        self.hide_animation.finished.connect(self.hide)

        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint);
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.clicked = False
        self.resize(0, 0)

    def closeEvent(self, event):
        event.ignore()

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(int(self.pos().x() - dx), int(self.pos().y() - dy))
        self.old_pos = event.screenPos()
        self.clicked = True

        return QtWidgets.QWidget.mouseMoveEvent(self, event)
    
    def shower(self):
        self.setWindowOpacity(0)
        self.show()
        self.show_animation.start()
    
    def hider(self):
        self.hide_animation.start()

    def closeEvent(self, event):
        event.ignore()
        self.hide_animation.start()

class mainMarker(QtWidgets.QMainWindow):
    def __init__(self):
        self.moveFlag = True
        super().__init__()
        QtWidgets.QWidget.__init__(self)
        
        self.show_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.show_animation.setDuration(300)
        self.show_animation.setStartValue(0)
        self.show_animation.setEndValue(1)
        
        self.hide_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.hide_animation.setDuration(300)
        self.hide_animation.setStartValue(1)
        self.hide_animation.setEndValue(0)
        self.hide_animation.finished.connect(self.hide)

        self.close_animation = QtCore.QPropertyAnimation(self, b"windowOpacity")
        self.close_animation.setDuration(300)
        self.close_animation.setStartValue(1)
        self.close_animation.setEndValue(0)
        self.close_animation.finished.connect(sys.exit)

        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint);
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.clicked = False
        self.resize(0, 0)

    def mousePressEvent(self, event):
        self.old_pos = event.screenPos()

    def mouseMoveEvent(self, event):
        if self.clicked and self.moveFlag:
            dx = self.old_pos.x() - event.screenPos().x()
            dy = self.old_pos.y() - event.screenPos().y()
            self.move(int(self.pos().x() - dx), int(self.pos().y() - dy))
        self.old_pos = event.screenPos()
        self.clicked = True

        return QtWidgets.QMainWindow.mouseMoveEvent(self, event)

    def showEvent(self, event):
        self.setWindowOpacity(0)
        self.show_animation.start()
        super().showEvent(event)
    
    def hider(self):
        self.hide_animation.start()

    def closeEvent(self, event):
        event.ignore()
        self.close_animation.start()


class AnimatedSystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def UpdateIcon(self):
        icon = QtGui.QIcon()
        icon.addPixmap(self.iconMovie.currentPixmap())
        self.setIcon(icon)

    def __init__(self, movie, parent=None):
        super(AnimatedSystemTrayIcon, self).__init__(parent)
        menu = QtWidgets.QMenu(parent)
        exitAction = menu.addAction("Exit")
        self.setContextMenu(menu)

        self.iconMovie = movie
        self.iconMovie.start()

        self.iconMovie.frameChanged.connect(self.UpdateIcon)


class Error:
    def __str__(self):
        raise ValueError('')


def shadow(obj, radius): 
    return QtWidgets.QGraphicsDropShadowEffect(obj,
    blurRadius=radius,
    color=QtGui.QColor(0, 0, 0, 100),
    offset=QtCore.QPointF(-1, -1))  


class onscreenWindow(onscreenMarker):
    def __init__(self):
        super().__init__()
        self.setObjectName("popupForm")
        self.setWindowTitle('onScreen')
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Tool);
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.setWindowIcon(QtGui.QIcon(files_+'Icon.ico'))
        #self.resize(0, 0)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 255);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        global changeTrans
        def changeTrans(e):
            color = info['bg'].split(',')
            r,g,b = int(color[0]),int(color[1]),int(color[2])
            self.popupFrame.setStyleSheet(f"background-color: rgba({r}, {g}, {b}, {e});\n"
            "border-bottom-left-radius: 0;")
            info['alpha'] = f'{e}'
            save()

        global changeBg
        def changeBg(e):
            color = info['bg'].split(',')
            r,g,b = int(color[0]),int(color[1]),int(color[2])
            color = QtWidgets.QColorDialog.getColor(initial=QtGui.QColor(r, g, b))
            if color.isValid():
                self.popupFrame.setStyleSheet(f"background-color: rgba({color.red()}, {color.green()}, {color.blue()}, {int(info['alpha'])});\nborder-bottom-left-radius: 0;")
                setbgcolorButton("border: 1px solid;\n"
                "border-radius: 4px;\n"
                f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")
                info['bg'] = f'{color.red()},{color.green()},{color.blue()}'
                save()

        global changeFg
        def changeFg(e):
            color = info['fg'].split(',')
            r,g,b = int(color[0]),int(color[1]),int(color[2])
            color = QtWidgets.QColorDialog.getColor(initial=QtGui.QColor(r, g, b))
            if color.isValid():
                for i in [self.popupLabel1, self.popupLabel2, self.popupLabel3, self.popupLabel4, self.popupLabel5, self.popupLabel6, self.popupLabel7]:
                    i.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                    f"color: rgb({color.red()}, {color.green()}, {color.blue()});\n"
                    "border-radius: 0px;")
                setfgcolorButton("border: 1px solid;\n"
                "border-radius: 4px;\n"
                f"background-color: rgb({color.red()}, {color.green()}, {color.blue()});")
                info['fg'] = f'{color.red()},{color.green()},{color.blue()}'
                save()

        global changeItems
        def changeItems(ch, state):
            items = info["items"]
            if ch=='cpuUsage':
                if state==True:
                    self.popupLabel3.show()
                    if not '1' in items: info["items"] = items+'1'
                else:
                    self.popupLabel3.hide()
                    info["items"] = items.replace('1', '')
            elif ch=='cpuTemp':
                if state==True:
                    self.popupLabel4.show()
                    if not '2' in items: info["items"] = items+'2'
                else:
                    self.popupLabel4.hide()
                    info["items"] = items.replace('2', '')
            elif ch=='gpuUsage':
                if state==True:
                    self.popupLabel1.show()
                    if not '3' in items: info["items"] = items+'3'
                else:
                    self.popupLabel1.hide()
                    info["items"] = items.replace('3', '')
            elif ch=='gpuTemp':
                if state==True:
                    self.popupLabel2.show()
                    if not '4' in items: info["items"] = items+'4'
                else:
                    self.popupLabel2.hide()
                    info["items"] = items.replace('4', '')
            elif ch=='ramUsage':
                if state==True:
                    self.popupLabel5.show()
                    if not '5' in items: info["items"] = items+'5'
                else:
                    self.popupLabel5.hide()
                    info["items"] = items.replace('5', '')
            elif ch=='hard1Temp':
                if state==True:
                    self.popupLabel6.show()
                    if not '6' in items: info["items"] = items+'6'
                else:
                    self.popupLabel6.hide()
                    info["items"] = items.replace('6', '')
            elif ch=='hard2Temp':
                if state==True:
                    self.popupLabel7.show()
                    if not '7' in items: info["items"] = items+'7'
                else:
                    self.popupLabel7.hide()
                    info["items"] = items.replace('7', '')
            save()

        self.popupFrame = QtWidgets.QFrame(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupFrame.sizePolicy().hasHeightForWidth())
        self.popupFrame.setSizePolicy(sizePolicy)
        color = info['bg'].split(',')
        r,g,b = int(color[0]),int(color[1]),int(color[2])
        self.popupFrame.setStyleSheet(f"background-color: rgba({r}, {g}, {b}, {int(info['alpha'])});\n"
"border-bottom-left-radius: 0;")
        self.popupFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popupFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popupFrame.setObjectName("popupFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.popupFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.popupLayout = QtWidgets.QVBoxLayout()
        self.popupLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.popupLayout.setObjectName("popupLayout")
        self.popupLabel1 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel1.sizePolicy().hasHeightForWidth())
        color = info['fg'].split(',')
        r,g,b = int(color[0]),int(color[1]),int(color[2])
        self.popupLabel1.setSizePolicy(sizePolicy)
        self.popupLabel1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel1.setObjectName("popupLabel1")
        self.popupLabel2 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel2.sizePolicy().hasHeightForWidth())
        self.popupLabel2.setSizePolicy(sizePolicy)
        self.popupLabel2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel2.setObjectName("popupLabel2")
        self.popupLabel3 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel3.sizePolicy().hasHeightForWidth())
        self.popupLabel3.setSizePolicy(sizePolicy)
        self.popupLabel3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel3.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel3.setObjectName("popupLabel3")
        self.popupLayout.addWidget(self.popupLabel3)
        self.popupLabel4 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel4.sizePolicy().hasHeightForWidth())
        self.popupLabel4.setSizePolicy(sizePolicy)
        self.popupLabel4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel4.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel4.setObjectName("popupLabel4")
        self.popupLayout.addWidget(self.popupLabel4)
        self.popupLayout.addWidget(self.popupLabel1)
        self.popupLayout.addWidget(self.popupLabel2)
        self.popupLabel5 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel5.sizePolicy().hasHeightForWidth())
        self.popupLabel5.setSizePolicy(sizePolicy)
        self.popupLabel5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel5.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel5.setObjectName("popupLabel5")
        self.popupLayout.addWidget(self.popupLabel5)
        self.popupLabel6 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel6.sizePolicy().hasHeightForWidth())
        self.popupLabel6.setSizePolicy(sizePolicy)
        self.popupLabel6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel6.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel6.setObjectName("popupLabel6")
        self.popupLayout.addWidget(self.popupLabel6)
        self.popupLabel7 = QtWidgets.QLabel(self.popupFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupLabel7.sizePolicy().hasHeightForWidth())
        self.popupLabel7.setSizePolicy(sizePolicy)
        self.popupLabel7.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
f"color: rgb({r}, {g}, {b});\n"
"border-radius: 0px;")
        self.popupLabel7.setAlignment(QtCore.Qt.AlignCenter)
        self.popupLabel7.setObjectName("popupLabel7")

        items = info["items"]
        if not '1' in items:
            self.popupLabel3.hide()
        if not '2' in items:
            self.popupLabel4.hide()
        if not '3' in items:
            self.popupLabel1.hide()
        if not '4' in items:
            self.popupLabel2.hide()
        if not '5' in items:
            self.popupLabel5.hide()
        if not '6' in items:
            self.popupLabel6.hide()
        if not '7' in items:
            self.popupLabel7.hide()

        self.popupLayout.addWidget(self.popupLabel7)
        self.gridLayout_2.addLayout(self.popupLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.popupFrame, 0, 0, 1, 1)

        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.popupLabel1.setText("Loading")
        self.popupLabel2.setText("Loading")
        self.popupLabel3.setText("Loading")
        self.popupLabel4.setText("Loading")
        self.popupLabel5.setText("Loading")
        self.popupLabel6.setText("Loading")
        self.popupLabel7.setText("Loading")

    def mover(self, x, y):
            self.move(x-self.width(), y)


class settingsWindow(Marker):
    def __init__(self, applyMaintheme):
        super().__init__()
        self.applyMaintheme = applyMaintheme
        self.EditWindow = editWindow();self.EditWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.setObjectName("popupForm")
        self.setWindowTitle('Settings')
        self.setWindowIcon(QtGui.QIcon(files_+'Icon.ico'))
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint);
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True);
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True);
        self.settingsFrame = QtWidgets.QFrame(self)
        self.settingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.settingsFrame.setGraphicsEffect(shadow(self.settingsFrame, 25))
        self.settingsFrame.setObjectName("settingsFrame")
        self.settingsFrame.resize(329, 258)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.s_layout1 = QtWidgets.QVBoxLayout()
        self.s_layout1.setObjectName("s_layout1")
        self.s_layout2 = QtWidgets.QHBoxLayout()
        self.s_layout2.setObjectName("s_layout2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.s_layout2.addItem(spacerItem)
        self.settingscloseBtn = QtWidgets.QPushButton(self.settingsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.settingscloseBtn.sizePolicy().hasHeightForWidth())
        self.settingscloseBtn.setSizePolicy(sizePolicy)
        self.settingscloseBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.settingscloseBtn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.settingscloseBtn.setFont(font)
        self.settingscloseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingscloseBtn.setStyleSheet("border: 0px;\n"
"color: rgb(86, 86, 86);")
        self.settingscloseBtn.setFlat(False)
        self.settingscloseBtn.setObjectName("settingscloseBtn")
        self.settingscloseBtn.clicked.connect(lambda: self.hider() or self.EditWindow.hider())
        self.s_layout2.addWidget(self.settingscloseBtn)
        self.s_layout1.addLayout(self.s_layout2)
        self.s_layout3 = QtWidgets.QHBoxLayout()
        self.s_layout3.setObjectName("s_layout3")
        self.settingsGroupbox1 = QtWidgets.QGroupBox(self.settingsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsGroupbox1.sizePolicy().hasHeightForWidth())
        self.settingsGroupbox1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settingsGroupbox1.setFont(font)
        self.settingsGroupbox1.setObjectName("settingsGroupbox1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.settingsGroupbox1)
        self.gridLayout_9.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.s_layout4 = QtWidgets.QVBoxLayout()
        self.s_layout4.setContentsMargins(-1, 15, -1, 25)
        self.s_layout4.setObjectName("s_layout4")

        def startupLauncher(e):
            if e:
                info["autostart"] = 'true'
                if not check_autostart_registry("LoCoToring"): set_autostart_registry("LoCoToring", sys.argv[0], autostart=True)
            else:
                info["autostart"] = 'false'
                if check_autostart_registry("LoCoToring"): set_autostart_registry("LoCoToring", sys.argv[0], autostart=False)
            save()

        self.launchStartup = QtWidgets.QCheckBox(self.settingsGroupbox1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.launchStartup.setFont(font)
        self.launchStartup.setChecked(False)
        self.launchStartup.setObjectName("thememodeSystem")
        self.launchStartup.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.launchStartup.setText('Start with windows')
        self.launchStartup.setToolTip('NOTE: If enabled, the program will run hidden (system tray) next times.\nNOTE: Don\'t change program location after you check this option.')
        self.launchStartup.stateChanged.connect(startupLauncher)
        self.launchStartup.setChecked(True) if info["autostart"]=='true' else self.launchStartup.setChecked(False)
        self.s_layout4.addWidget(self.launchStartup)

        self.thememodeLabel = QtWidgets.QLabel(self.settingsGroupbox1)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.thememodeLabel.setFont(font)
        self.thememodeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thememodeLabel.setObjectName("thememodeLabel")
        self.s_layout4.addWidget(self.thememodeLabel)

        def changeTheme(ch, hider=False):
            chs = [self.thememodeSystem, self.thememodeDark, self.thememodeLight]
            if ch.isChecked():
                for i in chs:
                    if ch!=i:
                        i.setChecked(False)
                self.applyMaintheme(ch.text())
                self.applySettingstheme(ch.text())
                self.EditWindow.applyEdittheme(ch.text())
                if not hider: 
                    self.hider();self.show()
                info["theme"] = ch.text().lower()
                save()
            else:
                if chs[0].isChecked()==False and chs[1].isChecked()==False and chs[2].isChecked()==False:
                    ch.setChecked(True)

        self.changeTheme = changeTheme

        self.thememodeSystem = QtWidgets.QCheckBox(self.settingsGroupbox1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.thememodeSystem.setFont(font)
        self.thememodeSystem.setObjectName("thememodeSystem")
        self.s_layout4.addWidget(self.thememodeSystem)
        self.thememodeDark = QtWidgets.QCheckBox(self.settingsGroupbox1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.thememodeDark.setFont(font)
        self.thememodeDark.setObjectName("thememodeDark")
        self.s_layout4.addWidget(self.thememodeDark)
        self.thememodeLight = QtWidgets.QCheckBox(self.settingsGroupbox1)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.thememodeLight.setFont(font)
        self.thememodeLight.setObjectName("thememodeLight")
        self.thememodeSystem.setText("System")
        self.thememodeDark.setText("Dark")
        self.thememodeLight.setText("Light")
        self.thememodeSystem.clicked.connect(lambda e: changeTheme(self.thememodeSystem, True))
        self.thememodeDark.clicked.connect(lambda e: changeTheme(self.thememodeDark, True))
        self.thememodeLight.clicked.connect(lambda e: changeTheme(self.thememodeLight, True))
        self.s_layout4.addWidget(self.thememodeLight)
        self.gridLayout_9.addLayout(self.s_layout4, 0, 0, 1, 1)
        self.s_layout3.addWidget(self.settingsGroupbox1)
        self.settingsGroupbox2 = QtWidgets.QGroupBox(self.settingsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settingsGroupbox2.sizePolicy().hasHeightForWidth())
        self.settingsGroupbox2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.settingsGroupbox2.setFont(font)
        self.settingsGroupbox2.setObjectName("settingsGroupbox2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.settingsGroupbox2)
        self.gridLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_10.setContentsMargins(-1, 26, -1, 7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.s_layout8 = QtWidgets.QHBoxLayout()
        self.s_layout8.setObjectName("s_layout8")
        self.sideLabel = QtWidgets.QLabel(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.sideLabel.setFont(font)
        self.sideLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.sideLabel.setObjectName("sideLabel")
        self.s_layout8.addWidget(self.sideLabel)
        self.SideCombobox = QtWidgets.QComboBox(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SideCombobox.setFont(font)
        self.SideCombobox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SideCombobox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SideCombobox.setMinimumContentsLength(1)
        self.SideCombobox.setFrame(False)
        self.SideCombobox.setObjectName("SideCombobox")
        self.SideCombobox.addItem("")
        self.SideCombobox.addItem("")
        self.SideCombobox.addItem("")
        self.SideCombobox.addItem("")
        self.s_layout8.addWidget(self.SideCombobox)
        self.gridLayout_10.addLayout(self.s_layout8, 3, 0, 1, 1)
        self.s_layout6 = QtWidgets.QHBoxLayout()
        self.s_layout6.setObjectName("s_layout6")
        self.fgcolorLabel = QtWidgets.QLabel(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.fgcolorLabel.setFont(font)
        self.fgcolorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fgcolorLabel.setObjectName("fgcolorLabel")
        self.s_layout6.addWidget(self.fgcolorLabel)

        global setbgcolorButton
        def setbgcolorButton(s):
            self.bgcolorButton.setStyleSheet(s)
        global setfgcolorButton
        def setfgcolorButton(s):
            self.fgcolorButton.setStyleSheet(s)

        self.fgcolorButton = QtWidgets.QPushButton(self.settingsGroupbox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.fgcolorButton.sizePolicy().hasHeightForWidth())
        self.fgcolorButton.setSizePolicy(sizePolicy)
        self.fgcolorButton.setMinimumSize(QtCore.QSize(16, 16))
        self.fgcolorButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.fgcolorButton.setFont(font)
        self.fgcolorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fgcolorButton.setText("")
        self.fgcolorButton.setFlat(False)
        color = info['fg'].split(',')
        r,g,b = int(color[0]),int(color[1]),int(color[2])
        self.fgcolorButton.setStyleSheet("border: 1px solid;\n"
"border-radius: 4px;\n"
f"background-color: rgb({r}, {g}, {b});")
        self.fgcolorButton.setObjectName("fgcolorButton")
        self.fgcolorButton.clicked.connect(changeFg)
        self.s_layout6.addWidget(self.fgcolorButton)
        self.gridLayout_10.addLayout(self.s_layout6, 1, 0, 1, 1)
        self.s_layout5 = QtWidgets.QHBoxLayout()
        self.s_layout5.setObjectName("s_layout5")
        self.bgcolorLabel = QtWidgets.QLabel(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.bgcolorLabel.setFont(font)
        self.bgcolorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bgcolorLabel.setObjectName("bgcolorLabel")
        self.s_layout5.addWidget(self.bgcolorLabel)
        self.bgcolorButton = QtWidgets.QPushButton(self.settingsGroupbox2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.bgcolorButton.sizePolicy().hasHeightForWidth())
        self.bgcolorButton.setSizePolicy(sizePolicy)
        self.bgcolorButton.setMinimumSize(QtCore.QSize(16, 16))
        self.bgcolorButton.setMaximumSize(QtCore.QSize(16, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.bgcolorButton.setFont(font)
        self.bgcolorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bgcolorButton.setText("")
        self.bgcolorButton.setFlat(False)
        color = info['bg'].split(',')
        r,g,b = int(color[0]),int(color[1]),int(color[2])
        self.bgcolorButton.setStyleSheet("border: 1px solid;\n"
"border-radius: 4px;\n"
f"background-color: rgb({r}, {g}, {b});")
        self.bgcolorButton.setObjectName("bgcolorButton")
        self.bgcolorButton.clicked.connect(changeBg)
        self.s_layout5.addWidget(self.bgcolorButton)
        self.gridLayout_10.addLayout(self.s_layout5, 0, 0, 1, 1)
        self.s_layout9 = QtWidgets.QHBoxLayout()
        self.s_layout9.setObjectName("s_layout9")
        self.itemsLabel = QtWidgets.QLabel(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.itemsLabel.setFont(font)
        self.itemsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemsLabel.setObjectName("itemsLabel")
        self.s_layout9.addWidget(self.itemsLabel)

        self.editButton = QtWidgets.QPushButton(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editButton.setFont(font)
        self.editButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editButton.setObjectName("editButton")
        self.editButton.clicked.connect(self.EditWindow.show)
        self.s_layout9.addWidget(self.editButton)
        self.gridLayout_10.addLayout(self.s_layout9, 4, 0, 1, 1)
        self.s_layout7 = QtWidgets.QVBoxLayout()
        self.s_layout7.setContentsMargins(-1, 2, -1, 2)
        self.s_layout7.setSpacing(1)
        self.s_layout7.setObjectName("s_layout7")
        self.transparencyLabel = QtWidgets.QLabel(self.settingsGroupbox2)
        font = QtGui.QFont()
        font.setFamily("Unispace")
        font.setPointSize(10)
        self.transparencyLabel.setFont(font)
        self.transparencyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.transparencyLabel.setObjectName("transparencyLabel")
        self.s_layout7.addWidget(self.transparencyLabel)
        self.transparencySlider = QtWidgets.QSlider(self.settingsGroupbox2)
        self.transparencySlider.setMinimumSize(QtCore.QSize(158, 0))
        self.transparencySlider.setMaximumSize(QtCore.QSize(158, 16777215))
        self.transparencySlider.setMaximum(255)
        self.transparencySlider.setValue(int(info['alpha']))
        self.transparencySlider.setOrientation(QtCore.Qt.Horizontal)
        self.transparencySlider.setObjectName("transparencySlider")
        self.transparencySlider.valueChanged.connect(lambda e: changeTrans(e))
        self.s_layout7.addWidget(self.transparencySlider)
        self.gridLayout_10.addLayout(self.s_layout7, 2, 0, 1, 1)
        self.s_layout3.addWidget(self.settingsGroupbox2)
        self.s_layout1.addLayout(self.s_layout3)
        self.gridLayout_2.addLayout(self.s_layout1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.settingsFrame, 0, 0, 1, 1)
        self.sideLabel.hide() #loco
        self.SideCombobox.hide() #loco

        self.settingscloseBtn.setText("x")
        self.settingsGroupbox1.setTitle("Main app")
        self.thememodeLabel.setText("Theme mode:  ")
        self.settingsGroupbox2.setTitle("OnScreen window")
        self.sideLabel.setText("Side:  ")
        self.SideCombobox.setItemText(0, "TopRight")
        self.SideCombobox.setItemText(1, "TopLeft")
        self.SideCombobox.setItemText(2, "BottomRight")
        self.SideCombobox.setItemText(3, "BottomLeft")
        self.fgcolorLabel.setText("FG Color:     ")
        self.bgcolorLabel.setText("BG Color:     ")
        self.itemsLabel.setText("Items:     ")
        self.editButton.setText("Edit")
        self.transparencyLabel.setText("Transparency:  ")

    def applySettingstheme(self, mode):
        if mode=='System':
            if darkdetect.isLight(): mode='Light'
            else: mode='Dark'

        if mode=='Light':
            self.settingsFrame.setStyleSheet(StyleSheets.frame1_light)
            self.settingsGroupbox1.setStyleSheet(StyleSheets.groupbox_light)
            self.settingsGroupbox2.setStyleSheet(StyleSheets.groupbox_light)
            self.launchStartup.setStyleSheet(StyleSheets.checkbox1_light)
            self.thememodeLabel.setStyleSheet(StyleSheets.subjects_light)
            self.thememodeSystem.setStyleSheet(StyleSheets.checkbox1_light)
            self.thememodeDark.setStyleSheet(StyleSheets.checkbox1_light)
            self.thememodeLight.setStyleSheet(StyleSheets.checkbox1_light)
            self.sideLabel.setStyleSheet(StyleSheets.subjects_light)
            self.SideCombobox.setStyleSheet(StyleSheets.combobox_light)
            self.fgcolorLabel.setStyleSheet(StyleSheets.values_light)
            self.bgcolorLabel.setStyleSheet(StyleSheets.values_light)
            self.itemsLabel.setStyleSheet(StyleSheets.values_light)
            self.editButton.setStyleSheet(StyleSheets.editbutton_light)
            self.transparencyLabel.setStyleSheet(StyleSheets.values_light)
            self.transparencySlider.setStyleSheet(StyleSheets.slider_light)

        elif mode=='Dark':
            self.settingsFrame.setStyleSheet(StyleSheets.frame1_dark)
            self.settingsGroupbox1.setStyleSheet(StyleSheets.groupbox_dark)
            self.settingsGroupbox2.setStyleSheet(StyleSheets.groupbox_dark)
            self.launchStartup.setStyleSheet(StyleSheets.checkbox1_dark)
            self.thememodeLabel.setStyleSheet(StyleSheets.subjects_dark)
            self.thememodeSystem.setStyleSheet(StyleSheets.checkbox1_dark)
            self.thememodeDark.setStyleSheet(StyleSheets.checkbox1_dark)
            self.thememodeLight.setStyleSheet(StyleSheets.checkbox1_dark)
            self.sideLabel.setStyleSheet(StyleSheets.subjects_dark)
            self.SideCombobox.setStyleSheet(StyleSheets.combobox_dark)
            self.fgcolorLabel.setStyleSheet(StyleSheets.values_dark)
            self.bgcolorLabel.setStyleSheet(StyleSheets.values_dark)
            self.itemsLabel.setStyleSheet(StyleSheets.values_dark)
            self.editButton.setStyleSheet(StyleSheets.editbutton_dark)
            self.transparencyLabel.setStyleSheet(StyleSheets.values_dark)
            self.transparencySlider.setStyleSheet(StyleSheets.slider_dark)


class editWindow(Marker):
    def __init__(self):
        super().__init__()
        self.setObjectName("Form")
        self.resize(270, 270)
        self.setMinimumSize(QtCore.QSize(270, 0))
        self.setMaximumSize(QtCore.QSize(270, 16777215))
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.setWindowIcon(QtGui.QIcon(files_+'Icon.ico'))
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self)
        self.frame.setMinimumSize(QtCore.QSize(248, 0))
        self.frame.setMaximumSize(QtCore.QSize(248, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setGraphicsEffect(shadow(self.frame, 25))
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeBtn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.closeBtn.sizePolicy().hasHeightForWidth())
        self.closeBtn.setSizePolicy(sizePolicy)
        self.closeBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.closeBtn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.closeBtn.setFont(font)
        self.closeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeBtn.setStyleSheet("border: 0px;\n"
"color: rgb(86, 86, 86);")
        self.closeBtn.setFlat(False)
        self.closeBtn.setObjectName("closeBtn")
        self.closeBtn.clicked.connect(self.hider)
        self.horizontalLayout.addWidget(self.closeBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.cpuusageCh = QtWidgets.QCheckBox(self.frame)
        self.cpuusageCh.setChecked(True)
        self.cpuusageCh.setTristate(False)
        self.cpuusageCh.setObjectName("checkBox")
        self.cpuusageCh.stateChanged.connect(lambda e: changeItems('cpuUsage', self.cpuusageCh.isChecked()))
        self.verticalLayout.addWidget(self.cpuusageCh)
        self.cputempCh = QtWidgets.QCheckBox(self.frame)
        self.cputempCh.setChecked(True)
        self.cputempCh.setTristate(False)
        self.cputempCh.setObjectName("checkBox_6")
        self.cputempCh.stateChanged.connect(lambda e: changeItems('cpuTemp', self.cputempCh.isChecked()))
        self.verticalLayout.addWidget(self.cputempCh)
        self.gpuusageCh = QtWidgets.QCheckBox(self.frame)
        self.gpuusageCh.setChecked(True)
        self.gpuusageCh.setTristate(False)
        self.gpuusageCh.setObjectName("checkBox_5")
        self.gpuusageCh.stateChanged.connect(lambda e: changeItems('gpuUsage', self.gpuusageCh.isChecked()))
        self.verticalLayout.addWidget(self.gpuusageCh)
        self.gputempCh = QtWidgets.QCheckBox(self.frame)
        self.gputempCh.setChecked(True)
        self.gputempCh.setTristate(False)
        self.gputempCh.setObjectName("checkBox_4")
        self.gputempCh.stateChanged.connect(lambda e: changeItems('gpuTemp', self.gputempCh.isChecked()))
        self.verticalLayout.addWidget(self.gputempCh)
        self.ramusageCh = QtWidgets.QCheckBox(self.frame)
        self.ramusageCh.setChecked(True)
        self.ramusageCh.setTristate(False)
        self.ramusageCh.setObjectName("checkBox_3")
        self.ramusageCh.stateChanged.connect(lambda e: changeItems('ramUsage', self.ramusageCh.isChecked()))
        self.verticalLayout.addWidget(self.ramusageCh)
        self.hard1Ch = QtWidgets.QCheckBox(self.frame)
        self.hard1Ch.setChecked(True)
        self.hard1Ch.setTristate(False)
        self.hard1Ch.setObjectName("checkBox_2")
        self.hard1Ch.stateChanged.connect(lambda e: changeItems('hard1Temp', self.hard1Ch.isChecked()))
        self.verticalLayout.addWidget(self.hard1Ch)
        self.hard2Ch = QtWidgets.QCheckBox(self.frame)
        self.hard2Ch.setChecked(True)
        self.hard2Ch.setTristate(False)
        self.hard2Ch.setObjectName("checkBox_7")
        self.hard2Ch.stateChanged.connect(lambda e: changeItems('hard2Temp', self.hard2Ch.isChecked()))

        items = info["items"]
        if not '1' in items:
            self.cpuusageCh.setChecked(False)
        if not '2' in items:
            self.cputempCh.setChecked(False)
        if not '3' in items:
            self.gpuusageCh.setChecked(False)
        if not '4' in items:
            self.gputempCh.setChecked(False)
        if not '5' in items:
            self.ramusageCh.setChecked(False)
        if not '6' in items:
            self.hard1Ch.setChecked(False)
        if not '7' in items:
            self.hard2Ch.setChecked(False)

        self.verticalLayout.addWidget(self.hard2Ch)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.setWindowTitle("Edit")
        self.closeBtn.setText("x")
        self.cpuusageCh.setText("CPU Usage")
        self.cputempCh.setText("CPU Temp")
        self.gpuusageCh.setText("GPU Usage")
        self.gputempCh.setText("GPU Temp")
        self.ramusageCh.setText("RAM Usage")
        self.hard1Ch.setText("HARD1 Temp")
        self.hard2Ch.setText("HARD2 Temp")

    def applyEdittheme(self, mode):
        if mode=='System':
            if darkdetect.isLight(): mode='Light'
            else: mode='Dark'

        if mode=='Light':
            self.frame.setStyleSheet(StyleSheets.frame1_light)
            self.cpuusageCh.setStyleSheet(StyleSheets.checkbox2_light)
            self.cputempCh.setStyleSheet(StyleSheets.checkbox2_light)
            self.gpuusageCh.setStyleSheet(StyleSheets.checkbox2_light)
            self.gputempCh.setStyleSheet(StyleSheets.checkbox2_light)
            self.ramusageCh.setStyleSheet(StyleSheets.checkbox2_light)
            self.hard1Ch.setStyleSheet(StyleSheets.checkbox2_light)
            self.hard2Ch.setStyleSheet(StyleSheets.checkbox2_light)
        
        elif mode=='Dark':
            self.frame.setStyleSheet(StyleSheets.frame1_dark)
            self.cpuusageCh.setStyleSheet(StyleSheets.checkbox2_dark)
            self.cputempCh.setStyleSheet(StyleSheets.checkbox2_dark)
            self.gpuusageCh.setStyleSheet(StyleSheets.checkbox2_dark)
            self.gputempCh.setStyleSheet(StyleSheets.checkbox2_dark)
            self.ramusageCh.setStyleSheet(StyleSheets.checkbox2_dark)
            self.hard1Ch.setStyleSheet(StyleSheets.checkbox2_dark)
            self.hard2Ch.setStyleSheet(StyleSheets.checkbox2_dark)

class aboutWindow(Marker):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('About')
        self.setWindowIcon(QtGui.QIcon(files_+'Icon.ico'))
        self.resize(340, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(340, 488))
        self.setMaximumSize(QtCore.QSize(340, 488))
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.aboutFrame = QtWidgets.QLabel(self)
        self.aboutFrame.setGeometry(QtCore.QRect(11, 14, 317, 465))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutFrame.sizePolicy().hasHeightForWidth())
        self.aboutFrame.setSizePolicy(sizePolicy)
        self.aboutFrame.setMinimumSize(QtCore.QSize(317, 465))
        self.aboutFrame.setMaximumSize(QtCore.QSize(317, 465))
        self.aboutFrame.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.aboutFrame.setText("")
        self.aboutFrame.setGraphicsEffect(shadow(self.aboutFrame, 22))
        self.aboutFrame.setPixmap(QtGui.QPixmap(files_+"About-dark.png"))
        self.aboutFrame.setScaledContents(True)
        self.aboutFrame.setObjectName("aboutFrame")
        self.aboutcloseBtn = QtWidgets.QPushButton(self)
        self.aboutcloseBtn.setGeometry(QtCore.QRect(276, 20, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.aboutcloseBtn.sizePolicy().hasHeightForWidth())
        self.aboutcloseBtn.setSizePolicy(sizePolicy)
        self.aboutcloseBtn.setMinimumSize(QtCore.QSize(40, 40))
        self.aboutcloseBtn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.aboutcloseBtn.setFont(font)
        self.aboutcloseBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutcloseBtn.setStyleSheet("border: 0px;\n"
"color: rgb(86, 86, 86);")
        self.aboutcloseBtn.setFlat(False)
        self.aboutcloseBtn.setObjectName("aboutcloseBtn")
        self.aboutcloseBtn.clicked.connect(self.hider)
        self.gmailButton = QtWidgets.QPushButton(self)
        self.gmailButton.setGeometry(QtCore.QRect(131, 398, 80, 69))
        self.gmailButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gmailButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.gmailButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(files_+"Gmail.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gmailButton.setIcon(icon)
        self.gmailButton.setIconSize(QtCore.QSize(50, 50))
        self.gmailButton.setObjectName("gmailButton")
        self.gmailButton.clicked.connect(lambda: webbrowser.open('mailto:hosseinbahiraei81@gmail.com?subject=Hi LoCo&body=Your feedback'))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.aboutcloseBtn.setText(_translate("Form", "x"))

class styleSheets:
    frame1_light = "background-color: rgb(250, 245, 255);\nborder-radius: 18px;"
    settingsframe_light = "border: 0;\nborder-radius: 6px;\nbackground-color: rgba(235, 235, 235, 0);"
    onscreenbtn_light = "border: 0;\nborder-radius: 6px;\nbackground-color: rgb(230, 225, 235);\ncolor: rgb(85, 80, 90);"
    settingsbtn_light = "border: 0;\nbackground-color: rgba(255, 255, 255, 0);"
    frame2_light = ("QGroupBox {\n"
"    border: 0px solid silver;\n"
"    border-radius: 12px;\n"
"    margin-top: 9px;\n"
"    background-color: rgb(233, 228, 238);\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
    groupbox_light = ("QGroupBox {\n"
"    border: 0px solid silver;\n"
"    border-radius: 12px;\n"
"    margin-top: 14px;\n"
"    background-color: rgb(220, 215, 225);\n"
"    color: rgb(5, 0, 10);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
    subjects_light = "color: rgb(85, 80, 90);\nbackground-color: rgba(255, 255, 255, 0);"
    values_light = "color: rgb(105, 100, 110);\nbackground-color: rgba(255, 255, 255, 0);"
    values_persents_light = "background-color: rgba(244, 244, 244, 0);\ncolor: rgb(135, 120, 130)"
    usage_chart_light = ("QProgressBar\n"
"{\n"
"border: 0px solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.482, y1:0, x2:0.472, y2:1, stop:0 rgba(193, 0, 0, 255), stop:0.120603 rgba(200, 62, 0, 255), stop:0.241206 rgba(205, 95, 0, 255), stop:0.346734 rgba(205, 130, 0, 255), stop:0.507538 rgba(200, 170, 0, 255), stop:0.628141 rgba(183, 189, 0, 255), stop:0.748744 rgba(153, 200, 0, 255), stop:0.879397 rgba(107, 201, 0, 255), stop:1 rgba(8, 203, 0, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(238, 233, 243);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    usage_chart2_light = ("QProgressBar\n"
"{\n"
"border: 0px solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.482, y1:0, x2:0.472, y2:1, stop:0 rgba(193, 0, 0, 255), stop:0.120603 rgba(200, 62, 0, 255), stop:0.241206 rgba(205, 95, 0, 255), stop:0.346734 rgba(205, 130, 0, 255), stop:0.507538 rgba(200, 170, 0, 255), stop:0.628141 rgba(183, 189, 0, 255), stop:0.748744 rgba(153, 200, 0, 255), stop:0.879397 rgba(107, 201, 0, 255), stop:1 rgba(8, 203, 0, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(225, 220, 230);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    temp_chart_light = ("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.486, y2:1, stop:0 rgba(211, 0, 0, 255), stop:1 rgba(5, 0, 211, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(238, 233, 243);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    temp_chart2_light = ("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.486, y2:1, stop:0 rgba(211, 0, 0, 255), stop:1 rgba(5, 0, 211, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(225, 220, 230);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    groupbox2_light = ("QGroupBox {\n"
"    border: 0px solid silver;\n"
"    border-radius: 12px;\n"
"    margin-top: 16px;\n"
"    background-color: rgb(233, 228, 238);\n"
"    color: rgb(104, 10, 184);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
    line_light = "background-color: rgb(208, 203, 213);"
    ram_light = "background-color: rgba(238, 238, 238, 0);color: rgb(85, 80, 90);"
    ram2_light = "background-color: rgba(238, 238, 238, 0);color: rgb(105, 100, 110);"
    combobox_light = ("QComboBox\n"
"{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(55, 50, 60);\n"
"}\n"
"QComboBox:drop-down\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"QComboBox::drop-down::button\n"
"{\n"
"    border: 0px;\n"
"    width: 0px;\n"
"}")
    editbutton_light = ("color: rgb(95, 90, 100);\n"
"border-radius: 4px;\nbackground-color: rgb(200, 195, 205);")
    slider_light = ("QSlider {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    background-color: rgb(250, 245, 255);\n"
"    border: 0px;\n"
"    height: 7px;\n"
"    margin: 0px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(125, 120, 130);\n"
"    border: 0px;\n"
"    height: 20px;\n"
"    width: 10px;\n"
"    margin: -5px 0px;\n"
"}")
    checkbox1_light = ("""QCheckBox{
	background-color: rgba(255, 255, 255, 0);
	color: rgb(45, 40, 50);
}
QCheckBox::indicator{
	border-radius: 3px;
}
QCheckBox::indicator::checked{
	background-color: rgb(50, 10, 105);
}
QCheckBox::indicator::unchecked{
	background-color: rgb(200, 195, 205);
}""")
    checkbox2_light = ("""QCheckBox{
	background-color: rgba(255, 255, 255, 0);
	color: rgb(45, 40, 50);
}
QCheckBox::indicator{
	border-radius: 3px;
}
QCheckBox::indicator::checked{
	background-color: rgb(50, 10, 105);
}
QCheckBox::indicator::unchecked{
	background-color: rgb(220, 215, 225);
}""")


    frame1_dark = "background-color: rgb(31, 29, 33);\nborder-radius: 18px;"
    settingsframe_dark = "border: 0;\nborder-radius: 6px;\nbackground-color: rgba(50, 50, 50, 0);"
    onscreenbtn_dark = "border: 0;\nborder-radius: 6px;\nbackground-color: rgb(51, 49, 53);\ncolor: rgb(140, 140, 140);"
    settingsbtn_dark = "border: 0;\nbackground-color: rgba(255, 255, 255, 0);"
    frame2_dark = ("QGroupBox {\n"
"    border: 0px solid silver;\n"
"    border-radius: 12px;\n"
"    margin-top: 9px;\n"
"    background-color: rgb(48, 46, 50);\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
    groupbox_dark = ("QGroupBox {\n"
"    border: 0px solid silver;\n"
"    border-radius: 12px;\n"
"    margin-top: 14px;\n"
"    background-color: rgb(59, 57, 61);\n"
"    color: rgb(226, 224, 228);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
    subjects_dark = "color: rgb(166, 164, 168);\nbackground-color: rgba(255, 255, 255, 0);"
    values_dark = "color: rgb(141, 139, 143);\nbackground-color: rgba(255, 255, 255, 0);"
    values_persents_dark = "background-color: rgba(200, 200, 200, 0);\ncolor: rgb(131, 129, 133)"
    usage_chart_dark = ("QProgressBar\n"
"{\n"
"border: 0px solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.482, y1:0, x2:0.472, y2:1, stop:0 rgba(193, 0, 0, 255), stop:0.120603 rgba(200, 62, 0, 255), stop:0.241206 rgba(205, 95, 0, 255), stop:0.346734 rgba(205, 130, 0, 255), stop:0.507538 rgba(200, 170, 0, 255), stop:0.628141 rgba(183, 189, 0, 255), stop:0.748744 rgba(153, 200, 0, 255), stop:0.879397 rgba(107, 201, 0, 255), stop:1 rgba(8, 203, 0, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(46, 44, 48);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    usage_chart2_dark = ("QProgressBar\n"
"{\n"
"border: 0px solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.482, y1:0, x2:0.472, y2:1, stop:0 rgba(193, 0, 0, 255), stop:0.120603 rgba(200, 62, 0, 255), stop:0.241206 rgba(205, 95, 0, 255), stop:0.346734 rgba(205, 130, 0, 255), stop:0.507538 rgba(200, 170, 0, 255), stop:0.628141 rgba(183, 189, 0, 255), stop:0.748744 rgba(153, 200, 0, 255), stop:0.879397 rgba(107, 201, 0, 255), stop:1 rgba(8, 203, 0, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(56, 54, 58);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    temp_chart_dark = ("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.486, y2:1, stop:0 rgba(211, 0, 0, 255), stop:1 rgba(5, 0, 211, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(46, 44, 48);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    temp_chart2_dark = ("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 5px;\n"
"background-color: qlineargradient(spread:pad, x1:0.477, y1:0, x2:0.486, y2:1, stop:0 rgba(211, 0, 0, 255), stop:1 rgba(5, 0, 211, 255));\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: rgb(56, 54, 58);\n"
"border-top-left-radius :5px;\n"
"border-top-right-radius :5px;\n"
"}    ")
    groupbox2_dark = ("QGroupBox {\n"
"    border: 0px solid silver;\n"
"    border-radius: 12px;\n"
"    margin-top: 16px;\n"
"    color: rgb(108, 17, 184);\n"
"    background-color: rgb(48, 46, 50);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0px 5px 0px 5px;\n"
"}")
    line_dark = "background-color: rgb(43, 41, 45);"
    ram_dark = "background-color: rgba(238, 238, 238, 0);color: rgb(166, 164, 168);"
    ram2_dark = "background-color: rgba(238, 238, 238, 0);color: rgb(146, 144, 148);"
    combobox_dark = ("QComboBox\n"
"{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(191, 189, 193);\n"
"}\n"
"QComboBox:drop-down\n"
"{\n"
"    border-radius: 0px;\n"
"}\n"
"QComboBox::drop-down::button\n"
"{\n"
"    border: 0px;\n"
"    width: 0px;\n"
"}")
    editbutton_dark = ("color: rgb(141, 139, 143);\n"
"border-radius: 4px;\nbackground-color: rgb(36, 34, 38);")
    slider_dark = ("QSlider {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    background-color: rgb(31, 29, 33);\n"
"    border: 0px;\n"
"    height: 7px;\n"
"    margin: 0px;\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(131, 129, 133);\n"
"    border: 0px;\n"
"    height: 20px;\n"
"    width: 10px;\n"
"    margin: -5px 0px;\n"
"}")
    checkbox1_dark = ("""QCheckBox{
	background-color: rgba(255, 255, 255, 0);
	color: rgb(181, 179, 183);
}
QCheckBox::indicator{
	border-radius: 3px;
}
QCheckBox::indicator::checked{
	background-color: rgb(50, 10, 105);
}
QCheckBox::indicator::unchecked{
	background-color: rgb(36, 34, 38);
}""")
    checkbox2_dark = ("""QCheckBox{
	background-color: rgba(255, 255, 255, 0);
	color: rgb(180, 180, 180);
}
QCheckBox::indicator{
	border-radius: 3px;
}
QCheckBox::indicator::checked{
	background-color: rgb(50, 10, 105);
}
QCheckBox::indicator::unchecked{
	background-color: rgb(22, 20, 24);
}""")
StyleSheets = styleSheets()


def set_autostart_registry(app_name, key_data=None, autostart: bool = True) -> bool:
    """
    Create/update/delete Windows autostart registry key

    ! Windows ONLY
    ! If the function fails, OSError is raised.

    :param app_name:    A string containing the name of the application name
    :param key_data:    A string that specifies the application path.
    :param autostart:   True - create/update autostart key / False - delete autostart key
    :return:            True - Success / False - Error, app name dont exist
    """

    with winreg.OpenKey(
            key=winreg.HKEY_CURRENT_USER,
            sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
            reserved=0,
            access=winreg.KEY_ALL_ACCESS,
    ) as key:
        try:
            if autostart:
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, key_data)
            else:
                winreg.DeleteValue(key, app_name)
        except OSError:
            return False
    return True


def check_autostart_registry(value_name):
    """
    Check Windows autostart registry status

    ! Windows ONLY
    ! If the function fails, OSError is raised.

    :param value_name:  A string containing the name of the application name
    :return: True - Exist / False - Not exist
    """

    with winreg.OpenKey(
            key=winreg.HKEY_CURRENT_USER,
            sub_key=r'Software\Microsoft\Windows\CurrentVersion\Run',
            reserved=0,
            access=winreg.KEY_ALL_ACCESS,
    ) as key:
        idx = 0
        while idx < 1_000:     # Max 1.000 values
            try:
                key_name, _, _ = winreg.EnumValue(key, idx)
                if key_name == value_name:
                    return True
                idx += 1
            except OSError:
                break
    return False



global info
info = {}

def save():
    string = ''
    for i in list(info.keys()):
        string+=i+'='+info[i]+'\n'
    file = open(f'{data_}PerfoTor.data', 'w')
    file.write(base64.b85encode(string.encode()).decode()[::-1])
    file.close()

def restore():
    if os.path.exists(f'{data_}PerfoTor.data'):
        file = open(f'{data_}PerfoTor.data', 'r')
        string = base64.b85decode(file.read()[::-1]).decode().strip('\n')
        for line in string.split('\n'):
            info[line.strip('\n').split('=')[0]] = line.strip('\n').split('=')[1]
        file.close()
    else:
        info['autostart'] = 'false'
        info['theme'] = 'system'
        info['bg'] = '110,35,120'
        info['fg'] = '255,255,255'
        info['alpha'] = '100'
        info['items'] = '1234567'
        info['onscreen'] = 'false'
restore()