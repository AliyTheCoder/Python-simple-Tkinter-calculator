import tkinter as tk

from tkinter import *

ekran = tk.Tk()

ekran.geometry("300x355")  # ekran buyuklugu

ekran.title("toplama makinesi")  # ekranbar ismi




def hesaplatoplama():
    numara1 = int(entry1.get())
    numara2 = int(entry2.get())

    

    cevap = (numara1 + numara2)

    cevapyazi.config(text=cevap)

def hesaplacikarma():
    numara1 = int(entry1.get())
    numara2 = int(entry2.get())

    

    cevap = (numara1 - numara2)

    cevapyazi.config(text=cevap)

def hesaplacarpma():
    numara1 = int(entry1.get())
    numara2 = int(entry2.get())

    

    cevap = (numara1 * numara2)

    cevapyazi.config(text=cevap)

def hesaplabolme():
    numara1 = int(entry1.get())
    numara2 = int(entry2.get())

    

    cevap = (numara1 / numara2)

    cevapyazi.config(text=cevap)



# label = Label(ekran,text="Hesap makinesi",font=('Arial',20,'bold'))
# label.pack()


entry1 = Entry(ekran, font=('Arial', 20, 'bold'))
entry1.pack(side=LEFT)
entry1.place(x=0, y=100)


entry2 = Entry(ekran, font=('Arial', 20, 'bold'))
entry2.pack(side=LEFT)
entry2.place(x=0, y=190)


submit1 = Button(ekran, text="ekle", command=hesaplatoplama)
submit1.pack(side=LEFT)
submit1.place(x=0, y=235)

submit2 = Button(ekran, text="cikar", command=hesaplacikarma)
submit2.pack(side=LEFT)
submit2.place(x=0, y=266)

submit3 = Button(ekran, text="carp", command=hesaplacarpma)
submit3.pack(side=LEFT)
submit3.place(x=0, y=297)

submit4 = Button(ekran, text="bol", command=hesaplabolme)
submit4.pack(side=LEFT)
submit4.place(x=0, y=328)

cevapyazi = Label(ekran, text="Bos", font=('Arial', 20, 'bold'))
cevapyazi.pack()
# cevapyazi.place(x=0,y=0)


ekran.mainloop()
