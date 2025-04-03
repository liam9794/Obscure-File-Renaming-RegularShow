import os
import re

ogDir = input("What is the working directory?: ")
ogDir = ogDir.strip('"').strip("'")	#Allows you to paste path with quotes and still work

os.chdir(ogDir)	#Change directory (folder)

for currDir in os.listdir(ogDir):	#For each folder (season)
	os.chdir(currDir)	#Change directory (folder)
	print("Current Directory (Season):", os.getcwd())
	match = re.search(r'\d+', currDir)	#Takes the season number from the folder name
	seasonNum = match.group()
	files = os.listdir()
	files.sort(key=lambda x: float(re.search(r'E(\d+(\.\d+)?)', x).group(1)))	#I don't like doing 1, 10, 11, ... 19, then 2, 20, 21, ...29, 3... So I sort first to do a normal 1, 2, 3, etc.
	for currFile in files:	#For each file in the folder
		if re.search(r"S\d +E\d+", currFile):
			print("This file name has already been reformatted!: ", currFile)
		else:
			numbers = [int(num) for num in re.findall(r'\d+', currFile)]
			partOption = ""
			if "Episode" in currFile:
				episodeNum = numbers[0] #If one of the renamed ones, take the first number
				episodeName = currFile.split('- ', 1)[1] #Take only the title, nothing else
			elif "RegularShow" in currFile:
				episodeNum = numbers[1] #If the original format, take the second number
				episodeName = currFile.split('-')[2]	#Take just the title
				episodeName = episodeName + ".mp4"
				result = re.search(r'pt(\d+)', currFile)
				if result:	#If this is a multipart episode, adjust name format
					partOption = "." + result.group(1)
				else:	#Otherwise, disregard
					partOption = ""
			episodeName = re.sub(r'([a-z])([A-Z])', r'\1 \2', episodeName)	#Add spaces beteween the end of a word and the start of another, lowercase followed by uppercase
			episodeName = re.sub(r'_', r'\'', episodeName)	#Replaces underscores with apostrophes
			newFilename = "S" + seasonNum + " E" + str(episodeNum) + partOption + " - " + episodeName	#Construct the file name
			if os.path.exists(newFilename):	#Some episodes are repeated by mistake. Remove them.
				os.remove(currFile)
			else:	
				os.rename(currFile, newFilename)	#If it's not a repeat, rename the episode
				print("Renamed file from \"" + currFile + "\" to \"" + newFilename + "\"")
	os.chdir("..")	#Change directory (folder)