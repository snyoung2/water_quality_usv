# Unmanned-Surface-Vehicle
Purpose: The purpose of this project is to allow one to deploy a USV to take water quality measurements

### Setup
1. Install raspbian on a raspberry pi.
2. Go through the setup process for a gertduino (tutorials can be found online).
3. After downloading the Unmanned-Surface-Vehicle project directory, navigate to the arduino folder
   in terminal.
4. From here, run "program_328 atlasTest.hex" command in terminal
	- If tab-autocomplete fails to fill in this command, then program_328 is not in the /bin directory.
	  To fix this, go to the gertduino directory where setup was initally done. From here type 
	  "sudo mv program_328 /bin/program_328". If program_328 is in the current directory, it will be moved
	  to the /bin directory.
5. If the file successfully uploads to the arduino, run "minicom -D /dev/ttyAMA0 -b 9600". If there is
   readable output over the serial connection, then the sensors are working correctly.
	- In the case that the output is not human-readable, try reuploading the sketch as defined in step 4
	- If this doesn't work, make sure the gertduino is connected to the raspberry pi, the rx and tx pins
	  on both are connected to the opposite's, and the Atlas Scientific sensor arduion sensor shield is
	  attached to the gertduino.
	  
### Usage:
1. After starting up the pi, run the "minicom -D /dev/ttyAMA0 -b 9600" command in terminal. If there is
   human-readable output, continue forward.
   - In the case that the output is not human-readable or that nothing is sent over serial, follow step
     4 in setup.
2. Once the gertduino is sending information over serial, open the python directory in terminal. Run
   "sudo python main.py". This should open port 80 on the raspberry pi for a browser to connect to.
  
3. From another device on the network, type the raspberry pi's ip address in a browser. This should bring
   up a webpage. 
   
	- Stop Reading: This button will close the current file. Must be pressed if data is to be saved to a file.
	- Toggle constant readings: If toggled, this is constantly log data from every sensor currently toggled.
	- Toggle all sensors off: If toggled, this will change all sensors to off if currently on.
	- Toggle all sensor on: If toggled, this will change all sensors to on if currently off.
	- Take a single reading: This will log a single reading of all currently toggled sensors to the current
     log file. This will also output to the text box adjacent to the button.
	- Toggle s1 sensor: This button will toggle s1 to either on or off. Will not log to the current log file
	  unless "Toggle constant readings" is toggled or the "Take a single reading" button is pressed.
	  (s1 default = DO)
	- Toggle s2 sensor: This button will toggle s2 to either on or off. Will not log to the current log file
	  unless "Toggle constant readings" is toggled or the "Take a single reading" button is pressed.
	  (s1 default = PH)
	- Toggle s3 sensor: This button will toggle s3 to either on or off. Will not log to the current log file
	  unless "Toggle constant readings" is toggled or the "Take a single reading" button is pressed.
	  (s1 default = ORP)
	- Toggle s4 sensor: This button will toggle s4 to either on or off. Will not log to the current log file
	  unless "Toggle constant readings" is toggled or the "Take a single reading" button is pressed.
	  (s1 default = EC)
   

### main.py
In the event that a sensor needs to be changed or the interval at which the log files are created needs
to change, the main.py file needs to be edited.

- Log file interval: This is the rate at which log files are created. This number represents seconds
					 between when the current log file will be generated and when the next one will be
					 generated. (Default: 3600 - 1 Hour)
					 
- Change a sensor: 	 After changing out a sensor on the Atlas Scientific arduino shield, make note of it's
					 position in relation to the left most sensor. For instance, if the EC sensors was
					 changed out for a temperature probe, since it's the 4th most probe, change the value
					 next to the s4 parameter in the tem dictionary from 'EC' to 'TEMP'.
	- Note: this is purly an asthetic change as the log file does not know what data
			it is currently recieving.
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 
					 