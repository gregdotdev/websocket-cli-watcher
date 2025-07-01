# 📈 LTC Price Tracker (CLI Version)

```
 ▄████▄   ██▀███ ▓██   ██▓ ██▓███  ▄▄▄█████▓ ▒█████      █     █░ ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██ ▓█████  ██▀███  
▒██▀ ▀█  ▓██ ▒ ██▒▒██  ██▒▓██░  ██▒▓  ██▒ ▓▒▒██▒  ██▒   ▓█░ █ ░█░▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▓██ ░▄█ ▒ ▒██ ██░▓██░ ██▓▒▒ ▓██░ ▒░▒██░  ██▒   ▒█░ █ ░█ ▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██▀▀█▄   ░ ▐██▓░▒██▄█▓▒ ▒░ ▓██▓ ░ ▒██   ██░   ░█░ █ ░█ ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░██▓ ▒██▒ ░ ██▒▓░▒██▒ ░  ░  ▒██▒ ░ ░ ████▓▒░   ░░██▒██▓  ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒▓ ░▒▓░  ██▒▒▒ ▒▓▒░ ░  ░  ▒ ░░   ░ ▒░▒░▒░    ░ ▓░▒ ▒   ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒     ░▒ ░ ▒░▓██ ░▒░ ░▒ ░         ░      ░ ▒ ▒░      ▒ ░ ░    ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░
░          ░░   ░ ▒ ▒ ░░  ░░         ░      ░ ░ ░ ▒       ░   ░    ░   ▒    ░      ░         ░  ░░ ░   ░     ░░   ░ 
░ ░         ░     ░ ░                           ░ ░         ░          ░  ░        ░ ░       ░  ░  ░   ░  ░   ░     
░                 ░ ░                                                              ░                                
```

> **CLI VERSION - v1**

---

## 💡 Sobre

Este é um projeto simples de **CLI Tracker** que acompanha o preço do **Litecoin (LTC)** em tempo real, utilizando a API WebSocket da [Binance](https://www.binance.com/). Toda vez que o preço mudar, ele é atualizado instantaneamente no terminal.

---

## ⚙️ Tecnologias

- Python 3
- [websocket-client](https://pypi.org/project/websocket-client/)
- API WebSocket da Binance

---

## 🧪 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/ltc-price-cli.git
cd ltc-price-cli
```

2. Instale os requisitos:

```bash
pip install websocket-client
```

3. Execute o programa:

```bash
python tracker.py
```

---

## 📺 Exemplo de saída

```
Currently watching: LTC
-------------------------------- 

Preço Atual: R$358.24
```

---

## 📝 Código principal

O script conecta-se ao WebSocket de trades da Binance para o par `ltcbrl@trade`, e imprime o preço em tempo real sempre que houver alteração.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.