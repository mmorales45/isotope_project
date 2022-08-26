#!/usr/bin/env python
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QToolTip, QMessageBox, QLabel)
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu,QDesktopWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QTimer

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import rospy    
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QMenu,QDesktopWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, QTimer

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import os
import signal
import subprocess
import roslaunch
from argonne_final_project.LaunchRunClass import *
from moveit_commander.conversions import pose_to_list, list_to_pose

from geometry_msgs.msg import Pose


import time
import sys
path = sys.path[0]

import rospkg
# get an instance of RosPack with the default search paths
rospack = rospkg.RosPack()
from std_srvs.srv import Empty, Trigger


import atexit
print('is this first')
def exit_handler():
	kill_all()
atexit.register(exit_handler)



        
list_of_classes = []
def kill_all():
	print("Stoping all Processes...")
	for class_name in list_of_classes:
		class_name.stop()
	print("All Processes Stopped")


powerOnur5e= CustomNodeRun("argonne_final_project", "hardwareSrcNode","-POn_UR5e")
list_of_classes.append(powerOnur5e)

def powerOn5e():
    print("Powering On UR5e")
    powerOnur5e.start()

powerOnur16e= CustomNodeRun("argonne_final_project", "hardwareSrcNode","-POn_UR16e")
list_of_classes.append(powerOnur5e)

def powerOn16e():
    print("Powering On UR16e")
    powerOnur16e.start()
##
powerOffur5e= CustomNodeRun("argonne_final_project", "hardwareSrcNode","-POff_UR5e")
list_of_classes.append(powerOffur5e)

def powerOff5e():
    print("Powering Off UR16e")
    powerOffur5e.start()

powerOffur16e= CustomNodeRun("argonne_final_project", "hardwareSrcNode","-POff_UR16e")
list_of_classes.append(powerOffur16e)

def powerOff16e():
    print("Powering Off UR16e")
    powerOffur16e.start()
##
BRur5e= CustomNodeRun("argonne_final_project", "hardwareSrcNode","-BR_UR5e")
list_of_classes.append(BRur5e)

def br5e():
    print("Powering Off UR16e")
    BRur5e.start()

BRur16e= CustomNodeRun("argonne_final_project", "hardwareSrcNode","-BR_UR16e","IT WORKED")
list_of_classes.append(BRur16e)     

def br16e():
    print("Powering Off UR16e")
    BRur16e.start()


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setStyleSheet("background-color: white;")
        self.title = "GUI"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.pushButton = QPushButton("Hardware Menu", self)
        self.pushButton.resize(200, 50  )
        self.pushButton.move(225, 200)
        self.pushButton.setToolTip("<h3>Start the Session</h3>")

        self.pushButton2 = QPushButton("EE Movement", self)
        self.pushButton2.resize(200, 50  )
        self.pushButton2.move(225, 300)
        self.pushButton2.setToolTip("<h3>Start the Session</h3>")

        self.pushButton3 = QPushButton("Joint Control", self)
        self.pushButton3.resize(200, 50  )
        self.pushButton3.move(225, 400)
        self.pushButton3.setToolTip("<h3>Start the Session</h3>")

        self.pushButton.clicked.connect(self.window2)              # <===
        self.pushButton2.clicked.connect(self.window3)              # <===
        self.pushButton3.clicked.connect(self.window4)              # <===


        self.main_window()

    def main_window(self):
        self.label = QLabel("Manager", self)
        self.label.move(285, 175)
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def window2(self):                                             # <===
        self.w = CreateGUi()
        self.w.show()
        self.hide()
    def window3(self):                                             # <===
        self.w = Ui_MainWindow()
        self.w.show()
        self.hide()

    def window4(self):                                             # <===
        self.w = Jsp_MainWindow()
        self.w.show()
        self.hide()
    

