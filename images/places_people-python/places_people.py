#!/usr/bin/env python

import csv
import json
import sqlalchemy

engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
print("engine")
print(engine)
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
people = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)
places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)
city = sqlalchemy.schema.Table('city', metadata, autoload=True, autoload_with=engine)
county = sqlalchemy.schema.Table('county', metadata, autoload=True, autoload_with=engine)
country = sqlalchemy.schema.Table('country', metadata, autoload=True, autoload_with=engine)
raw_places = sqlalchemy.schema.Table('raw_places', metadata, autoload=True, autoload_with=engine)

str_sql = sqlalchemy.text("SET FOREIGN_KEY_CHECKS = 0;\
                           truncate table city;\
                           truncate table county;\
                           truncate table country;\
                           truncate table people;\
                           truncate table places; \
                           truncate table raw_places;\
                           SET FOREIGN_KEY_CHECKS = 1; ")

connection.execute(str_sql)

with open('/data/places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(raw_places.insert().values(city = row[0],county = row[1],country = row[2]))

str_sql = "insert into city (name) select distinct city from raw_places;"

connection.execute(str_sql)

str_sql = "insert into county (name) select distinct county from raw_places;"

connection.execute(str_sql)

str_sql = "insert into country (name) select distinct country from raw_places;"

connection.execute(str_sql)

with open('/data/places.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(places.insert().values(city = row[0],county = row[1],country = row[2]))


with open('/data/people.csv') as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader:
    connection.execute(people.insert().values(given_name = row[0],family_name = row[1],date_of_birth = row[2],place_of_birth = row[3]))

