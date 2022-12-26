#!/usr/bin/env python

import csv
import json
import sqlalchemy

# connect to the database
engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")
print("engine")
print(engine)
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# make an ORM object to refer to the table
people = sqlalchemy.schema.Table('people', metadata, autoload=True, autoload_with=engine)
places = sqlalchemy.schema.Table('places', metadata, autoload=True, autoload_with=engine)


with open('/data//summary_output.json', 'w') as json_file:

  str_sql = sqlalchemy.text("select pla.country,count(1) as bornNumber from people p \
                      inner join places pla on p.place_of_birth=pla.city \
                      group by pla.country;")

  rows = connection.execute(str_sql).fetchall()
  rows = dict(rows)
  json.dump(rows, json_file, separators=(',', ':'))