class CreateGUi(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(700, 350))    
        self.setWindowTitle("Mobile Dual UR System") 
        
        all_buttons = self.createAllButtons()
        
        # for button in all_buttons:
        #     button.clicked.connect()
        self.bt1.clicked.connect(self.Button1)
        self.bt2.clicked.connect(self.Button2)
        self.bt3.clicked.connect(self.Button3)
        self.bt4.clicked.connect(self.Button4)
        self.bt5.clicked.connect(self.Button5)
        self.bt6.clicked.connect(self.Button6)
        self.bt9.clicked.connect(self.ButtonReturn)
        # self.bt10.clicked.connect(self.Button10)
        # self.bt11.clicked.connect(self.Button11)
        
        self.center()
        self.show()
        
    def Button1(self):
        powerOn5e()
        
    def Button2(self):
        powerOn16e()

    def Button3(self):
        powerOff5e()
        
    def Button4(self):
        powerOff16e()
    
    def Button5(self):
        br5e()
        
    def Button6(self):
        br16e()
    
    def ButtonReturn(self):
        self.returnWindow()

    def Refresh(self):
        if self.count > 0:
            self.bt3.setText(str(self.count)+' seconds')
            self.count -= 1
        else:
            self.time.stop()
            self.bt3.setEnabled(True)
            self.bt3.setText('Button 3')
            self.count = 10
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def createSingleButton(self,title,length,width,color):
        button = QPushButton(title,self)
        button.resize(length, width)
        if color == "green":
            button.setStyleSheet("background-color : green")
        elif color == "red":
            button.setStyleSheet("background-color : red")
        elif color == "blue":
            button.setStyleSheet("background-color : blue")
        elif color == "orange":
            button.setStyleSheet("background-color : orange")

        return button
    def space_out(self,list,space,x,y):
        current_x = x
        for i in list:
            i.move(current_x,y)
            current_x += space
            
    def createAllButtons(self):
        length = 140
        width = 45
        self.bt1 = self.createSingleButton("PowerOn UR5e",length,width,"green")
        self.bt2 = self.createSingleButton("PowerOn UR16e",length,width,"green")

        self.bt3 = self.createSingleButton("PowerOff UR5e",140,width,"red")
        self.bt4 = self.createSingleButton("PowerOff UR16e",140,width,"red")
        self.bt5 = self.createSingleButton("Release UR5e",140,width,"orange")
        self.bt6 = self.createSingleButton("Release UR16e",140,width,"orange")

        self.bt7 = self.createSingleButton("Load Script UR5e ",140,width,"blue")
        self.bt8 = self.createSingleButton("Load Script UR16e",140,width,"blue")
        self.bt9 = self.createSingleButton("Return To Main",140,width,None)

        self.bt10 = self.createSingleButton("Stop",140,width,"red")
        self.bt11 = self.createSingleButton("Release Stop",140,width,"green")
        self.bt12 = self.createSingleButton("Test",140,width,None)

        row1 =  [self.bt1, self.bt2]
        row2 = [self.bt3, self.bt4, self.bt5, self.bt6]
        row3 = [ self.bt7, self.bt8, self.bt9]
        row4  = [ self.bt10, self.bt11, self.bt12]

        all_buttons = row1 + row2
        self.space_out(row1,space=150,x=200,y=50)
        #Second Row
        self.space_out(row2,space=150,x=50,y=100)

        #Third Row
        self.space_out(row3,space=150,x=50,y=150)
        self.space_out(row4,space=150,x=50,y=200)
        return all_buttons
    
    def returnWindow(self):                                             # <===
        print('hi')
        self.w = Window()
        self.w.show()
        self.hide()
        
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(1)

    def setupUi(self, QMainWindow):
        self.resize(422, 355)
        self.centralwidget = QtWidgets.QWidget(self)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))

        # For displaying confirmation message along with user's info.
        self.label = QtWidgets.QLabel(self.centralwidget)   
        self.label.setGeometry(QtCore.QRect(170, 0, 301, 111))

        # Keeping the text of label empty initially.      
        self.label.setText("")    

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(self)
    def returnWindow(self):                                             # <===
        self.w = Window()
        self.w.show()
        self.hide()
    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.pushButton.clicked.connect(self.takeinputs)

        self.pushConfirm = QPushButton("Confirm", self)
        self.pushConfirm.setText(_translate("MainWindow", "Send"))
        self.pushConfirm.clicked.connect(self.cartesian_Move)
        self.pushConfirm.move(250, 200)

        self.pushRetry = QPushButton("Input Again", self)
        self.pushRetry.setText(_translate("MainWindow", "Menu"))
        self.pushRetry.clicked.connect(self.returnWindow)
        self.pushRetry.move(50, 200)
        
    def takeinputs(self):
        pos_x, done1 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter X Position:')

        pos_y, done2 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Enter Y Position:') 

        pos_z, done3 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter Z Position:')

        orien_x, done4 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter X Orientation:')
        orien_y, done5 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter Y Orientation:')
        orien_z, done6 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter Z Orientation:')
        orien_w, done7 = QtWidgets.QInputDialog.getDouble(
            self, 'Input Dialog', 'Enter W Orientation:')

        if done1 and done2 and done3 and done7 :
            # Showing confirmation message along
            # with information provided by user.
            self.label.setText('Robot will go to the following '
                                '\nPosition X: ' + str(pos_x) + 
                                '\nPosition Y: ' + str(pos_y) + 
                                '\nPosition Z: ' + str(pos_z) + 
                                '\nOrientation X: ' + str(orien_x) + 
                                '\nOrientation Y: ' + str(orien_y) + 
                                '\nOrientation Z: ' + str(orien_z) + 
                                '\nOrientation W: ' + str(orien_w) )
            # Hide the pushbutton after inputs provided by the use.
            self.new_pose = [pos_x,pos_y,pos_z,orien_x,orien_y,orien_z,orien_w]
            self.pushButton.hide()
    def cartesian_Move(self):
        print(self.new_pose)
        a = list_to_pose(self.new_pose)
        print(a)
        return self.new_pose 

