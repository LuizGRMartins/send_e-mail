from iqoptionapi.stable_api import IQ_Option
from iqoptionapi.constants import ACTIVES as PARES
from telethon.sync import TelegramClient
from datetime import datetime, timedelta
from time import time, sleep
import sys, os
import requests
from multiprocessing import Process
import json
import pandas as pd
import requests


APP_ID = 8871234
APP_HASH = '109847d376b5847c2fd4aaff41d63ea1'
client = ''
canais = []
id = 0
N = 0
filtro = []
sinais = []
Azul = '#5eb0e5'
Amarelo = '#f3d060'
Branco = '#f3f3f3'
Laranja = '#ee7762'

Canal = 'Sinais NTS'
BotNome = 'MobNTS'
os.system('cls' if os.name == 'nt' else 'clear')


def conexao(sinal):
	url = "http://mobtrader.atwebpages.com/botnuvem.php"    
	resp = requests.post(url)
	retorno = resp.text
	contas = retorno.split(',')
	contas.remove('')

	for dados in contas:
		dados = dados.split(' ')
		email = dados[0]
		senha = dados[1]
		id = dados[2]
		status = dados[3]
		entrada = dados[4]
		entrada_ini = entrada
		stoploss = dados[5]
		stopwin = dados[6]
		gales = dados[7] 
		carteira = dados[8]
		

		Process(target=show_data, args=(id, email, senha, status, entrada, stoploss, stopwin, gales, carteira, entrada_ini, sinal,)).start()

def stop(lucro, gain, loss):
    global Azul
    global Amarelo
    global Branco
    global Laranja
    global ENT
    
    if gain == 0:
        gain = 999999999
    elif loss == 0:
        loss = 999999999
    else:
        pass

    if lucro <= (abs(loss) * -1):
        print(f' > Opa!, Stop LOSS Atingido! < ')
        ENT = 0
        input('\n\n Aperte enter para sair')
        sys.exit()
        
    elif lucro >= float(abs(gain)):
        print(f' > Opa!, Stop WIN Batido parabens! < ')
        ENT = 0
        input('\n\n Aperte enter para sair')
        sys.exit()
    else:
        pass

def banca():
    global API
    return API.get_balance()

def horario():
    hora = datetime.now() + timedelta(seconds=20)
    hora = hora.strftime('%H:%M')
    return hora        

def entrada(par, dir, timeframe, valor, hora):
	global API
	global QTD

	show( f'\n> Abrindo operação no par {par} aguarde...\n' )

	try:
		status, id = API.buy_digital_spot_v2(par, valor, dir, timeframe)
		Verifica_status(id, par, dir, timeframe, valor, hora, QTD)
	except Exception as e:
		show( f' > Erro ao abrir operação em {par}!\n {e}\n' )
		status = False
  

def Verifica_status(API, id, par, dir, timeframe, valor, hora, QTD):
    #global gales
    #global ENT
    #global caixa
    #global DER
    #global VIT
    #global gerencia
    #global mao
    #global stopwin
    #global stoploss

    
    if isinstance(id, int):
            
        status = False
        while status == False:
            
            status, lucro = API.check_win_digital_v2(id)
        
        if lucro < 0 and QTD > 0:
            NOVO = float(round(valor, 2))*2.1
            gales += 1
            print(f' > Martingale: {gales} | valor: {round(NOVO, 2)} < ')
            QTD -= 1
            status, id = API.buy_digital_spot_v2(par, NOVO, dir, timeframe)
            B = Thread(target=Verifica_status, args=(id, par, dir, timeframe, NOVO, hora, QTD,))
            B.daemon = True
            B.start()
                
        elif lucro > 0:
                                   
            print(f' > Resultado da operação em {par}: WIN < ')
            caixa += round(lucro, 2)
            VC = 'R$ {:,.2f}'.format(caixa)
            
            gales = 0
            LC = 'R$ {:,.2f}'.format(lucro)
            VL = 'R$ {:,.2f}'.format(valor)
            
            VIT += 1
            
            print(f'Lucro: {LC}')
                
        elif lucro < 0:
            print(f' > Resultado da operação em {par}: LOSS < ')
            caixa += round(lucro, 2)
            VC = 'R$ {:,.2f}'.format(caixa)
            gales += 1
            LC = 'R$ {:,.2f}'.format(lucro)
            VL = 'R$ {:,.2f}'.format(valor)
            DER += 1
            
            print(f'Lucro: {LC}')
            
                    
        if stopwin == 0 and stoploss == 0:
            pass
        elif stopwin > 0 or stoploss > 0:
            stop(caixa, stopwin, stoploss)

def entrada(API, par, dir, timeframe, valor, hora, gales):
    
    QTD = gales
    
    show( f'\n> Abrindo operação no par {par} aguarde...\n' )

    try:
        status, id = API.buy_digital_spot_v2(par, valor, dir, timeframe)
        Verifica_status(id, API, par, dir, timeframe, valor, hora, QTD)
    except Exception as e:
        show( f' > Erro ao abrir operação em {par}!\n {e}\n' )
        status = False

def show_data(id, email, senha, status, entrada, stoploss, stopwin, gales, carteira,entrada_ini, sinal): # dados = {'email': 'saodhasdih@gmail.com', 'senha': 'ushshushus'}]
	API = IQ_Option(email, senha)
	
	try:
		API.connect()
		print(email)
	except:
		print(email, ' ERRO AO LOGAR')
		sys.exit()
	
	if API.check_connect() == False:
		print(email, ' Erro ao conectar')
		API.connect()
		if API.check_connect() == False:
			print(email, ' Nao foi possivel realizar o login')
			sys.exit()
   
	#sinal = input("Digite o sinal: ")
	sinal = sinal.split(' ')
	if sinal[0] == 'M1':
		timeframe = 1
	elif sinal[0] == 'M5':
		timeframe = 5
	elif sinal[0] == 'M15':
		timeframe = 15

	par = sinal[1]
	dir = sinal[2].lower()
	hora = '11:00'
	valor = float(entrada)
	QTD = gales

	print( f'\n> {email} - Abrindo operação no par {par} aguarde...\n' )

	try:
		status, id = API.buy_digital_spot_v2(par, valor, dir, timeframe)
		Verifica_status(API, id, par, dir, timeframe, valor, hora, QTD)
	except Exception as e:
		print( f' > {email} - Erro ao abrir operação em {par}!\n {e}\n' )
		status = False
 
	
	#status, id = API.buy_digital_spot_v2('BTCUSD', int(entrada), 'call', 1)
	'''
	while True:
		print('ID = ' + str(id) + ' | saldo = ' + str(API.get_balance()))
		sleep(0.5)		
	'''	


if __name__ == '__main__':
	print('Iniciando os logins MobNTS')
	
	sinal = input('Digite o sinal: ')#'M1 BTCUSD CALL'
	
	conexao(sinal)
		
	while True:
		sleep(0.5)		