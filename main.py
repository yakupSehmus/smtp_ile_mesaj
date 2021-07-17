import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


mesaj = MIMEMultipart()

mesaj["from"] = "göderenin maili"

mesaj["to"] = "alıcının maili"

mesaj["subject"] = "smtp mail gönderme"

yazi = """
göderilmek istenen metin
"""

mesaj_gövdesi= MIMEText(yazi,"plain")

mesaj.attach(mesaj_gövdesi)

try:
    mail = smtplib.SMTP("smtp.gmail.com", 587)

    mail.ehlo()

    mail.starttls()

    mail.login("mailini giriniz", "şifrenizi giriniz")

    mail.sendmail(mesaj["from"],mesaj["to"],mesaj.as_string())

    print("mail gönderildi")

    mail.close()
except:
    sys.stderr.write("bir sorun var")
    sys.stderr.flush()