class Jsp_MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(1)

    def setupUi(self, QMainWindow):
        self.resize(422, 255)
        self.centralwidget = QtWidgets.QWidget(self)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 130, 93, 28))

        # For displaying confirmation message along with user's info.
        self.label = QtWidgets.QLabel(self.centralwidget)   
        self.label.setGeometry(QtCore.QRect(170, 40, 201, 111))

        # Keeping the text of label empty initially.      
        self.label.setText("")    

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.pushButton.clicked.connect(self.takeinputs)

        self.pushConfirm = QPushButton("Confirm", self)
        self.pushConfirm.setText(_translate("MainWindow", "Send"))
        self.pushConfirm.clicked.connect(self.move_Joints)
        self.pushConfirm.move(250, 200)

        self.pushRetry = QPushButton("Input Again", self)
        self.pushRetry.setText(_translate("MainWindow", "Menu"))
        self.pushRetry.clicked.connect(self.returnWindow)
        self.pushRetry.move(50, 200)
        
    def takeinputs(self):
        j1, done1 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Value for Joint 1')

        j2, done2 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Value for Joint 2')

        j3, done3 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Value for Joint 3')

        j4, done4 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Value for Joint 4')

        j5, done5 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Value for Joint 5')

        j6, done6 = QtWidgets.QInputDialog.getDouble(
        self, 'Input Dialog', 'Value for Joint 6')

        if done1 and done2 and done3 and done6 :
            # Showing confirmation message along
            # with information provided by user.
            self.label.setText('Robot will go to the following '
                                '\nJoint 1: ' + str(j1) + 
                                '\nJoint 2: ' + str(j2) + 
                                '\nJoint 3: ' + str(j3) + 
                                '\nJoint 4: ' + str(j4) + 
                                '\nJoint 5: ' + str(j5) + 
                                '\nJoint 6: ' + str(j6) ) 
            self.jointStates = [j1,j2,j3,j4,j5,j6]
        self.pushButton.hide()
    def move_Joints(self):
        print(self.jointStates)
        a = list_to_pose(self.jointStates)
        print(a)
        return self.jointStates 
# def joint_Control(joint_list):

    def returnWindow(self):                                             # <===
        self.w = Window()
        self.w.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    rospy.init_node('GUIII')

    powerOn5e_srv = rospy.ServiceProxy("/ur5e/ur_hardware_interface/dashboard/power_on",Trigger)
    powerOn16e_srv = rospy.ServiceProxy("/ur16e/ur_hardware_interface/dashboard/power_on",Trigger)
    sys.exit( app.exec_() )