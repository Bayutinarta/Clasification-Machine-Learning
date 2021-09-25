import minimalmodbus as mb
import datetime as dt
import csv
import time
import os

inst = mb.Instrument('/dev/ttyUSB0',1)
inst.serial.baudrate=38400

def read_modbus():
    x = {
        'Datetime' : dt.datetime.now(),
        'Voltage' : round(inst.read_float(0),2),
        'Current' : round(inst.read_float(4),2),
        'Cos_teta' : round(inst.read_float(6),2),
        'Power_faktor' : round(inst.read_float(8),2),
        'Active_power' : round(inst.read_float(10),2),
        'Reactive_power' : round(inst.read_float(12),2),
        'Apparent_power' : round(inst.read_float(14),2),
        'THDV' : round(inst.read_float(16),2),
        'THDI' : round(inst.read_float(18),2),
        
    }
    for i in range (78, 141, 2):
         if i<109:
          x['HV{}'.format(i-77)] = round(inst.read_float(i),2)
         else:
          x['HI{}'.format(i-109)] = round(inst.read_float(i),2)
    return x

while True:
    if os.path.exists('data.csv'):
        with open ('data.csv', 'a') as csv_file:
            write = csv.DictWriter(csv_file, fieldnames = read_modbus().keys())
            
            write.writerow(read_modbus())
    else:
        with open ('data.csv', 'w') as csv_file:
            write = csv.DictWriter(csv_file, fieldnames = read_modbus().keys())
            write.writeheader()
            write.writerow(read_modbus())
    print(read_modbus())
    print('----'*12)
    time.sleep(1)
 