#! /usr/bin/env python3

#Author: Julian Gonzalez 
#Project 1 Shell

import os, sys, time, re 
import fileinput


def exec(arg): # code snippets from ecex.py demo
    for dir in re.split(":", os.environ['PATH']): # try each directory in path
        program = "%s/%s" % (dir, arg[0].strip())
        try:
            os.execve(program, arg, os.environ) # try to exec program
        except FileNotFoundError:             # ...expected
            pass     
def outChange(arg,newFile):
	os.close(1)
	sys.stdout = open(newFile,"w")
	os.set_inheritable(1, True)
	return sys.stdout

def inChange(arg):
	os.close(0)
	sys.stdin = open(arg[-1], "r")   # read from file
	os.set_inheritable(0, True)
	args = [arg[0]]
	return sys.stdin, arg

def commands(ins):
	pid = os.getpid() # get and remember pid

	flagIn = False
	flagOut = False
	flagPipe = False

	#gets info on certain commands
	if ' < ' in ins:
		arg = ins.split(' < ') # might need to change
		arg[-1] = arg[-1]   #strip?

		flagIn = True
	if ' > ' in ins:
		arg = ins.split(' > ')
		newFile = arg[-1].strip()
		#folder item?
		arg = arg[0] 		# split?
		flagOut = True
	if ' | ' in ins:
		procs = ins.split(' | ') # get information that would be used for pipe
		arg = procs[0] 			 # split?
		flagPipe = True
	else:
		arg = ins.split()

	rc = os.fork() #start fork

	if rc < 0: # code snippet from demos
		print("fork failed, returning %d\n" % rc, file=sys.stderr)
		sys.exit(1)

	elif rc == 0: #child
		if flagPipe:
			return
		if flagOut:
			sys.stdout = outChange(arg,newFile)
		if flagIn:
			sys.stdin = inChange(arg)
		if not flagPipe:
			exec(arg)
		print("No command exists.\n")
		#sys.exit(1) #need?


	else:
		os.wait()



def shellLoop(Uinput, enviroment):
	while True:
		x = os.getcwd()
		print(x , end = " ")
		Uinput = input(enviroment["1"])

		if Uinput == "exit":# exit loop and shell
			print("Closing Shell...\n")
			break
		if "cd" in Uinput:
			getArg = Uinput.split()
			if getArg[0] == "cd": #check if cd is in first arg
				if len(getArg) == 1:# prevents  a traceback error 
						#do nothing
					continue # go to top of loop
				if getArg[1] == "..": # up a directory
					os.chdir("..")
					continue
				else: # go to arg directory
					os.chdir(getArg[1])
					continue
		commands(Uinput)# if no to all go into commands function
		Uinput = ""

print("Entering shell")
e = os.environ
e["1"] = "$ "
shellLoop("",e)







