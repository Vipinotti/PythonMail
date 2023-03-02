import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração das credenciais do remetente
remetente = "email"
password = "senha"

# Configuração do servidor SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Configuração da mensagem
destinatario = "email_destinatario@gmail.com"
mensagem = MIMEMultipart()
mensagem['From'] = remetente
mensagem['To'] = destinatario
mensagem['Subject'] = "assunto/título"
corpo_mensagem = "conteúdo da mensagem"
mensagem.attach(MIMEText(corpo_mensagem, 'plain'))

# Inicio de sessão e envio do email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(remetente, password)
    texto = mensagem.as_string()
    server.sendmail(remetente, destinatario, texto)
