import random
import json

import paho.mqtt as mqtt
from paho.mqtt import client as mqtt_client

def on_connect(client:mqtt_client.Client, userdata:any, flags:Dict[str, any], reason_code:mqtt.reasoncodes.ReasonCodes):
    if reason_code.id == 0:
        print(f"Connected to MQTT Broker with cient {client._client_id}.")
    else:
        print(f"Failed to connect, return code {reason_code}")

def create_client(client_id, broker_address, broker_port=1883) -> mqtt_client:
    
    # Create client
    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION2, client_id)

    # Bind connection function bind and connect
    client.on_connect = on_connect
    client.connect(broker_address, broker_port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    # Load json config
    with open("config.json", "r") as file:
        config = json.load(file)
        
    # Generate a Client ID with the subscribe prefix.
    client_id = "mqtt-dsmr-parser"
    client = create_client()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
