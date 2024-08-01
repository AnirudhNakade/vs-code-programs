from tkinter import *

class GUI:

    def __init__(self) -> None:
        self.win = Tk()
        self.win.wm_title("Student Details Form")
        self.win.geometry('800x300')

        self.label1 = Label(master=self.win, text="Roll No.", font=('consolas', 18, 'bold'), fg='blue')
        self.label1.place(x=20, y=20, width=250, height=30)

        self.label2 = Label(master=self.win, text="Name", font=('consolas', 18, 'bold'), fg='blue')
        self.label2.place(x=20, y=60, width=250, height=30)

        self.label3 = Label(master=self.win, text="Course", font=('consolas', 18, 'bold'), fg='blue')
        self.label3.place(x=20, y=100, width=250, height=30)

        self.label4 = Label(master=self.win, text="Fees", font=('consolas', 18, 'bold'), fg='blue')
        self.label4.place(x=20, y=140, width=250, height=30)

        self.enrno = Entry(master=self.win, font=('consolas', 18, 'bold'), fg='black')
        self.enrno.place(x=290, y=20, width=250, height=30)
        self.enname = Entry(master=self.win, font=('consolas', 18, 'bold'), fg='black')
        self.enname.place(x=290, y=60, width=250, height=30)
        self.encourse = Entry(master=self.win, font=('consolas', 18, 'bold'), fg='black')
        self.encourse.place(x=290, y=100, width=250, height=30)
        self.enfees = Entry(master=self.win, font=('consolas', 18, 'bold'), fg='black')
        self.enfees.place(x=290, y=140, width=250, height=30)

        self.btnfirst = Button(master=self.win, text="First", font=('consolas', 18, 'bold'))
        self.btnprev = Button(master=self.win, text="Previous", font=('consolas', 18, 'bold'))
        self.btnnext = Button(master=self.win, text="Next", font=('consolas', 18, 'bold'))
        self.btnlast = Button(master=self.win, text="Last", font=('consolas', 18, 'bold'))

        self.btnclr = Button(master=self.win, text="Clear", font=('consolas', 18, 'bold'))
        self.btninsert = Button(master=self.win, text="Insert", font=('consolas', 18, 'bold'))
        self.btnupdate = Button(master=self.win, text="Update", font=('consolas', 18, 'bold'))
        self.btndelete = Button(master=self.win, text="Delete", font=('consolas', 18, 'bold'))

        self.btnfirst.place(x=20, y=190, width=120, height=30)
        self.btnprev.place(x=150, y=190, width=120, height=30)
        self.btnnext.place(x=280, y=190, width=120, height=30)
        self.btnlast.place(x=410, y=190, width=120, height=30)

        self.btnclr.place(x=20, y=240, width=120, height=30)
        self.btninsert.place(x=150, y=240, width=120, height=30)
        self.btnupdate.place(x=280, y=240, width=120, height=30)
        self.btndelete.place(x=410, y=240, width=120, height=30)


        self.win.mainloop()


def main():
    g = GUI()

main()
