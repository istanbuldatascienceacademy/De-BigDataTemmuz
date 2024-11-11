import pandas as pd
from kafka import KafkaProducer
import json
import time


producer = KafkaProducer(bootstrap_servers='34.44.147.207:9092',
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                        key_serializer=lambda v: json.dumps(v).encode('utf-8'))

df = pd.read_csv('water_quality.csv',sep=';')

for i,row in df.iterrows():
    producer.send(
        topic='deneme1',
        value= row.to_dict())
    
    producer.flush()
    time.sleep(1)
