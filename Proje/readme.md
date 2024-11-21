## Servis Ayarları
Google Dataproc üzerinde Spark makinesi ve VM makine üzerinden de 4 vCPU + 16 GB memory sahip bir makine oluşturulmuştur.

Dataproc Makinesi
```bash	
gcloud dataproc clusters create cluster-f22c --region us-central1 --subnet default --single-node --master-machine-type n1-standard-2 --master-boot-disk-type pd-balanced --master-boot-disk-size 100 --image-version 2.2-debian12 --project project-id
```

## VM makine üzerinde docker ile Kafka, Cassandra ve Grafana kurulumu

**Açılması gereken portlar:** 8080, 9092, 9042, 3000, 9043, 9044




**Önemli Not:** Makinede Docker ve Docker Compose kurulu olmalıdır.

```bash
sudo su

apt update && apt upgrade -y && apt install docker.io -y && apt install docker-compose -y
```

Nano ile docker-compose.yml dosyası oluşturulur ve aşağıdaki kodlar yapıştırılır. sonra ctrl + x ve y ardından enter tuşlarına basılır.
```bash
nano docker-compose.yml
```

```yaml
version: '3.9'
services:
  cassandra-1:
    image: cassandra
    container_name: cassandra1
    hostname: cassandra1
    ports:
      - "9042:9042"
    networks:
      - proje_net
    environment: 
      CASSANDRA_SEEDS: "cassandra1,cassandra2"
      CASSANDRA_CLUSTER_NAME: MyTestCluster 
      CASSANDRA_DC: DC1 
      CASSANDRA_RACK: RACK1 
      CASSANDRA_ENDPOINT_SNITCH: GossipingPropertyFileSnitch 
      CASSANDRA_NUM_TOKENS: 128 
  
  cassandra-2:
    image: cassandra
    container_name: cassandra2
    hostname: cassandra2
    ports:
      - "9043:9042"
    networks:
      - proje_net
    environment: 
      CASSANDRA_SEEDS: "cassandra1,cassandra2"
      CASSANDRA_CLUSTER_NAME: MyTestCluster 
      CASSANDRA_DC: DC1 
      CASSANDRA_RACK: RACK1 
      CASSANDRA_ENDPOINT_SNITCH: GossipingPropertyFileSnitch 
      CASSANDRA_NUM_TOKENS: 128
    
    depends_on:
      cassandra-1:
        condition: service_started
    
  cassandra-3:
    image: cassandra
    container_name: cassandra3
    hostname: cassandra3
    ports:
      - "9044:9042"
    networks:
      - proje_net
    environment: 
      CASSANDRA_SEEDS: "cassandra1,cassandra2"   
      CASSANDRA_CLUSTER_NAME: MyTestCluster 
      CASSANDRA_DC: DC1 
      CASSANDRA_RACK: RACK1 
      CASSANDRA_ENDPOINT_SNITCH: GossipingPropertyFileSnitch 
      CASSANDRA_NUM_TOKENS: 128

    depends_on:
      cassandra-2:
        condition: service_started
    
  graphana:
    image: grafana/grafana-enterprise
    container_name: grafana
    ports:
      - "3000:3000"
    networks:
      - proje_net

  zookeeper:
    image: zookeeper:3.8.0
    container_name: zookeeper-docker
    hostname: zookeeper # hostname kafkada kullanılacak amacı ise zookeeper'ın container içindeki ismiyle iletişim kurabilmesi
    ports:
      - "2181:2181"
    networks:
      - proje_net

  kafka-server-1:
    image: "bitnami/kafka:3.3.1"
    container_name: kafka-container-1
    hostname: kafka-1
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 0
      KAFKA_CFG_LISTENERS: "PLAINTEXT://:9092,PLAINTEXT_HOST://:9093"  
      KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP: "PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT"
      # Eğer VM makine üzerinde çalıştırılıyorsa localhost yerine external ip adresi yazılmalıdır.
      # KAFKA_CFG_ADVERTISED_LISTENERS: "PLAINTEXT://23.43.321:9092,PLAINTEXT_HOST://localhost:9093"
      KAFKA_CFG_ADVERTISED_LISTENERS: "PLAINTEXT://34.172.240.148:9092,PLAINTEXT_HOST://kafka-1:9093" 
      KAFKA_CFG_ZOOKEEPER_CONNECT: zookeeper:2181/kafka-1
      ALLOW_PLAINTEXT_LISTENER: "yes"
    networks:
      - proje_net
      
  kafka-ui:
    container_name: kafka-ui
    image: provectuslabs/kafka-ui:master
    ports:
      - 8080:8080 # Changed to avoid port clash with akhq
    depends_on:
      - kafka-server-1
    environment:
      KAFKA_CLUSTERS_0_NAME: local
      KAFKA_CLUSTERS_0_BOOTSTRAPSERVERS: kafka-1:9093
      # KAFKA_CLUSTERS_0_SCHEMAREGISTRY: http://schema-registry:8081
      DYNAMIC_CONFIG_ENABLED: 'true'
    networks:
      - proje_net
volumes:
  cassandra:
networks:
  proje_net:
    driver: bridge
    
```

Sistemi çalıştırmak için aşağıdaki komutu çalıştırın.
```bash
docker-compose up -d
```

Kafka UI'da kur isminde bir topic oluşturulur.

