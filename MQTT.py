import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("geral")
    client.subscribe("limousine")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#def on_lost_connection():

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Teste de envio para o broker da hivemq  disponivel em http://www.hivemq.com/demos/websocket-client/
client.connect("broker.mqttdashboard.com", 1883, 60)
msgs = [{'topic':"geral", 'payload':"multiples 1"},
    ("geral", "multiplo 2", 0, False)]
publish.multiple(msgs, hostname="broker.mqttdashboard.com")
# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#garantir loop da execução
client.loop_forever()