import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QLabel

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>650</width>
    <height>550</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>372</x>
      <y>385</y>
      <width>101</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Зарегистрированы?</string>
    </property>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>140</x>
      <y>120</y>
      <width>331</width>
      <height>101</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_5">
       <item>
        <widget class="QLabel" name="label_8">
         <property name="text">
          <string>Имя</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_9">
         <property name="text">
          <string>Логин</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_10">
         <property name="text">
          <string>Пароль</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_6">
       <item>
        <widget class="QLineEdit" name="NameLineEdit_3"/>
       </item>
       <item>
        <widget class="QLineEdit" name="LoginLineEdit_3"/>
       </item>
       <item>
        <widget class="QLineEdit" name="PasswordLineEdit_3"/>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>232</x>
      <y>235</y>
      <width>151</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Зарегистрироваться</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>376</x>
      <y>415</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QLabel" name="pic">
    <property name="geometry">
     <rect>
      <x>94</x>
      <y>25</y>
      <width>501</width>
      <height>81</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>650</width>
     <height>26</height>
    </rect>
   </property>
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
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.run)
        self.pixmap = QPixmap('kartinka.jpg')
        self.pic.setPixmap(self.pixmap)

    def run(self):
        print('k')
        print('k')
        print('k')
        print('k')

        print('k')

    def except_hook(cls, exception, traceback):
        sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
