from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from  smtplib import SMTP
from pandas.io import clipboard
from tkinter import Entry,Label,Button,Tk,Text
def open_mail(event):
    def send_mail(event):
        global username,password
        msg = MIMEMultipart()
        msg['From'] =username
        password = password
        msg['To'] = receiver_field.get()
        msg['Subject'] = subject.get()
        message = message_field.get("1.0",'end-1c')
        try:
            msg.attach(MIMEText(message, 'plain'))
            server = SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(msg['From'], password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            status.configure(text="successfully sent email to %s:" % (msg['To']))
        except Exception as e:
            status.configure(text=e)
    global username,password
    username= userid_field.get()
    password= password_field.get()
    #resetting the frame
    userid_label.place_forget()
    userid_field.place_forget()
    password_label.place_forget()
    password_field.place_forget()
    login_btn.place_forget()
    #creating new window
    receiver_label=Label(display,text="Enter your receiver email Id ")
    receiver_label.place(y=70,x=50)
    receiver_field = Entry(display, fg="green")
    receiver_field.place(y=70,x=300,width=300,height=20)

    subject_label = Label(display, text="Enter your Subject ")
    subject_label.place(x=50,y=100)
    subject = Entry(display, fg="green")
    subject.place(x=300,y=100,width=300,height=20)

    message_field = Text(display, bg="#888888", fg="white")
    message_field.place(x=50, y=150, height='260',width="800")
    status=Label(display, text='No problems found', fg="red")
    status.place(x=30, y=410)
    send= Button(display, text='Send', bg="blue", fg="white")
    send.bind("<Button-1>", send_mail)
    send.place(x=400,y=440, height="50", width="100")





username=""
password=""
display = Tk()
display.geometry("900x600")
display.title("Email")
display.iconbitmap('smtpicon.ico')
header = Label(display, text="Welcome to SMTP GUI program", fg="orange")
header.place(x=350,y=30)
userid_label = Label(display, text="Enter your GmailId")
userid_label.place(x=100,y=100)
password_label = Label(display, text="Enter your Gmail Password")
password_label.place(x=100,y=200)
userid_field = Entry(display, fg = "red")
userid_field.place(x=500,y=100,height=20,width=200)
password_field= Entry(display, fg="red")
password_field.place(x=500,y=200,height=20,width=200)
login_btn = Button(display, text="Login" , bg="blue", fg="white")
login_btn.place(x=400,y=250,height="40",width="100")
login_btn.bind("<Button-1>", open_mail)
note= "Before Proceed Make sure you have turned on the email for less secure apps..\nTurn it on here \t https://myaccount.google.com/lesssecureapps"

notice_label=Label(display,text=note, fg="brown")
notice_label.place(x=30,y=500)
copy_btn = Button(display, text="Copy URL", bg="red", fg='white')
copy_btn.place(x=30,y=550)
copy_btn.bind('<Button-1>',lambda event : clipboard.copy("https://myaccount.google.com/lesssecureapps"))
display.mainloop()

