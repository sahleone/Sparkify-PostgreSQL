# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS  songs"
artist_table_drop =  "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


songplay_table_create = ("""CREATE TABLE songplays (
songplay_id serial primary key,
start_time time NOT NULL,
user_id int REFERENCES users(user_id),
level varchar(4) CHECK (level IN ('free','paid')),
song_id varchar REFERENCES songs(song_id),
artist_id varchar  REFERENCES artists(artist_id),
session_id varchar,
location varchar,
user_agent varchar)
""")

user_table_create = ("""CREATE TABLE  users (
user_id int primary key,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
gender char CHECK (gender IN ('M','F')),
level varchar(4) CHECK (level IN ('free','paid'))

)
""")

song_table_create = ("""CREATE TABLE songs (
song_id varchar primary key,
title varchar NOT NULL,
artist_id varchar REFERENCES artists(artist_id),
year int NOT NULL,
duration numeric

)
""")

artist_table_create = ("""CREATE TABLE artists (
artist_id varchar primary key,
name TEXT NOT NULL,
location varchar,
latitude int,
longitude int

)
""")

time_table_create = ("""CREATE TABLE time (
start_time time NOT NULL,
hour int,
day int,
week int,
month int, 
year int,
weekday TEXT
)
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays 
                                (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
                            VALUES 
                                (%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""INSERT INTO users 
                            (user_id, first_name, last_name, gender, level) 
                        VALUES 
                            (%s,%s,%s,%s,%s)
                        ON CONFLICT (user_id) 
                        DO UPDATE SET 
                            first_name=EXCLUDED.first_name, last_name=EXCLUDED.last_name, level=EXCLUDED.level,gender=EXCLUDED.gender;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) 
                        VALUES
                            (%s,%s,%s,%s,%s)
                        ON CONFLICT (song_id) 
                        DO UPDATE SET 
                            title = EXCLUDED.title, artist_id = EXCLUDED.artist_id, year= EXCLUDED.year, duration= EXCLUDED.duration;
""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) 
                          VALUES
                              (%s,%s,%s,%s,%s)
                          ON CONFLICT (artist_id) 
                          DO UPDATE SET 
                              artist_id = EXCLUDED.artist_id, name = EXCLUDED.name, latitude= EXCLUDED.latitude, longitude= EXCLUDED.longitude;
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                        VALUES
                            (%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, songs.artist_id
FROM songs 
JOIN artists 
ON songs.artist_id = artists.artist_id 
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s


""")

# QUERY LISTS

create_table_queries = [ user_table_create,  artist_table_create, song_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]