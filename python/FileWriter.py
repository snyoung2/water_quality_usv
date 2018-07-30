import time as t				#FileWriter
import os
from threading import Thread

class FileWriter():

	def __init__(self, interval = 3600, path=None):
		self.interval = interval
		self.currentFile = ""
		self.timeCur = 0
		self.timeStart = 0
		self.path = os.getcwd()
		self.f = ""
		
		p = path.split("/")
		
		fileName = ("%s_log.csv" % self.getTime())
		
		l = LogFile(fileName)
		
		for x in range(0, len(p)):
			if(os.path.exists(p[x])):
				self.path+= "/"+str(p[x])
				
			else:
				os.mkdir(self.path + "/" + str(p[x]))
				self.path+= "/"+str(p[x])
				
		if(os.path.exists(self.path + "/" + l.date)):
			self.path+= "/"+str(l.date)
			
		else:
			os.mkdir(self.path + "/" + l.date)
			self.path+= "/"+str(l.date)
		self.f = open(self.path+ "/" + fileName, "w+")
		
		try:
			t = Thread(target = self.openFile, args = ())
		except Exception:
			print("Unable to start thread")

		t.start()
	def writeFile(self, valueToWrite):
		fileWrite = ("%s, %s\n" % (abs(self.timeCur - self.timeStart), valueToWrite))
		self.f.write(fileWrite)
		t.sleep(0.1)

	def openFile(self):
		self.timeStart = self.splitTime()[6]
		openNew = False

		while(True):
			self.timeCur = self.splitTime()[6]
			
			if(openNew):
				fileName = ("%s_log.csv" % self.getTime())
				self.f = open(self.path + "/" + fileName, "w")
				openNew = False

			if(abs(self.timeStart - self.timeCur) > self.interval):
				self.timeStart = self.timeCur	
				self.f.close()
				openNew = True

	def end(self):
		self.f.close()

	def getTime(self):
		return t.strftime("%m-%d-%Y %H-%M-%S", t.localtime())

	def splitTime(self):
		list = []
		time = self.getTime()
		for x in time.split(" "):
			for y in x.split("-"):
				list.append((int)(y))
		list.append(t.time())
		return list
		
class LogFile():
	
	def __init__(self, name):
		self.dateTime = []
		self.name = name
		try:
			self.date = name.split("/")[len(name.split("/"))-1].split(" ")[0]
			fileName = name.split("/")[len(name.split("/"))-1][:-8]
		except Exception:
			self.date = name.split(" ")[0]
			fileName = name[:-8]
		try:
			self.time = int(t.mktime(t.strptime(fileName, "%m-%d-%Y %H-%M-%S")))
		except Exception:
			self.time = None
		
		try:
			for x in range(0, 2):
				for y in range(0, 3):
					self.dateTime.append((int)(fileName.split(" ")[x].split("-")[y]))
		except Exception:
			print "Log Error"

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
