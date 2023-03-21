# esp32_mpy_mqtt_ha
ESP32 mit MicroPython über MQTT an Home Assistant


```yaml
mqtt:
  switch:
    command_topic: ESP001/cmd
    state_topic: ESP001/state
    payload_on: "ON"
    payload_off: "OFF"
    name: "ESP001"
```
