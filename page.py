from tkinter import *
import user
from PIL import Image, ImageTk
import mysql.connector

import main_page

def fun():
    root1 = Toplevel()
    root1.title("Title")
    root1.geometry("600x600")


    class Example(Frame):
        def __init__(self, master, *pargs):
            Frame.__init__(self, master, *pargs)

            self.image = Image.open("D:\\ges.gif")
            self.img_copy = self.image.copy()

            self.background_image = ImageTk.PhotoImage(self.image)

            self.background = Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)

        def _resize_image(self, event):
            new_width = event.width
            new_height = event.height

            self.image = self.img_copy.resize((new_width, new_height))

            self.background_image = ImageTk.PhotoImage(self.image)
            self.background.configure(image=self.background_image)

    e = Example(root1)
    e.pack(fill=BOTH, expand=YES)

    class sign_up_page():

        @classmethod
        def onclick_sign_up(cls):
            def send_to_database():
                name = entry_name.get()
                mail = entry_mail.get()
                pass_ = entry_pass.get()
                connection = mysql.connector.connect(user="root", password="", database="users")

                u1 = user.user(name, mail, pass_)
                print(connection.is_connected())
                cursor = connection.cursor()
                print(type(cursor))
                sql3 = "insert into users values('{}','{}','{}')".format(u1.name, u1.email,u1.password)
                cursor.execute(sql3)
                connection.commit()
                sign_in_label = Label(root1, text="you are successfully registered", font=("Helvetica",20, "bold"),
                                      foreground="tomato", background="white")
                sign_in_label.place(x=570, y=600)
            lblhead = Label(root1, text="GESTURE MESSENGER", font=("Helvetica", 40, "bold"), foreground="white",
                            background="tomato")
            lblhead.place(x=400, y=100)

            lbl_sign = Label(root1, text="sign up", font=("Helvetica", 30, "bold"), foreground="tomato", background="white")
            lbl_sign.place(x=650, y=170)

            lbl_name = Label(root1, text="Name", font=("Helvetica", 16, "bold"), foreground="black")
            lbl_name.place(x=475, y=259)

            lbl_mail = Label(root1, text="E-mail", font=("Helvetica", 16, "bold"))
            lbl_mail.place(x=475, y=310)

            lbl_pass = Label(root1, text="password", font=("Helvetica", 16, "bold"))
            lbl_pass.place(x=440, y=361)

            lbl_repeat_pass = Label(root1, text="Repeat-password", font=("Helvetica", 16, "bold"))
            lbl_repeat_pass.place(x=360, y=411)

            entry_name = Entry(root1, font=("Helvetica", 16) )
            entry_name.configure({"background": "white", "foreground": "black", "width": "30"})
            entry_name.place(x=570, y=260)

            entry_mail = Entry(root1, font=("Helvetica", 16))
            entry_mail.configure({"background": "white", "foreground": "black", "width": "30"})
            entry_mail.place(x=570, y=310)

            entry_pass = Entry(root1, font=("Helvetica", 16), show="*")
            entry_pass.configure({"background": "white", "foreground": "black", "width": "30"})
            entry_pass.place(x=570, y=361)

            entry_repeat_pass = Entry(root1, font=("Helvetica", 16), show="*")
            entry_repeat_pass.configure({"background": "white", "foreground": "black", "width": "30"})
            entry_repeat_pass.place(x=570, y=411)

            btnSubmit = Button(root1,command=send_to_database, text="Register", font=("Helvetica", 16, "bold"), foreground="white", background="tomato")
            btnSubmit.place(x=700, y=500)


            root1.mainloop()
    sign_up_page.onclick_sign_up()

class login_page:
    def login(self):

        def user_login():
            username = entry_username.get()
            password = entry_password.get()

            con1 = mysql.connector.connect(user="root", password="", database="users")

            print(con1.is_connected())
            print(type(con1))
            cursor = con1.cursor()
            print(type(cursor))
            sql3 = "select *from users"
            cursor.execute(sql3)
            rows = cursor.fetchall()
            for row in rows:
                if(username==row[0] and password==row[2]):
                    main_page.main_page.call_main()
            con1.commit()


        root = Tk()
        canvas = Canvas(root, width=1550, height=900)
        canvas.pack()
        root.config(background="white")
        root.geometry('600x400')
        my = PhotoImage(file='D:\people.png')
        canvas.config(background="white")
        canvas.create_image(0, 0, anchor=NW, image=my)




        lbl_heading = Label(root, text="GESTURE MESSENGER", font=("Helvetica", 40, "bold"), foreground="white",background="tomato")
        lbl_heading.place(x=400,y=100)

        lbl_username = Label(root, text="username", font=("Helvetica", 16, "bold"), foreground="black")
        lbl_username.place(x=450,y=209   )

        entry_username = Entry(root, font=("Helvetica", 16))
        entry_username.configure({"background": "white", "foreground": "black", "width": "30"})
        entry_username.place(x=570, y=210)

        lbl_password = Label(root, text="password", font=("Helvetica", 16, "bold"))
        lbl_password.place(x=450,y=260)

        entry_password = Entry(root, font=("Helvetica", 16),show="*")
        entry_password.configure({"background": "white", "foreground": "black", "width": "30"})
        entry_password.place(x=570, y=260)

        btnSubmit = Button(root,command=user_login , text="log in", font=("Helvetica", 16, "bold"), foreground="white",background="tomato")
        btnSubmit.place(x=600, y=350)

        btn_reg = Button(root,command=fun,text="SIGN UP", font=("Helvetica", 16, "bold"), foreground="black")
        btn_reg.place(x=750, y=350)
        root.mainloop()

e = login_page()
e.login()

