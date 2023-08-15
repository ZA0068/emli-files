#!/bin/bash

# Source the environmental variables
source /etc/environment.d/influxenv.conf

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "Usage: $0 <field> <value> <database>"
    exit 1
fi


FIELD=$1
VALUE=$2
DATABASE=$3

response=$(curl -s -o /dev/null -w "%{http_code}" -XPOST "http://$INFLUXDB_HOST:$INFLUXDB_PORT/write?db=$DATABASE&u=$INFLUXDB_USERNAME&p=$INFLUXDB_PASSWORD" --data-binary "$FIELD value=$VALUE")

if [ -z "$response" ] || [ "$response" -ne "204" ]; then
    echo "Failed to post data to InfluxDB. HTTP response code: $response"
    exit 2
else
    echo "Data posted successfully."
fi