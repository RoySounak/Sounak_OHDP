# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CDAC.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
##
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import *


import cv2
import numpy as np
import matplotlib.pyplot as plt

from tkinter import *
import tkinter as tk
from tkinter import filedialog

from PIL import Image
from PIL import ImageTk
from PIL import ImageQt

import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
from skimage.feature import greycomatrix, greycoprops


from scipy.ndimage import imread
import sys

####NEW ADDD###
from OtherWindow import Ui_OtherWindow
##


class Ui_MainWindow(object):
    def __init__(self):
         self.MainWindow = QtWidgets.QMainWindow()
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
        
        self.window.show()
         
######FILE OPEN LEFT#######
    def fOpenCheck(self):
        print("Success File Open")
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        print(file_path)
        
        #img_zi = Image.open(file_path)
        #area_zi = (10000,1000,20000,3000)
        #zoom_img_zi = img_zi.crop(area_zi)
        #img_zi.show()
        #tkimage = ImageTk.PhotoImage(img_zi)
        #tk.Label(root, image=tkimage).pack()
        #return img_zi
        #framed = QGraphicsView()
        #file_path = imread(file_path)
        #height, width, channels = file_path.shape
        #bytesPerLine = channels * width
        #qImg = QImage(file_path.data, width, height, bytesPerLine, QImage.Format_RGB888)
        #pixmap01 = QPixmap.fromImage(qImg)
        #pixmap_image = QPixmap(pixmap01)
        img = Image.open(file_path)
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        
        
        scene = QGraphicsScene()
        scene.addPixmap(pixMap)
        #scene.addPixmap(QPixmap(file_path))
        #scene.addPixmap(pixmap_image)
        self.frame.setScene(scene)
        self.frame.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.frame.show()     
###### 
######FILE OPEN Right#######
    def fOpenCheckR(self):
        print("Success File Open")
        root = tk.Tk()
        root.withdraw()
        file_path2 = filedialog.askopenfilename()
        print(file_path2)
        
        #img_zi = Image.open(file_path)
        #area_zi = (10000,1000,20000,3000)
        #zoom_img_zi = img_zi.crop(area_zi)
        #img_zi.show()
        #tkimage = ImageTk.PhotoImage(img_zi)
        #tk.Label(root, image=tkimage).pack()
        #return img_zi
        #framed = QGraphicsView()
        #file_path = imread(file_path)
        #height, width, channels = file_path.shape
        #bytesPerLine = channels * width
        #qImg = QImage(file_path.data, width, height, bytesPerLine, QImage.Format_RGB888)
        #pixmap01 = QPixmap.fromImage(qImg)
        #pixmap_image = QPixmap(pixmap01)
        img = Image.open(file_path2)
        w, h = img.size
        self.imgQ = ImageQt.ImageQt(img)  # we need to hold reference to imgQ, or it will crash
        pixMap = QPixmap.fromImage(self.imgQ)
        
        
        scene = QGraphicsScene()
        scene.addPixmap(pixMap)
        #scene.addPixmap(QPixmap(file_path))
        #scene.addPixmap(pixmap_image)
        self.frame_4.setScene(scene)
        self.frame_4.fitInView(QRectF(0, 0, w, h), Qt.KeepAspectRatio)
        self.frame_4.show()            
##### 
        
        #####Zoom In#####
    #def fzoomInCheck(self):
       
        #####Algo PracTice GSCM#####
    def GSCM(self):
        
        print("Success File Open")
        root = tk.Tk()
        root.withdraw()
        file_path1 = filedialog.askopenfilename()
        print(file_path1)
        
        
        print("Success File Open")
        root = tk.Tk()
        root.withdraw()
        file_path2 = filedialog.askopenfilename()
        print(file_path2)
        
        import numpy as np
        import cv2
        import matplotlib.pyplot as plt

        img1 = cv2.imread(file_path1,0)
        img2 = cv2.imread(file_path2,0)

        orb = cv2.ORB_create()

        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = bf.match(des1,des2)
        matches = sorted(matches, key = lambda x:x.distance)

        img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)
        
        cv2.imwrite("/home/rahul/Desktop/tmp.jpg",img3)
        
        self.openWindow()
        
      ####  
    def setupUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame = QtWidgets.QGraphicsView(self.centralwidget)
        
        self.frame.setGeometry(QtCore.QRect(220, 60, 271, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 520, 99, 27))
        self.pushButton.setObjectName("pushButton")
        ##OPen Left Connection###
        file_path = self.pushButton.clicked.connect(self.fOpenCheck)
        ###
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 520, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        ####OPen Right Connection###
        file_path2 = self.pushButton_2.clicked.connect(self.fOpenCheckR)
        ###
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 90, 99, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        ###ZOOM IN###
        #self.pushButton_3.clicked.connect(self.fzoomInCheck)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 140, 99, 27))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 190, 99, 27))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(60, 410, 99, 27))
        self.pushButton_6.setObjectName("pushButton_6")
        #self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3 = QtWidgets.QGraphicsView(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(30, 460, 171, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        #self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(520, 60, 271, 451))
        self.frame_4.setMaximumSize(QtCore.QSize(800, 600))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 20, 111, 27))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(280, 20, 111, 27))
        self.pushButton_8.setObjectName("pushButton_8")
        ####GSCM COnnection###
        self.pushButton_8.clicked.connect(self.GSCM)
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(410, 20, 111, 27))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(530, 20, 111, 27))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(660, 20, 111, 27))
        self.pushButton_11.setObjectName("pushButton_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi()#(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open Left"))
        self.pushButton_2.setText(_translate("MainWindow", "Open Right"))
        self.pushButton_3.setText(_translate("MainWindow", "Zoom In"))
        self.pushButton_4.setText(_translate("MainWindow", "Zoom Out"))
        self.pushButton_5.setText(_translate("MainWindow", "Crop"))
        self.pushButton_6.setText(_translate("MainWindow", "Calculate"))
        self.pushButton_7.setText(_translate("MainWindow", "Morphological"))
        self.pushButton_8.setText(_translate("MainWindow", "GSCM"))
        self.pushButton_9.setText(_translate("MainWindow", "GLCM"))
        self.pushButton_10.setText(_translate("MainWindow", "SIFT"))
        self.pushButton_11.setText(_translate("MainWindow", "HOG"))

    def show(self):
        MainWindow.show()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    
    sys.exit(app.exec_())
    
