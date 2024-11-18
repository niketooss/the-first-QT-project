import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
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
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>250</x>
      <y>260</y>
      <width>151</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Зарегистрироваться</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>410</y>
      <width>101</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Зарегистрированы?</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton_2">
    <property name="geometry">
     <rect>
      <x>394</x>
      <y>440</y>
      <width>91</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QWidget" name="">
    <property name="geometry">
     <rect>
      <x>158</x>
      <y>145</y>
      <width>331</width>
      <height>101</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <layout class="QVBoxLayout" name="verticalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>Имя</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_2">
         <property name="text">
          <string>Логин</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLabel" name="label_3">
         <property name="text">
          <string>Пароль</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <layout class="QVBoxLayout" name="verticalLayout_2">
       <item>
        <widget class="QLineEdit" name="NameEnter"/>
       </item>
       <item>
        <widget class="QLineEdit" name="LoginEnter"/>
       </item>
       <item>
        <widget class="QLineEdit" name="PasswordEnter"/>
       </item>
      </layout>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Main(QWidget):
    def __init__(self):
        '''инициализация'''
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.initUI()

        self.pushButton.clicked.connect(self.pushButton)
        self.pushButton_2.clicked.connect(self.pushButton_2)
        self.NameEnter = QLineEdit(self)
        self.LoginEnter = QLineEdit(self)
        self.PasswordEnter = QLineEdit(self)

    def initUI(self):
        '''Настройка интерфейса'''
        self.setWindowTitle('Редактор текстовых файлов')

    def except_hook(cls, exception, traceback):
        sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
