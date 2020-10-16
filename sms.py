#SMS SENDER 1.1 pt-BR by PoisonBR
import os
import time
import requests

R = "\033[1;31m"
B = "\033[1;34m"
C = "\033[1;37m"
Y = "\033[1;33m"
G = "\033[1;32m"
RT = "\033[;0m"

os.system('clear')

print(C+"                            /+osyhhhhhhyys++/")
print("                         +oydddhhhhyyhhhhdddhy+/")
print("                      /+yddhyyyys.josue.syyhddhs/")
print("                     +hddyyssssssssssssssssssyyhdds/")
print("                   /sddhyyyyyyssssssssssssssyyyyyhmh+")
print("                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo")
print("                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo")
print("                /hmmmy"+B+".           `````          `"+C+"smddd+")
print("                smddm/"+B+"     `````          `````   "+C+"mdhmh/")
print("               +ddydm+"+B+"  -/osyyyys+.    ./syyyyso/-"+C+"mdydms")
print("               ymhyhmh"+B+".yyo/ -- +hdo  /dho -- /oyh."+C+"ymdyymd/")
print("              /dmyyymd"+B+".  ``.-   ./   -/.-   .``  `"+C+"dmhsydmo")
print("              smdysymd"+B+"   shdhyydy      sdyyhddy   "+C+"dmyyshmy")
print("              dmysshmy"+B+"                            "+C+"smhssymd/")
print("             /dmyssymd"+B+"                            "+C+"hmhsyymm/")
print("             /dmyssyhms"+B+"                          /"+C+"mdysyymm/")
print("             /dmyssyydm/"+B+"  sh       hh/     -hy  ."+C+"dmyssyymm/")
print("              dmhssssydd/"+B+" -hdhysshdysdhssyhdd  -"+C+"hmhyssyymd/")
print("              ymhssssyyddo"+B+"``. //+/.` ./+// -` /"+C+"ddhysssyhmh")
print("              +mdysssssyhdh"+B+" `     `/+`      -"+C+"sddysssssydmo")
print("               ymhysssssyyddh/"+B+"`   `dm.   ` "+C+"sddhysssssyhmh/")
print("               /hmhysssssyyyhdds"+B+" ..dm . "+C+"ohddhyyssssyyhmd+")
print("                /yddhyssssssyyhhddhddddddhyyssssssyydmh+")
print("               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/")
print("           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/")
print("         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+")
print("        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo")
print("        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms")
print("         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/")
print("           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///")
print("                       ///////+++++++++++++//////")
print("                        ___  _                 ___   ____")
print("                       / _ \(_)               |  _ \|  __ \ ")
print("                 ____ | | | | |___   _   ____ | |_| | |__) |")
print("                |  _ \| | | | / __|/ _ \|  _ \| |_ <|  _  /")
print("                | |_) | |_| | \__ \ (_) | | | | |_| ) | \ \ ")
print("                |  __/ \___/|_|___/\___/|_| |_|____/|_|  \_\ ")
print(C+"                | |"+RT+B+"*t.me/p0isonBR*"+RT)
print(C+"                |_|"+RT+B+"*by p0isonBR"+RT)

time.sleep(3)
os.system('clear')

print(B+"*By PoisonBR"+RT)
print(G+"""┏━━━┳━┓┏━┳━━━┓  ┏━━━┓       ┏┓
┃┏━┓┃┃┗┛┃┃┏━┓┃  ┃┏━┓┃       ┃┃
┃┗━━┫┏┓┏┓┃┗━━┓  ┃┗━━┳━━┳━┓┏━┛┣━━┳━┓
┗━━┓┃┃┃┃┃┣━━┓┣━━╋━━┓┃┃━┫┏┓┫┏┓┃┃━┫┏┛
┃┗━┛┃┃┃┃┃┃┗━┛┣━━┫┗━┛┃┃━┫┃┃┃┗┛┃┃━┫┃
┗━━━┻┛┗┛┗┻━━━┛  ┗━━━┻━━┻┛┗┻━━┻━━┻┛ v 1.1""")
print(C+"Consiga suas credenciais gratis no site d7networks.com."+RT)
print()
D7 = "https://http-api.d7networks.com/send"
SMS = {
'from': "SMSinfo",
'dlr-method': "POST",
'dlr-url': "https://4ba60af1.ngrok.io/receive",
'dlr': "yes",
'dlr-level': "3"
}
H = {
'cache-control': "no-cache"
}

