import socket
import sys
import time
import re
import os
import sys

server = "irc.freenode.net"       #settings
channel = sys.argv[1] or "#web"
botnick = "LauraK"
logFolder = sys.argv[2] or "logs"

# Will only work on UNIX
if (hasattr(time, 'tzset')):
	os.environ['TZ'] = 'Europe/London'
	time.tzset()

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+server
irc.connect((server, 6667))                                                         #connects to the server
irc.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Test!\n") #user authentication
irc.send("NICK "+ botnick +"\n")                            #sets nick
irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ channel +"\n")        #join the chan

while 1:    #puts it in a loop
	text=irc.recv(4096)  #receive the text
	time_stamp = time.strftime("%H:%M:%S")
	dateStamp = time.strftime("%Y-%m-%d")
	#print text   #print text to console
	with open(logFolder + "/%s.log" % dateStamp, "a") as log:
		for line in text.split("\n"):
			if (line): #some lines are just "" causing the logs to have blank lines
				print line
				# User is talking
				if re.match(":(.+)\!.*:(\w.+)$", line):
					user = re.search(":(.+)\!.*:(\w.+)$", line).group(1)
					msg = re.search(":(.+)\!.*:(\w.+)$", line).group(2)
					if user != "NickServ":
						log.write("%s <%s> %s" % (time_stamp, user, msg))
				# User joins channel
				# for some reason Joins and Parts need a \n whereas talking doesn't
				elif re.search("JOIN\s", line):
					user = re.search(":(.+)\!([^\s]*)", line).group(1)
					host = re.search(":(.+)\!([^\s]*)", line).group(2)
					log.write("%s --> <%s> (%s) joins %s \n" % (time_stamp, user, host, channel))
				# User parts channel
				elif re.search("PART\s", line):
					user = re.search(":(.+)\!([^\s]*)", line).group(1)
					host = re.search(":(.+)\!([^\s]*)", line).group(2)
					log.write("%s <-- <%s> (%s) parts %s \n" % (time_stamp, user, host, channel))

			

	if text.find('PING') != -1:                          #check if 'PING' is found
  		irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)