import time
import zugang
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
#esp.osdebug(None)
#import gc
#gc.collect()

ssid = zugang.ssid
password = zugang.password
mqtt_server = '192.168.2.2'
client_id = ubinascii.hexlify(machine.unique_id())
print(client_id)

state_topic = b'ESP001/state'
cmd_topic = b'ESP001/cmd'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())

MAC = station.config('mac')
print(MAC)

ausgang = 'OFF'

def hexMac(byteMac):
    """
    Die Funktion hexMAC nimmt die MAC-Adresse im Bytecode
    entgegen und bildet daraus einen String fuer die Rueckgabe
    """
    macString = ""
    for i in range(0,len(byteMac)):
        macString += hex(byteMac[i])[2:]
        if i <len(byteMac)-1 :
            macString +="-"
    return macString 


def sub_cb(topic, msg):
  global ausgang
  print((topic, msg))
  if topic == b'ESP001/cmd' and msg == b'ON':
    print('ESP ON')
    ausgang = b'ON'
  elif topic == b'ESP001/cmd' and msg == b'OFF': 
    print('ESP OFF')
    ausgang = b'OFF'
  client.publish(state_topic, ausgang)
    

def connect_and_subscribe():
  global client_id, mqtt_server, cmd_topic
  myid = hexMac(MAC)
  print(myid)
  client = MQTTClient(myid, mqtt_server, user="mqtt-user", password="Mspl5clo6Q")
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(cmd_topic)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, cmd_topic))
  return client



client = connect_and_subscribe()
print(client)

while True:
    time.sleep(1.0)
    client.check_msg()




