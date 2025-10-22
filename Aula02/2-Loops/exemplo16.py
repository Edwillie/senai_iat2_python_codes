import time
from datetime import datetime

while True:
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M:%S")
    print("Hora Atual: ", hora_atual, end="\r")
    time.sleep(1)