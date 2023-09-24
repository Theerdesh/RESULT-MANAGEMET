from tkinter import *
import pandas as pd
import csv

the = 'C:\\Users\\theer\\Dropbox (Old)\\My PC (LAPTOP-22AL3TB0)\\Desktop\\marks1.csv'
df = pd.read_csv(the)
df.set_index('Ad.No', inplace=True)

w = Tk()
w.title('STUDENT RESULTS')
w.geometry('900x750')
w.resizable(1200, 1500)
v1 = IntVar(w)
v2 = StringVar(w)
v3 = StringVar(w)
v4 = StringVar(w)
v5 = StringVar(w)
v6 = StringVar(w)
Labl2 = Label(w, text='STUDENTS RESULTS', font=('Algerian', 25, 'bold'), fg='brown')
Labl2.place(x=300, y=0)
Labl = Label(w, text='Select Your LOGIN to proceed:', font=('calibri', 15))
Labl.place(x=0, y=70)
lab1 = Label(w, text='Enter Staff ID :', font=('Calibri', 15), fg='blue')
lab2 = Label(w, text='Enter your Password :', font=('calibri', 15), fg='blue')
en1 = Entry(w, textvariable=v2, width=20, font=('calibri', 13))
en2 = Entry(w, textvariable=v3, width=20, font=('calibri', 13), show='*')
en3 = Entry(w, textvariable=v6, width=20, font=('calibri', 13))
lab3 = Label(w, text='Enter Student ID :', font=('calibri', 15), fg='blue')
lab4 = Label(w, text='Enter your Password :', font=('calibri', 15), fg='blue')
lab5 = Label(w, text='Student ID:', font=('calibri', 15), fg='blue')
Lb1 = Listbox(w,height=15)
Lb2 = Label(w, text='***Login credentials are incorrect check again !!!', fg='red', font=('calibri', 15))
Lb3 = Label(w, text='***Incorrect Student ID !!!', fg='red', font=('calibri', 15))
f1 = Label(w, text='OLD PASSWORD', font=('Calibri', 15), fg='blue')
f2 = Label(w, text='NEW Password', font=('calibri', 15), fg='blue')
f3 = Label(w, text='NEW MARKS', font=('calibri', 15), fg='blue')
s2 = Entry(w, textvariable=v5, width=20, font=('calibri', 13))
s3 = Entry(w, textvariable=v4, width=20, font=('calibri', 13))


def stf():
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')
    v6.set('')
    f1.place_forget()
    f2.place_forget()
    s2.place_forget()
    w1.place_forget()
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    lab5.place_forget()
    en3.place_forget()
    t2.place_forget()
    lab3.place_forget()
    lab4.place_forget()
    Lb1.place_forget()
    Lb2.place_forget()
    lab1.place(x=0, y=140)
    lab2.place(x=0, y=170)
    en1.place(x=200, y=140)
    en2.place(x=200, y=170)
    but.place(x=350, y=250)


def sdt():
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')
    v6.set('')
    f1.place_forget()
    f2.place_forget()
    s2.place_forget()
    w1.place_forget()
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    lab1.place_forget()
    lab2.place_forget()
    lab5.place_forget()
    en3.place_forget()
    t2.place_forget()
    Lb1.place_forget()
    Lb2.place_forget()
    Lb3.place_forget()
    lab3.place(x=0, y=140)
    lab4.place(x=0, y=170)
    en1.place(x=200, y=140)
    en2.place(x=200, y=170)
    bt.place(x=350, y=250)


