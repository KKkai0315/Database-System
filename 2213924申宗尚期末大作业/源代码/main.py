import pymysql
from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk


def delButton(tree):
    x = tree.get_children()
    for item in x:
        tree.delete(item)


def back(root):
    root.destroy()
    StartPage()

image1 = None
img1 = None


# (1)物流信息管理系统
def StartPage():
    global image1
    global img1
    root = tk.Tk()
    root.title('医院信息管理系统')
    root.geometry('490x650+500+100')
    root['background'] = 'white'
    image1 = Image.open('logo.png')
    img1 = ImageTk.PhotoImage(image1)
    Label(root, image=img1).pack()  # place(relx=0,rely=0)
    Button(root, text="医生\护士登录", font=tkFont.Font(size=16), command=lambda: Login(root), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.21,
                                                                                                           rely=0.45)
    Button(root, text="受诊人登录", font=tkFont.Font(size=16), command=lambda: PatientChoosePage(root), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.21,
                                                                                                           rely=0.6)
    Button(root, text='退出系统', height=2, font=tkFont.Font(size=16), width=25, command=root.destroy,
           fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.21, rely=0.75)
    root.mainloop()


image2 = None
img2 = None


# (2)管理员登录页面
def Login(root):
    global image2
    global img2
    root.destroy()
    root = tk.Tk()
    root.title('登录页面')
    root.geometry('490x650+500+100')
    root['background'] = 'white'
    image2 = Image.open('logo.png')
    img2 = ImageTk.PhotoImage(image2)
    Label(root, image=img2).pack()
    Label(root, text='职工号：', font=("楷体", 15), bg='white').place(relx=0.32, rely=0.35)
    Label(root, text='密码：', font=("楷体", 15), bg='white').place(relx=0.32, rely=0.45)
    staffID = StringVar()
    pwd = StringVar()
    entry_staffID = Entry(root, textvariable=staffID, show=None)
    entry_staffID.place(relx=0.45, rely=0.35, relwidth=0.3, relheight=0.039)
    entry_pwd = Entry(root, textvariable=pwd, show='*')
    entry_pwd.place(relx=0.45, rely=0.45, relwidth=0.3, relheight=0.039)
    Button(root, text="登录", width=15, font=tkFont.Font(size=15),
           command=lambda: sign_in(root, entry_staffID, entry_pwd), fg='black', activebackground='black',
           activeforeground='white').place(relx=0.34, rely=0.57)
    Button(root, text="注册", width=15, font=tkFont.Font(size=15), command=lambda: register_Page(root), fg='black',
           activebackground='black', activeforeground='white').place(relx=0.34, rely=0.65)
    root.protocol('WM_DELETE_WINDOW', lambda: back(root))
    root.mainloop()

