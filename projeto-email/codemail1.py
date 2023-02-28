import os
import smtplib
from email.message import EmailMessage
from SEGREDOS import senha1
from SEGREDOS import email1
 #configuração email e senha
 ENDERECO_EMAIL = email1
 SENHA_EMAIL = senha1

 #criar email
 msg = EmailMessage()
 msg['Subject'] = 'titulo/tópico'
 msg['From'] = email1
 msg['To'] = 'destinatário'
 msg.set_content('mensagem')

 #enviar email, nos parenteses, especificar provedor de email ex: smtp.gmail.com e especificar porta ex: 465
 with smtplib.SMTP_SSL('', 465 ) as smtp:
     smtp.login(ENDERECO_EMAIL,SENHA_EMAIL)
     smtp.send_message(msg)