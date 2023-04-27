#import mysql.connector as m
from mysql.connector import *
db=connect(host="localhost",
          user="root",
          password="",
          database="first"
          )
if (db):
    print("Connected")
else:
    print("Some error")