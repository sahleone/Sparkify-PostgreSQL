# Song Play

## Overview

Sparkify, a startup wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. With particularly focus on understanding what songs users are listening to. To do this, a Postgres database with tables designed to optimize queries on song play analysis needed to be created. Currently, the data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


## Schema and ETL pipeline
State and justify your database schema design and ETL pipeline.

### Fact Table

#### Songsplays
records in log data associated with song plays i.e. records with page NextSong  

1. songplay_id serial primary key,
2. start_time BIGINT,
3. user_id int REFERENCES users(user_id),
4. level varchar CHECK (level IN ('free','paid')),
5. song_id varchar REFERENCES songs(song_id),
6. artist_id varchar  REFERENCES artists(artist_id),
7. session_id varchar,
8. location varchar,
9. user_agent varchar


### Dimension Tables
#### Users
users in the app  
user_id int primary key,
first_name varchar,
last_name varchar,
gender char CHECK (gender IN ('M','F')),
level varchar CHECK (level IN ('free','paid')


#### Songs
1. songs in the music database
2. song_id varchar primary key,
3. title varchar,
4. artist_id varchar,
5. year int,
6. duration real


#### artists
1. artists in the music database
2. artist_id varchar primary key,
3. name varchar,
4. location varchar,
5. latitude int,
6. longitude int


#### time
1. timestamps of records in songplays broken down into specific units
2. start_time time,
3. hour int,
4. day int,
5. week int,
6. month int, 
7. year int,
8. weekday int


From the requirements, this was an Online Analytical Processing (OLAP) problem. A Star schema was used as it will make it rather simple to optimize queries on song play analysis.

All the tables have a primary key except time as the timestamp is not unique. The timestamp in the time dimension table was split into day, hour, week, month, year ,and weekday. This was done to make it easier to query the table. 

