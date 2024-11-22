import sys
import io
from qwerty import Main


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
    <height>556</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>144</x>
      <y>215</y>
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
   <widget class="QPushButton" name="loginButton">
    <property name="geometry">
     <rect>
      <x>230</x>
      <y>330</y>
      <width>151</width>
      <height>21</height>
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
      <y>60</y>
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


        self.loginButton.clicked.connect(self.reg_save)
        self.feedbackButton.clicked.connect(self.button_clicked)
        self.pic.setPixmap(self.pixmap)

    def reg_save(self):
        '''сохранение данных регистрации'''
        self.NameUser = (self.NameLineEdit_3.text())
        self.LoginUser = (self.LoginLineEdit_3.text())
        self.PasswordUser = (self.PasswordLineEdit_3.text())

        print(self.NameUser, self.LoginUser, self.PasswordUser, sep='\n')

        self.hide()
        app2 = QApplication(sys.argv)
        ex2 = Main()
        ex2.show()
        sys.exit(app2.exec())


    def button_clicked(self, s):
        '''отзыв о моем проекте('''
        print("click", s)
        dlg = QMessageBox(self)
        self.setWindowTitle('RTF - Redactor Text Files')
        dlg = QMessageBox(text=f"Вам понравилось RTF?", parent=self)
        dlg.setWindowTitle("Отзыв")
        dlg.setStandardButtons(QMessageBox.StandardButton.No |
                               QMessageBox.StandardButton.Yes)
        print(s)
        dlg.exec()

    def open_new_windows(self):
        app2 = QApplication(sys.argv)
        ex2 = Main()
        ex2.show()
        sys.exit(app2.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Registr()
    app.setStyleSheet("""
        QWidget {
            background-color: "blue";
            color: "white";
        }
        QPushButton {
            font-size: 16px;
            background-color: "darkblue"
        }
        QLineEdit {
            background-color: "white";
            color: "black";
        }
    """)
    ex.show()
    sys.exit(app.exec())


