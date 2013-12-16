#!/usr/bin/python
import sys

import psycopg2

class LogviewerDB:

	def __init__():
		# DB connection string
		conn_string = "host='127.0.0.1' dbname='postgres' user='postgres' password='strangehat'"
		
		# Print connection string
		print "Connecting to database\n -> %s" % (conn_string)
		
		# get a connection
		conn = psycopg2.connect(conn_string)
		
		# conn.curser will return a cursor object, you can use this to perform queries
		cursor = conn.cursor()
		print "connected!\n"

def main():
	logviewerDB = LogviewerDB()

if __name__ == "__main__":
	main()