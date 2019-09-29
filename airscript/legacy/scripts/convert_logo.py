#!/usr/bin/env python3
# This module is needed in the source of the program
import base64
# This is not needed in the source, just here to read arguements
import sys
# Setup some things
selfName = sys.argv[0]
if len(sys.argv) < 3:
	print("Convert ascii art logo from a specified file to basic python source.")
	print("You can then copy the source into your program and simply print the logo.")
	print("This way your ascii art doesn't make your source file messy or have long lines.")
	print("Usage: {} [ascii logo file] [variable name]".format(selfName))
	sys.exit(0)
fileName = sys.argv[1]
varName = sys.argv[2]
varLen = len(varName)
if varLen > 50:
	print("Error: Variable name too long.")
	sys.exit(1)
with open(fileName,"r") as fileToRead:
	fileContents = fileToRead.read()
# Generate our source here
fileContents = base64.b64encode(fileContents.encode('utf-8')).decode('utf-8')
chunks = (79 - varLen)
fileContents = [fileContents[i:i+chunks] for i in range(0,len(fileContents),chunks)]
finalItem = fileContents[len(fileContents) - 1]
loopCounter = 0
for i in fileContents:
	if loopCounter == 0:
		print("# This module is needed!")
		print("import base64")
		print("{} = (\"{}\"".format(varName,i))
	elif i == finalItem:
		print("    \"{}\")".format(i))
		print("{0} = base64.b64decode({0}.encode('utf-8')).decode('utf-8')".format(varName))
		print("# Print the result if you want! remove '#' ")
		print("# Don't forget to indent to fit your code!")
		print("#print({})".format(varName))
	else:
		print("    \"{}\"".format(i))
	loopCounter += 1
