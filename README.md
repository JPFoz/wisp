# WISP
Raspberry PI Zero powered Weather Station! 

## Summary
This is just a quick MVP hack job to get a running weather station collecting data. 
The goal is to collect:
1. Wind speed 
2. Humidity
3. Temperature 
4. Pressure

## Frameworks + Technology
* Measurements stored in a MySQL db (TODO: Experiment with Influx)
* Python Flask Api serves the static resources (TODO: Use NGINX to do this)
* The same Flask service provides a somewhat RESTful Api to provide historic data on temp, pressure and humidity for the graphs
* Uses websockets to stream realtime wind speed data to the frontend which is written in React
* Use a very basic infinitely running daemon to collect measurements from the sensors and write them to the database


## Overall Architecture

### Data flow

1. Sensors -> deamon -> MySQL DB 
2. MySQL DB-> Rest API -> Dashboard
3. MySQL DB -> Websocket API -> Dashboard
