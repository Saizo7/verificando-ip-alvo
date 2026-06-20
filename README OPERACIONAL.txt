===================================================================
     DOCUMENTAÇÃO OPERACIONAL: SCRIPT DE VERIFICAÇÃO DE IP
===================================================================

1. DESCRIÇÃO DO PROJETO
-------------------------------------------------------------------
Este projeto é uma ferramenta de Reconhecimento (Recon) passivo e 
automação desenvolvida em Python. O objetivo é verificar a 
conectividade e latência de um IP ou domínio alvo na rede através do 
protocolo ICMP (Ping), automatizando a execução e tratando os dados
diretamente pelo terminal do Windows.


2. ESTRUTURA ARQUITETURAL DA PASTA
-------------------------------------------------------------------
A pasta raiz "D:\GitHub\Verificando IP alvo" deve conter apenas:

    ├── verificador.py     # Script principal com a lógica em Python
    ├── iniciar_ping.bat   # Executável que inicializa o script no terminal
    ├── .gitignore         # Filtro que impede o envio de logs de teste
    └── README_OPERACIONAL.txt # Esta documentação técnica


3. LOGICA DO CÓDIGO E LIMPEZA (REFACTOR)
-------------------------------------------------------------------
* import os: Permite que o Python execute comandos do sistema operacional.
* import subprocess: Dispara o ping em segundo plano e captura a resposta.
* Remoção de Código Morto (sys): O módulo 'sys' foi completamente 
  removido do código por ser inútil na estrutura atual, garantindo 
  um script mais limpo, leve e seguro.


4. AMBIENTE OTIMIZADO (SISTEMA OPERACIONAL)
-------------------------------------------------------------------
* Automação do Terminal: O Git CMD foi configurado através da variável 
  de ambiente do sistema (%HOME%) para abrir DIRETAMENTE em "D:\GitHub".
* Impacto: Eliminada a necessidade de digitar "D:" e caminhos longos 
  toda vez que o terminal é iniciado.


5. COMO EXECUTAR A FERRAMENTA
-------------------------------------------------------------------
Método A (Automático):
   -> Dê dois cliques no arquivo "iniciar_ping.bat".

Método B (Manual via Terminal Otimizado):
   1. Abra o Git CMD (ele já iniciará em D:\GitHub).
   2. Digite apenas: cd "Verificando IP alvo"
   3. Execute: python verificador.py


6. SEGURANÇA OPERACIONAL (OPSEC)
-------------------------------------------------------------------
* Filtro de Privacidade: O '.gitignore' bloqueia o arquivo 'log.txt'. 
  Alvos rastreados localmente JAMAIS sobem para o GitHub público.
===================================================================