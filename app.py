import pymysql
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
win=Tk()
win.title('EMPLOYEE MANAGEMENT SYSTEM')
win.config(bg='gray')
win.geometry('800x600')

def show():
    conn=pymysql.connect(user='root',password='Python@123',
                             host='localhost',database='emp_db')
    qur='SELECT * FROM emp'
    mycur=conn.cursor()
    mycur.execute(qur)
    tup1=mycur.fetchall()
    print(tup1)
    for i in tup1:
        treev.insert('',END,values=(i[0],i[1],i[2],i[3],i[4]))
    mycur.close()
    conn.close()

def add():
    emp_id=id1.get()
    emp_name=n1.get()
    mob_num=m1.get()
    dept=d1.get()
    sal=s1.get()
    if emp_id=='' or emp_name=='' or mob_num=='' or dept=='' or sal=='':
        messagebox.showinfo('info','ALL fields are compulsory')
    else:
        conn=pymysql.connect(user='root',password='Python@123',
                             host='localhost',database='emp_db')

        qur=f'INSERT INTO emp VALUES("{emp_id}","{emp_name}","{mob_num}","{dept}","{sal}")'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data inserted successfully')
        id1.set('')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
        
        

def salary():
    root=Tk()
    root.title('SALARY MANAGEMENT SYSTEM')
    root.config(bg='gray')
    root.geometry('800x600')
    
    l8=Label(root,text='ENTER ID>>',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
    l8.place(x=100,y=80)
    
    var3=StringVar()
    e8=Entry(root,textvariable=var3,bg='white',fg='black',width=40,bd=5,
            relief='ridge',font=('times new roman',12,'bold'))
    e8.place(x=310,y=80)
    
    b8=Button(root,text='SHOW SALARY',width=14,command=lambda:show_sal(e8.get(),l9),bd=5,relief='ridge',
              bg='black',fg='white',font=('times new roman',11,'bold'))
    b8.place(x=200,y=120)

    l9=Label(root,text='Result is here >>',bg='white',fg='black',width=40,bd=5,height=5,
        relief='ridge',font=('times new roman',14,'bold'))
    l9.place(x=100,y=200)

    root.mainloop()

def show_sal(id2,l9):
    if id2=='':
        messagebox.showinfo('info','ALL fields are compulsory')
    else:
        conn=pymysql.connect(user='root',password='Python@123',
                             host='localhost',database='emp_db')

        qur=f'SELECT emp_name,emp_salary FROM emp WHERE emp_id="{id2}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        row=mycur.fetchone()
        x=f"{row[0]}'s Salary is {row[1]}"
        l9.config(text=x)
        mycur.close()
        conn.close()
    

def delete():
    del_data=var1.get()
    if del_data=='':
        messagebox.showinfo('info','ALL fields are compulsory')
    else:
        conn=pymysql.connect(user='root',password='Python@123',
                             host='localhost',database='emp_db')

        qur=f'DELETE FROM emp WHERE emp_id="{del_data}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data deleted successfully')
        var1.set('')
    


def select():
    up_data=var2.get()
    if up_data=='':
        messagebox.showinfo('info','ALL fields are compulsory')
    else:
        conn=pymysql.connect(user='root',password='Python@123',
                             host='localhost',database='emp_db')

        qur=f'SELECT * FROM emp WHERE emp_id="{up_data}"'
        mycur=conn.cursor()
        mycur.execute(qur)
        tup1=mycur.fetchone()
        e1.insert(0,tup1[0])
        e2.insert(0,tup1[1])
        e3.insert(0,tup1[2])
        e4.delete(0,END)
        e4.insert(0,tup1[3])
        e5.insert(0,tup1[4])
        mycur.close()
        conn.close()
        
    

