from confluent_kafka import Consumer, KafkaError

configs = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "grupo01",
    "enable.auto.commit": True,
    "default.topic.config": { "auto.offset.reset": "latest"}
}

consumidor = Consumer(configs)

consumidor.subscribe(["labsschool.mensageria.pc.1"])

#timeout pra leitura do tópico
msg = consumidor.poll(0.1)

if msg is None:
    print("Nenhuma mensagem")
elif not msg.error():
    print("Mensagem chegou :", msg.key(), msg.value())
else:
    print("Veio erro: ", msg.error())
    if msg.error().code == KafkaError._PARTITION_EOF:
        print(">>> Sem mais mensagens nas partições")

consumidor.close()        
