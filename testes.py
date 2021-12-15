
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
login = "@gmail.com"
senha = "123456"

# ARMAZENAMENDO DA LISTA DE EMAIL
##lista_email = []
lista_email = "01@gmail.com,02@gmail.com"

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
    print(f"Enviando Email {cont}...", end='\r')
    
    server = smtplib.SMTP(host,port)

    server.ehlo()
    server.starttls()

    server.login(login, senha)

    #======================================
    # MENSAGEM A SER ENVIADA
    corpo = '''
    <br><div style="font-size:10pt;font-family:Verdana,Geneva,sans-serif"><div class="adM">
    </div><p><span style="font-size:10pt">Bom Dia, tudo bem?</span></p>
    <div id="m_-1451008425066883092forwardbody1">
    <div style="font-size:10pt;font-family:Verdana,Geneva,sans-serif">
    <p><br></p>
    <p>Sou a Daniela da empresa Eletrotec.<br>&nbsp;</p>
    <p>Trabalhamos no segmento de manutenção em nobreak, vendas de baterias e nobreaks novos<br>&nbsp;</p>
    <p>Estou encaminhando uma apresentação de nossos serviços.<br>&nbsp;</p>
    <p>Caso supra as necessidades, será um prazer atendê-los.<br>&nbsp;</p>
    <p>À disposição!</p><font color="#888888">
    <div id="m_-1451008425066883092v1signature">-- <br>
    <div style="margin:0;padding:0;font-family:monospace">
    <div style="margin:0;padding:0;font-family:monospace">&nbsp;</div>
    <div style="margin:0;padding:0;font-family:monospace"><img src="https://github.com/mobdevkyel/emailPython/blob/main/unnamed.jpg?raw=true" data-image-whitelisted="" class="CToWUd a6T" tabindex="0"><div class="a6S" dir="ltr" style="opacity: 0.01; left: 581px; top: 526.422px;"><div id=":2l7" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Fazer o download do anexo 49611983.jpeg" data-tooltip-class="a1V" data-tooltip="Fazer o download"><div class="akn"><div class="aSK J-J5-Ji aYr"></div></div></div><div id=":2l8" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Adicionar anexo ao Drive: 49611983.jpeg" jslog="119524; u014N:cOuCgd,xr6bB; 43:WyJpbWFnZS9qcGVnIiw2MDMyN10." data-tooltip-class="a1V" data-tooltip="Adicionar ao Google Drive"><div class="akn"><div class="wtScjd J-J5-Ji aYr XG"><div class="T-aT4" style="display: none;"><div></div><div class="T-aT4-JX"></div></div></div></div></div><div id=":2la" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" role="button" tabindex="0" aria-label="Salvar no Fotos" jslog="54186; u014N:cOuCgd,xr6bB; 43:WyJpbWFnZS9qcGVnIiw2MDMyN10." data-tooltip-class="a1V" data-tooltip="Salvar no Fotos"><div class="akn"><div class="J-J5-Ji aYr akS"><div class="T-aT4" style="display: none;"><div></div><div class="T-aT4-JX"></div></div></div></div></div></div></div>
    <div style="margin:0;padding:0;font-family:monospace">&nbsp;</div>
    <div style="margin:0;padding:0;font-family:monospace">&nbsp;</div>
    <div style="margin:0;padding:0;font-family:monospace">&nbsp;</div>
    <div style="margin:0;padding:0;font-family:monospace">&nbsp;</div>
    </div>
    <div style="margin:0;padding:0;font-family:monospace">&nbsp;</div>
    </div>
    </font></div><div class="yj6qo"></div><div class="adL">
    </div></div><div class="adL">
    </div></div></br>
    '''

    # INICIANDO SERVIDOR DE ENVIOS
    email_msg = MIMEMultipart()
    
    # DE
    email_msg['from'] = remetente
    
    # PARA
    email_msg['To'] = lista
    
    # TITULO DO EMAIL
    email_msg['subject'] = f"Apresentação Eletrotec Sistemas"
    
    # TIPO DE EMAIL
    email_msg.attach(MIMEText(corpo, 'html')) #plai = Comum

    # LER UM ANEXO PARA ENVIAR
    arquivo_caminho = "C:\\Users\\Ezequiel\\Downloads\\Apresentação_Eletrotec.pdf"
    attchment = open(arquivo_caminho, 'rb')
    
    # TRANSFORMANDO O ANEXO EM BASE64
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)
    
    # CRIAR UM CABEÇARIO DE ANEXO
    att.add_header('Content-Disposition', f'attachment; filename=Apresentacao_Eletrotec.pdf')
    
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
