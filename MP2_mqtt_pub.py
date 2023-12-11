import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time
import json
import random

mqttBroker = "test.mosquitto.org"
client = mqtt.Client()
#client.username_pw_set(username='Jagannath',password='rao1961')
client.connect(mqttBroker,port=1883) 

# Generate random data for features and label
def generate_data():
    feature_1 = random.random()
    feature_2 = random.random()
    label = 1 if feature_1 + feature_2 > 1 else 0
    return {"feature_1": feature_1, "feature_2": feature_2, "label": label}

while True:
    data = generate_data()
    message = json.dumps(data)
    client.publish("INFO4160", message)
    print("Just published " + str(message) + " to topic INFO4160")
    time.sleep(5)