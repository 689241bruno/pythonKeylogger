import requests
import json
import os
import datetime
import time


def enviar_para_discord(caminho_log, webhook_URL, nome):
    if not os.path.exists(caminho_log):
        print(f"ERRO: Arquivo não encontrado no caminho: {caminho_log}")
        return
    
    # pegar hora 

    try: 
        hora = datetime.datetime.now()
        hora_format = hora.strftime("%H:%M:%S")
    except Exception as e:
        hora_format = "?:?:?"
        print("Erro ao pegar as horas: {e}")

    try:
        with open(caminho_log, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except Exception as e:
        print(f"ERRO ao ler o arquivo: {e}")

    discord_mensage = f"**Conteúdo do arquivo `{os.path.basename(caminho_log)}`- {hora_format}**\n```ini\n{conteudo} \n```"

    payload = {
        "content": discord_mensage,
        "username": nome
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(webhook_URL, data=json.dumps(payload), headers=headers)
        response.raise_for_status()

        if response.status_code == 204:
            print("Mensagem enviada com sucesso para o discord")
        else:
            print(f"Erro inesperado do discord: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"ERRO na requisição HTTP: {e}")


def loop_do_envio(caminho_log, webhook_URL, nome, segundos):
    print("thread de envio")
    while True:
        enviar_para_discord(caminho_log, webhook_URL, nome)
        time.sleep(segundos)

