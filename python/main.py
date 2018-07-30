import time as t
import random
import serial
from math import sqrt, log10
from FileWriter import *
from threading import Thread
import json
from flask import Flask, render_template, request, Response

interval = 3600
#running = True
continous = False
ph = False
do = False
ec = False
orp = False
preState = ['','','','','']
valueToWrite = ''
f = FileWriter(interval=interval, path="logs")

app = Flask(__name__)

tem = {
	'title': 'RC Boat Interface',
	'tog_reading': '',
	'tog_ph': '',
	'tog_do': '',
	'tog_ec': '',
	'tog_orp': '',
	'ph': '0',
	'do': '0',
	'ec': '0',
	'orp': '0',
	's1': 'DO',
	's2': 'PH',
	's3': 'ORP',
	's4': 'EC'
}

def main():
	global running
	user = ''
	try:
		t1 = Thread(target = input, args = ())
		t2 = Thread(target = writeToFileC, args= ())
	except Exception:
		print("Unable to start thread")

	t1.start()
	t2.start()
	
	#running = False

def writeToFileS():
	global f
	global valueToWrite
	if(not continous):
		f.writeFile(parseValue(valueToWrite))
	
def writeToFileC():
	global f
	global running
	global valueToWrite
	while(True):
		if(continous):
			f.writeFile(parseValue(valueToWrite))
		#if(not running):
		#	break
		
def parseValue(value):
	global tem
	values = value.split(', ')
	print values
	out = ''
	
	if(do):
		if(len(out) == 0):
			tem['do'] = values[0]
			out+=values[0]
		else:
			tem['do'] = values[0]
			out+=(', ' + values[0])
	else:
		if(len(out) == 0):
			tem['do'] = 0
			out+="0"
		else:
			tem['do'] = 0
			out+=(', ' + "0")
	if(ph):
		if(len(out) == 0):
			tem['ph'] = values[1]
			out+=values[1]
		else:
			tem['ph'] = values[1]
			out+=(', ' + values[1])
	else:
		if(len(out) == 0):
			tem['ph'] = 0
			out+="0"
		else:
			tem['ph'] = 0
			out+=(', ' + "0")
	if(orp):
		if(len(out) == 0):
			tem['orp'] = values[2]
			out+=values[2]
		else:
			tem['orp'] = values[2]
			out+=(', ' + values[2])
	else:
		if(len(out) == 0):
			tem['orp'] = 0
			out+="0"
		else:
			tem['orp'] = 0
			out+=(', ' + "0")
	if(ec):
		if(len(out) == 0):
			tem['ec'] = values[3]
			out+=values[3]
		else:
			tem['ec'] = values[3]
			out+=(', ' + values[3])
	else:
		if(len(out) == 0):
			tem['ec'] = 0
			out+="0"
		else:
			tem['ec'] = 0
			out+=(', ' + "0")
	return out
		
def changeAllOn():
	global ph
	ph = True
	global do
	do = True
	global ec
	ec = True
	global orp
	orp = True

def changeAllOff():
	global ph
	ph = False
	global do
	do = False
	global ec
	ec = False
	global orp
	orp = False

def toggleContinous():
	global continous
	continous = not continous
	
def changePh():
	global ph 
	ph = not ph

def changeDo():
	global do
	do = not  do

def changeEc():
	global ec 
	ec = not ec

def changeOrp():
	global orp 
	orp = not orp
	
def getStates():
	global ph
	global do
	global ec
	global continous
	global orp
	return ("PH: %s\nDO: %s\nEC: %s\nORP: %s\nContinous: %s" % (ph, do, ec, orp, continous))

def help():
	return "List of Commands\n\th: Help\n\tr: Logs a reading\n\tton: Toggles all sensors to on\n\ttof: Toggles all sensors to off\n\tph: Toggles " \
			+"PH sensor\n\tdo: Toggles DO sensor\n\tec: Toggles EC sensor\n\torp: Toggles ORP sensor\n\t"\
			+"g: Displays the state of all sensors\n\tq: Quits program\n"
			
def input():
    global valueToWrite

    ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=9600,
    timeout=5000)

    while(ser.isOpen()):
	    buffer = ''
	    out = ''
	    while(True):
	    	if(ser.inWaiting() > 0):
			buffer = ser.read(1)
			if(buffer == 's'):
				out = ''
			elif(buffer == 'e'):
				valueToWrite = out
				#print valueToWrite
			else:
				out+=buffer

    print("Serial Closed")
'''
def input():
	global valueToWrite
	global running
	while(True):
		#if(not running):
		#	break
		valueToWrite = generateValue()
		t.sleep(3)
'''
def generateValue():
	value = ''
	value += str(random.randint(10, 30) * 0.2)
	value += ', '
	value += str(random.randint(40, 50) * 0.7)
	value += ', '
	value += str(random.randint(200, 400))
	value += ', '
	value += str(random.randint(600, 700))
	return value

@app.route("/", methods=['GET'])
def getRequest():
	return render_template('interface.html', **tem)

@app.route("/", methods=['POST'])
def action():
	global f
	tem['tog_reading'] = 'checked' if request.form['tog_reading']=='true' else ''
	tem['tog_ph'] = 'checked' if request.form['tog_ph']=='true' else ''
	tem['tog_do'] = 'checked' if request.form['tog_do']=='true' else ''
	tem['tog_ec'] = 'checked' if request.form['tog_ec']=='true' else ''
	tem['tog_orp'] = 'checked' if request.form['tog_orp']=='true' else ''
	
	if(request.form['log'] == 'true'):
		writeToFileS()
	if(request.form['log'] == 'false'):
		f.end()
	if(tem['tog_reading'] != preState[4]):
		toggleContinous()
		preState[4] = tem['tog_reading']
	if(tem['tog_ph'] != preState[0]):
		changePh()
		preState[0] = tem['tog_ph']
	if(tem['tog_do'] != preState[1]):
		changeDo()
		preState[1] = tem['tog_do']
	if(tem['tog_ec'] != preState[2]):
		changeEc()
		preState[2] = tem['tog_ec']
	if(tem['tog_orp'] != preState[3]):
		changeOrp()
		preState[3] = tem['tog_orp']
		
	return Response(json.dumps(tem))	

if __name__ == "__main__":
	try:
		main()
		app.run(host='0.0.0.0', port=80, debug=True)
	except Exception:
		print("Port 80 already in use")
