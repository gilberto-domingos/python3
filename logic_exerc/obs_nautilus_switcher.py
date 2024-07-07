import asyncio
import websockets
import psutil
import time

# Configurações fornecidas pelo OBS Studio
SERVER_IP = "10.1.1.169"
SERVER_PORT = 4455
SERVER_PASSWORD = "pQgxPBKZICyub1B9"

URL_WEBSOCKET_OBS = f"ws://{SERVER_IP}:{SERVER_PORT}"
SENHA_OBS = SERVER_PASSWORD
NOME_PROCESSO_NAUTILUS = "nautilus"
NOME_PROCESSO_OBS = "obs"  # Nome do processo do OBS Studio

async def trocar_cena(nome_cena):
    async with websockets.connect(URL_WEBSOCKET_OBS) as websocket:
        await websocket.send(f'{{"request-type": "SetCurrentScene", "scene-name": "{nome_cena}", "request-id": "1", "password": "{SENHA_OBS}"}}')

async def monitorar_nautilus():
    while True:
        nautilus_rodando = any(proc.name() == NOME_PROCESSO_NAUTILUS for proc in psutil.process_iter())
        if nautilus_rodando:
            await trocar_cena("Cena Nautilus")
        else:
            await trocar_cena("Cena Padrão")
        await asyncio.sleep(5)  # Ajuste o intervalo conforme necessário

def obs_esta_rodando():
    return any(proc.name() == NOME_PROCESSO_OBS for proc in psutil.process_iter())

async def monitorar_obs_e_nautilus():
    while True:
        if obs_esta_rodando():
            print("OBS Studio está em execução. Iniciando monitoramento do Nautilus.")
            await monitorar_nautilus()
        else:
            print("OBS Studio não está em execução. Aguardando...")
            time.sleep(5)  # Verifique a cada 5 segundos se o OBS foi iniciado

asyncio.run(monitorar_obs_e_nautilus())
