import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt6.QtGui import QPixmap, QIcon



template2 = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTextEdit" name="fileNameEdit">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>80</y>
      <width>211</width>
      <height>61</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="exitButton">
    <property name="geometry">
     <rect>
      <x>680</x>
      <y>520</y>
      <width>111</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>Выйти</string>
    </property>
   </widget>
   <widget class="QPushButton" name="reverseButton">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>200</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Развернуть строки </string>
    </property>
   </widget>
   <widget class="QLabel" name="lablefile">
    <property name="geometry">
     <rect>
      <x>210</x>
      <y>20</y>
      <width>171</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Содержимое файла</string>
    </property>
   </widget>
   <widget class="Line" name="line">
    <property name="geometry">
     <rect>
      <x>520</x>
      <y>50</y>
      <width>41</width>
      <height>521</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Vertical</enum>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>50</y>
      <width>71</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Имя файла</string>
    </property>
   </widget>
   <widget class="QPushButton" name="openButton_2">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>150</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Открыть файл</string>
    </property>
   </widget>
   <widget class="QListWidget" name="listWidgetFile">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>40</y>
      <width>521</width>
      <height>531</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Main(QMainWindow):
    def __init__(self):
        '''инициализация'''
        super().__init__()
        f = io.StringIO(template2)
        uic.loadUi(f, self)

        self.setWindowTitle('RTF - Redactor Text Files')
        self.setWindowIcon(QIcon("logotip.png"))
        self.pixmap = QPixmap('logotip.png')
        
        


if __name__ == '__main__':
    app2 = QApplication(sys.argv)
    ex2 = Main()
    app2.setStyleSheet("""
        
        QPushButton {
            font-size: 16px;
            background-color: "lightblue"
        
        }
    """)
    ex2.show()
    sys.exit(app2.exec())
