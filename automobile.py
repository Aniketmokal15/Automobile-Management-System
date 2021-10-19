from tkinter import *
from tkinter.ttk import Combobox, Scrollbar
import tkinter.ttk as ttk
import  datetime
import mysql.connector as mysql
from PIL import ImageTk, Image

class GymManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("AUTOMOBILE MANAGEMENT PROJECT")
        self.root.geometry("1300x660+0+0")
        # self.root.attributes('-alpha',0.5)
        self.root.config(bg="black")

        self.name=StringVar()
        self.phnno=StringVar()
        self.address=StringVar()
        self.company=StringVar()
        self.custid=StringVar()
        self.rate=StringVar()


        conn = mysql.connect(user='root', password='root', host='localhost', database="autodb")
        cur = conn.cursor()
        cur.execute("select custid from auto_table where custid=(select max(custid) from auto_table)")
        ele=cur.fetchone()
        print(ele)
        add=ele[0]+1
        self.custid.set(add)
        conn.close()

        def moki(event=""):
            res=(self.company.get())
            if res=='Royal Enfield':
                img = Image.open(r"C:\Users\ANIKET MOKAL\Desktop\b1.jpg")
                img = img.resize((620, 310), Image.ANTIALIAS)
                tst = ImageTk.PhotoImage(img)
                l1 = Label(DataFrameLeft, image=tst)
                l1.image = tst
                l1.place(x=0, y=0)
                self.rate.set("2.15lakhs")
            elif res=='KTM':
                img = Image.open(r"C:\Users\ANIKET MOKAL\Desktop\ktm.jpg")
                img = img.resize((620, 310), Image.ANTIALIAS)
                tst = ImageTk.PhotoImage(img)
                l1 = Label(DataFrameLeft, image=tst)
                l1.image = tst
                l1.place(x=0, y=0)
                self.rate.set("2.45lakhs")
            elif res=='Honda':
                img = Image.open(r"C:\Users\ANIKET MOKAL\Desktop\cbr150.jpg")
                img = img.resize((620, 310), Image.ANTIALIAS)
                tst = ImageTk.PhotoImage(img)
                l1 = Label(DataFrameLeft, image=tst)
                l1.image = tst
                l1.place(x=0, y=0)
                self.rate.set("1.40lakhs")
            else:
                pass


        def confirm():
            conn = mysql.connect(user='root', password='root', host='localhost', database="autodb")
            cur = conn.cursor()

            cur.execute("insert into auto_table (name,phnno,address,company,rate) values(%s,%s,%s,%s,%s)",
                        (self.name.get(),self.phnno.get(),self.address.get(),self.company.get()
                         ,self.rate.get()))

            print("Data inserted...")

            conn.commit()
            fetch_data()
            conn.close()
        def clear():
            self.name.set("")
            self.phnno.set("")
            self.address.set("")
            self.company.set("")
            self.custid.set("")
            self.rate.set("")
        def book():
            pass
        def cancel():
            conn = mysql.connect(user='root', password='root', host='localhost', database="autodb")
            cur = conn.cursor()
            cur.execute("delete from auto_table where custid=%s", (self.custid.get(),))
            print("Data Deleted...")
            conn.commit()
            clear()
            fetch_data()
            conn.close()
        def fetch_data():
            conn = mysql.connect(user='root', password='root', host='localhost', database="autodb")
            cur = conn.cursor()
            cur.execute("select * from auto_table")

            
            r1 = cur.fetchall()
            rows=r1[1:]
            if len(rows) != 0:
                self.automobile_table.delete(*self.automobile_table.get_children())
                for i in rows:
                    self.automobile_table.insert("", END, values=i)
                conn.commit()
            else:
                self.automobile_table.delete(*self.automobile_table.get_children())
            conn.close()
        def get_cursor(event=""):
            cur_row = self.automobile_table.focus()
            content = self.automobile_table.item(cur_row)
            row = content['values']
            self.name.set(row[1])
            self.phnno.set(row[2])
            self.address.set(row[3])
            self.company.set(row[4])
            self.custid.set(row[0])
            self.rate.set(row[5])
        ####treeview####

        FrameDetails = Frame(self.root, bg="#4f4f4f", bd=10, relief=RIDGE, padx=20)
        FrameDetails.place(x=0, y=500, width=1365, height=200)

        lbltitle = Label(self.root, text="AUTOMOBILE MANAGEMENT SYSTEM", bg="black", fg="white", bd=13,
                         relief=RIDGE, font=("Comic Sans MS", 30), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame= Frame(self.root, bd=12, relief=RIDGE, bg="#4f4f4f", padx=20)
        frame.place(x=0, y=92, width=1365, height=400)
        #######Left frame########
        DataFrameLeft = LabelFrame(frame, text="", bg="#918e86",
                                   fg="black", bd=10, relief=RIDGE, font=("Cambria", 15, "bold"), padx=2,
                                   pady=6)
        DataFrameLeft.place(x=0, y=3, width=650, height=350)


        #####RIGHT FRAME####

        DataFrameRight = LabelFrame(frame, text="CUSTOMER DETAILS", bg="#918e86", fg="black", bd=10,
                                    relief=RIDGE, font=("Cambria", 15, "bold"), padx=2, pady=6)
        DataFrameRight.place(x=651, y=3, width=650, height=350)

        lblName = Label(DataFrameRight, font=("Cambria", 12), text="Name -", bg="#918e86", padx=2, pady=6)
        lblName.grid(row=2, column=0, sticky=W)
        txtName = Entry(DataFrameRight, font=("Cambria", 12), width=35, textvariable=self.name)
        txtName.grid(row=2, column=1)

        lblphnno=Label(DataFrameRight,font=("Cambria",12),text="Phnno -",bg="#918e86",padx=2,pady=6)
        lblphnno.grid(row=3, column=0, sticky=W)
        txtphnno=  Entry(DataFrameRight, font=("Cambria", 12), width=35, textvariable=self.phnno)
        txtphnno.grid(row=3, column=1)

        lbladdress = Label(DataFrameRight, font=("Cambria", 12), text="Address -", bg="#918e86", padx=2, pady=6)
        lbladdress.grid(row=4, column=0, sticky=W)
        txtaddress = Entry(DataFrameRight, font=("Cambria", 12), width=35, textvariable=self.address)
        txtaddress.grid(row=4, column=1)

        lblcompany = Label(DataFrameRight, font=("Cambria", 12), text="company -", bg="#918e86", padx=2, pady=6)
        lblcompany.grid(row=5, column=0, sticky=W)
        comcompany = Combobox(DataFrameRight, state='readonly', font=("times new roman", 10, "bold"),width=42,
                             textvariable=self.company)
        print(comcompany.bind("<<ComboboxSelected>>",moki))
        comcompany["values"] = ("Honda", "Royal Enfield", "KTM")


        comcompany.grid(row=5, column=1)

        lblcustid = Label(DataFrameRight, font=("Cambria", 12), text="custid -", bg="#918e86", padx=2, pady=6)
        lblcustid.grid(row=0, column=0, sticky=W)
        txtcustid = Entry(DataFrameRight, font=("Cambria", 12), width=35, textvariable=self.custid,state="disabled")
        txtcustid.grid(row=0, column=1)


        lblrate = Label(DataFrameRight, font=("Cambria", 12), text="rate-", bg="#918e86", padx=2, pady=6)
        lblrate.grid(row=6, column=0, sticky=W)
        txtrate = Entry(DataFrameRight, font=("Cambria", 12), width=35, textvariable=self.rate)
        txtrate.grid(row=6, column=1)

        btnconfirm = Button(DataFrameRight, text='confirm', font=("Comic Sans MS", 10, "bold"), width=22, bg="black",
          fg="white", command=confirm)

        btnconfirm.grid(row=7,column=0)

        btnclear = Button(DataFrameRight, text='clear', font=("Comic Sans MS", 10, "bold"), width=22, bg="black",
                            fg="white", command=clear)

        btnclear.grid(row=7, column=1)

        btnbook = Button(DataFrameRight, text='book', font=("Comic Sans MS", 10, "bold"), width=22, bg="black",
                          fg="white", command=book)

        btnbook.grid(row=8, column=0,padx=10,pady=15)

        btnunbook = Button(DataFrameRight, text='unbook', font=("Comic Sans MS", 10, "bold"), width=22, bg="black",
                         fg="white", command=cancel)

        btnunbook.grid(row=8, column=1)

        Table_frame = Frame(FrameDetails, bg="#918e86", bd=5, relief=RIDGE)
        Table_frame.place(x=0, y=0, width=1320, height=180)
        xscroll = Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = Scrollbar(Table_frame, orient=VERTICAL)

        self.automobile_table = ttk.Treeview(Table_frame, column=("name", "phnno", "address", "company", "model",
                                                               "rate"), xscrollcommand=xscroll.set,
                                          yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.config(command=self.automobile_table.xview)
        yscroll.config(command=self.automobile_table.yview)
        self.automobile_table.heading("name", text="Name")
        self.automobile_table.heading("phnno", text="Phnno")
        self.automobile_table.heading("address", text="Address")
        self.automobile_table.heading("company", text="Company")
        self.automobile_table.heading("model", text="Model")
        self.automobile_table.heading("rate", text="Rate")

        self.automobile_table["show"] = "headings"
        self.automobile_table.pack(fill=BOTH, expand=1)
        fetch_data()
        self.automobile_table.bind("<ButtonRelease-1>", get_cursor)


if __name__=='__main__':
    root=Tk()
    obj=GymManagementSystem(root)
    root.mainloop()
