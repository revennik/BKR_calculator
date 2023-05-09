import sys
import math
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from design import Ui_MainWindow
from que1 import Ui_Dialog
from que2 import Ui_Dialog2
from que3 import Ui_Dialog3
import psycopg2

app = QApplication(sys.argv)

win = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(win)
win.show()



def reguch():
    st = ui.comboBox1_itu_2.currentText()           # стандарт кабеля
    speed = ui.comboBox1_speed_2.currentText()      # скорость передачи
    per = ui.comboBox1_per.currentText()            # мощность предатчика
    pr = ui.comboBox1_pr.currentText()              # мин мощность приемника
    connection = psycopg2.connect(user="postgres", password="4545", host="localhost", port="5432", database="reg_uch")
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    cursor.execute("SELECT * FROM public.cd")
    stdb = cursor.fetchall()
    cursor.execute("SELECT * FROM public.speed")
    speeddb = cursor.fetchall()
    i=0
    l=0
    while stdb[i][1] != st:
        i=i+1
    while speeddb[l][1] != speed:
        l=l+1
    speeddb = float(speeddb[l][2])
    per = int(per[0]+per[1])
    if pr == "p-i-n фотодиод":
        pr = -55
    else:
        pr = -70
    energ_pot = per - pr
    ruchz = (energ_pot+0.1+2*0.9-0.2)/(float(stdb[i][3])+(0.1/4))
    ruchz = str(round(ruchz,2))
    Dpy = 10400/speeddb**2
    ruchxd = round(Dpy/float(stdb[i][2]),2)
    if (ruchxd > 1000):
        ruchxd = str("1000+")
    else:
        ruchxd = str(ruchxd)
    ruchpmd = str(round(140/speeddb,2))
    ui.rez1_2.setText(str(ruchz) + "km " + "- длина ру ограниченного затуханием" + "\n" + ruchxd + "km"
                      + "- длина ру ограниченного хроматической дисперсией" + "\n" + ruchpmd + "km"
                      + "- длина ру ограниченного поляризационной модовой дисперсией")


def opt_bud():
    st = ui.comboBox1_itu_3.currentText()  # стандарт кабеля
    dl = ui.tb2_Lstr_2.toPlainText()       # длина линии
    sdl = ui.tb2_Lstr.toPlainText()        # строительная длина кабеля
    nrs = ui.tb2_dop_nrs.toPlainText()     # к-во доп неразъёмных соединений
    rs = ui.tb2_dop_rs.toPlainText()       # к-во доп разъёмных соединений
    per = ui.comboBox2_per.currentText()   # мощность предатчика
    pr = ui.comboBox2_pr.currentText()     # мин мощность приемника
    if (bool(ui.tb2_Lstr_2.toPlainText())) & (bool(ui.tb2_Lstr.toPlainText())) == 0:
        error = QMessageBox()
        error.setWindowTitle("Ошибка")
        error.setText("Поля длины кабеля и строительной длины должны быть заполнены")
        error.exec()
    else:
        per = int(per[0] + per[1])
        if pr == "p-i-n фотодиод":
            pr = -55
        else:
            pr = -70
        energ_pot = per - pr
        n = float(dl) / float(sdl)
        connection = psycopg2.connect(user="postgres", password="4545", host="localhost", port="5432", database="reg_uch")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        cursor.execute("SELECT * FROM public.cd")
        stdb = cursor.fetchall()
        i=0
        while stdb[i][1] != st:
            i=i+1
        sum = (float(stdb[i][3])*float(sdl)*n)+(0.1*(n+1))+(0.9*2)+(float(nrs)*0.1)+(float(rs)*0.9)
        print(n)
        print(float(stdb[i][3]))
        print(float(stdb[i][3])*float(sdl)*n)
        print((0.1*(n+1))+(0.9*2))
        print((float(nrs)*0.1)+(float(rs)*0.9))
        print(energ_pot)
        sum = energ_pot - sum
        sum = round(sum,2)
        ui.rez2.setText(str(sum)+"dB " + "-бюджет мощности")


def disp():
    st = ui.comboBox1_itu_4.currentText()
    speed = ui.comboBox3_speed.currentText()
    connection = psycopg2.connect(user="postgres", password="4545", host="localhost", port="5432", database="reg_uch")
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    cursor.execute("SELECT * FROM public.cd")
    stdb = cursor.fetchall()
    cursor.execute("SELECT * FROM public.speed")
    speeddb = cursor.fetchall()
    i=0
    l=0
    while stdb[i][1] != st:
        i=i+1
    while speeddb[l][1] != speed:
        l=l+1
    D = float(stdb[i][2])
    lam = float(stdb[i][4])
    b2 = -(D*10**-6*lam**2*10**-3)/(2*3.14*300*10**6)
    print(b2)
    Tb = float(speeddb[l][3])
    T0 = Tb/(2*math.sqrt(2))
    print(T0)
    Ld = (T0**2*10**-12)/abs(b2)
    Ld = round(Ld,2)
    ui.rez3.setText(str(Ld) + "km " + "- дисперсионная длина")



def what1():
    global q1
    q1 = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(q1)
    q1.show()


def what2():
    global q2
    q2 = QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(q2)
    q2.show()


def what3():
    global q3
    q3 = QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(q3)
    q3.show()


ui.button1_2.clicked.connect(reguch)
ui.button2.clicked.connect(opt_bud)
ui.button1.clicked.connect(disp)
ui.button1_que.clicked.connect(what1)
ui.button2_que.clicked.connect(what2)
ui.button3_que.clicked.connect(what3)


app.exec()