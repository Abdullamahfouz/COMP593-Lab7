"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3
from datetime import datetime
import random
from faker import Faker

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()
    
def create_people_table():
    """Creates the people table in the database"""
    con = sqlite3.connect(db_path)
    
    cur = con.cursor()
    
    create_people_tble_query =  """
         CREATE TABLE IF NOT EXISTS people
         (
             id    INTEGER PRIMARY KEY,
             name     TEXT NOT NULL,
             email    TEXT NOT NULL,
             address  TEXT NOT NULL,
             city     TEXT NOT NULL,
             province TEXT NOT NULL,
             bio      TEXT,
             age      INTEGER,
             created_at DATETIME NOT NULL,
             updated_at DATETIME NOT NULL
         );
"""
    cur.execute(create_people_tble_query)
    con.commit()
    con.close()
        
         
def populate_people_table():
    """Populates the people table with 200 fake people"""
    con = sqlite3.connect(db_path)
    
    cur = con.cursor()
    
    add_person_query = """
         INSERT INTO people
         ( 
             name,
             email,
             address,
             city,
             province,
             bio,
             age,
             created_at,
             updated_at
         )
         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
    
    fake = Faker("en_CA")
    firstname = fake.first_name()
    lastname = fake.last_name()
    for _ in range(200):
        name = f"{firstname} {lastname}"
        email = fake.email()
        address = fake.street_address()
        city = fake.city()
        province = fake.administrative_unit()
        bio = fake.text()
        age = random.randint(1, 100)
        created_at = datetime.now()
        updated_at = datetime.now()

        people = (name,email,address,city, province, bio, age, created_at, updated_at)
        
        cur.execute(add_person_query, people)
        con.commit
        con.close
        
 
    
    

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()