def update():
    emp_id=id1.get()
    emp_name=n1.get()
    mob_num=m1.get()
    dept=d1.get()
    sal=s1.get()
    if emp_id=='' or emp_name=='' or mob_num=='' or dept=='' or sal=='':
        messagebox.showinfo('info','ALL fields are compulsory')
    else:
        conn=pymysql.connect(user='root',password='Python@123',
                             host='localhost',database='emp_db')

        qur=f'''UPDATE emp SET emp_id="{emp_id}",emp_name="{emp_name}",mob_no="{mob_num}",
        dept="{dept}",emp_salary="{sal}" WHERE emp_id="{emp_id}"'''
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data updated successfully')
        id1.set('')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
    

def clear():
    treev.delete(*treev.get_children())



# main label
l0=Label(win,text='EMPLOYEE MANAGEMENT SYSTEM',bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',18,'bold'))
l0.place(x=268,y=20)

# emp id >> label and entry

l1=Label(win,text='EMPLOYEE ID',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l1.place(x=100,y=80)

id1=StringVar()
e1=Entry(win,textvariable=id1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e1.place(x=310,y=80)

# emp_name >> label and entry

l2=Label(win,text='EMPLOYEE NAME',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l2.place(x=100,y=120)

n1=StringVar()
e2=Entry(win,textvariable=n1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e2.place(x=310,y=120)

# mob_num >> label entry

l3=Label(win,text='MOBILE NUMBER',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l3.place(x=100,y=160)

m1=StringVar()
e3=Entry(win,textvariable=m1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e3.place(x=310,y=160)

# dept >> label entry

l4=Label(win,text='DEPARTMENT',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l4.place(x=100,y=200)

d1=StringVar()
e4=ttk.Combobox(win,textvariable=d1,width=38,font=('times new roman',12,'bold'))
e4.place(x=310,y=200,height=30)
e4['values']=('R&D','Marketing','Production','HR')
e4.current(0)

# salary >> label ,entry

l5=Label(win,text='SALARY',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l5.place(x=100,y=240)

s1=StringVar()
e5=Entry(win,textvariable=s1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e5.place(x=310,y=240)

# 4 buttons >> show exit add salary

b1=Button(win,text='SHOW',width=12,command=show,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b1.place(x=180,y=300)

b2=Button(win,text='ADD',width=12,command=add,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b2.place(x=410,y=300)

b3=Button(win,text='EXIT',width=12,command=win.destroy,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b3.place(x=180,y=340)

b4=Button(win,text='SALARY',width=12,command=salary,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b4.place(x=410,y=340)


# DELETE INTERFACE
# Label entry button

l6=Label(win,text='ENTER ID>>',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l6.place(x=100,y=400)

var1=StringVar()
e6=Entry(win,textvariable=var1,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e6.place(x=310,y=400)

b5=Button(win,text='DELETE',width=12,command=delete,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b5.place(x=310,y=440)


# UPDATE INTERFACE
# label ,entry ,2 buttons

l7=Label(win,text='ENTER ID>>',bg='white',fg='black',width=20,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
l7.place(x=100,y=490)

var2=StringVar()
e7=Entry(win,textvariable=var2,bg='white',fg='black',width=40,bd=5,
        relief='ridge',font=('times new roman',12,'bold'))
e7.place(x=310,y=490)

b6=Button(win,text='SELECT',width=12,command=select,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b6.place(x=200,y=540)
b7=Button(win,text='UPDATE',width=12,command=update,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b7.place(x=350,y=540)


# tree view

treev=ttk.Treeview(win,height=23)
treev.place(x=700,y=80,width=565)

treev["columns"] = ("1", "2", "3","4","5")
treev['show'] = 'headings'

treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
treev.column("4", width = 90, anchor ='se')
treev.column("5", width = 90, anchor ='se')

treev.heading("1", text ="Emp_ID")
treev.heading("2", text ="Emp_Name")
treev.heading("3", text ="Mob NO")
treev.heading("4", text ="Dept")
treev.heading("5", text ="Salary")

# clear

b8=Button(win,text='CLEAR',width=12,command=clear,bd=5,relief='ridge',
          bg='black',fg='white',font=('times new roman',11,'bold'))
b8.place(x=910,y=570)


win.mainloop()