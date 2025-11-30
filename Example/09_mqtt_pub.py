import paho.mqtt.client as mqtt
broker_address="broker.emqx.io"
broker_port=1883
topic="idt/check"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(broker_address,broker_port)

client.publish(topic,"Hi iDektep")