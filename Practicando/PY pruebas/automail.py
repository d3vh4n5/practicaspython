from tkinter import *
from tkinter import messagebox
from asyncio.windows_events import NULL
import sqlite3 as sq3
from email.message import EmailMessage
import ssl
import smtplib

'''
=========================
IMPORTANTE:
para hacer lo mismo con gmail se piden
otros permisos desde gmail desde la web.

este funciona así nada mas con hotmail
=========================
'''

'''Hacer pestaña de instrucciones en la barra de menú'''

email_emisor = 'juanangelbasgall@hotmail.com'
email_pass= 'acá va el pass'

email_receptor = 'juanangelbasgall@hotmail.com'

asunto= 'Mail de pruebas py'
cuerpo='''
Este es un mail de pruebas con python
'''

em = EmailMessage()
em['From'] = email_emisor
em['To'] = email_receptor
em['Subject'] = asunto

em.set_content(cuerpo)


contexto = ssl.create_default_context()
print('Poner el password ya que la elimine por seguridad')
try:

    #with smtplib.SMTP_SSL('smtp-mail.outlook.com', 587) as smtp:
    #    smtp.login(email_emisor, email_pass)
    #   smtp.sendmail(email_emisor, email_receptor, em.as_string())
    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(email_emisor, email_pass)
    server.sendmail(email_emisor, email_receptor, em.as_string())
    messagebox.showinfo('Hecho!', 'Tu mensaje ha sido enviado con éxito')
    server.quit()
except Exception as e:
    messagebox.showerror('Error', 'No se pudo enviar el mail')
    print(e)