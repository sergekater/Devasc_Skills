#!/bin/bash

curl -H "Accept: application/yang-data+json" -k -X "DELETE" \
 "https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity" -u 'cisco:cisco123!'
 