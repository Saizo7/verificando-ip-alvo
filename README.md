# 🔍 Verificador de IP e Conectividade (Recon)

Este é um script em Python focado em **automação de rede e reconhecimento (Recon)**. A ferramenta recebe a URL de um site alvo, limpa o endereço automaticamente e valida o estado real do servidor.

---

## 🚀 Como Funciona?

1. **Limpeza Automática:** Remove sujeiras da URL (como `http://`, `https://` e barras extras).
2. **Resolução de DNS:** Descobre o IP real do servidor usando a biblioteca nativa `socket`.
3. **Validação de Conectividade:** Dispara um teste de `ping` via terminal e analisa o parâmetro `TTL` para evitar falsos positivos do Windows.
4. **Histórico de Logs:** Salva automaticamente o resultado (Alvo, IP e Status) em um arquivo `log.txt` sem apagar os testes anteriores.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Módulos Nativos:** `socket`, `subprocess`, `sys`

---

## 📦 Como Executar

1. Baixe o script na sua máquina.
2. Execute o arquivo principal:
```bash
python seu_script.py
