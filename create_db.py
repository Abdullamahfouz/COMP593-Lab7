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
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        address TEXT NOT NULL,
        city TEXT NOT NULL,
        province TEXT NOT NULL,
        bio TEXT NOT NULL,
        age INTEGER NOT NULL,
        created_at TIMESTAMP NOT NULL,
        updated_at TIMESTAMP NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def populate_people_table():
    """Populates the people table with 200 fake people"""
    fake = Faker()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for _ in range(200):
        name = f"{fake.first_name()} {fake.last_name()}"
        email = fake.email()
        address = fake.street_address()
        city = fake.city()
        province = fake.state()
        bio = fake.text()
        age = random.randint(1, 100)
        created_at = updated_at = datetime.now()

        cursor.execute("""
        INSERT INTO people (name, email, address, city, province, bio, age, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (name, email, address, city, province, bio, age, created_at, updated_at))

    conn.commit()
    conn.close()

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
    main()
