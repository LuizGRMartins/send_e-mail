
# IMPORTAÇÃO DAS BIBLIOTECAS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import sys, os
#=============================================

# VARIAVEIS DE CONEXÃO
host = "smtp.gmail.com"
port = "587"
login = "ezequieleoss1986@gmail.com"
senha = "@Kauan12"

# ARMAZENAMENDO DA LISTA DE EMAIL
##lista_email = "ezequieleoss1986@gmail.com,Danielaviera71@gmail.com,Danisantos@voegol.com.br,dev.lm.teste@outlook.com,devsdofuturo@outlook.com,agroluizgustavo@outlook.com,agroluizgustavo@gmail.com,maxijader@gmail.com,kyelclash@gmail.com"
lista_email = "ezequieleoss1986@gmail.com,kyelclash@gmail.com"

# SEPARANDO OS EMAIL POR VIRGULAS
destinos = lista_email.split(",")

# FAZENDO A CONTAGEM DE EMAIL
cont = 0
#=======================================

# CRIANDO LAÇO DE EMAIL
os.system('cls' if os.name == 'nt' else 'clear')
for i in destinos:
    cont += 1
    remetente = login
    lista = i
    print(f"Enviando Email {cont}.", end='\r')
    
    server = smtplib.SMTP(host,port)

    server.ehlo()
    server.starttls()

    server.login(login, senha)

    #======================================
    # MENSAGEM A SER ENVIADA
    corpo = f"<b>olá, este é o email numero {cont}!</b>"

    # INICIANDO SERVIDOR DE ENVIOS
    email_msg = MIMEMultipart()
    
    # DE
    email_msg['from'] = remetente
    
    # PARA
    email_msg['To'] = lista
    
    # TITULO DO EMAIL
    email_msg['subject'] = f"Mob teste de email numero {cont}"
    
    # TIPO DE EMAIL
    email_msg.attach(MIMEText(corpo, 'html')) #plai = Comum

    # LER UM ANEXO PARA ENVIAR
    arquivo_caminho = "C:\\Users\Ezequiel\\Desktop\\projetobet\\testes.py"
    attchment = open(arquivo_caminho, 'rb')
    
    # TRANSFORMANDO O ANEXO EM BASE64
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    
    # CRIAR UM CABEÇARIO DE ANEXO
    att.add_header('Content-Disposition', f'attachment; filename=testearquivo.py')
    
    # FEXAMENTO DO ANEXO
    attchment.close()
    
    #  COLOCAR ANEXO NO EMAIL
    email_msg.attach(att)
            
    # ENVIAR TUDO
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())

    # FEXANDO SERVIDOR
    server.quit()
    
# FINALIZANDO OS ENVIOS
print(f'\nOk, enviamos {cont} emails.')