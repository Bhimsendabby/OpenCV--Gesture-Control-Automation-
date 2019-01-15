from tkinter import *
from tkinter import ttk
import mygesture
import speech_message
import FaceDetection
def g():
    # FaceDetection.haarcascade.call_haarcascade()
    mygesture.gesture.call_gesture()

def s():
    s1 = speech_message.speech_message()
    s1.start()
class main_page:
    @classmethod
    def call_main(cls):
        root = Toplevel()
        root.title("Title")
        root.geometry("600x600")

        left = Frame(root, borderwidth=2, relief="solid")
        right = Frame(root, borderwidth=2, relief="solid")
        container = Frame(left, borderwidth=2, relief="solid")
        box1 = Frame(right, borderwidth=2, relief="solid")
        box2 = Frame(right, borderwidth=2, relief="solid")


        canvas = Canvas(left, width=645, height=230)
        canvas.pack()
        my = PhotoImage(file='D:\\gesture4.gif')
        canvas.config(background="tomato")
        canvas.create_image(0, 0, anchor=NW, image=my)
        title = Label(left,text="WELCOME TO GESTURE MESSENGER", font=("Helvetica", 16), foreground="white",background="tomato")
        title.place(x=350,y=200)

        canvas_container = Canvas(container, width=500, height=1000)
        canvas_container.pack()
        my_1 = PhotoImage(file='D:\\gest.gif')
        canvas_container.config(background="skyblue")
        container.config(background="skyblue")
        canvas_container.create_image(0, 0, anchor=NW, image=my_1)

        label_1=Label(container,text="FIRST GESTURE CAN SEND MESSAGE TO MOM ",font=("Helvetica", 18), foreground="skyblue",background="white")
        label_1.place(x=125,y=100)
        label_2 = Label(container, text="SECOND GESTURE CAN SEND MESSAGE ON WHATSAPP TO BROTHER ", font=("Helvetica", 18),  foreground="tomato",background="white")
        label_2.place(x=125 ,y=150)
        label_3 = Label(container, text="THIRD GESTURE CAN LOGIN INTO FACEBOOK", font=("Helvetica", 18),  foreground="skyblue",background="white")
        label_3.place(x=125, y=200)
        label_4 = Label(container, text="FOURTH GESTURE CAN SEND MESSAGE TO DAD", font=("Helvetica", 18), foreground="tomato",background="white")
        label_4.place(x=125, y=250)
        label_5 = Label(container, text="FIFTH GESTURE CAN SHOW MY ATTENDANCE", font=("Helvetica", 18),  foreground="skyblue",  background="white")
        label_5.place(x=125, y=300)
        label_6 = Label(container,text="YOU CAN SEND MESSAGE TO MOM,DAD,BROTHER THROUGH SPEECH ALSO", font=("Helvetica", 18),  foreground="tomato",background="white")
        label_6.place(x=125,y=350)

        heading_label = Label(box1,text="YOU CAN START HERE",font=("Helvetica",25, "bold"),  foreground="skyblue",background="white")
        heading_label.place(x=40,y=30)
        start_button = Button(box1,command=g,text="Gesture Message", font=("Helvetica", 16, "bold"), foreground="white",background="tomato")
        start_button.place(x=125,y=90)
        speech_button = Button(box1,text="Speech Message",command=s,font=("Helvetica", 16, "bold"), foreground="white",background="tomato")
        speech_button.place(x=125,y=150)

        lbl_req = Label(box2,text="Please use white background",font=("Helvetica",15, "bold"),  foreground="tomato",background="white")
        lbl_req.place(x=40,y=30)
        lbl_power = Label(box2, text="Made by:", font=("Helvetica", 15, "bold"), foreground="skyblue",background="white")
        lbl_power.place(x=40, y=80)
        lbl_power = Label(box2, text="Bhim Sen", font=("Helvetica", 15, "bold"), foreground="tomato",
                          background="white")
        lbl_power.place(x=40, y=130)
        lbl_power = Label(box2, text="Arunav Goel", font=("Helvetica", 15, "bold"), foreground="tomato",
                          background="white")
        lbl_power.place(x=40, y=180)
        left.pack(side="left", expand=True, fill="both")
        right.pack(side="right", expand=True, fill="both")
        container.pack(expand=True, fill="both", padx=5, pady=5)
        box1.pack(expand=True, fill="both", padx=10, pady=10)
        box2.pack(expand=True, fill="both", padx=10, pady=10)



        root.mainloop()