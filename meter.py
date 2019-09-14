#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import time  # sleep
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import paho.mqtt.client as mqtt
import json

client = ModbusClient(method='rtu', port='/dev/ttyS0', timeout=1, stopbits = 1, bytesize = 8,  parity='N', baudrate= 9600)
client.connect()

iot_hub = 'demo.thingsboard.io'
port = 1883
username = 'tUonoVRCvVY4DB5ELY5k'
password = ''
topic = 'v1/devices/me/telemetry'

clnt = mqtt.Client()
clnt.username_pw_set(username,password)
clnt.connect(iot_hub,port)
print 'Connection successful'

data = dict()

while True:

    v = client.read_holding_registers(51284,1,unit=115)
    v = v.registers[0]
    
    c = client.read_holding_registers(57345,1,unit=115)
    c = c.registers[0]
    
    h = client.read_holding_registers(51280,1,unit=115)
    h = h.registers[0]
    
    t = client.read_holding_registers(51457,1,unit=115)
    t = t.registers[0]
    
    f = client.read_holding_registers(51287,1,unit=115)
    f = f.registers[0]
    
    
    print 'Voltage:', float(v/100.0),'V'
    data['Voltage'] = float(v/100.0)
    data_out = json.dumps(data)
    clnt.publish(topic,data_out,0)
    
    print 'Current:', c,'A'
    data['Current (A)'] = c
    data_out = json.dumps(data)
    clnt.publish(topic,data_out,0)
    
    print 'Operating hour:', h,'h'
    data['Operating hour (Hour)'] = h
    data_out = json.dumps(data)
    clnt.publish(topic,data_out,0)
    
    print 'Temperature:', t, chr(176),'C'
    data['Temperature (C)'] = t
    data_out = json.dumps(data)
    clnt.publish(topic,data_out,0)
    
    print 'Frequency:', float(f/100.0),'Hz'
    data['Frequency (Hz)'] = float(f/100.0)
    data_out = json.dumps(data)
    clnt.publish(topic,data_out,0)
    print "--------------------------------"                                                         
    
    time.sleep (3)
