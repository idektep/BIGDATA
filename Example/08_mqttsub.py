import paho.mqtt.client as mqtt
broker_address="broker.emqx.io"
broker_port=1883
topic="idt/temperature"

def on_connect(self,client,userdata,rc):
    print("MQTT connect")
    self.subscribe(topic)

def on_message(client,userdata,msg):
    print(msg.payload.decode("utf-8","strict"))
    x=msg.payload.decode("utf-8","strict")
    x=float(x)

    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address,broker_port)
client.loop_forever()