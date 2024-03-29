# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QApplication

from Skiimage_Func import Skiimage_Functions
from Common_Proc import Common_Proc

class Ui_MainWindow(Skiimage_Functions,object):
    
    def __init__(self):
        """
        Constructor of runner

        Returns
        -------
        None.

        """
        super().__init__()
    
    def setupUi(self, MainWindow):
        """
        GUI

        Parameters
        ----------
        MainWindow : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        #MAIN WINDOW
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        #GroupBox SOURCE_IMAGE
        self.groupBox_Input_Image = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Input_Image.setMinimumSize(QtCore.QSize(400, 500))
        self.groupBox_Input_Image.setObjectName("groupBox_Input_Image")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_Input_Image)
        self.gridLayout_2.setObjectName("gridLayout_2")
        #Label SOURCE_IMAGE
        self.Label_Source_Image = QtWidgets.QLabel(self.groupBox_Input_Image)
        self.Label_Source_Image.setMinimumSize(QtCore.QSize(200, 200))
        self.Label_Source_Image.setMaximumSize(QtCore.QSize(600, 600))
        self.Label_Source_Image.setAutoFillBackground(True)
        self.Label_Source_Image.setText("")
        self.Label_Source_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Source_Image.setObjectName("Label_Source_Image")
        
        self.gridLayout_2.addWidget(self.Label_Source_Image, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_Input_Image)
        #GroupBox OUTPUT_IMAGE
        self.groupBox_Output_Image = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Output_Image.setMinimumSize(QtCore.QSize(400, 500))
        self.groupBox_Output_Image.setObjectName("groupBox_Output_Image")
        
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_Output_Image)
        self.gridLayout_3.setObjectName("gridLayout_3")
        #Label OUTPUT_IMAGE
        self.Label_Output_Image = QtWidgets.QLabel(self.groupBox_Output_Image)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Label_Output_Image.sizePolicy().hasHeightForWidth())
        
        self.Label_Output_Image.setSizePolicy(sizePolicy)
        self.Label_Output_Image.setMinimumSize(QtCore.QSize(200, 200))
        self.Label_Output_Image.setMaximumSize(QtCore.QSize(600, 600))
        self.Label_Output_Image.setMouseTracking(False)
        self.Label_Output_Image.setAutoFillBackground(True)
        self.Label_Output_Image.setText("")
        self.Label_Output_Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Label_Output_Image.setObjectName("Label_Output_Image")
        
        self.gridLayout_3.addWidget(self.Label_Output_Image, 0, 0, 1, 1)
        self.horizontalLayout_7.addWidget(self.groupBox_Output_Image)
        
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        #GroupBox SOURCE
        self.groupBox_Source = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Source.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_Source.setObjectName("groupBox_Source")
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_Source)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        #Button SOURCE_INPUT
        self.Button_Source_Input = QtWidgets.QPushButton(self.groupBox_Source)
        self.Button_Source_Input.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Source_Input.setObjectName("Button_Source_Input")
        self.Button_Source_Input.clicked.connect(lambda : Common_Proc.File(self))
        
        self.horizontalLayout_5.addWidget(self.Button_Source_Input)
        #Button SOURCE_EXPORT
        self.Button_Source_Export = QtWidgets.QPushButton(self.groupBox_Source)
        self.Button_Source_Export.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Source_Export.setObjectName("Button_Source_Export")
        self.Button_Source_Export.setEnabled(False)
        self.Button_Source_Export.clicked.connect(lambda : Common_Proc.Export_As_Source(self))
        
        self.horizontalLayout_5.addWidget(self.Button_Source_Export)
        #Button SOURCE_CLEAR
        self.Button_Source_Clear = QtWidgets.QPushButton(self.groupBox_Source)
        self.Button_Source_Clear.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Source_Clear.setObjectName("Button_Source_Clear")
        self.Button_Source_Clear.setEnabled(False)
        self.Button_Source_Clear.clicked.connect(lambda : Common_Proc.Clear_Source(self))

        
        
        self.horizontalLayout_5.addWidget(self.Button_Source_Clear, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6.addWidget(self.groupBox_Source)
        
        #GroupBox OUTPUT
        self.groupBox_Output = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Output.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_Output.setObjectName("groupBox_Output")
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_Output)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #Button OUTPUT_SAVE
        self.Button_Output_Save = QtWidgets.QPushButton(self.groupBox_Output)
        self.Button_Output_Save.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Output_Save.setObjectName("Button_Output_Save")
        self.Button_Output_Save.setEnabled(False)
        self.Button_Output_Save.clicked.connect(lambda : Common_Proc.Save_Output(self))
        
        self.horizontalLayout_3.addWidget(self.Button_Output_Save)
        #Button OUTPUT_SAVE_AS
        self.Button_Output_SaveAs = QtWidgets.QPushButton(self.groupBox_Output)
        self.Button_Output_SaveAs.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Output_SaveAs.setObjectName("Button_Output_SaveAs")
        self.Button_Output_SaveAs.setEnabled(False)
        self.Button_Output_SaveAs.clicked.connect(lambda : Common_Proc.Save_As_Output(self))
        
        self.horizontalLayout_3.addWidget(self.Button_Output_SaveAs)
        #Button OUTPUT_EXPORT_AS
        self.Button_Output_ExportAs = QtWidgets.QPushButton(self.groupBox_Output)
        self.Button_Output_ExportAs.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Output_ExportAs.setObjectName("Button_Output_ExportAs")
        self.Button_Output_ExportAs.setEnabled(False)
        self.Button_Output_ExportAs.clicked.connect(lambda : Common_Proc.Export_As_Output(self))
        
        self.horizontalLayout_3.addWidget(self.Button_Output_ExportAs)
        #Button OUTPUT_CLEAR
        self.Button_Output_Clear = QtWidgets.QPushButton(self.groupBox_Output)
        self.Button_Output_Clear.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Output_Clear.setObjectName("Button_Output_Clear")
        self.Button_Output_Clear.setEnabled(False)
        self.Button_Output_Clear.clicked.connect(lambda : Common_Proc.Clear_Output(self))

        
        
        self.horizontalLayout_3.addWidget(self.Button_Output_Clear)
        #Button OUTPUT_UNDO
        self.Button_Output_Undo = QtWidgets.QPushButton(self.groupBox_Output)
        self.Button_Output_Undo.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Output_Undo.setObjectName("Button_Output_Undo")
        self.Button_Output_Undo.setEnabled(False)
        self.Button_Output_Undo.clicked.connect(lambda : Common_Proc.Undo(self))
        self.Button_Output_Undo.clicked.connect(lambda : Common_Proc.Output_Show(self))
        
        self.horizontalLayout_3.addWidget(self.Button_Output_Undo)
        #Button OUTPUT_REDO
        self.Button_Output_Redo = QtWidgets.QPushButton(self.groupBox_Output)
        self.Button_Output_Redo.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Output_Redo.setObjectName("Button_Output_Redo")
        self.Button_Output_Redo.setEnabled(False)
        self.Button_Output_Redo.clicked.connect(lambda : Common_Proc.Redo(self))
        self.Button_Output_Redo.clicked.connect(lambda : Common_Proc.Output_Show(self))
        
        
        self.horizontalLayout_3.addWidget(self.Button_Output_Redo, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6.addWidget(self.groupBox_Output)
        
        #GroupBox COLOR CONVERSION
        self.groupBox_Color_Conversion = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Color_Conversion.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_Color_Conversion.setAutoFillBackground(False)
        self.groupBox_Color_Conversion.setFlat(False)
        self.groupBox_Color_Conversion.setObjectName("groupBox_Color_Conversion")
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_Color_Conversion)        
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #Button RGB2HSV
        self.Button_Color_RGB2HSV = QtWidgets.QPushButton(self.groupBox_Color_Conversion)
        self.Button_Color_RGB2HSV.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Color_RGB2HSV.setObjectName("Button_Color_RGB2HSV")
        self.Button_Color_RGB2HSV.setEnabled(False)
        self.Button_Color_RGB2HSV.clicked.connect(lambda : Skiimage_Functions.Skiimage_RGB2HSV(self))
        self.Button_Color_RGB2HSV.clicked.connect(lambda : Common_Proc.Output_Show(self))
        
        self.horizontalLayout_2.addWidget(self.Button_Color_RGB2HSV)
        #Button RGB2GREY
        self.Button_Color_RGB2Grey = QtWidgets.QPushButton(self.groupBox_Color_Conversion)
        self.Button_Color_RGB2Grey.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Color_RGB2Grey.setObjectName("Button_Color_RGB2Grey")
        self.Button_Color_RGB2Grey.setEnabled(False)
        self.Button_Color_RGB2Grey.clicked.connect(lambda : Skiimage_Functions.Skiimage_RGB2Gray(self))
        self.Button_Color_RGB2Grey.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        self.horizontalLayout_2.addWidget(self.Button_Color_RGB2Grey, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6.addWidget(self.groupBox_Color_Conversion)
        
        #GroupBox SEGMENTATION
        self.groupBox_Segmentation = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Segmentation.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_Segmentation.setObjectName("groupBox_Segmentation")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_Segmentation)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #Button CHAN_VESE
        self.Button_Seg_ChanVese = QtWidgets.QPushButton(self.groupBox_Segmentation)
        self.Button_Seg_ChanVese.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Seg_ChanVese.setObjectName("Button_Seg_ChanVese")
        self.Button_Seg_ChanVese.setEnabled(False)
        self.Button_Seg_ChanVese.clicked.connect(lambda : Skiimage_Functions.Skiimage_Chan_Vese(self))
        self.Button_Seg_ChanVese.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        
        
        self.horizontalLayout.addWidget(self.Button_Seg_ChanVese)
        #Button MULTI_OTSU
        self.Button_Seg_Otsu = QtWidgets.QPushButton(self.groupBox_Segmentation)
        self.Button_Seg_Otsu.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Seg_Otsu.setObjectName("Button_Seg_Otsu")
        self.Button_Seg_Otsu.setEnabled(False)
        self.Button_Seg_Otsu.clicked.connect(lambda : Skiimage_Functions.Skiimage_Otsu(self))
        self.Button_Seg_Otsu.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        self.horizontalLayout.addWidget(self.Button_Seg_Otsu)
        #Button MORPHOLOGICAL_SNAKES
        self.Button_Seg_Morp = QtWidgets.QPushButton(self.groupBox_Segmentation)
        self.Button_Seg_Morp.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Seg_Morp.setObjectName("Button_Seg_Morp")
        self.Button_Seg_Morp.setEnabled(False)
        self.Button_Seg_Morp.clicked.connect(lambda : Skiimage_Functions.Skiimage_Morp_Snake(self))
        self.Button_Seg_Morp.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        
        self.horizontalLayout.addWidget(self.Button_Seg_Morp, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6.addWidget(self.groupBox_Segmentation)
        
        #GroupBox EDGE DETECTION
        self.groupBox_EdgeDetection = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_EdgeDetection.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_EdgeDetection.setObjectName("groupBox_EdgeDetection")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_EdgeDetection)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #Button EDGE_SCHARR
        self.Button_Edge_Scharr = QtWidgets.QPushButton(self.groupBox_EdgeDetection)
        self.Button_Edge_Scharr.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Edge_Scharr.setObjectName("Button_Edge_Scharr")
        self.Button_Edge_Scharr.setEnabled(False)
        self.Button_Edge_Scharr.clicked.connect(lambda : Skiimage_Functions.Skiimage_Scharr(self))
        self.Button_Edge_Scharr.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        self.horizontalLayout_4.addWidget(self.Button_Edge_Scharr)
        #Button EDGE_ROBERTS
        self.Button_Edge_Roberts = QtWidgets.QPushButton(self.groupBox_EdgeDetection)
        self.Button_Edge_Roberts.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Edge_Roberts.setObjectName("Button_Edge_Roberts")
        self.Button_Edge_Roberts.setEnabled(False)
        self.Button_Edge_Roberts.clicked.connect(lambda : Skiimage_Functions.Skiimage_Roberts(self))
        self.Button_Edge_Roberts.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        
        
        self.horizontalLayout_4.addWidget(self.Button_Edge_Roberts)
        #Button EDGE_SOBEL
        self.Button_Edge_Sobel = QtWidgets.QPushButton(self.groupBox_EdgeDetection)
        self.Button_Edge_Sobel.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Edge_Sobel.setObjectName("Button_Edge_Sobel")
        self.Button_Edge_Sobel.setEnabled(False)
        self.Button_Edge_Sobel.clicked.connect(lambda : Skiimage_Functions.Skiimage_Sobel(self))
        self.Button_Edge_Sobel.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        
        self.horizontalLayout_4.addWidget(self.Button_Edge_Sobel)
        #Button EDGE_PREWITT
        self.Button_Edge_Prewitt = QtWidgets.QPushButton(self.groupBox_EdgeDetection)
        self.Button_Edge_Prewitt.setMaximumSize(QtCore.QSize(40, 25))
        self.Button_Edge_Prewitt.setObjectName("Button_Edge_Prewitt")
        self.Button_Edge_Prewitt.setEnabled(False)
        self.Button_Edge_Prewitt.clicked.connect(lambda : Skiimage_Functions.Skiimage_Prewitt(self))
        self.Button_Edge_Prewitt.clicked.connect(lambda : Skiimage_Functions.Output_Show(self))
        
        
        
        self.horizontalLayout_4.addWidget(self.Button_Edge_Prewitt, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_6.addWidget(self.groupBox_EdgeDetection)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #MENUBAR
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 26))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setObjectName("menuExport_As")
        
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setObjectName("menuClear")
        
        self.menuSegmentation = QtWidgets.QMenu(self.menubar)
        self.menuSegmentation.setObjectName("menuSegmentation")
        
        self.menuEdge_Detection = QtWidgets.QMenu(self.menubar)
        self.menuEdge_Detection.setObjectName("menuEdge_Detection")
        
        self.menuColor_Conversion = QtWidgets.QMenu(self.menubar)
        self.menuColor_Conversion.setObjectName("menuColor_Conversion")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.showMessage("Application succesfully opened")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionRGB_to_HSV = QtWidgets.QAction(MainWindow)
        self.actionRGB_to_HSV.setVisible(True)
        self.actionRGB_to_HSV.setIconVisibleInMenu(True)
        self.actionRGB_to_HSV.setObjectName("actionRGB_to_HSV")
        
        self.actionRGB_Grey = QtWidgets.QAction(MainWindow)
        self.actionRGB_Grey.setObjectName("actionRGB_Grey")
        
        self.actionScharr = QtWidgets.QAction(MainWindow)
        self.actionScharr.setObjectName("actionScharr")
        
        self.actionRoberts = QtWidgets.QAction(MainWindow)
        self.actionRoberts.setObjectName("actionRoberts")
        
        self.actionSobel = QtWidgets.QAction(MainWindow)
        self.actionSobel.setObjectName("actionSobel")
        
        self.actionPrewit = QtWidgets.QAction(MainWindow)
        self.actionPrewit.setObjectName("actionPrewit")
        
        self.actionChan_Vese_Segmentation = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ChanVese.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChan_Vese_Segmentation.setIcon(icon)
        self.actionChan_Vese_Segmentation.setObjectName("actionChan_Vese_Segmentation")
        self.actionOtsu_Segmentation = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("otsu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOtsu_Segmentation.setIcon(icon1)
        self.actionOtsu_Segmentation.setObjectName("actionOtsu_Segmentation")
        self.actionMorpSnakes_Segmentation = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("morphological.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMorpSnakes_Segmentation.setIcon(icon2)
        self.actionMorpSnakes_Segmentation.setObjectName("actionMorpSnakes_Segmentation")
        self.actionOpen_Source = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("open_source.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Source.setIcon(icon3)
        self.actionOpen_Source.setObjectName("actionOpen_Source")
        self.actionSave_Output = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Save-PNG-Image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_Output.setIcon(icon4)
        self.actionSave_Output.setObjectName("actionSave_Output")
        self.actionSave_As_Output = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As_Output.setIcon(icon5)
        self.actionSave_As_Output.setObjectName("actionSave_As_Output")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionSource_menuExport_As = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("input.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSource_menuExport_As.setIcon(icon7)
        self.actionSource_menuExport_As.setObjectName("actionSource_menuExport_As")
        self.actionOutput_menuExport_As = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("output.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOutput_menuExport_As.setIcon(icon8)
        self.actionOutput_menuExport_As.setObjectName("actionOutput_menuExport_As")
        self.actionUndo_Output = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo_Output.setIcon(icon9)
        self.actionUndo_Output.setObjectName("actionUndo_Output")
        self.actionRedo_Output = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo_Output.setIcon(icon10)
        self.actionRedo_Output.setObjectName("actionRedo_Output")
        self.actionClear_Source = QtWidgets.QAction(MainWindow)
        self.actionClear_Source.setIcon(icon7)
        self.actionClear_Source.setObjectName("actionClear_Source")
        self.actionClear_Output = QtWidgets.QAction(MainWindow)
        self.actionClear_Output.setIcon(icon8)
        self.actionClear_Output.setObjectName("actionClear_Output")
        
        
        #FILE MENU SIGNALS
        
        
        self.menuExport_As.addAction(self.actionSource_menuExport_As)
        #default enabled
        self.actionSource_menuExport_As.setEnabled(False)
        self.actionSource_menuExport_As.triggered.connect(lambda : Common_Proc.Export_As_Source(self))
        
        self.menuExport_As.addAction(self.actionOutput_menuExport_As)
        #default enabled
        self.actionOutput_menuExport_As.setEnabled(False)
        self.actionOutput_menuExport_As.triggered.connect(lambda : Common_Proc.Export_As_Output(self))
        
        self.menuFile.addAction(self.actionOpen_Source)
        #connecting with file searching window (QFileDialog)
        self.actionOpen_Source.triggered.connect(lambda : Common_Proc.File(self))
        
        self.menuFile.addAction(self.actionSave_Output)
        #default enabled
        self.actionSave_Output.setEnabled(False)
        self.actionSave_Output.triggered.connect(lambda : Common_Proc.Save_Output(self))
        
        self.menuFile.addAction(self.actionSave_As_Output)
        #default enabled
        self.actionSave_As_Output.setEnabled(False)
        self.actionOutput_menuExport_As.triggered.connect(lambda : Common_Proc.Save_As_Output(self))
    
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addAction(self.actionExit)
        #default enabled
         # self.actionExit.setEnabled(False)
        # self.actionExit.triggered.connect(self.close)
        
        
        self.menuClear.addAction(self.actionClear_Source)
        self.actionClear_Source.setEnabled(False)
        self.actionClear_Source.triggered.connect(lambda : Common_Proc.Clear_Source(self))
        
        self.menuClear.addAction(self.actionClear_Output)
        self.actionClear_Output.setEnabled(False)
        self.actionClear_Output.triggered.connect(lambda : Common_Proc.Clear_Output(self))
        
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addAction(self.actionUndo_Output)
        self.actionUndo_Output.setEnabled(False)
        self.actionUndo_Output.triggered.connect(lambda : Common_Proc.Undo(self))
        self.actionUndo_Output.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuEdit.addAction(self.actionRedo_Output)
        self.actionRedo_Output.setEnabled(False)
        self.actionRedo_Output.triggered.connect(lambda : Common_Proc.Redo(self))
        self.actionRedo_Output.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        
        self.menuSegmentation.addAction(self.actionChan_Vese_Segmentation)
        self.actionChan_Vese_Segmentation.setEnabled(False)
        self.actionChan_Vese_Segmentation.triggered.connect(lambda : Skiimage_Functions.Skiimage_Chan_Vese(self))
        self.actionChan_Vese_Segmentation.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuSegmentation.addAction(self.actionOtsu_Segmentation)
        self.actionOtsu_Segmentation.setEnabled(False)
        self.actionOtsu_Segmentation.triggered.connect(lambda : Skiimage_Functions.Skiimage_Otsu(self))
        self.actionOtsu_Segmentation.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        
        self.menuSegmentation.addAction(self.actionMorpSnakes_Segmentation)
        self.actionMorpSnakes_Segmentation.setEnabled(False)
        self.actionMorpSnakes_Segmentation.triggered.connect(lambda : Skiimage_Functions.Skiimage_Scharr(self))
        self.actionMorpSnakes_Segmentation.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        
        self.menuEdge_Detection.addAction(self.actionScharr)
        self.actionScharr.setEnabled(False)
        self.actionScharr.triggered.connect(lambda : Skiimage_Functions.Skiimage_Scharr(self))
        self.actionScharr.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuEdge_Detection.addAction(self.actionRoberts)
        self.actionRoberts.setEnabled(False)
        self.actionRoberts.triggered.connect(lambda : Skiimage_Functions.Skiimage_Roberts(self))
        self.actionRoberts.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuEdge_Detection.addAction(self.actionSobel)
        self.actionSobel.setEnabled(False)
        self.actionSobel.triggered.connect(lambda : Skiimage_Functions.Skiimage_Sobel(self))
        self.actionSobel.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuEdge_Detection.addAction(self.actionPrewit)
        self.actionPrewit.setEnabled(False)
        self.actionPrewit.triggered.connect(lambda : Skiimage_Functions.Skiimage_Prewitt(self))
        self.actionPrewit.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuColor_Conversion.addAction(self.actionRGB_to_HSV)
        self.actionRGB_to_HSV.setEnabled(False)
        self.actionRGB_to_HSV.triggered.connect(lambda : Skiimage_Functions.Skiimage_RGB2HSV(self))
        self.actionRGB_to_HSV.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menuColor_Conversion.addAction(self.actionRGB_Grey)
        self.actionRGB_Grey.setEnabled(False)
        self.actionRGB_Grey.triggered.connect(lambda : Skiimage_Functions.Skiimage_RGB2Gray(self))
        self.actionRGB_Grey.triggered.connect(lambda : Common_Proc.Output_Show(self))
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuColor_Conversion.menuAction())
        self.menubar.addAction(self.menuEdge_Detection.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OOP_2_LabProject"))
        self.groupBox_Input_Image.setTitle(_translate("MainWindow", "Source Image"))
        self.groupBox_Output_Image.setTitle(_translate("MainWindow", "Output Image"))
        self.groupBox_Source.setTitle(_translate("MainWindow", "Source"))
        self.Button_Source_Input.setText(_translate("MainWindow", "Input"))
        self.Button_Source_Export.setText(_translate("MainWindow", "Exp"))
        self.Button_Source_Clear.setText(_translate("MainWindow", "Clr"))
        self.groupBox_Output.setTitle(_translate("MainWindow", "Output"))
        self.Button_Output_Save.setText(_translate("MainWindow", "Save"))
        self.Button_Output_SaveAs.setText(_translate("MainWindow", "SvAs"))
        self.Button_Output_ExportAs.setText(_translate("MainWindow", "ExAs"))
        self.Button_Output_Clear.setText(_translate("MainWindow", "Clr"))
        self.Button_Output_Undo.setText(_translate("MainWindow", "Undo"))
        self.Button_Output_Redo.setText(_translate("MainWindow", "Redo"))
        self.groupBox_Color_Conversion.setTitle(_translate("MainWindow", "Color Conversion"))
        self.Button_Color_RGB2HSV.setText(_translate("MainWindow", "HSV"))
        self.Button_Color_RGB2Grey.setText(_translate("MainWindow", "GRY"))
        self.groupBox_Segmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.Button_Seg_ChanVese.setText(_translate("MainWindow", "CV"))
        self.Button_Seg_Otsu.setText(_translate("MainWindow", "OT"))
        self.Button_Seg_Morp.setText(_translate("MainWindow", "MRP"))
        self.groupBox_EdgeDetection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.Button_Edge_Scharr.setText(_translate("MainWindow", "SC"))
        self.Button_Edge_Roberts.setText(_translate("MainWindow", "RB"))
        self.Button_Edge_Sobel.setText(_translate("MainWindow", "SB"))
        self.Button_Edge_Prewitt.setText(_translate("MainWindow", "PR"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuSegmentation.setTitle(_translate("MainWindow", "Segmentation"))
        self.menuEdge_Detection.setTitle(_translate("MainWindow", "Edge Detection"))
        self.menuColor_Conversion.setTitle(_translate("MainWindow", "Color Conversion"))
        self.actionRGB_to_HSV.setText(_translate("MainWindow", "RGB -> HSV"))
        self.actionRGB_to_HSV.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionRGB_Grey.setText(_translate("MainWindow", "RGB -> Grey"))
        self.actionRGB_Grey.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionScharr.setText(_translate("MainWindow", "Scharr"))
        self.actionRoberts.setText(_translate("MainWindow", "Roberts"))
        self.actionSobel.setText(_translate("MainWindow", "Sobel"))
        self.actionPrewit.setText(_translate("MainWindow", "Prewitt"))
        self.actionChan_Vese_Segmentation.setText(_translate("MainWindow", "Chan-Vese Segmentation"))
        self.actionOtsu_Segmentation.setText(_translate("MainWindow", "Multi-Otsu Segmentation"))
        self.actionMorpSnakes_Segmentation.setText(_translate("MainWindow", "Morphological Snakes"))
        self.actionOpen_Source.setText(_translate("MainWindow", "Open Source"))
        self.actionOpen_Source.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Output.setText(_translate("MainWindow", "Save Output"))
        self.actionSave_Output.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As_Output.setText(_translate("MainWindow", "Save As Output"))
        self.actionSave_As_Output.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Shift+F4"))
        self.actionSource_menuExport_As.setText(_translate("MainWindow", "Source"))
        self.actionOutput_menuExport_As.setText(_translate("MainWindow", "Output"))
        self.actionUndo_Output.setText(_translate("MainWindow", "Undo Output"))
        self.actionUndo_Output.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo_Output.setText(_translate("MainWindow", "Redo Output"))
        self.actionClear_Source.setText(_translate("MainWindow", "Source"))
        self.actionClear_Output.setText(_translate("MainWindow", "Output"))

    
    