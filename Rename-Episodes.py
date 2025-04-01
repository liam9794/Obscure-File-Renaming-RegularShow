import os
import re

ogDir = input("What is the working directory?: ")

os.chdir(ogDir)

for currDir in os.listdir(ogDir):
	os.chdir(currDir)
	print("Current Directory:", os.getcwd())
	match = re.search(r'\d+', currDir)
	seasonNum = int(match.group())
	files = os.listdir()
	files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))
	for currFile in files:
		numbers = [int(num) for num in re.findall(r'\d+', currFile)]
		if "Episode" in currFile:
			episodeNum = numbers[0]
			episodeName = currFile.split('- ', 1)[1]
		elif "RegularShow" in currFile:
			episodeNum = numbers[1]
			tempName = currFile.split('-', 2)[2]
			tempName = tempName.split('-')[0] + ".mp4"
			episodeName = re.sub(r'([a-z])([A-Z])', r'\1 \2', tempName.split('.')[0]) + ".mp4"
		newFilename = "S" + str(seasonNum) + " E" + str(episodeNum) + " - " + episodeName
		print("Renamed file from \"" + currFile + "\" to \"" + newFilename + "\"")
	os.chdir("..")