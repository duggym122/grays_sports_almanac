# Create a database here. 
# Reference this article: http://stackoverflow.com/questions/19426448/creating-a-postgresql-db-using-psycopg2
# Reference this tutorial: https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# Consider refactoring later to do this: http://stackoverflow.com/questions/35153483/create-db-and-tables-from-setup-py
import passfile
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = None
con = connect(user='duggym122', host = 'localhost', port = '5432', password = passfile.dbpass)

newdb = "grays_almanac"

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE ' + newdb)
cur.close()
con.close()