# (2.1)
def sign_in(root, entry_staffID, entry_pwd):
    db = pymysql.connect(host="localhost", user="root", \
                         password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    sql = "select StaffID, userpassword, Position from Staff where StaffID='%s'" % (entry_staffID.get())
    try:
        cur.execute(sql)
        result = cur.fetchone()
        if result is not None:
            mima = result[1]
        else:
            showinfo(title='提示', message='账号/密码错误！')
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cur.close()
        db.close()
        table = result[2]

    if mima == entry_pwd.get():
        MangerChoosePage(root,table)
    else:
        showinfo(title='提示', message='账号/密码错误！')


image8 = None
img8 = None


# （3）注册页面
def register_Page(root):
    global image8
    global img8
    root.destroy()
    root = Tk()
    root.title('账号注册页面')
    root.geometry('490x650+500+100')
    root['background'] = 'white'
    image8 = Image.open('logo.png')
    img8 = ImageTk.PhotoImage(image8)
    Label(root, image=img8).pack()
    Label(root, text='输入职工号：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.35)
    Label(root, text='输入姓名：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.40)
    Label(root, text='输入性别：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.45)
    Label(root, text='输入职位：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.50)
    Label(root, text='输入部门：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.55)
    Label(root, text='输入密码：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.60)
    Label(root, text='确认密码：', font=("楷体", 15), bg='white').place(relx=0.30, rely=0.65)
    staffID = StringVar()
    name = StringVar()
    gender = StringVar()
    position = StringVar()
    department = StringVar()
    pwd = StringVar()
    sure_pwd = StringVar()
    entry_staffID = Entry(root, textvariable=staffID, show=None)
    entry_staffID.place(relx=0.465, rely=0.35, relwidth=0.34, relheight=0.039)
    entry_name = Entry(root, textvariable=name, show=None)
    entry_name.place(relx=0.465, rely=0.40, relwidth=0.34, relheight=0.039)
    entry_gender = Entry(root, textvariable=gender, show=None)
    entry_gender.place(relx=0.465, rely=0.45, relwidth=0.34, relheight=0.039)
    entry_position = Entry(root, textvariable=position, show=None)
    entry_position.place(relx=0.465, rely=0.50, relwidth=0.34, relheight=0.039)
    entry_department = Entry(root, textvariable=department, show=None)
    entry_department.place(relx=0.465, rely=0.55, relwidth=0.34, relheight=0.039)
    entry_pwd = Entry(root, textvariable=pwd, show='*')
    entry_pwd.place(relx=0.465, rely=0.60, relwidth=0.34, relheight=0.039)
    entry_sure_pwd = Entry(root, textvariable=sure_pwd, show='*')
    entry_sure_pwd.place(relx=0.465, rely=0.65, relwidth=0.34, relheight=0.039)
    Button(root, text="注册", width=15, font=tkFont.Font(size=15),
           command=lambda: register(root, entry_staffID, entry_name, entry_gender, entry_position, entry_department, entry_pwd, entry_sure_pwd),
           fg='black',activebackground='black', activeforeground='white').place(relx=0.32, rely=0.75)
    Button(root, text="退出", width=15, font=tkFont.Font(size=15), command=lambda: Login(root), fg='black',
           activebackground='black', activeforeground='white').place(relx=0.32, rely=0.85)
    root.protocol('WM_DELETE_WINDOW', lambda: Login(root))
    root.mainloop()


# (3.1)
def register(root, entry_staffID, entry_name, entry_gender, entry_position, entry_department, entry_pwd, entry_sure_pwd):
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    sql = "insert into Staff values('%s','%s','%s','%s','%s','%s')" % (entry_staffID.get(), entry_name.get(), entry_gender.get(), entry_position.get(), entry_department.get(), entry_pwd.get())
    cur.execute("select * from Staff where staffID = '%s'" % (entry_staffID.get()))
    result = cur.fetchall()
    if result:
        showinfo('提示','该账号已存在，请重新输入！')
    else:
        print('ok')
        if len(entry_pwd.get()) == 6:
            if entry_sure_pwd.get() == entry_pwd.get():
                cur.execute(sql)
                db.commit()
                showinfo('提示', '注册成功！')
                Login(root)
            else:
                showinfo('提示', '两次输入密码不相同，请重新输入！')
        else:
            showinfo("提示", "请输入六位数密码！")
    cur.close()
    db.close()



image3 = None
img3 = None


# (4)管理员信息选择操作页面
def MangerChoosePage(root,table):
    global image3
    global img3
    root.destroy()
    root = Tk()
    root.title('医生/护士信息选择操作页面')
    root.geometry('490x650+500+100')  # ('950x700')
    root['background'] = 'white'
    image3 = Image.open('logo.png')
    img3 = ImageTk.PhotoImage(image3)
    Label(root, image=img3).pack()

    Button(root, text="病人信息管理", font=tkFont.Font(size=16), command=lambda: Uers_infor_Page(root, table), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.3)

    Button(root, text="诊断信息操作", font=tkFont.Font(size=16), command=lambda: MangerPage(root,table), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.45)

    Button(root, text="诊断开药", font=tkFont.Font(size=16), command=lambda: MedicineChoosePage(root, table), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.6)

    Button(root, text='退出', height=2, font=tkFont.Font(size=16), width=25, command=lambda: back(root),
           fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22, rely=0.75)
    root.protocol('WM_DELETE_WINDOW', lambda: back(root))
    root.mainloop()


image9 = None
img9 = None

# (4)受诊人信息选择操作页面
def PatientChoosePage(root):
    global image9
    global img9
    root.destroy()
    root = Tk()
    root.title('受诊人信息选择操作页面')
    root.geometry('490x650+500+100')  # ('950x700')
    root['background'] = 'white'
    image9 = Image.open('logo.png')
    img9 = ImageTk.PhotoImage(image9)
    Label(root, image=img9).pack()

    Button(root, text="诊断信息查询", font=tkFont.Font(size=16), command=lambda: GuestPage(root), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.45)

    Button(root, text="药品查询", font=tkFont.Font(size=16), command=lambda: MedicinePage(root), width=25,
           height=2, fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22,
                                                                                                           rely=0.6)
    Button(root, text='退出', height=2, font=tkFont.Font(size=16), width=25, command=lambda: back(root),
           fg='black', bg='gainsboro', activebackground='black', activeforeground='white').place(relx=0.22, rely=0.75)
    root.protocol('WM_DELETE_WINDOW', lambda: back(root))
    root.mainloop()


image4 = None
img4 = None

image6 = None
img6 = None


# (6)病人信息操作页面
def Uers_infor_Page(root, table):
    global image6
    global img6
    root.destroy()
    root = Tk()
    root.geometry('900x700+300+50')
    root.title("病人信息操作页面")
    root['background'] = 'white'
    image6 = Image.open('logo.png')
    img6 = ImageTk.PhotoImage(image6)
    Label(root, text="病人信息操作页面", compound='bottom', image=img6, font=('楷体', 30), fg='blue', bg='white').pack()
    Label(root, text="身份证号" + '：').place(relx=0.02, rely=0.08, relwidth=0.1)
    Label(root, text="姓名：").place(relx=0.5, rely=0.08, relwidth=0.1)
    Label(root, text="性别：").place(relx=0.02, rely=0.14, relwidth=0.1)
    Label(root, text="年龄：").place(relx=0.5, rely=0.14, relwidth=0.1)
    Label(root, text="电话号码：").place(relx=0.02, rely=0.2, relwidth=0.1)

    ID = StringVar()
    name = StringVar()
    sex = StringVar()
    age = StringVar()
    phonenumber = StringVar()

    entry_ID = Entry(root, textvariable=ID)
    entry_ID.place(relx=0.12, rely=0.08, relwidth=0.3, height=25)
    entry_name = Entry(root, textvariable=name)
    entry_name.place(relx=0.6, rely=0.08, relwidth=0.3, height=25)
    entry_sex = Entry(root, textvariable=sex)
    entry_sex.place(relx=0.12, rely=0.14, relwidth=0.3, height=25)
    entry_age = Entry(root, textvariable=age)
    entry_age.place(relx=0.6, rely=0.14, relwidth=0.3, height=25)
    entry_phonenumber = Entry(root, textvariable=phonenumber)
    entry_phonenumber.place(relx=0.12, rely=0.2, relwidth=0.3, height=25)

    list1 = [entry_ID, entry_name, entry_sex, entry_age, entry_phonenumber]

    Tree1 = ttk.Treeview(root, show='headings', column=('ID', 'name', 'sex', 'age', 'phonenumber'))
    Tree1.column('ID', width=70, anchor="center")
    Tree1.column('name', width=50, anchor="center")
    Tree1.column('sex', width=70, anchor="center")
    Tree1.column('age', width=40, anchor="center")
    Tree1.column('phonenumber', width=70, anchor="center")
    # 表格标题设置
    Tree1.heading('ID', text="身份证号")
    Tree1.heading('name', text='姓名')
    Tree1.heading('sex', text='性别')
    Tree1.heading('age', text="年龄")
    Tree1.heading('phonenumber', text='电话号码')

    Tree1.place(relx=0.01, rely=0.65, relwidth=0.98)

    def treeviewClick(event):
        item = Tree1.selection()[0]
        item_text = Tree1.item(item, "values")

        entry_ID.delete(0, 'end')
        entry_name.delete(0, 'end')
        entry_sex.delete(0, 'end')
        entry_age.delete(0, 'end')
        entry_phonenumber.delete(0, 'end')

        entry_ID.insert(0, item_text[0])
        entry_name.insert(0, item_text[1])
        entry_sex.insert(0, item_text[2])
        entry_age.insert(0, item_text[3])
        entry_phonenumber.insert(0, item_text[4])

    Button(root, text="显示所有人员信息", command=lambda: showAll_user_Info(tree=Tree1)).place(relx=0.12,
                                                                                                            rely=0.3,
                                                                                                            width=120)
    Button(root, text="增加人员信息", command=lambda: append_user_Info(tree=Tree1, list=list1)).place(
        relx=0.32, rely=0.3, width=120)
    Button(root, text="删除人员信息", command=lambda: delete_user_Info(tree=Tree1)).place(relx=0.52,
                                                                                                       rely=0.3,
                                                                                                       width=120)
    Button(root, text="更改人员信息", command=lambda: update_user_Info(tree=Tree1, list=list1)).place(
        relx=0.72, rely=0.3, width=120)

    Button(root, text="根据姓名查找",
           command=lambda: find_use_Info(tree=Tree1, entry=entry_name, flag='name')).place(relx=0.02,
                                                                                                        rely=0.38,
                                                                                                        width=135)
    Button(root, text="根据身份证号查找",
           command=lambda: find_use_Info(tree=Tree1,  entry=entry_ID, flag='ID')).place(relx=0.22,
                                                                                                    rely=0.38,
                                                                                                    width=135)
    Button(root, text="根据年龄查找",
           command=lambda: find_use_Info(tree=Tree1, entry=entry_age, flag='age')).place(relx=0.42,
                                                                                                              rely=0.38,
                                                                                                              width=135)
    Button(root, text="根据性别查找",
           command=lambda: find_use_Info(tree=Tree1, entry=entry_sex, flag='sex')).place(relx=0.62,
                                                                                                      rely=0.38,
                                                                                                      width=135)
    Button(root, text="根据电话号码查找",
           command=lambda: find_use_Info(tree=Tree1, entry=entry_phonenumber, flag="phonenumber")).place(
        relx=0.82, rely=0.38, width=135)

    Tree1.bind('<ButtonRelease-1>', treeviewClick)
    root.protocol('WM_DELETE_WINDOW', lambda: MangerChoosePage(root,table))
    root.mainloop()


# (6.1)
def showAll_user_Info(tree):
    delButton(tree)
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()  # 用db操作游标
    sql = "select * from Patient"
    cur.execute(sql)  # 执行sql语句
    # fetchone()返回一条记录（元组），没有结果则返回none
    # fetchall()返回所有元组，构成一个二维元组
    results = cur.fetchall()
    for item in results:
        tree.insert('', "end", values=item)
    cur.close()
    db.close()  # 关闭连接


# (6.2)
def append_user_Info(tree, list):
    delButton(tree)
    list2 = []
    for i in range(len(list)):
        if list[i].get() == '':
            showerror(title='提示', message='输入不能为空!')
            return
        else:
            list2.append(list[i].get())

    x = tree.get_children()
    for item in x:
        tree.delete(item)

    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    try:
        sql = "INSERT INTO Patient (PatientID, Name, Gender, Age, Number) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (list2[0], list2[1], list2[2], list2[3], list2[4]))
        db.commit()

        sql = "SELECT * FROM Patient"
        cur.execute(sql)
        results = cur.fetchall()
        for item in results:
            tree.insert('', "end", values=item)
        showinfo(title='提示', message='添加/更改成功！')
    except pymysql.MySQLError as e:
        db.rollback()
        error_msg = str(e)
        if '年龄填写错误！' in error_msg:
            showerror(title='错误', message='年龄填写错误！')
        elif '性别填写错误！' in error_msg:
            showerror(title='错误', message='性别填写错误！')
        elif 'Duplicate entry' in error_msg:
            showerror(title='错误', message='该人员/编号已存在！')
        else:
            showerror(title='错误', message='操作失败，请重试！')
    except Exception as e:
        db.rollback()
        print(e)
        showerror(title='错误', message='操作失败，请重试！')
    finally:
        cur.close()
        db.close()


# (6.3)
def delete_user_Info(tree):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    res = askyesno('提示', '是否确认删除？')
    if res == True:
        for item in tree.selection():
            selectedItem = tree.selection()[0]
            no1 = tree.item(selectedItem, 'values')[0]
            tree.delete(item)
            sql = "delete from Patient where PatientID = '%s' " % no1
            db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
            cur = db.cursor()
            cur.execute(sql)
            db.commit()
            cur.close()
            db.close()
            showinfo(title='提示', message='删除成功！')


# (6.4)
def update_user_Info(tree, list):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    else:
        res = askyesno("提示", "是否确认更新数据？")
        if res == True:
            for item in tree.selection():
                selectedItem = tree.selection()[0]
                no1 = tree.item(selectedItem, 'values')[0]
                tree.delete(item)
                sql = "delete from Patient where PatientID = '%s' " % no1
                db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
                cur = db.cursor()
                cur.execute(sql)
                db.commit()

                cur.close()
                db.close()
            append_user_Info(tree, list)
            return


# (6.5)
def find_sql_line(flag, entry):
    if flag == 'name':
            sql = "select * from Patient where Name = '%s'" % (entry.get())
    elif flag == 'ID':
            sql = "select * from Patient where PatientID = '%s'" % (entry.get())
    elif flag == 'age':
            sql = "select * from Patient where Age = '%s'" % (entry.get())
    elif flag == 'sex':
            sql = "select * from Patient where Gender = '%s'" % (entry.get())
    else:
            sql = "select * from Patient where Number = '%s'" % (entry.get())

    return sql


# (6.6)
def find_use_Info(tree, entry, flag):
    delButton(tree)
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    sql = find_sql_line(flag=flag, entry=entry)
    cur.execute(sql)
    results = cur.fetchall()
    if results:
        for item in results:
            tree.insert('', "end", values=item)
    else:
        showinfo('提示', '无该信息！')
    cur.close()
    db.close()


image7 = None
img7 = None


# （7）诊断信息操作页面
def MangerPage(root1,table):
    global image7
    global img7
    if table != '医生':
        showinfo('提示','只有医生可以进行诊断')
        return
    root1.destroy()
    root1 = Tk()
    root1.geometry('1000x700+300+50')
    root1.title('诊断信息操作页面')
    root1['background'] = 'white'
    image7 = Image.open('logo2.png')
    img7 = ImageTk.PhotoImage(image7)
    Label(root1, text='诊断信息操作页面', bg='white', fg='blue', font=('楷体', 20), compound='bottom',
          image=img7).pack()
    Label(root1, text="诊断编号：", font=('楷体', 13)).place(relx=0.48, rely=0.07, relwidth=0.12)
    Label(root1, text="诊断时间：", font=('楷体', 13)).place(relx=0.48, rely=0.12, relwidth=0.12)
    Label(root1, text="科室：", font=('楷体', 13)).place(relx=0.48, rely=0.17, relwidth=0.12)
    Label(root1, text="医生：", font=('楷体', 13)).place(relx=0.48, rely=0.22, relwidth=0.12)
    Label(root1, text="受诊人身份证号：", font=('楷体', 13)).place(relx=0.48, rely=0.27, relwidth=0.12)
    Label(root1, text="受诊人：", font=('楷体', 13)).place(relx=0.48, rely=0.32, relwidth=0.12)
    Label(root1, text="症状：", font=('楷体', 13)).place(relx=0.48, rely=0.37, relwidth=0.12)
    Label(root1, text="医嘱：", font=('楷体', 13)).place(relx=0.48, rely=0.42, relwidth=0.12)

    Dnum = StringVar()
    Dtime = StringVar()
    Department = StringVar()
    DocName = StringVar()
    PatID = StringVar()
    PatName = StringVar()
    Symptom = StringVar()
    Advice = StringVar()

    entry_Dnum = Entry(root1, textvariable=Dnum)
    entry_Dnum.place(relx=0.6, rely=0.07, relwidth=0.3, height=25)
    entry_Dtime = Entry(root1, textvariable=Dtime)
    entry_Dtime.place(relx=0.6, rely=0.12, relwidth=0.3, height=25)
    entry_Department = Entry(root1, textvariable=Department)
    entry_Department.place(relx=0.6, rely=0.17, relwidth=0.3, height=25)
    entry_DocName = Entry(root1, textvariable=DocName)
    entry_DocName.place(relx=0.6, rely=0.22, relwidth=0.3, height=25)
    entry_PatID = Entry(root1, textvariable=PatID)
    entry_PatID.place(relx=0.6, rely=0.27, relwidth=0.3, height=25)
    entry_PatName = Entry(root1, textvariable=PatName)
    entry_PatName.place(relx=0.6, rely=0.32, relwidth=0.3, height=25)
    entry_Symptom = Entry(root1, textvariable=Symptom)
    entry_Symptom.place(relx=0.6, rely=0.37, relwidth=0.3, height=25)
    entry_Advice = Entry(root1, textvariable=Advice)
    entry_Advice.place(relx=0.6, rely=0.42, relwidth=0.3, height=25)

    list1 = [entry_Dnum, entry_Dtime, entry_Department, entry_DocName, entry_PatID, PatName,
             entry_Symptom, entry_Advice]

    Tree1 = ttk.Treeview(root1, show='headings',
                         column=(
                         'Dnum', 'Dtime', 'Department', 'DocName', 'PatID', 'PatName', 'Symptom',
                         'Advice'))
    Tree1.column('Dnum', width=50, anchor="center")
    Tree1.column('Dtime', width=60, anchor="center")
    Tree1.column('Department', width=40, anchor="center")
    Tree1.column('DocName', width=50, anchor="center")
    Tree1.column('PatID', width=90, anchor="center")
    Tree1.column('PatName', width=50, anchor="center")
    Tree1.column('Symptom', width=70, anchor="center")
    Tree1.column('Advice', width=70, anchor="center")

    Tree1.heading('Dnum', text='诊断编号')
    Tree1.heading('Dtime', text='诊断时间')
    Tree1.heading('Department', text='科室')
    Tree1.heading('DocName', text='医生')
    Tree1.heading('PatID', text='受诊人身份证号')
    Tree1.heading('PatName', text='受诊人')
    Tree1.heading('Symptom', text='症状')
    Tree1.heading('Advice', text='医嘱')

    Tree1.place(rely=0.65, relwidth=1)

    Button(root1, text="根据编号查找", activebackground='gray', font=('楷体', 13),
           command=lambda: findInfo(check=1, tree=Tree1, list=list1)).place(relx=0.15, rely=0.17, width=150)
    Button(root1, text="查询所有诊断", activebackground='gray', font=('楷体', 13),
           command=lambda: showAllInfo(tree=Tree1)).place(relx=0.15, rely=0.10, width=150)
    Button(root1, text="开具诊断", activebackground='gray', font=('楷体', 13),
           command=lambda: appendInfo(tree=Tree1, list=list1)).place(relx=0.15, rely=0.24, width=150)
    Button(root1, text="删除诊断", activebackground='gray', font=('楷体', 13),
           command=lambda: deleteInfo(tree=Tree1)).place(relx=0.15, rely=0.31, width=150)
    Button(root1, text="更改诊断信息", activebackground='gray', font=('楷体', 13),
           command=lambda: updateInfo(tree=Tree1, list=list1)).place(relx=0.15, rely=0.38, width=150)

    def treeviewClick(event):
        item = Tree1.selection()
        item_text = Tree1.item(item, "values")

        entry_Dnum.delete(0, 'end')
        entry_Dtime.delete(0, 'end')
        entry_Department.delete(0, 'end')
        entry_DocName.delete(0, 'end')
        entry_PatID.delete(0, 'end')
        entry_PatName.delete(0, 'end')
        entry_Symptom.delete(0, 'end')
        entry_Advice.delete(0, 'end')

        entry_Dnum.insert(0, item_text[0])
        entry_Dtime.insert(0, item_text[1])
        entry_Department.insert(0, item_text[2])
        entry_DocName.insert(0, item_text[3])
        entry_PatID.insert(0, item_text[4])
        entry_PatName.insert(0, item_text[5])
        entry_Symptom.insert(0, item_text[6])
        entry_Advice.insert(0, item_text[7])

    Tree1.bind('<ButtonRelease-1>', treeviewClick)
    root1.protocol('WM_DELETE_WINDOW', lambda: MangerChoosePage(root1,table))
    root1.mainloop()

image11 = None
img11 = None

def MedicineChoosePage(root1, table):
    global image11
    global img11
    if table != '医生':
        showinfo('提示', '只有医生可以进行开药')
        return
    root1.destroy()
    root1 = Tk()
    root1.geometry('490x650+500+100')
    root1.title('开药信息操作页面')
    root1['background'] = 'white'
    image11 = Image.open('logo.png')
    img11 = ImageTk.PhotoImage(image11)
    Label(root1, text='开药信息操作页面', bg='white', fg='blue', font=('楷体', 20), compound='bottom',
          image=img11).pack()
    Label(root1, text="药品编号：", font=('楷体', 13)).place(relx=0.48, rely=0.10, relwidth=0.16)
    Label(root1, text="药品名称：", font=('楷体', 13)).place(relx=0.48, rely=0.20, relwidth=0.16)
    Label(root1, text="诊断编号：", font=('楷体', 13)).place(relx=0.48, rely=0.30, relwidth=0.16)
    Label(root1, text="开药：", font=('楷体', 13)).place(relx=0.1, rely=0.40, relwidth=0.16)

    MID = StringVar()
    Mname = StringVar()
    DID = StringVar()
    Pres = StringVar()

    entry_MID = Entry(root1, textvariable=MID)
    entry_MID.place(relx=0.6, rely=0.10, relwidth=0.3, height=25)
    entry_Mname = Entry(root1, textvariable=Mname)
    entry_Mname.place(relx=0.6, rely=0.20, relwidth=0.3, height=25)
    entry_DID = Entry(root1, textvariable=DID)
    entry_DID.place(relx=0.6, rely=0.30, relwidth=0.3, height=25)
    entry_Pres = Entry(root1, textvariable=Pres)
    entry_Pres.place(relx=0.22, rely=0.40, relwidth=0.7, height=25)

    Tree1 = ttk.Treeview(root1, show='headings', column=('MID', 'Mname', 'Mprice'))
    Tree1.column('MID', width=100, anchor="center")
    Tree1.column('Mname', width=150, anchor="center")
    Tree1.column('Mprice', width=100, anchor="center")

    Tree1.heading('MID', text='药品编号')
    Tree1.heading('Mname', text='药品名称')
    Tree1.heading('Mprice', text='药品价格')

    Tree1.place(rely=0.65, relwidth=1)

    Button(root1, text="查找药品编号", activebackground='gray', font=('楷体', 13),
           command=lambda: Doc_Find_medi_Name(tree=Tree1, entry_name=entry_Mname)).place(relx=0.1, rely=0.20, width=150)
    Button(root1, text="查找药品名称", activebackground='gray', font=('楷体', 13),
           command=lambda: Doc_Find_medi_ID(tree=Tree1, entry_MID=entry_MID)).place(relx=0.1, rely=0.10, width=150)
    Button(root1, text="开药", activebackground='gray', font=('楷体', 13),
            command=lambda: DoPres(Tree1, entry_DID.get(), entry_Pres.get().split(','))).place(relx=0.1, rely=0.30, width=150)
    root1.protocol('WM_DELETE_WINDOW', lambda: MangerChoosePage(root1, table))
    root1.mainloop()

def Doc_Find_medi_ID(tree, entry_MID):
    delButton(tree)  # 清空Treeview中的所有行
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    try:
        query = """
                SELECT 
                    *
                FROM 
                    Medicine
                WHERE 
                    MedicineID = %s
                """
        cur.execute(query, (entry_MID.get()))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            for item in results:
                tree.insert('', "end", values=item)
    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()

def Doc_Find_medi_Name(tree, entry_name):
    delButton(tree)  # 清空Treeview中的所有行
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    try:
        query = """
                SELECT 
                    *
                FROM 
                    Medicine
                WHERE 
                    Name = %s
                """
        cur.execute(query, (entry_name.get()))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            for item in results:
                tree.insert('', "end", values=item)
    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()

def DoPres(tree, num, med_list):
    delButton(tree)

    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    sql = """
        INSERT INTO Prescript
        VALUES (%s, %s)
    """
    try:
        for element in med_list:
            cur.execute(sql, (num, element))
            db.commit()
        showinfo(title='提示', message='开药成功！')
    except pymysql.MySQLError as e:
        db.rollback()
        showerror(title='提示', message='操作失败，请重试！')
    except Exception as e:
        db.rollback()
        print(e)
        showerror(title='提示', message='操作失败，请重试！')
    finally:
        cur.close()
        db.close()

# (7.1)
def showAllInfo(tree):
    delButton(tree)
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()  # 用db操作游标
    sql =   '''
        SELECT
            d.PrescriptionID, 
            d.DiagnosisDate, 
            st.Department, 
            st.Name AS DocName, 
            p.PatientID AS PatID,
            p.Name AS PatName, 
            r.Symptom, 
            r.advice 
        FROM 
            Diagnosis d
        JOIN 
            Staff st ON d.DoctorID = st.StaffID
        JOIN 
            Patient p ON d.PatientID = p.PatientID
        JOIN 
            Prescription r ON d.PrescriptionID = r.PrescriptionID
        '''
    cur.execute(sql)
    results = cur.fetchall()
    for item in results:
        tree.insert('', "end", values=item)
    cur.close()
    db.close()  # 关闭连接


# (7.2)
def appendInfo(tree, list):
    delButton(tree)
    list2 = []
    for i in range(len(list)):
        if list[i].get() == '':
            showerror(title='提示', message='输入不能为空!')
            return
        else:
            list2.append(list[i].get())

    x = tree.get_children()
    for item in x:
        tree.delete(item)

    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    try:
        cur.execute("CALL UpdateDiagnosis(%s, %s, %s, %s, %s, %s)",
                    (list2[0], list2[6], list2[7], list2[3], list2[4], list2[1]))
        db.commit()
        showinfo(title='提示', message='添加/更新成功！')

        showAllInfo(tree)
    except pymysql.MySQLError as e:
        db.rollback()
        error_msg = str(e)
        print(error_msg)
        if '医生未找到' in error_msg:
            showerror(title='错误', message='医生未找到')
        elif 'PrescriptionID长度必须大于等于1且小于等于15' in error_msg:
            showerror(title='错误', message='PrescriptionID长度必须大于等于1且小于等于15')
        elif 'DiagnosisDate必须在2022年到当前日期之间' in error_msg:
            showerror(title='错误', message='DiagnosisDate必须在2022年到当前日期之间')
        else:
            showerror(title='提示', message='操作失败，请重试！')
    except Exception as e:
        db.rollback()
        print(e)
        showerror(title='提示', message='操作失败，请重试！')
    finally:
        cur.close()
        db.close()


# (7.3)
def deleteInfo(tree):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    res = askyesno('提示！', '是否确认删除？')
    if res == True:
        for item in tree.selection():
            selectedItem = tree.selection()[0]
            no1 = tree.item(selectedItem, 'values')[0]
            tree.delete(item)

            db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
            try:
                cur = db.cursor()
                cur.execute("START TRANSACTION")

                # 确认相关记录的存在及其关系
                cur.execute("""
                    SELECT d.PrescriptionID
                    FROM Diagnosis d
                    JOIN Prescription p ON d.PrescriptionID = p.PrescriptionID
                    WHERE d.PrescriptionID = %s
                """, (no1,))
                result = cur.fetchone()
                if not result:
                    raise ValueError("未找到相关记录")

                # 删除 Diagnosis 表中的记录
                cur.execute("DELETE FROM Diagnosis WHERE PrescriptionID = %s", (no1,))

                # 删除 Prescription 表中的记录
                cur.execute("DELETE FROM Prescription WHERE PrescriptionID = %s", (no1,))

                db.commit()
                showinfo(title='提示', message='删除成功！')

            except pymysql.MySQLError as e:
                db.rollback()
                showerror(title='错误', message=f'删除失败: {e}')

            except ValueError as ve:
                db.rollback()
                showerror(title='错误', message=str(ve))

            finally:
                cur.close()
                db.close()


# (7.4)
def updateInfo(tree, list):
    if not tree.selection():
        showerror(title='提示', message='请选择一条信息！')
        return
    else:
        res = askyesno("提示！", "是否确认更新数据？")
        if res == True:
            selectedItem = tree.selection()[0]
            no1 = tree.item(selectedItem, 'values')[0]

            db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
            cur = db.cursor()
            list2 = []
            for i in range(len(list)):
                if list[i].get() == '':
                    showerror(title='提示', message='输入不能为空!')
                    return
                else:
                    list2.append(list[i].get())

            try:
                cur.execute("CALL UpdateDiagnosis(%s, %s, %s, %s, %s, %s)",
                            (list2[0], list2[6], list2[7], list2[3], list2[4], list2[1]))

                # Commit the transaction if everything goes well
                cur.execute("COMMIT")
                showinfo(title='提示', message='更新成功！')
            except pymysql.MySQLError as e:
                db.rollback()
                error_msg = str(e)
                print(error_msg)
                if '医生未找到' in error_msg:
                    showerror(title='错误', message='医生未找到')
                elif 'PrescriptionID长度必须大于等于1且小于等于15' in error_msg:
                    showerror(title='错误', message='PrescriptionID长度必须大于等于1且小于等于15')
                elif 'DiagnosisDate必须在2022年到当前日期之间' in error_msg:
                    showerror(title='错误', message='DiagnosisDate必须在2022年到当前日期之间')
                else:
                    showerror(title='提示', message='操作失败，请重试！')
            except Exception as e:
                db.rollback()
                print(e)
                showerror(title='提示', message='操作失败，请重试！')
            finally:
                showAllInfo(tree)
                cur.close()
                db.close()


# (7.5)
def findInfo(check, tree, list):
    if check:
        delButton(tree)
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    sql = '''
           SELECT
               PrescriptionID, 
               DiagnosisDate, 
               Department, 
               DocName, 
               PatID,
               PatName, 
               Symptom, 
               advice 
           FROM 
               DiagnosisInfo
           WHERE
               PrescriptionID = %s
           '''
    cur.execute(sql, (list[0].get()))
    results = cur.fetchall()
    if results:
        for item in results:
            tree.insert('', "end", values=item)
    else:
        showinfo(title='提示', message='无该诊断编号！')
    cur.close()
    db.close()



image5 = None
img5 = None


# (8)游客订单信息查询页面
def GuestPage(root):
    global image5
    global img5
    root.destroy()
    root = Tk()
    root.title('诊断书查询页面')
    root.geometry('850x730+300+50')
    root['background'] = 'white'
    image5 = Image.open('logo.png')
    img5 = ImageTk.PhotoImage(image5)
    Label(root, text='病人诊断书查询页面', compound='bottom', image=img5, bg='white', fg='blue',
          font=('楷体', 20)).pack(side=TOP, fill='x')
    Label(root, text='诊断号：', font=('楷体', 13)).place(relx=0.07, rely=0.15, relwidth=0.15)
    Label(root, text='受诊人姓名：', font=('楷体', 13)).place(relx=0.07, rely=0.25, relwidth=0.15)
    Label(root, text='受诊人身份证号：', font=('楷体', 13)).place(relx=0.07, rely=0.35, relwidth=0.15)
    Label(root, text='诊断日期：', font=('楷体', 13)).place(relx=0.07, rely=0.45, relwidth=0.15)

    Onum = StringVar()
    Sname = StringVar()
    SID = StringVar()
    Otime = StringVar()

    entry_Onum = Entry(root, textvariable=Onum)
    entry_Onum.place(relx=0.2, rely=0.15, relwidth=0.3, height=25)
    entry_Sname = Entry(root, textvariable=Sname)
    entry_Sname.place(relx=0.2, rely=0.25, relwidth=0.3, height=25)
    entry_SID = Entry(root, textvariable=SID)
    entry_SID.place(relx=0.2, rely=0.35, relwidth=0.3, height=25)
    entry_Otime = Entry(root, textvariable=Otime)
    entry_Otime.place(relx=0.2, rely=0.45, relwidth=0.3, height=25)

    Tree1 = ttk.Treeview(root, show='headings', column=('Onum', \
                                                        'Otime', 'Department', 'Docname', 'Sname',
                                                        'Symptom', 'Advice'))
    Tree1.column('Onum', width=50, anchor="center")
    Tree1.column('Otime', width=80, anchor="center")
    Tree1.column('Department', width=40, anchor="center")
    Tree1.column('Docname', width=40, anchor="center")
    Tree1.column('Sname', width=40, anchor="center")
    Tree1.column('Symptom', width=100, anchor="center")
    Tree1.column('Advice', width=100, anchor="center")
    # 表格标题设置
    Tree1.heading('Onum', text='诊断编号')
    Tree1.heading('Otime', text='诊断日期')
    Tree1.heading('Department', text='科室')
    Tree1.heading('Docname', text='医生姓名')
    Tree1.heading('Sname', text='受诊人')
    Tree1.heading('Symptom', text='症状')
    Tree1.heading('Advice', text='医嘱')
    Tree1.place(rely=0.6, relwidth=1)

    Button(root, text="按诊断编号查询", bg='gainsboro', fg='black', activebackground='grey', font=('楷体', 13),
           command=lambda: Find_infor_num(Tree1, entry_Onum)).place(relx=0.65, rely=0.15, width=150)
    Button(root, text="按姓名和诊断日期查询", bg='gainsboro', fg='black', activebackground='grey', font=('楷体', 13),
           command=lambda: Find_infor_name(Tree1, entry_Sname, entry_Otime)).place(relx=0.65, rely=0.3, width=150)
    Button(root, text="按身份证号查询", bg='gainsboro', fg='black', activebackground='grey', font=('楷体', 13),
           command=lambda: Find_infor_ID(Tree1, entry_SID)).place(relx=0.65, rely=0.45, width=150)
    root.protocol('WM_DELETE_WINDOW', lambda: PatientChoosePage(root))
    root.mainloop()


# (8.1)
def Find_infor_num(Tree1, entry_Onum):
    delButton(Tree1)  # 清空Treeview中的所有行
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()

    try:
        # 构建查询语句
        query = """
        SELECT 
            d.PrescriptionID, 
            d.DiagnosisDate, 
            s.Department, 
            s.Name AS DoctorName, 
            p.Name AS PatientName, 
            r.Symptom, 
            r.advice 
        FROM 
            Diagnosis d
        JOIN 
            Staff s ON d.DoctorID = s.StaffID
        JOIN 
            Patient p ON d.PatientID = p.PatientID
        JOIN 
            Prescription r ON d.PrescriptionID = r.PrescriptionID
        WHERE 
            d.PrescriptionID = %s
        """
        cur.execute(query, (entry_Onum.get(),))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            for item in results:
                Tree1.insert('', "end", values=item)
        else:
            showinfo(title='提示', message='无该订单编号！')

    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()


# (8.2)
def Find_infor_name(Tree1, entry_Sname, entry_Otime):
    delButton(Tree1)  # 清空Treeview中的所有行
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()

    try:
        query = """
        SELECT 
            d.PrescriptionID, 
            d.DiagnosisDate, 
            st.Department, 
            st.Name AS DoctorName, 
            p.Name AS PatientName, 
            r.Symptom, 
            r.advice 
        FROM 
            Diagnosis d
        JOIN 
            Staff st ON d.DoctorID = st.StaffID
        JOIN 
            Patient p ON d.PatientID = p.PatientID
        JOIN 
            Prescription r ON d.PrescriptionID = r.PrescriptionID
        WHERE 
            p.Name = %s AND d.DiagnosisDate = %s
        """
        cur.execute(query, (entry_Sname.get(), entry_Otime.get()))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            for item in results:
                Tree1.insert('', "end", values=item)
        else:
            showinfo(title='提示', message='无该受诊人或日期的记录！')

    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()



# (8.3)
def Find_infor_ID(Tree1, entry_SID):
    delButton(Tree1)
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()

    try:
        query = """
        SELECT 
            d.PrescriptionID, 
            d.DiagnosisDate, 
            st.Department, 
            st.Name AS DoctorName, 
            p.Name AS PatientName, 
            r.Symptom, 
            r.advice 
        FROM 
            Diagnosis d
        JOIN 
            Staff st ON d.DoctorID = st.StaffID
        JOIN 
            Patient p ON d.PatientID = p.PatientID
        JOIN 
            Prescription r ON d.PrescriptionID = r.PrescriptionID
        WHERE 
            p.PatientID = %s 
        """
        cur.execute(query, (entry_SID.get(), ))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            for item in results:
                Tree1.insert('', "end", values=item)
        else:
            showinfo(title='提示', message='无该受诊人的记录！')

    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()

image10 = None
img10 = None

# (10)药品查询页面
def MedicinePage(root):
    global image10
    global img10
    root.destroy()
    root = Tk()
    root.title('药品查询页面')
    root.geometry('850x730+300+50')
    root['background'] = 'white'
    image5 = Image.open('logo.png')
    img5 = ImageTk.PhotoImage(image5)
    Label(root, text='病人药品查询页面', compound='bottom', image=img5, bg='white', fg='blue',
          font=('楷体', 20)).pack(side=TOP, fill='x')
    Label(root, text='诊断号：', font=('楷体', 13)).place(relx=0.07, rely=0.15, relwidth=0.15)
    Label(root, text='受诊人姓名：', font=('楷体', 13)).place(relx=0.07, rely=0.25, relwidth=0.15)
    Label(root, text='受诊人身份证号：', font=('楷体', 13)).place(relx=0.07, rely=0.35, relwidth=0.15)
    Label(root, text='诊断日期：', font=('楷体', 13)).place(relx=0.07, rely=0.45, relwidth=0.15)
    total_price_label = Label(root, text="总价: 0")
    total_price_label.pack()
    Onum = StringVar()
    Sname = StringVar()
    SID = StringVar()
    Otime = StringVar()

    entry_Onum = Entry(root, textvariable=Onum)
    entry_Onum.place(relx=0.2, rely=0.15, relwidth=0.3, height=25)
    entry_Sname = Entry(root, textvariable=Sname)
    entry_Sname.place(relx=0.2, rely=0.25, relwidth=0.3, height=25)
    entry_SID = Entry(root, textvariable=SID)
    entry_SID.place(relx=0.2, rely=0.35, relwidth=0.3, height=25)
    entry_Otime = Entry(root, textvariable=Otime)
    entry_Otime.place(relx=0.2, rely=0.45, relwidth=0.3, height=25)

    Tree1 = ttk.Treeview(root, show='headings', column=('Onum', \
                                                        'Ptime','Pname','MID',
                                                        'Mname', 'Mprice'))
    Tree1.column('Onum', width=80, anchor="center")
    Tree1.column('Ptime', width=80, anchor="center")
    Tree1.column('Pname', width=80, anchor="center")
    Tree1.column('MID', width=80, anchor="center")
    Tree1.column('Mname', width=80, anchor="center")
    Tree1.column('Mprice', width=50, anchor="center")
    # 表格标题设置
    Tree1.heading('Onum', text='诊断编号')
    Tree1.heading('Ptime', text='受诊日期')
    Tree1.heading('Pname', text='受诊人姓名')
    Tree1.heading('MID', text='药品编号')
    Tree1.heading('Mname', text='药品名称')
    Tree1.heading('Mprice', text='药品价格')
    Tree1.place(rely=0.6, relwidth=1)

    Button(root, text="按诊断编号查询", bg='gainsboro', fg='black', activebackground='grey', font=('楷体', 13),
           command=lambda: Find_medi_num(Tree1, entry_Onum,total_price_label)).place(relx=0.65, rely=0.15, width=150)
    Button(root, text="按姓名和诊断日期查询", bg='gainsboro', fg='black', activebackground='grey', font=('楷体', 13),
           command=lambda: Find_medi_name(Tree1, entry_Sname, entry_Otime,total_price_label)).place(relx=0.65, rely=0.3, width=150)
    Button(root, text="按身份证号查询", bg='gainsboro', fg='black', activebackground='grey', font=('楷体', 13),
           command=lambda: Find_medi_ID(Tree1, entry_SID,total_price_label)).place(relx=0.65, rely=0.45, width=150)
    root.protocol('WM_DELETE_WINDOW', lambda: PatientChoosePage(root))
    root.mainloop()

import pymysql
from tkinter.messagebox import showinfo

def Find_medi_name(Tree1, entry_Sname, entry_Otime,total_price_label):
    delButton(Tree1)  # 清空Treeview中的所有行
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()

    try:
        query = """
                SELECT 
                    d.PrescriptionID, 
                    d.DiagnosisDate, 
                    p.Name AS PName, 
                    m.MedicineID,
                    m.Name,
                    m.Price
                FROM 
                    Diagnosis d
                JOIN 
                    Patient p ON d.PatientID = p.PatientID
                JOIN 
                    Prescript p2 ON d.PrescriptionID = p2.PrescriptionID
                JOIN
                    Medicine m ON p2.MedicineID = m.MedicineID
                WHERE 
                    p.Name = %s AND d.DiagnosisDate = %s
                """
        cur.execute(query, (entry_Sname.get(), entry_Otime.get()))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            total_price = 0  # 初始化总价
            for item in results:
                Tree1.insert('', "end", values=item)
                total_price += item[5]  # 累加每个药品的价格（假设价格在第六个字段）

            # 在Label上显示总价
            total_price_label.config(text=f"总价: {total_price}")
        else:
            total_price_label.config(text="总价: 0")  # 如果没有结果，总价设置为0
            showinfo(title='提示', message='无该受诊人或日期的记录！')
    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()

def Find_medi_num(Tree1, entry_Onum,total_price_label):
    delButton(Tree1)  # 清空Treeview中的所有行
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()
    try:
        query = """
                SELECT 
                    d.PrescriptionID, 
                    d.DiagnosisDate, 
                    p.Name AS PName, 
                    m.MedicineID,
                    m.Name,
                    m.Price
                FROM 
                    Diagnosis d
                JOIN 
                    Patient p ON d.PatientID = p.PatientID
                JOIN 
                    Prescript p2 ON d.PrescriptionID = p2.PrescriptionID
                JOIN
                    Medicine m ON p2.MedicineID = m.MedicineID
                WHERE 
                    d.PrescriptionID = %s
                """
        cur.execute(query, (entry_Onum.get(),))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            total_price = 0  # 初始化总价
            for item in results:
                Tree1.insert('', "end", values=item)
                total_price += item[5]  # 累加每个药品的价格（假设价格在第六个字段）

            # 在Label上显示总价
            total_price_label.config(text=f"总价: {total_price}")
        else:
            total_price_label.config(text="总价: 0")  # 如果没有结果，总价设置为0
            showinfo(title='提示', message='无该受诊人或日期的记录！')
    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()

def Find_medi_ID(Tree1, entry_SID,total_price_label):
    delButton(Tree1)
    db = pymysql.connect(host="localhost", user="root", password="glgldsk.", db="db", port=3306)
    cur = db.cursor()

    try:
        query = """
                SELECT 
                    d.PrescriptionID, 
                    d.DiagnosisDate, 
                    p.Name AS PName, 
                    m.MedicineID,
                    m.Name,
                    m.Price
                FROM 
                    Diagnosis d
                JOIN 
                    Patient p ON d.PatientID = p.PatientID
                JOIN 
                    Prescript p2 ON d.PrescriptionID = p2.PrescriptionID
                JOIN
                    Medicine m ON p2.MedicineID = m.MedicineID
                WHERE 
                    p.PatientID = %s
                """
        cur.execute(query, (entry_SID.get(),))
        results = cur.fetchall()  # 获取查询的所有记录

        if results:
            total_price = 0  # 初始化总价
            for item in results:
                Tree1.insert('', "end", values=item)
                total_price += item[5]  # 累加每个药品的价格（假设价格在第六个字段）

            # 在Label上显示总价
            total_price_label.config(text=f"总价: {total_price}")
        else:
            total_price_label.config(text="总价: 0")  # 如果没有结果，总价设置为0
            showinfo(title='提示', message='无该受诊人或日期的记录！')
    except Exception as e:
        print(f"Error: {e}")
        showinfo(title='错误', message='查询出错，请检查数据库连接和查询语句。')

    finally:
        cur.close()
        db.close()

if __name__ == '__main__':
    StartPage()