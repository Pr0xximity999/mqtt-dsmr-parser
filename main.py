import random
import json

from paho.mqtt import client as mqtt_client

# Load json config
with open("config.json", "r") as file:
    config = json.load(file)
    
# Generate a Client ID with the subscribe prefix.
client_id = "mqtt-dsmr-parser"

def connect_mqtt(address, port) -> mqtt_client:
    def on_connect(client, userdata, flags, reason_code):
        if reason_code == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", reason_code)

    client = mqtt_client.Client(mqtt_client.CallbackAPIVersion.VERSION1, client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(address, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
