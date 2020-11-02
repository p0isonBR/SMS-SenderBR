#SMS SENDER 1.1.1 pt-BR by PoisonBR
import os,time,requests

#Cores
R="\033[1;31m"; B="\033[1;34m"; C="\033[1;37m"; Y="\033[1;33m"; G="\033[1;32m"; RT="\033[;0m"

os.system('cls' if os.name=="nt" else 'clear')

print(f"""{C}
                            /+osyhhhhhhyys++/
                         +oydddhhhhyyhhhhdddhy+/
                      /+yddhyyyys.josue.syyhddhs/
                     +hddyyssssssssssssssssssyyhdds/
                   /sddhyyyyyyssssssssssssssyyyyyhmh+
                  /hmdhhddddddhhhyyyyyyhhhhdddddhhhddo
                 /hmmdhs+/ //+osyhhhhhhysso+////ohddmdo
                /hmmmy{B}.           `````          `{C}smddd+
                smddm/{B}     `````          `````   {C}mdhmh/
               +ddydm+{B}  -/osyyyys+.    ./syyyyso/-{C}mdydms
               ymhyhmh{B}.yyo/ -- +hdo  /dho -- /oyh.{C}ymdyymd/
              /dmyyymd{B}.  ``.-   ./   -/.-   .``  `{C}dmhsydmo
              smdysymd{B}   shdhyydy      sdyyhddy   {C}dmyyshmy
              dmysshmy{B}                            {C}smhssymd/
             /dmyssymd{B}                            {C}hmhsyymm/
             /dmyssyhms{B}                          /{C}mdysyymm/
             /dmyssyydm/{B}  sh       hh/     -hy  .{C}dmyssyymm/
              dmhssssydd/{B} -hdhysshdysdhssyhdd  -{C}hmhyssyymd/
              ymhssssyyddo{B}``. //+/.` ./+// -` /{C}ddhysssyhmh
              +mdysssssyhdh{B} `     `/+`      -{C}sddysssssydmo
               ymhysssssyyddh/{B}`   `dm.   ` {C}sddhysssssyhmh/
               /hmhysssssyyyhdds{B} ..dm . {C}ohddhyyssssyyhmd+
                /yddhyssssssyyhhddhddddddhyyssssssyydmh+
               /+sdmmdhhyyyysssyyyyyyyyyysssyyyyyhddmdyo+/
           /+shdddhhyhhddddddhhhhhhhhhhhhhhdddddddhyyhhdddyo/
         /shddhyyysssssyyyyhhhhhhhhhhhhhhhhhhyyyyyssssyyyhdddy+
        /hmhyyssssssssssssssssssssssssssssssssssssssssssssyyhddo
        /dmhyyyyyssssssssssssssssssssssssssssssssssssssyyyyyydms
         +yhddddddhhhhhyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhdddddddhs/
           //++oossyyhhhhhhhdddddddddddddddddhhhhhhyyssoo++///
                       ///////+++++++++++++//////


     ██████╗  ██████╗ ██╗███████╗ ██████╗ ███╗   ██╗██████╗ ██████╗
     ██╔══██╗██╔═══██╗██║██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗
     ██████╔╝██║   ██║██║███████╗██║   ██║██╔██╗ ██║██████╔╝██████╔╝
     ██╔═══╝ ██║   ██║██║╚════██║██║   ██║██║╚██╗██║██╔══██╗██╔══██╗
     ██║     ╚██████╔╝██║███████║╚██████╔╝██║ ╚████║██████╔╝██║  ██║
     ╚═╝      ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝
     {RT}{B}*t.me/p0isonBR*{RT}""")

time.sleep(3)
os.system('cls' if os.name=='nt' else 'clear')

print(f"""{B}*By PoisonBR{RT}{G}
███████╗███╗   ███╗███████╗      ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔════╝      ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████╗█████╗███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
╚════██║██║╚██╔╝██║╚════██║╚════╝╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║███████║      ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚══════╝      ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝ v1.1.1{C}
Consiga suas credenciais gratis no site d7networks.com.
{RT}""")

d7="https://http-api.d7networks.com/send"
sms={
'from': "",
'dlr-method': "POST",
'dlr-url': "https://4ba60af1.ngrok.io/receive",
'dlr': "yes",
'dlr-level': "3"
}
h={
'cache-control': "no-cache"
}
sms["username"]=input(f"{B}Username da API: {C}")
sms["password"]=input(f"{B}Senha da API: {C}")
sms["content"]=input(f"{B}Digite o texto a ser enviado: {C}")

try:
 np=int(input(f"{B}Para quantas pessoas deseja enviar?: {C}"))
except (ValueError,TypeError):
 np=int(input(f"{R}Digite um valor NUMERICO valido (1-10): {C}"))
except KeyboardInterrupt:
 print("Cancelado pelo usuário.")
 exit(f"{R}Ctrl+C Pressionado{C}")

while(np > 10):
 print(f"""{Y}
No maximo 10 pessoas por vez.
 """); time.sleep(2)
 np=int(input(f"{B}Digite novamente o numero de pessoas: {C}"))
print(f"""{Y}
ATENCAO: {C}Coloque o codigo do pais na frente do numero! ({G}+55{C})
""")

for sender in range(np):
 sms['to']=input(f"{B}Dgite o numero destino: {C}")
 print(f"""{Y}
Enviando SMS...
""")
 send=requests.request("GET",d7,headers=h,params=sms)
 res=send.text
 feed=send.text[0:6]
 if feed=="Succes":
  print(f"""{G}SMS enviado com sucesso!
""")
 else:
  print(f"{R}Erro ao enviar SMS, confira os dados e tente novamente.")
  time.sleep(2)
  print(f"{Y}Resposta do servidor: {C}{res}")
  print()

print(f"""{C}Me acompanhe no Github: {G}https://github.com/p0isonBR
{C}""")
