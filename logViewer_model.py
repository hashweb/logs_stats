#!/usr/bin/python
import sys

import psycopg2

class LogviewerDB:

	def __init__(self):
		# DB connection string
		conn_string = "host='127.0.0.1' dbname='postgres' user='postgres' password='strangehat'"
		
		# Print connection string
		print "Connecting to database\n -> %s" % (conn_string)
		
		# get a connection
		conn = psycopg2.connect(conn_string)
		
		# conn.curser will return a cursor object, you can use this to perform queries
		self.cursor = conn.cursor()
		print "connected!\n"

	def add_message(self):
		"INSERT INTO messages (\"user\", content, action) VALUES (%d, %s, %s)"

	# Check if user exists then return the user ID, if not return false
	def check_user_host_exists(self, user, host):
		self.cursor.execute("SELECT * FROM users WHERE \"user\"='%s' AND host='%s'" % (user, host))
		if self.cursor.rowcount:
			return self.cursor.fetchone()[1]
		else:
			return False

def main():
	logviewerDB = LogviewerDB()
	logviewerDB.check_user_host_exists('Jayflux', 'Jayflux@lol.com')

if __name__ == "__main__":
	main()