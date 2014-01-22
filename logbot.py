# -*- coding: utf-8 -*- 

import socket
import sys
import time
import re
import os
import sys
import threading

# abstraction layer between this and postgres
from logViewer_model import LogviewerDB

server = "adams.freenode.net"       #settings
channel = sys.argv[1] or "#web-testing"
logFolder = sys.argv[2] or "logs"
botnick = sys.argv[3] or "LauraK2"
logviewerDB = LogviewerDB();

# Will only work on UNIX
if (hasattr(time, 'tzset')):
	os.environ['TZ'] = 'Europe/London'
	time.tzset()

def writeLog(text):
	time_stamp = time.strftime("%H:%M:%S")
	dateStamp = time.strftime("%Y-%m-%d")
	#print text   #print text to console
	with open(logFolder + "/%s.log" % dateStamp, "a") as log:
		for line in text.split("\n"):
			if (line): #some lines are just "" causing the logs to have blank lines
				# User is talking
				print line
				print repr(line)
				try:
					line = line.decode('UTF-8', 'ignore')
				except UnicodeError:
					line = line.decode('iso-8859-1', 'ignore')

				# still getting UnicodeEncodeError: 'ascii' codec can't encode character u'\xa3'
				# http://paste.pm/d99.sh

				if re.match(":(.+)\![^\s]* PRIVMSG %s :(\w.+)$" % channel, line):
					# http://rubular.com/r/DgRGvzImQb
					user = re.search("^:?(\S+)!(\S+)@(\S+)\s(\S+) (#?\S+) :(.+)", line).group(1)
					host = re.search("^:?(\S+)!(\S+)@(\S+)\s(\S+) (#?\S+) :(.+)", line).group(3)
					msg = re.search("^:?(\S+)!(\S+)@(\S+)\s(\S+) (#?\S+) :(.+)", line).group(6)
					action = 'message'
					if user != "NickServ":
						log.write("%s <%s> %s" % (time_stamp, user, msg))
						logviewerDB.add_message(user, host, msg)
				# User joins channel
				# for some reason Joins and Parts need a \n whereas talking doesn't
				elif re.search(":(.+)\!.* JOIN [^:]?(.+)$", line):
					user = re.search(":(.+)\!([^\s]*)", line).group(1)
					host = re.search(":(.+)\!([^\s]*)", line).group(2)
					action = "join"
					log.write("%s --> <%s> (%s) joins %s \n" % (time_stamp, user, host, channel))
					logviewerDB.add_join(user, host)
				# User parts channel
				elif re.search("PART\s", line):
					user = re.search(":(.+)\!([^\s]*)", line).group(1)
					host = re.search(":(.+)\!([^\s]*)", line).group(2)
					action = "part"
					log.write("%s <-- <%s> (%s) parts %s \n" % (time_stamp, user, host, channel))
					logviewerDB.add_part(user, host)
				# User quits channel
				elif re.search(":(.+)\!.* QUIT :(.+)$", line):
					user = re.search(":(.+)\!([^\s]*)", line).group(1)
					host = re.search(":(.+)\!([^\s]*)", line).group(2)
					action = "quit"
					log.write("%s <-- <%s> (%s) quits %s \n" % (time_stamp, user, host, channel))
					logviewerDB.add_quit(user, host)
				# User Emotion
				elif re.search("ACTION", line):
					# 2 after, 1 for \n, the other for that weird character
					user = re.search("^:?(\S+)!(\S+)@(\S+)\s(\S+) (#?\S+) :(.+)", line).group(1)
					host = re.search("^:?(\S+)!(\S+)@(\S+)\s(\S+) (#?\S+) :(.+)", line).group(3)
					msg = re.search("^:?(\S+)!(\S+)@(\S+)\s(\S+) (#?\S+) :(.+)", line).group(6)
					action = "emote"
					log.write("%s <%s> *%s* \n" % (time_stamp, user, msg))
					logviewerDB.add_emote(user, host, msg)


		if text.find('PING') != -1:                          #check if 'PING' is found
  			irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+ server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Test!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")        #join the chan

while 1:    #puts it in a loop
	text=irc.recv(4096)  #receive the text
	writeLog(text)
	
