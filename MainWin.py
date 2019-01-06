'''
下一步工作：
销货登记功能实现 ←
销售查询功能实现
库存查询功能实现

相关功能提示窗口完善

系统测试

代码精简

文档书写
'''
import sys
import function
import pymysql
# from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from QtUI.Ui_MainWindow import Ui_MainWindow

import QtUI.Ui_LoginWindow
import QtUI.Ui_LoginErrorWindow

import LoginWin
import LoginErrorWin
import MenuWin
import WareRegisterWin
import RegisterErrorDialog
import PurchaseRegisterWin

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.login = LoginWin.LoginWindow() # 登录界面
        self.login_error = LoginErrorWin.LoginErrorWindow() # 账号密码不匹配提示界面
        self.menu = MenuWin.MenuWindow()  # 功能界面
        self.wareRegister = WareRegisterWin.WareRegisterWindow()  #商品信息注册界面
        self.registerError = RegisterErrorDialog.RegisterErrorDialog() #注册内容出错回滚界面
        self.purchaseRegister = PurchaseRegisterWin.PurchaseRegisterWindow()

        '''
        注意！！！
        这里跳过了登录操作
        上线前记得修改！！！

        把menu.show()改成LoginCheck
        '''

        self.Login_PushButton.clicked.connect(self.menu.show)
        self.Login_PushButton.clicked.connect(self.close)
        
        self.login.Login_PushButton_Submit.clicked.connect(self.LoginCheck)

        self.menu.WareRegister_PushButton.clicked.connect(self.wareRegister.show)
        self.menu.PurchaseRegister_PushButton.clicked.connect(self.purchaseRegister.show)

        self.wareRegister.Clear_PushButton.clicked.connect(self.Register_DataClear)
        self.wareRegister.Submit_PushButton.clicked.connect(self.Register_Action)

        # self.registerError.buttonBox.clicked.connect

        self.purchaseRegister.Clear_PushButton.clicked.connect(self.PurchaseRegister_DataClear)
        self.purchaseRegister.Submit_PushButton.clicked.connect(self.PurchaseRegister_Action)
        


    def LoginCheck(self):
    # 检查登录信息
        user_name = self.login.Login_LineEdit_UserName.text()
        password = self.login.Login_LineEdit_Password.text()

        db = function.connect_database()
        cursor = db.cursor()
        check_sql = 'SELECT PASSWORD FROM ADMIN WHERE ID=%s'
        cursor.execute(check_sql, user_name)
        result = cursor.fetchone()
    # 这里有问题：
    # 如果账号不在数据库内，会跳 TypeError: 'NoneType' object is not subscriptable
        if str(result[0]) == str(password):
            self.menu.show()
            self.login.close()
        else:
            self.login_error.show()
            self.login.Login_LineEdit_UserName.clear()
            self.login.Login_LineEdit_Password.clear()

    def Register_DataClear(self):
        self.wareRegister.Name_LineEdit.clear()
        self.wareRegister.ID_LineEdit.clear()
        self.wareRegister.Format_LineEdit.clear()
        self.wareRegister.Quantity_SpinBox.clear()
        self.wareRegister.PurchasePrice_LineEdit.clear()
        self.wareRegister.SellPrice_LineEdit.clear()
        self.wareRegister.MaxStock_SpinBox.clear()
        self.wareRegister.MinStock_SpinBox.clear()

    def Register_Action(self):
        ware_data = []
        ware_data.append(self.wareRegister.Name_LineEdit.text())
        ware_data.append(int(self.wareRegister.ID_LineEdit.text()))
        ware_data.append(int(self.wareRegister.Format_LineEdit.text()))
        ware_data.append(int(self.wareRegister.Quantity_SpinBox.text()))
        ware_data.append(int(self.wareRegister.PurchasePrice_LineEdit.text()))
        ware_data.append(int(self.wareRegister.SellPrice_LineEdit.text()))
        ware_data.append(int(self.wareRegister.MaxStock_SpinBox.text()))
        ware_data.append(int(self.wareRegister.MinStock_SpinBox.text()))

        insert_sql = """
                     INSERT INTO ware_data
                     (name, ware_id, format, quantity, purchase_price, sell_price, max_stock, min_stock) 
                     VALUES(%s,%s,%s,%s,%s,%s,%s,%s)
                     """
        db = function.connect_database()
        cursor = db.cursor()
        while True:
            try:
                cursor.execute(insert_sql, ware_data)
            except Exception as e:
                print(e)
                db.rollback()
                self.Register_DataClear()
                # self.registerError.show()
                break
            else:
                db.commit()
                break
        cursor.close()
        db.close()
        '''
        未完成：
        完善商品注册功能
        创建错误提示（重复id，商品信息不完全，商品数据格式错误balabala）窗口
        创建录入成功窗口

        懒了，其他活干完再来完善吧
        '''
        

    def PurchaseRegister_DataClear(self):
        self.purchaseRegister.dateTimeEdit.clear()
        '''
        注意：
        这里，dataTimeEdit可能不应该用clear()方式
        清除数据时，会出现很奇怪的错误
        待日后完善
        '''
        self.purchaseRegister.PurchaseID_LineEdit.clear()
        self.purchaseRegister.WareID_LineEdit.clear()
        self.purchaseRegister.Quantity_SpinBox.clear()

    
    def PurchaseRegister_Action(self):
        purchase_data = []
        # 对从qt中收到的datetime数据进行转换，以适应数据库格式要求
        datetime = self.purchaseRegister.dateTimeEdit.text().replace(' ', '').replace('-', '')
        purchase_data.append(datetime)
        purchase_data.append(self.purchaseRegister.PurchaseID_LineEdit.text())
        purchase_data.append(self.purchaseRegister.WareID_LineEdit.text())
        purchase_data.append(self.purchaseRegister.Quantity_SpinBox.text())

        insert_sql = """
                     INSERT INTO purchase_data
                     (date_time, purchase_id, ware_id, quantity) 
                     VALUES(%s,%s,%s,%s)
                     """
        db = function.connect_database()
        cursor = db.cursor()
        while True:
            try:
                cursor.execute(insert_sql, purchase_data)
            except Exception as e:
                print(e)
                db.rollback()
                self.PurchaseRegister_DataClear
                break
            else:
                db.commit()
                break
        cursor.close()
        db.close()
        '''
        未完成：
        完善本功能
        创建相关窗口

        本工作可待主要功能大致完善后再进行
        '''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = MainWindow()
    Main.show()
    sys.exit(app.exec_())