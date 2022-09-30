# labsschool-kafka
Anotações e exemplos no estudo de kafka com a LabsSchool

## Instalando o Kafka

### Docker

https://developer.confluent.io/quickstart/kafka-docker/

Deixar no docker-compose.yml apenas o zookeeper e o broker.

Iniciar os containers:

> docker-compose up -d

Criar um tópico:

> docker exec broker \
    kafka-topics --bootstrap-server broker:9092 \
             --create \
             --topic quickstart

Produzir mensagem no tópico: 

> docker exec --interactive --tty broker \
    kafka-console-producer --bootstrap-server broker:9092 \
                       --topic quickstart

Ler mensagem do tópico:

> docker exec --interactive --tty broker \
    kafka-console-consumer --bootstrap-server broker:9092 \
                       --topic quickstart \
                       --from-beginning

### Download 

Baixar última versão do Kafka em https://kafka.apache.org/downloads e descompacte em um diretório (<kafka_dir>).

*Zookeeper*

1. Configurar <kafka_dir>/config/zookeeper.properties
2. subir zookeeper

> ./bin/zookeeper-server-start.sh ./config/zookeeper.properties 

*Brokers*

1. Configurar <kafka_dir>/config/server.properties

> log.dirs=/tmp/kafka-logs-broker01

2. subir broker

> ./bin/kafka-server-start.sh ./config/server.properties 

## Scripts

### Tópicos

*Create*
> ./bin/kafka-topics.sh --create --topic <nome_topico> --bootstrap-server <brokers>

*Describe*

Mostra o tópico, o id interno, a quantidade de partições, e o fator de réplica, quem é o servidor líder, quem são os servidores de réplica.

> ./bin/kafka-topics.sh --describe --topic <nome_topico> --bootstrap-server <brokers>

Ex: ./bin/kafka-topics.sh --describe --topic labsschool.mensageria.teclado.1 --bootstrap-server localhost:9092

### Producer

Envia para o tópico toda mensagem produzida no terminal, por linha. Para produzir eventos com chave, use as property parse.key e key.separator.

> ./bin/kafka-console-producer.sh \
    --topic <nome_topico> \
    --bootstrap-server <brokers> \
    --property parse.key=true \
    --property key.separator=":"

Ex: ./bin/kafka-console-producer.sh \
    --topic labsschool.mensageria.teclado.1 \
    --bootstrap-server localhost:9092 \
    --property parse.key=true \
    --property key.separator=":"

> chave1:mensagem da chave 1    

### Consumer

Fica lendo as mensagens recebidas no tópico e printa na saída do terminal. Se passar o parâmetro from-beginning indica que vai consumir desde a criação do tópico.

> ./bin/kafka-console-consumer.sh \
    --topic <nome_topico> \
    --bootstrap-server <brokers> \
    --from-beginning
    --property print.key=true \
    --property key.separator=":"

Ex: ./bin/kafka-console-consumer.sh \
    --topic labsschool.mensageria.teclado.1 \
    --bootstrap-server localhost:9092 \
    --from-beginning \
    --property print.key=true \
    --property key.separator=":"

> chave1:mensagem da chave 1

