#importing required libraries
from tkinter import *
import requests
from bs4 import BeautifulSoup
import smtplib
import time

# function which takes url of product and fetches required information
def pricetrack(URL):
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text().strip()

    try:
        price = soup.find(id="priceblock_dealprice").get_text()
    except:
        price = soup.find(id="priceblock_ourprice").get_text()

    z = price[1:].translate({ord(','): None})
    z = float(z)
    return title,z

#function to send emails
def email(URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('<put sender email here>', '<password for sender account>')

    subject = "alert!!!!! price dropped on your favourite item"
    body = "check amazon link for your product : "
    msg = f'Subject : {subject} \n\n Body : {body} {URL}'

    server.sendmail(
        '<put sender email here>',
        '< put receiver email here>',
        msg
    )
    server.quit()


//class for tkinter gui application
class MyWindow:
    def __init__(self, win):

        self.bgimg=PhotoImage(file="img_4.png")
        self.bglbl=Label(win,image=self.bgimg,height=450,width=320)
        self.bglbl.place(relwidth=1,relheight=1)

        self.lbl1=Label(win, text='Paste   URL  of   product :',bg='#33C3FF',bd=3)
        self.lbl2=Label(win, text='Price you wish to purchase:',bg='#33C3FF',bd=3)
        self.lbl3=Label(win, text='Product Description',bg='#B6FF33',bd=5)
        self.lbl4 = Label(win, text='Current Price', bg='#B6FF33', bd=5)
        self.lbl5 = Label(win, text='Avalability Result', bg='#B6FF33', bd=5)

        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bg='#FFE333',bd=3)
        self.t4 = Entry(bg='#FFE333', bd=3)
        self.t5 = Entry(bg='#FFE333',bd=3)

        self.lbl1.place(x=100, y=50)
        self.lbl2.place(x=90, y=120)
        self.lbl3.place(x=100, y=300)
        self.lbl4.place(x=130, y=400)
        self.lbl5.place(x=115, y=500)

        self.t1.place(x=250, y=40,width=450,height=50)
        self.t2.place(x=250, y=120)
        self.t3.place(x=250, y=290,width=450,height=50)
        self.t4.place(x=250, y=390,width=450,height=50)
        self.t5.place(x=250, y=490,width=450,height=50)

        self.b2=Button(win, text='Check Availability', command=self.pricemonitor,bg='#fa4299',bd=5,fg='white')
        self.b2.place(x=250, y=200)
        self.URL=self.t1.get()
        self.uprice=self.t2.get()

    def pricemonitor(self):
        self.t3.delete(0, 'end')
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        URL=self.t1.get()
        uprice=self.t2.get()

        titlex,zx=pricetrack(URL)

        self.t4.insert(END, str(zx))
        self.t3.insert(END, str(titlex))

        if float(uprice) >= zx:
            email(URL)
            k = "Congratulations product is available good price!!  EMAIL SENT!!!"
            self.t5.insert(END, k)
        else:
            k="sorry!!! will update price and give result !!"
            self.t5.insert(END,k)
            time.sleep(10)
            print("xyz")
            self.pricemonitor()

window=Tk()
mywin=MyWindow(window)
window.title('Amazon Price Tracker')
window.geometry("800x550")
window.mainloop()
