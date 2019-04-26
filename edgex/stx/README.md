How to run: under this directory, use docker-compose to run up or shut down.
run up all services defined in "docker-compose.yml"
```
docker-compose up
``` 

check service status
```
docker-compose ps
```

shut down all services and remove containers
```
docker-compose down
```

Notes:
1. "webapp" includes the codes and static pages of website, is mounted as a volume into webui container.
2. "mqtt-demo" was used for testing and based on websocket from MQTT broker, but now it's deprecated (not used any more).
3. "mosquitto" is mounted as a volume into mosquitto (a mqtt broker) container.



