# Using hobbyist RC boats for low-cost, rapid water quality assessments

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
					 
					 
____________________________

## What are hobbyist boats?
They are small systems, typically one meter or less, that operate via radio frequency remote control (RC). They are commonly used for racing, but with some adjustments can be used for rapid assessments of surface water quality. 

## Importance of surface water quality monitoring

Small RC aquatic systems are best suited for exploring low-flow open surface water bodies, such as small ponds, lakes, and streams. Surface water interacts with both groundwater supplies, as well as with runoff and seepage from urban and agricultural areas where contamination may occur. Common water quality contaminants of interest include nutrients, pesticides, sediment-associated contaminants, among others. Monitoring these contaminants in surface water can help researchers, scientists, and citizens determine impacts of human activity on an ecosystem. 

<img width="199" alt="image" src="https://user-images.githubusercontent.com/23243852/207980008-bc566669-411b-4901-8a72-4524e9a34135.png">.  <img width="237" alt="image" src="https://user-images.githubusercontent.com/23243852/207980012-9f5063c2-330f-4ac5-8ba0-2580e0fd45ec.png">

Above are two examples of RC boats previously used for surface water monitoring. (a) an airboat with a fiberglass hull, and (b) a Zelos Twin Pro Boat. Both boat systems are electric and run off of batteries.

## Developing your system
### Selecting your RC boat
There are many different design criteria to consider when selecting a ready-made system and deciding whether or not to build your own. For beginners, it is recommended to buy a ready-made system. 

### Hull type
There are three primary types of hulls: catamarans, Deep-V’s, and hydroplanes. Catamarans have a twin hull design that enable more stable deployment in rough waters with reduced drag, although they can blow over in windy conditions. Deep-V’s have a v-shaped bottom and turn well, can handle choppy water, and are great for beginners. Hydroplanes are typically used for racing as they can reach top speeds and make tight turns. For water quality monitoring, speeds are going to be much lower compared to racing, and stability due to increased sensor payload is of concern. Therefore, either Deep-V or catamaran hulls are recommended. 

### Gas vs electric
RC boats can be either electric or fuel powered. Electric boats are easier to maintain, quieter, and more affordable compared to gas boats. Gas-powered boats, however, can generally reach higher speeds and have longer run times. 

### Brushed vs brushless motor
Brushless motors are more powerful but are also more expensive. Brushed motors are cheaper and less powerful, but still have good runtime. Selection of a vehicle with brushed vs. brushless motors is generally dependent on budget and power requirements.

Below are several examples of electric hobby RC boats that are commercially available. Most hobbyist stores (e.g., Horizon Hobby or Hobby Tron) carry a wide range of RC systems. 

 ![image](https://user-images.githubusercontent.com/23243852/207980166-2b287ff4-2568-426c-9b5d-51e3772c8579.png) ![image](https://user-images.githubusercontent.com/23243852/207980176-69f84f52-9c1e-42f6-9048-882b2ea224c4.png) ![image](https://user-images.githubusercontent.com/23243852/207980183-05bd7e71-14c3-498c-a1bd-d53512a8bab8.png)

These are three examples of RC boats sold from Horizon Hobby: a) Blackjack Brushless Catamaran ($229) (b) Recoil Brushless Deep-V ($299), and (c) Veles 29" Brushless Catamaran ($399) (prices at time of writing).

## Developing the sensor system
These RC boats are best used for in situ measurement, or direct measurement of parameters in the water using sondes or probes that do not require obtaining physical samples. Some of the most commonly measured parameters that are possible with probes include temperature, dissolved oxygen (DO), electric conductivity (EC), and pH. There are a wide range of sensors that can be purchased, from low-cost consumer sensors, to high-cost lab-grade sensors. The example system shown below uses four sensor probes purchased from Atlas Scientific (www.atlas-scientific.com). 				 
					 
<img width="316" alt="image" src="https://user-images.githubusercontent.com/23243852/207980371-86a0f37f-4370-4e08-bf43-cd2a0c14a7d6.png"> <img width="314" alt="image" src="https://user-images.githubusercontent.com/23243852/207980378-c1cefc60-6eff-4521-a321-eba340f1a323.png">

*The sensor-equipped catamaran boat, and (b) close-up of the sensor array, Gertduino, and Raspberry Pi device.*
			 
<img width="280" alt="image" src="https://user-images.githubusercontent.com/23243852/207980737-6de08583-1375-4384-8784-4c4c151fa6c6.png">
*Example data for four water quality parameters collected with the example RC boat system and Atlas Scientific sensors.*


## Setup for an example system with Atlas Scientific sensors
The table below lists the components that were used in constructing the example system shown above. If you are building this system from scratch, you may use the items below; otherwise, if you have existing sensors, individual components can be found that are compatible for use.

| Item Description  | Cost |
| ------------- | ------------- |
| Lab grade pH probe  | $75  |
| Dissolved oxygen probe  | $218  |
| PT-1000 temperature probe| 	$20| 
| Conductivity probe K 1.0| 	$139| 
| Electrical isolation circuits (one per sensor)| 	$40-60 each| 
| Whitebox Labs Tentacle Shield | 	$127| 
| Raspberry Pi 3| 	$35| 
| GertDuino GPIO expansion board for Raspberry Pi | 	$18| 
| Portable 5V 2.1A rechargeable battery pack | 	$18-40| 
| USB GPS receiver antenna| 	$25| 

Things to Note: 
•	Atlas Scientific makes a few low-cost “consumer grade” probes for pH and oxidation reduction potential that can be used to lower the overall cost of the system. Additionally, users can select any number of sensors based on priorities and cost, as there are one-, two- and three-probe shields available. In this example, four probes are used as an example. 

•	The sensor probes can be assembled with the Whitebox Labs Tentacle Shield as instructed by the manufacturer. Be sure to follow the exact procedures for handling and storage to ensure safe operation. 

•	The Python code above enables a user to control the sensors with a graphical user interface (GUI) by accessing the Raspberry Pi’s IP address.

•	An Arduino sketch specifically for the Atlas Scientific sensors can be found under the ‘Arduino’ directory.

•	All electronics should be enclosed in a water-tight container and secured to the boat. Additionally, it is not recommended to let the sensors hang loose off the side of the boat as they can get entangled in debris or other items in the water. Atlas Scientific sells sensor racks which we used for this purpose.

•	It is advised to operate the RC boat according to manufacturer’s specifications, including battery handling and storage. Additionally, you should practice prior to deployment to become familiar with the speed and handling of the boat to avoid a crash or flip over. 

•	The launch location should be accessible by foot, and the boat should always be operated in line-of-sight. 

•	There are two options for GPS-tagging your data. First, the clock of the GPS and the Raspberry Pi can be synchronized, and the GPS data and sensor measurements can be matched up after-the-fact. Otherwise, the data logging sketch can be modified to include a GPS tag with each measurement taken; this will require a GPS Arduino shield, although these can sometimes have reduced performance. 
