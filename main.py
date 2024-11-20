import sys
import io

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt6.QtGui import QPixmap, QIcon

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
      <x>376</x>
      <y>430</y>
      <width>111</width>
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
      <x>144</x>
      <y>165</y>
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
   <widget class="QPushButton" name="regButton">
    <property name="geometry">
     <rect>
      <x>236</x>
      <y>280</y>
      <width>151</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Зарегистрироваться</string>
    </property>
   </widget>
   <widget class="QPushButton" name="loginButton">
    <property name="geometry">
     <rect>
      <x>380</x>
      <y>460</y>
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
      <x>210</x>
      <y>10</y>
      <width>401</width>
      <height>151</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
   <widget class="QPushButton" name="feedbackButton">
    <property name="geometry">
     <rect>
      <x>550</x>
      <y>10</y>
      <width>81</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Отзыв</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>650</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Registr(QMainWindow):
    '''В этом окне происходит регистрация'''

    def __init__(self):
        '''инициализация'''
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.setWindowTitle('RTF - Redactor Text Files')
        self.setWindowIcon(QIcon("logotip.png"))
        self.pixmap = QPixmap('logotip.png')

        self.regButton.clicked.connect(self.reg_save)
        self.loginButton.clicked.connect(self.button_clicked)
        self.feedbackButton.clicked.connect(self.button_clicked)
        self.pic.setPixmap(self.pixmap)

    def reg_save(self):
        '''сохранение данных регистрации'''
        self.NameUser = (self.NameLineEdit_3.text())
        self.LoginUser = (self.LoginLineEdit_3.text())
        self.PasswordUser = (self.PasswordLineEdit_3.text())

        print(self.NameUser, self.LoginUser, self.PasswordUser, sep='\n')

    def button_clicked(self, s):
        '''отзыв о моем проекте('''
        print("click", s)
        dlg = QMessageBox(self)
        self.setWindowTitle('RTF - Redactor Text Files')
        dlg = QMessageBox(text=f"Вам понравилось RTF?", parent=self)
        dlg.setWindowTitle("Отзыв")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes |
                               QMessageBox.StandardButton.No)

        dlg.exec()

    def except_hook(cls, exception, traceback):
        sys.excepthook(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    ex.show()
    sys.exit(app.exec())
