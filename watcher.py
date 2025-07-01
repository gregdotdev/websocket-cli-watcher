import websocket
import json

title = """

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

CLI VERSION - v1"""

print(title)

print("Currently watching: LTC")
print("-------------------------------- \n")


last_price = None

def on_message(ws, message):
    global last_price
    data = json.loads(message)
    try:
        # Para Binance, o preço vem em 'p' e o evento é 'trade'
        if data.get("e") == "trade":
            price = float(data['p'])
            if price != last_price:
                print(f"\rPreço Atual: R${price}", end="", flush=True)
                last_price = price
    except (KeyError, IndexError, TypeError, ValueError):
        pass

def on_open(ws):
    pass  # Não precisa enviar nada para Binance para stream público

ws = websocket.WebSocketApp(
    "wss://stream.binance.com:9443/ws/ltcbrl@trade",
    on_message=on_message,
    on_open=on_open
)

ws.run_forever()
