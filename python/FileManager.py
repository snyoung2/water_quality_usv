#Is not used but will parse the log files into a graph if implemented correctly.
#Example a the bottom of the file



import sys						#FileReader
import os
import time as t
import fpformat

#import numpy as np				#Plotter
import matplotlib.pyplot as plt

class FileReader():
	
	def __init__(self):
		self.values = []
		self.length = 0
		return
	
	def getFiles(self, filePath = None):
		files = []
		
		if(filePath == None):
			filePath = "."
			
		for x in os.listdir(filePath):
			if(len(x) > 4):
				if(x[len(x)-8:] == "_log.csv"):
					files.append(filePath+"/"+x)
					
		return files
	
	def readValues(self, file):
		
		f = open(file, "r")
		column = 0
		try: 
			while(True):
				text = f.readline()
				if(text == ""):
					break
				for x in text.split(", "):
					if(len(self.values) != len(text.split(", "))):
						self.values.append([])
					try:
						self.values[column].append((float)(x))
					except:
						self.values[column].append((float)(fpformat.fix((x[:len(x)-4]), 4)))
					column+=1
				column=0
			f.close()
		except IOError:
			print("File Not Found")
			f.close()
		self.size = len(self.values)
		
class FileHandler():
	
	def __init__(self, folder = None, files = None):
		self.fr = FileReader()
		self.files = []
		self.largestArray = 0
		if(folder != None):
			try:
				for x in folder:
					for y in self.fr.getFiles(x):
						self.files.append(y)
			except Exception:
				print "Folder Not Found"
				
		if(files != None):
			try:
				for x in files:
					f = open(x, "r")
					f.close()
					self.files.append(x)
			except IOError:
				print("File(s) Not Found")
	
	def sortFiles(self):
		filesArray = []
		flip = True
		index = 5
		for x in self.files:
			filesArray.append(LogFile(x))

		for x in range(0, index):
			while(True):
				flip = False
				for log in range(0, len(filesArray) - 1):
					#print filesArray[log].dateTime
					if(filesArray[log].dateTime[index-x] < filesArray[log+1].dateTime[index-x]):
						temp = filesArray[log]
						filesArray[log] = filesArray[log+1]
						filesArray[log+1] = temp
						flip = True
				if(not flip):
					break
		filesArray.reverse()
		return filesArray
		
	def mergeFiles(self, name=None):
		filesArray = self.sortFiles()
		
		self.completeArray = []
		arrayLocation = 0
		temp = []
		
		startTime = filesArray[0].time
		for x in filesArray:
			f = open(x.name, "r")
			if(self.largestArray < len(f.readline().split(", "))):
				self.largestArray = len(f.readline().split(", "))
		
		#print self.largestArray
		
		for x in filesArray:
			fr = FileReader()
			fr.readValues(x.name)
			time = x.time-startTime
			for length in range(0, self.largestArray):
				if(length == 0):
					if(len(self.completeArray) < self.largestArray):
						self.completeArray.append([])
					for y in fr.values[0]:
						self.completeArray[length].append(time+y)
				else:
					if(len(self.completeArray) < self.largestArray):
						self.completeArray.append([])
					try:
						for y in fr.values[length]:
							#print y
							self.completeArray[length].append(y)
					except IndexError:
						for y in range(0, len(fr.values[0])):
							self.completeArray[length].append(0)
				
		#print ""
		if(name != None):
			f = open(name, "w")
			for x in range(0, len(self.completeArray[0])):
				toWrite = ""
				a = self.completeArray
				for y in range(0, len(a)):
					if(y != len(a)-1):
						toWrite += str(a[y][x]) + ", "
					else:
						toWrite+= str(a[y][x]) + "\n"
				f.write(toWrite)
				#print toWrite
			f.close()
		
		
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

class Plotter():
	
	def __init__(self, fileHandler):
		self.fh = fileHandler
		self.fh.mergeFiles("testing.csv")
		self.fr = FileReader()
		self.graphs = []
		self.y = 0
		self.x = 0
	
	def populateGraph(self):
		values = self.fh.completeArray
		for x in range(1, len(values)):
			self.graphs.append([values[0], values[x]])
	
	def plot(self, g = None, colors = None, axis = None):
		self.populateGraph()
		for x in range(0, len(g)):
			plt.plot(self.graphs[g[x]][0], self.graphs[g[x]][1], colors[x], linestyle="-")
			
		if(axis != None):
			plt.axis([axis[0], axis[1], axis[2], axis[3]])
		else:
			plt.axis([0, 100, 0, 100])
		plt.xlim(6000, 8000)
		plt.show()
		
'''
f = FileReader()
z = f.readValues(f.getFiles("logs/03-26-2018")[0])
#for x in f.values[0]:
#	print x
fh = FileHandler(folder = ['logs/03-22-2018'])
#for x in fh.sortFiles():
#	print x.name
print(fh.mergeFiles())
p = Plotter(fh)
p.plot(g=[1],colors=["r", "b", "g"])





