def ent():
    b = v2.get()
    c = v3.get()
    u = 0
    with open(the, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            d = dict(row)
            if d['Ad.No'] == b and d['Password'] == c:
                u = 1
                Lb2.place_forget()
                but.place_forget()
                bt.place_forget()
                b1.place(x=250, y=240)
                b2.place(x=250, y=280)
                b3.place(x=250, y=320)

        else:
            if u == 0:
                Lb2.place(x=50, y=350)
    file.close()


rb1 = Radiobutton(w, text='Administration Staff Login', variable=v1, value=0, font=('Calibri', 16), command=stf)
rb2 = Radiobutton(w, text='Student Login', variable=v1, value=1, font=('Calibri', 16), command=sdt)


def ent1():
    s = 'jntua'
    p = 'university'
    e = v2.get()
    f = v3.get()
    if e == s and f == p:
        Lb2.place_forget()
        bt.place_forget()
        but.place_forget()
        b4.place(x=250, y=240)
        b5.place(x=250, y=320)
        b6.place(x=250, y=280)
    else:
        Lb2.place(x=50, y=350)


def start():
    v1.set('')
    rb1.place(x=275, y=50)
    rb2.place(x=275, y=80)


start()


def getm():
    a = v1.get()
    b = v2.get()
    c = v3.get()
    Lb1.place_forget()
    Lb2.place_forget()
    f1.place_forget()
    f2.place_forget()
    s2.place_forget()
    w1.place_forget()
    if a == 1:
        q = 0
        with open(the, 'r') as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                d = dict(row)
                if d['Ad.No'] == b and d['Password'] == c:
                    if b == d['Ad.No']:
                        Lb1.insert(1, ('        SEM - 1'))
                        Lb1.insert(2, ("Sub1", d['Se1S1']))
                        Lb1.insert(3, ("Sub2", d['Se1S2']))
                        Lb1.insert(4, ("Sub3", d['Se1S3']))
                        Lb1.insert(5, ("Sub4", d['Se1S4']))
                        Lb1.insert(6, ("Sub5", d['Se1S5']))
                        val1 = (int(d['Se1S1'][:2]) + int(d['Se1S2'][:2]) + int(d['Se1S3'][:2]) + int(
                            d['Se1S4'][:2]) + int(d['Se1S5'][:2])) / 5
                        Lb1.insert(7, ("Avg.Percent-", val1, '%'))
                        Lb1.insert(8, ('        SEM - 2'))
                        Lb1.insert(9, ("Sub1", d['Se2S1']))
                        Lb1.insert(10, ("Sub2", d['Se2S2']))
                        Lb1.insert(11, ("Sub3", d['Se2S3']))
                        Lb1.insert(12, ("Sub4", d['Se2S4']))
                        Lb1.insert(13, ("Sub5", d['Se2S5']))
                        val2 = (int(d['Se2S1'][:2]) + int(d['Se2S2'][:2]) + int(d['Se2S3'][:2]) + int(
                            d['Se2S4'][:2]) + int(d['Se2S5'][:2])) / 5
                        Lb1.insert(14, ('Avg.Percent-', val2, '%'))
                        Lb1.place(x=450, y=390)
                        q = 1
            else:
                if q == 0:
                    Lb2.place(x=50, y=350)


def ext():
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    Lb1.place_forget()
    Lb2.place_forget()
    Lb3.place_forget()
    lab1.place_forget()
    lab2.place_forget()
    lab3.place_forget()
    lab4.place_forget()
    lab5.place_forget()
    en1.place_forget()
    en2.place_forget()
    en3.place_forget()
    t2.place_forget()
    f1.place_forget()
    f2.place_forget()
    s2.place_forget()
    w1.place_forget()
    v2.set('')
    v3.set('')
    v4.set('')
    v5.set('')
    v6.set('')
    start()


bt = Button(w, text='ENTER', command=ent, font=('algerian', 20, 'bold'), bg='wheat', fg='brown', border=3)
but = Button(w, text='SUBMIT', command=ent1, font=('algerian', 20, 'bold'), bg='wheat', fg='brown', border=3)


def passw():
    t = v4.get()
    t1 = v5.get()
    text = open(the, "r")
    text = ''.join([i for i in text]) \
        .replace(t, t1)
    x = open(the, "w")
    x.writelines(text)
    x.close()
    f1.place_forget()
    f2.place_forget()
    s2.place_forget()
    s3.place_forget()
    w1.place_forget()
    ext()


def pas():
    v4.set('')
    v5.set('')
    Lb1.place_forget()
    f1.place(x=0, y=400)
    f2.place(x=0, y=440)
    s2.place(x=150, y=440)
    s3.place(x=150, y=400)
    w1.place(x=100, y=480)


def rem():
    pt.place_forget()
    lab5.place_forget()
    en3.place_forget()
    t2.place_forget()
    ext()


pt = Button(w, text='back', font=('calibri', 12), fg='red', bg='wheat', command=rem)


def up():
    b4.place_forget()
    b5.place_forget()
    b6.place_forget()
    lab5.place(x=0, y=280)
    en3.place(x=120, y=280)
    pt.place(x=500, y=200)
    t2.place(x=190, y=330)


def ast():
    pt.place_forget()
    tv = 0
    b = v6.get()
    with open(the, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            d = dict(row)
            if d['Ad.No'] == b:
                tv = 1
                Lb3.place_forget()
                lab5.place_forget()
                en3.place_forget()
                t2.place_forget()

                def sem1():
                    t2.place_forget()
                    lab5.place_forget()
                    en3.place_forget()
                    r1.place_forget()
                    r2.place_forget()
                    al.place_forget()

                    def MARKS6():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w7.place(x=100, y=450)

                    def MARKS7():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w8.place(x=100, y=450)

                    def MARKS8():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w9.place(x=100, y=450)

                    def MARKS9():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w10.place(x=100, y=450)

                    def MARKS10():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w11.place(x=100, y=450)

                    def remove():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        ad.place_forget()
                        al.place_forget()
                        ext()

                    ad = Button(w, text='back', font=('calibri', 12), fg='red', bg='wheat', command=remove)
                    ad.place(x=500, y=200)
                    S1 = Button(w, text='SUBJECT1', font=('calibri', 12), fg='red', bg='wheat', command=MARKS6)
                    S1.place(x=250, y=240)
                    S2 = Button(w, text='SUBJECT2', font=('calibri', 12), fg='red', bg='wheat', command=MARKS7)
                    S2.place(x=250, y=280)
                    S3 = Button(w, text='SUBJECT3', font=('calibri', 12), fg='red', bg='wheat', command=MARKS8)
                    S3.place(x=250, y=320)
                    S4 = Button(w, text='SUBJECT4', font=('calibri', 12), fg='red', bg='wheat', command=MARKS9)
                    S4.place(x=250, y=360)
                    S5 = Button(w, text='SUBJECT5', font=('calibri', 12), fg='red', bg='wheat', command=MARKS10)
                    S5.place(x=250, y=400)

                def sem2():
                    t2.place_forget()
                    lab5.place_forget()
                    en3.place_forget()
                    r1.place_forget()
                    r2.place_forget()
                    al.place_forget()

                    def MARKS1():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w2.place(x=100, y=450)

                    def MARKS2():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w3.place(x=100, y=450)

                    def MARKS3():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w4.place(x=100, y=450)

                    def MARKS4():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w5.place(x=100, y=450)

                    def MARKS5():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        f3.place(x=0, y=400)
                        s2.place(x=150, y=400)
                        w6.place(x=100, y=450)

                    def remove():
                        S1.place_forget()
                        S2.place_forget()
                        S3.place_forget()
                        S4.place_forget()
                        S5.place_forget()
                        ad.place_forget()
                        al.place_forget()
                        ext()

                    ad = Button(w, text='back', font=('calibri', 12), fg='red', bg='wheat', command=remove)
                    ad.place(x=500, y=200)
                    S1 = Button(w, text='SUBJECT1', font=('calibri', 12), fg='red', bg='wheat', command=MARKS1)
                    S1.place(x=250, y=240)
                    S2 = Button(w, text='SUBJECT2', font=('calibri', 12), fg='red', bg='wheat', command=MARKS2)
                    S2.place(x=250, y=280)
                    S3 = Button(w, text='SUBJECT3', font=('calibri', 12), fg='red', bg='wheat', command=MARKS3)
                    S3.place(x=250, y=320)
                    S4 = Button(w, text='SUBJECT4', font=('calibri', 12), fg='red', bg='wheat', command=MARKS4)
                    S4.place(x=250, y=360)
                    S5 = Button(w, text='SUBJECT5', font=('calibri', 12), fg='red', bg='wheat', command=MARKS5)
                    S5.place(x=250, y=400)

                def remov():
                    r1.place_forget()
                    r2.place_forget()
                    al.place_forget()
                    ext()

                al = Button(w, text="back", font=('calibri', 12), fg='red', bg='wheat', command=remov)
                al.place(x=500, y=200)
                r1 = Button(w, text="Sem1", font=('calibri', 12), fg='red', bg='wheat', command=sem1)
                r1.place(x=250, y=240)
                r2 = Button(w, text="Sem2", font=('calibri', 12), fg='red', bg='wheat', command=sem2)
                r2.place(x=250, y=280)

        else:
            if tv == 0:
                def remov():
                    ext()

                al = Button(w, text="back", font=('calibri', 12), fg='red', bg='wheat', command=remov)
                al.place(x=500, y=200)
                Lb3.place(x=50, y=400)


t2 = Button(w, text="Done", font=('calibri', 12), fg='red', bg='wheat', command=ast)


def marks1():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se2S1'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w2.place_forget()
    ast()


def marks2():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se2S2'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w3.place_forget()
    ast()


def marks3():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se2S3'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w4.place_forget()
    ast()


def marks4():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se2S4'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w5.place_forget()
    ast()


def marks5():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se2S5'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w6.place_forget()
    ast()


def Marks1():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se1S1'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w7.place_forget()
    ast()


def Marks2():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se1S2'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w8.place_forget()
    ast()


def Marks3():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se1S3'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w9.place_forget()


def Marks4():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se1S4'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w10.place_forget()
    ast()


def Marks5():
    q = v5.get()
    b = v6.get()
    df.at[b, 'Se1S5'] = q
    df.to_csv(the)
    s2.place_forget()
    f3.place_forget()
    w11.place_forget()
    ast()


w1 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=passw)
b1 = Button(w, text='Change Password', font=('calibri', 12), fg='red', bg='wheat', command=pas)
b2 = Button(w, text='EXIT', font=('calibri', 12), fg='red', bg='wheat', command=ext)
b3 = Button(w, text='Get Marks', font=('calibri', 12), fg='brown', bg='wheat', command=getm)
b4 = Button(w, text='New Student Details', font=('calibri', 12), fg='red', bg='wheat')
b5 = Button(w, text='EXIT', font=('calibri', 12), fg='red', bg='wheat', command=ext)
b6 = Button(w, text='Update Marks', font=('calibri', 12), fg='brown', bg='wheat', command=up)
w2 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=marks1)
w3 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=marks2)
w4 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=marks3)
w5 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=marks4)
w6 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=marks5)
w7 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=Marks1)
w8 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=Marks2)
w9 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=Marks3)
w10 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=Marks4)
w11 = Button(w, text='DONE', font=('calibri', 12), fg='red', bg='wheat', command=Marks5)

w.mainloop()