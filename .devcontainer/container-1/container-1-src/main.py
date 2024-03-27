import sqlite3
from sqlite3 import Error
from test import get_events, push_events, get_calendar_url

def main():
 db = db_init(':memory:')
 get_calendar_url()
 
 
 
 
 db.close()

def db_init(db_path):
  try:
    db = sqlite3.connect(db_path)
    print(sqlite3.version)
  except Error as e:
    print(e)
  finally:
    if db:
      return db

if __name__ == "__main__":
  main()
  
  
  