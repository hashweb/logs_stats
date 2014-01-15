#!/usr/bin/python
import sys
import json

import psycopg2

class LogviewerDB:

	def __init__(self):
		# DB connection string
		try:
			with open('config.json') as data:
				config = json.load(data)

			conn_string = "host='%s' dbname='%s' user='%s' password='%s'" % (config['db']['host'], config['db']['dbname'], config['db']['user'], config['db']['password'])
		except IOError as e:
			sys.exit("Error! No config file supplied, please create a config.json file in the root")
		
		# Print connection string
		print "Connecting to database\n -> %s" % (conn_string)
		
		# get a connection
		conn = psycopg2.connect(conn_string)
		
		# conn.curser will return a cursor object, you can use this to perform queries
		self.cursor = conn.cursor()
		self.conn = conn
		print "connected!\n"

	def add_message(self, user, host, msg):
		self.__add_message(user, host, msg, 'message')

	def add_join(self, user, host):
		self.__add_message(user, host, '', 'join')

	def add_part(self, user, host):
		self.__add_message(user, host, '', 'part')

	def add_quit(self, user, host):
		self.__add_message(user, host, '', 'quit')

	def add_emote(self, user, host, msg,):
		self.__add_message(user, host, msg, 'emote')

	def __add_message(self, user, host, msg, action):
		# Was this message from a user we already have in our database?
		# If so return the userID.
		userID = self.check_user_host_exists(user, host) or False
		# If userID is False, store the new combo then get back the userID
		if not userID:
			self.cursor.execute("INSERT INTO users (\"user\", \"host\") VALUES (%s, %s)", (user, host))
			self.conn.commit()
			# We should now have an ID for our new user/host combo
			userID = self.check_user_host_exists(user, host);

		if (action == 'message' or action == 'emote'):	
			self.cursor.execute("INSERT INTO messages (\"user\", \"content\", \"action\") VALUES (%s, %s, %s)", (userID, msg, action))
		else:
			self.cursor.execute("INSERT INTO messages (\"user\", \"action\") VALUES (%s, %s)", (userID, action))
		self.conn.commit()

	# Check if user exists then return the user ID, if not return false
	def check_user_host_exists(self, user, host):
		self.cursor.execute("SELECT * FROM users WHERE \"user\"= %s AND host=%s", (user, host))
		if self.cursor.rowcount:
			return self.cursor.fetchone()[1]
		else:
			return False

	def resetData(self):
		self.cursor.execute("DELETE FROM users;")
		self.cursor.execute("DELETE FROM messages;")
		self.cursor.execute("ALTER SEQUENCE messages_id_seq RESTART WITH 1;")
		self.cursor.execute("ALTER SEQUENCE users_id_seq RESTART WITH 1;")
		self.conn.commit()


def main():
	logviewerDB = LogviewerDB()
	logviewerDB.resetData();

if __name__ == "__main__":
	main()