SMS["username"] = input(B+"Username da API: "+C)
SMS["password"] = input(B+"Senha da API: "+C)
SMS["content"] = input(B+"Digite o texto a ser enviado: "+C)

try:
 NP = int(input(B+"Para quantas pessoas deseja enviar?: "+C))
except:
 NP = int(input(R+"Digite um valor NUMERICO valido (1-5): "+C))

while(NP >= 6):
 print()
 print(Y+"No maximo 5 pessoas por vez.")
 print()
 time.sleep(2)
 NP = int(input(B+"Digite novamente o numero de pessoas: "+C))

print(Y+"ATENCAO: "+C+"Coloque o codigo do pais na frente do numero! ("+G+"+55"+C+")")
print()
SMS['to'] = input(B+"Dgite o numero destino: "+C)
print()
print(Y+"Enviando SMS...")
print()
SEND = requests.request("GET", D7, headers=H, params=SMS)
RES = SEND.text
FEED = SEND.text[0:6]

if FEED == "Succes":
 print(G+"SMS enviado com sucesso!")
 print()
else:
 print(R+"Erro ao enviar SMS, confira os dados e tente novamente.")
 time.sleep(2)
 print(Y+"Resposta do servidor: "+C+RES)
 print()
if NP > 1:
 SMS['to'] = input(B+"Digite o "+C+"segundo"+B+"  numero destino: "+C)
 print()
 print(Y+"Enviando SMS...")
 print()
 SEND = requests.request("GET", D7, headers=H, params=SMS)
 RES = SEND.text
 FEED = SEND.text[0:6]
 if FEED == "Succes":
  print(G+"SMS enviado com sucesso!")
  print()
 else:
  print(R+"Erro ao enviar SMS, confira os dados e tente novamente.")
  time.sleep(1)
  print(Y+"Resposta do servidor: "+C+RES)
  print()
if NP > 2:
 SMS['to'] = input(B+"Digite o terceiro numero destino: "+C)
 print()
 print(Y+"Enviando SMS...")
 print()
 SEND = requests.request("GET", D7, headers=H, params=SMS)
 RES = SEND.text
 FEED = SEND.text[0:6]
 if FEED == "Succes":
  print(G+"SMS enviado com sucesso!")
  print()
 else:
  print(R+"Erro ao enviar SMS, confira os dados e tente novamente.")
  time.sleep(2)
  print(Y+"Resposta do servidor: "+C+RES)
  print()
if NP > 3:
 SMS['to'] = input(B+"Digite o quarto numero destino: "+C)
 print()
 print(Y+"Enviando SMS...")
 print()
 SEND = requests.request("GET", D7, headers=H, params=SMS)
 RES = SEND.text
 FEED = SEND.text[0:6]
 if FEED == "Succes":
  print(G+"SMS enviado com sucesso!")
  print()
 else:
  print(R+"Erro ao enviar SMS, confira os dados e tente novamente.")
  time.sleep(2)
  print(Y+"Resposta do servidor: "+C+RES)
  print()
if NP > 4:
 SMS['to'] = input(B+"Digite o quinto numero destino: "+C)
 print()
 print(Y+"Enviando SMS...")
 print()
 SEND = requests.request("GET", D7, headers=H, params=SMS)
 RES = SEND.text
 FEED = SEND.text[0:6]
 if FEED == "Succes":
  print(G+"SMS enviado com sucesso!")
  print()
 else:
  print(R+"Erro ao enviar SMS, confira os dados e tente novamente.")
  time.sleep(2)
  print(Y+"Resposta do servidor: "+C+RES)
  print()
print(C+"Me acompanhe no Github: "+G+"https://github.com/p0isonBR"+RT)
print()
