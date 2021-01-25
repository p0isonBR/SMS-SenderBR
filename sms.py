from os import system
from time import sleep
from requests import get
from subprocess import run
from banner import Banner

system('clear')

#Cores
R = '\033[1;31m'
B = '\033[1;34m'
C = '\033[1;37m'
Y = '\033[1;33m'
G = '\033[1;32m'
RT = '\033[;0m'

print(f'{G} Checando por atualizacoes...')

run(['git', 'pull'])

Banner()

sleep(3)

system('clear')

print(f'''{B}*By PoisonBR{RT}
{G}██████╗███╗   ███╗██████╗ {C}██████╗██████╗███╗   ██╗██████╗ ██████╗██████╗ 
{G}██╔═══╝████╗ ████║██╔═══╝ {C}██╔═══╝██╔═══╝████╗  ██║██╔══██╗██╔═══╝██╔══██╗
{G}██████╗██╔████╔██║██████╗ {C}██████╗████╗  ██╔██╗ ██║██║  ██║████╗  ██████╔╝
{G}╚═══██║██║╚██╔╝██║╚═══██║ {C}╚═══██║██╔═╝  ██║╚██╗██║██║  ██║██╔═╝  ██╔══██╗
{G}██████║██║ ╚═╝ ██║██████║ {C}██████║██████╗██║ ╚████║██████╔╝██████╗██║  ██║
{G}╚═════╝╚═╝     ╚═╝╚═════╝ {C}╚═════╝╚═════╝╚═╝  ╚═══╝╚═════╝ ╚═════╝╚═╝  ╚═╝{G}v1.1 {C}
Consiga suas credenciais gratis no site {B}d7networks.com{C}.
{RT}''')

d7 = 'https://http-api.d7networks.com/send'
sms = {
	'from': '', 
	'dlr-method': 'POST', 
	'dlr-url': 'https://4ba60af1.ngrok.io/receive', 
	'dlr': 'yes', 
	'dlr-level': '3'
	}
h = {
     'cache-control': 'no-cache'
	}
d = 0

try:
	sms['username'] = input(f'{B}Username da API: {C}')
	sms['password'] = input(f'{B}Senha da API: {C}')
	sms['content'] = input(f'{B}Digite o texto a ser enviado: {C}')
	np = int(input(f'{B}Para quantas pessoas deseja enviar?: {C}'))

except (ValueError, TypeError):
	np = int(input(f'{R}Digite um valor NUMERICO valido (1-10): {C}'))

except KeyboardInterrupt:
	print('Cancelado pelo usuário.')
	exit(f'{R}Ctrl+C Pressionado{C}')

try:
	while(np > 10):
		print(f'\n{Y}No maximo 10 pessoas por vez.\n')
		sleep(2)
		np = int(input(f'{B}Digite novamente o numero de pessoas: {C}'))
	print(f'\n{Y}ATENCAO: {C}Coloque o codigo do pais na frente do numero! ({G}+55{C})\n')

	for sender in range(np):
		d+=1
		d2 = str(d)
		extenso = {
			'1' :'primeiro',
			'2' :'segundo',
			'3' :'terceiro',
			'4' :'quarto',
			'5' :'quinto',
			'6' :'sexto',
			'7' :'setimo',
			'8' :'oitavo',
			'9' :'nono',
			'10' :'décimo'
			}

		for key, value in extenso.items():
			d2 = d2.replace(key, value)

		sms['to'] = input(f'{B}Digite o {C}{d2}{B} numero destino: {C}')

		print(f'\n{Y}Enviando SMS...\n')

		send = get(d7, headers=h, params=sms)
		res = send.text
		feed = send.text[0:6]

		if feed == 'Succes':
			print(f'{G}SMS enviado com sucesso!\n')

		else:
			print(f'{R}Erro ao enviar SMS, confira os dados e tente novamente.')
			sleep(2)
			print(f'{Y}Resposta do servidor: {C}{res}\n')

except KeyboardInterrupt:
	print(f'{C}Cancelado pelo usuário.')
	print(f'{C}Me acompanhe no Github: {G}https://github.com/p0isonBR{C}\n')
	exit(f'{R}Ctrl+C pressionado{C}')

print(f'{C}Me acompanhe no Github: {G}https://github.com/p0isonBR{C}\n')
