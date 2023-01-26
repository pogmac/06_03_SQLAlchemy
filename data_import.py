import sqlalchemy

import csv
from sqlalchemy import create_engine, Table, Column,String, Integer, Float, MetaData

engine = create_engine('sqlite:///sqlalchemy.db', echo=True)

metadata = MetaData()

# Define the table with sqlalchemy:
Stations = Table('Stations', metadata,
    Column('station', String),
    Column('latitude', Float),
    Column('longitude', Float),
    Column('elevation', Float),
    Column('name', String),
    Column('country', String),
    Column('state', String)
)

metadata.create_all(engine)
insert_query = Stations.insert()
#print("insert query B");print(insert_query); print("insert query END")

"""
with open('clean_stations.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
     # This skips the first row of the CSV file.
    next(csv_reader)

    engine.execute(
        insert_query,
        [{"station": row[0], "latitude": row[1], "longitude": row[2], 
          "elevation": row[3], "name": row[4], "country": row[5], "state": row[6]} 
            for row in csv_reader]
    )
"""
#station,latitude,longitude,elevation,name,country,state
#USC00519397,21.2716,-157.8168,3.0,WAIKIKI 717.2,US,HI    

# Define the table with sqlalchemy:
Measure = Table('Measure', metadata,
    Column('station', String),
    Column('date', String),
    Column('percip', Float),
    Column('tobs', Float)
)

metadata.create_all(engine)
insert_query = Measure.insert()

"""
with open('clean_measure.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)  # This skips the first row of the CSV file.
    engine.execute(
        insert_query,
        [{"Measure": row[0], "date": row[1], "percip": row[2], 
          "tobs": row[3]}
            for row in csv_reader]
    )
"""
#station,date,precip,tobs
#USC00519397,2010-01-01,0.08,65

# Data select 
conn = engine.connect()
result = conn.execute("SELECT * FROM stations LIMIT 5").fetchall()

for each in result:
    print(each)

############################################
##########      BACK UP         ############
############################################

# Or read the definition from the DB:
#metadata.reflect(engine, only=['Stations'])
#my_table = Table('Stations', metadata, autoload=True, autoload_with=engine)
#insert_query = my_table.insert()

# Or hardcode the SQL query:
# insert_query = "INSERT INTO MyTable (foo, bar) VALUES (:foo, :bar)"