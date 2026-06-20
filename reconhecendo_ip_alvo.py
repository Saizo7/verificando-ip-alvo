#Descobrindo IP alvo e Salvando em um arquivo de log

import sys
import socket
import subprocess

#Usando uma variavel Site onde o usuario digita o site alvao
Site = input('Digite o site alvo: ').lower()

#A primiera definição verifica o Url do alvo
def limpar_alvo(url):
    url = url.replace("https://", "")
    url = url.replace("http://", "")
    # Trate a astring aqui para remover http, https e barras extras
    url = url.split("/")[0]

    return url

alvo = limpar_alvo(Site)
print(f'Alvo limpo com sucesso: {alvo}')

#Criamos a segunda definição onde o IP do alvo é descoberto
def descobri_ip_alvo(dominio):
    try:
        ip = socket.gethostbyname(dominio)
        return ip
    except socket.gaierror:
        print('[-] Erro: Não foi possível resolver o domínio.')
        return None
#A Terceita definicação vai dispara o Ping no Endereço alvo, varificando o Status, está ON ou OFF
def disparar_ping(ip):
    if ip is None:
        print("[-] Não é possível dar ping em um IP inexistente.")
        return
    print(f'\n[+] Iniciando teste de conectividade (Ping) para {ip}...')

    comando = ["ping", "-n", "4", ip]
    resultado = subprocess.run(comando, capture_output=True, encoding="cp850")
    print(resultado.stdout)

    if "TTL=" in resultado.stdout:
        status = "ONLINE"
    else:
        status = "OFFLINE"
    print(f'[*] O alvo está: {status}')
    return status
#A quarta e ultima definição sempre vai salvar, o dominio, o ip, e o status do alvo em um arquivo log.txt
def salvar_log(dominio, ip, status):
    with open("log.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f'Alvo: {dominio} | IP: {ip} | Status: {status}\n')



ip_final = descobri_ip_alvo(alvo)
status_final = disparar_ping(ip_final)
salvar_log(alvo, ip_final, status_final)
