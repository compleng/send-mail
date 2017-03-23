import smtplib
def mail(receiver,Message):
    
    try:
        s=smtplib.SMTP()
        s.connect("smtp.gmail.com",587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login("sender@gmail.com", "password")
        s.sendmail("sender@gmail.com", receiver, Message)
    except Exception,R:
            return R

m="Hello world"
r="receiver@blabla.com"
mail(r,m)
