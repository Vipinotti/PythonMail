import smtplib
import email.message
from SEGREDOS import senha1
from SEGREDOS import email1

def enviar_email():
    corpo_email = """
	<p></p>
	"""

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = email1
    msg['To'] = 'destinatário'
    senha = 'senha' #senha específica Goolge, para Gmail!
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 487 #porta')
    s.starttls()

    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email Enviado')


enviar_email()#ação


