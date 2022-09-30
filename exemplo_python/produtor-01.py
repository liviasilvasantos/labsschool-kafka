from distutils.command.config import config
from gc import callbacks
from confluent_kafka import Producer

configs = {
    "bootstrap.servers": "localhost:9092"
}

produtor = Producer(configs)

def notificar_envio(error, message):
    if error is not None:
        print("Ocorreu erro:", error)
    else:
        print("Tratamento após o envio!")

produtor.produce(
    topic="labsschool.mensageria.pc.1",
    #key="",     #opcional
    #partition=0,    #opcional
    value="oi mundo 2",
    callback=notificar_envio
)

produtor.poll(0.5)

#envia e espera confirmação de envio
#produtor.flush(30)
