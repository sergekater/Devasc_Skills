#!/bin/bash

curl -i -k -X "OPTIONS" \
"https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" \
-H 'Accept: application/yang-data+json' \
-u 'cisco:cisco123!' 