Cassandra'ya bağlanmak için aşağıdaki komutu çalıştırın.
```bash
docker exec -it cassandra1 cqlsh
```

```sql
CREATE KEYSPACE IF NOT EXISTS test WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 3};

DESCRIBE KEYSPACES;

CREATE TABLE IF NOT EXISTS test.currency (
    id UUID PRIMARY KEY,
    isim TEXT,
    tarih Timestamp,
    currencyname TEXT,
    forexbuying FLOAT,
    forexselling FLOAT,
    banknotebuying FLOAT,
    banknoteselling FLOAT,
    crossrateusd FLOAT,
    crossrateother TEXT
);

DESCRIBE TABLE test.currency;
```


## Api ile Veri çekme ve Kafka'ya gönderme
Python ile yazılmış olan api.py dosyası ile veri çekilir ve Kafka'ya gönderilir.

```bash
pip install kafka-python
pip install requests
```

```python
import requests
from kafka import KafkaProducer
import json
import time
import uuid
# create timestamp
from datetime import datetime

producer = KafkaProducer(bootstrap_servers='34.172.240.148:9092',
                            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                            key_serializer=lambda v: json.dumps(v).encode('utf-8')
                            )

response = requests.get("http://hasanadiguzel.com.tr/api/kurgetir")
data = response.json()
print(data["TCMB_AnlikKurBilgileri"])



def get_data():
    response = requests.get("http://hasanadiguzel.com.tr/api/kurgetir")
    data = response.json()
    return data["TCMB_AnlikKurBilgileri"]

while True:
    data = get_data()
    for row in data:
        row["id"] = str(uuid.uuid4())
        row["Tarih"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(5)
        producer.send(
            'kur',
            value=row
            )
        producer.flush()
        print("mesaj gönderildi")
        print(row)
```

## Spark Streaming ile Kafka'dan Veri Okuma ve Cassandra'ya Yazma

Dataproc makinesine bağlandıkdan sonra aşağıdaki komutla kafka ve cassandra connector yapısıyla pyspark shell açılır.
```bash
pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1,com.datastax.spark:spark-cassandra-connector_2.12:3.2.0
```

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("spark-kafka-cassandra") \
    .config("spark.cassandra.connection.host", "34.28.159.67") \
    .config("spark.cassandra.connection.port", "9042") \
    .getOrCreate()

# spark = SparkSession.builder.appName("spark-kafka-cassandra") \
#     .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1") \
#     .config("spark.jars.packages", "com.datastax.spark:spark-cassandra-connector_2.12:3.2.0") \
#     .config("spark.cassandra.connection.host", "34.172.240.148") \
#     .config("spark.cassandra.connection.port", "9042") \
#     .getOrCreate()

# spark daki kurulu jarları görmek için
# spark.sparkContext.getConf().getAll()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "34.28.159.67:9092") \
    .option("subscribe", "kur").load()

df = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
from pyspark.sql.types import StructType, StructField, StringType, FloatType,TimestampType

schema = StructType([
    StructField("id", StringType(), True),
    StructField("BanknoteBuying", FloatType(), True),
    StructField("BanknoteSelling", FloatType(), True),
    StructField("CrossRateOther", StringType(), True),
    StructField("CrossRateUSD", FloatType(), True),
    StructField("CurrencyName", StringType(), True),
    StructField("ForexBuying", FloatType(), True),
    StructField("ForexSelling", FloatType(), True),
    StructField("Isim", StringType(), True),
    StructField("Tarih", StringType(), True)
])


from pyspark.sql.functions import from_json

df = df.withColumn("value", from_json("value", schema)).select("value.*")


df = df.withColumnRenamed("BanknoteBuying", "banknotebuying") \
    .withColumnRenamed("BanknoteSelling", "banknoteselling") \
    .withColumnRenamed("CrossRateOther", "crossrateother") \
    .withColumnRenamed("CrossRateUSD", "crossrateusd") \
    .withColumnRenamed("CurrencyName", "currencyname") \
    .withColumnRenamed("ForexBuying", "forexbuying") \
    .withColumnRenamed("ForexSelling", "forexselling") \
    .withColumnRenamed("Isim", "isim") \
    .withColumnRenamed("Tarih", "tarih")

# tarih formatını değiştirme '2024-05-01 15:40:00' -> '2024-05-01 15:40:00'
from pyspark.sql.functions import to_timestamp
df = df.withColumn("tarih", to_timestamp("tarih", "yyyy-MM-dd HH:mm:ss"))



df.writeStream.format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "test") \
    .option("table", "currency") \
    .option("checkpointLocation", "/tmp/checkpoint") \
    .start() \
    .awaitTermination()

```

Verilerin Cassandra'ya yazıldığını görmek için aşağıdaki komutu çalıştırın.
```bash
docker exec -it cassandra1 cqlsh
```

```sql
SELECT * FROM test.currency;
```


## Grafana ile Görselleştirme

Grafana'ya giriş yapmak için http://external-ip:3000 adresine gidin. Kullanıcı adı ve şifre olarak admin yazın.


``Add new connection`` kısımdan Cassandra'yı seçin ve install yapıyoruz ve add new datasource diyerek aşağıdaki ayarları yapın.

```bash

Host ->cassandra1:9042
Keyspace -> test
```
Ardından Save & Test diyerek test edin.
