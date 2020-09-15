#! /usr/bin/env python3

#Author: Julian Gonzalez 
#Project 1 Shell

import os, sys, time, re, fileinput

def shellLoop(Uinput, enviroment):
	while True:
		x = os.getcwd()
		print(x)
		Uinput = input(enviroment["1"])

		if Uinput == "exit":# exit loop and shell
			print("Closing Shell...\n")
			break
		if "cd" in Uinput:
			print("here")
			getArg = Uinput.split()
			if getArg[0] == "cd": #check if cd is in first arg
				print("here")
				if len(getArg) == 1:# prevents  a traceback error 
						#do nothing
					continue # go to top of loop
				if getArg[1] == "..":
					os.chdir("..")
					continue
				else:
					os.chdir(getArg[1])
					continue

print("Entering shell")
e = os.environ
e["1"] = "$ "
shellLoop("",e)







