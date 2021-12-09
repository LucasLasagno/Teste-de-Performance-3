#Questão 10

import socket, sys, os

def imprime_status(bytes, tam):
    kbytes = bytes/1024
    tam_bytes = tam/1024
    texto = 'Baixando... '
    texto = texto + '{:<.2f}'.format(kbytes) + ' KB '
    texto = texto + 'de ' + '{:<.2f}'.format(tam_bytes) + ' KB'
    print(texto)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nome_arq = input("Informe o nome do arquivo: ")
try:
    
    s.connect((socket.gethostname(), 8881))
    s.send(nome_arq.encode("ascii"))
    msg = s.recv(12)
    tamanho = int(msg.decode("ascii"))
   
   if tamanho >= 0:
        arq = open('download\\'+nome_arq, "wb")
        soma = 0
        bytes = s.recv(4096)
        
        while bytes:
            arq.write(bytes)
            
            soma = soma + len(bytes)
            os.system('cls')
            imprime_status(soma, tamanho)
            bytes = s.recv(4096)
        
        arq.close()
    else:
        print('Arquivo não encontrado no servidor!')
except Exception as erro:
    print(str(erro))


s.close()
input("Pressione qualquer tecla para sair...")