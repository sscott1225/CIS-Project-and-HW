### S12_PySQL_StarterFile.py  v3
#  K.Schmitz (c) 2022,2023
#  Starter File for CIS2010 Session 12, Structured Query Language
##################Initialization information, do not modify ################
from cis2010utils4 import StartHere, EndHere, runsql
##from colorama import Fore
import pandas as pd
import sqlite3
############################################################################
#
# Task 2a
StartHere( "Samantha Scott", "S12", "Fall 2023")
#
#
# Open up the database  ########## Do not modify these instructions#########
db_name =  "moviesUSA.db"
db_conn = sqlite3.connect(db_name)
# display fields in 3 tables
sqltxt = "SELECT COUNT(title) FROM movies" ; mz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of movies records\n", mz)
sqltxt = "SELECT COUNT(actor) FROM actors" ; az = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of actors records\n", az)
sqltxt = "SELECT COUNT(genre) FROM genre" ; gz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of genre records\n", gz)
sqltxt = "pragma table_info('movies')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("movies table\n", t1)
sqltxt = "pragma table_info('actors')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("\nactors table\n", t2)
sqltxt = "pragma table_info('genre')" ; t3 = pd.read_sql(sqltxt, db_conn) ; print("\ngenre table\n",t3)
############################################################################
#
#
# Task w3a
sqlw3a = """
SELECT year FROM movies
"""
w3a = runsql( sqlw3a, db_conn)

#
# Task w3c
sqlw3c = """
SELECT DISTINCT year FROM movies
"""
w3c = runsql( sqlw3c, db_conn)

#
# Task w4a
sqlw4a = """
SELECT year, title, duration, worldwide_gross_income
FROM movies
WHERE title='Ghostbusters'
"""
w4a = runsql( sqlw4a, db_conn)

#
# Task w4b
sqlw4b = """
SELECT year, title, duration, worldwide_gross_income, budget
FROM movies
WHERE title LIKE '%Frozen%'
"""
w4b = runsql( sqlw4b, db_conn)

#
# Task w4c
sqlw4c = """
SELECT year, title, duration, worldwide_gross_income, budget
FROM movies
WHERE title LIKE 'Frozen%'
ORDER BY year
"""
w4c = runsql( sqlw4c, db_conn)

#
# Task w5a  This code generates an error
sqlw5a = """
SELECT year, title, production_company, actor
FROM movies
WHERE title = 'Dolittle'
"""
w5a = runsql( sqlw5a, db_conn)

#
# Task w5b
sqlw5b = """
SELECT year, title, production_company, actor
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE title = 'Dolittle'
"""
w5b = runsql( sqlw5b, db_conn)


# Task w5c
sqlw5c = """
SELECT year, title, writer, worldwide_gross_income
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE title LIKE '%Dolittle%' AND actor= 'Eddie Murphy'
"""
w5c = runsql( sqlw5c, db_conn)

#
# Task w6a
sqlw6a = """
SELECT year, title, writer, MAX(worldwide_gross_income)
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor= 'Eddie Murphy'
"""
w6a = runsql( sqlw6a, db_conn)

#
# Task w6b
sqlw6b = """
SELECT actor, SUM(worldwide_gross_income)
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor= 'Eddie Murphy'
"""
w6b = runsql( sqlw6b, db_conn)

#
# Task w7a
sqlw7a = """
SELECT DISTINCT genre
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%shrek%'
"""
w7a = runsql( sqlw7a, db_conn)

#
# Task w7b
sqlw7b = """
SELECT genre, movies.title, writer
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%shrek%'
AND writer LIKE '%Andrew Adamson%'
"""
w7b = runsql( sqlw7b, db_conn)


# Workshop END
#
###########################################################
# Collaboration Challenge
#
# S12ccq Q5
sqlcc5 = """
SELECT title, COUNT(movies.title)
FROM movies
WHERE title Like 'Frozen%'

"""
cc5 = runsql( sqlcc5, db_conn)

#
# S12ccq Q6
sqlcc6 = """
SELECT title, COUNT(production_company)
FROM movies
WHERE title LIKE 'Frozen%'
And production_company Like 'Walt Disney Animation Studios'
"""
cc6 = runsql( sqlcc6, db_conn)

#
# S12ccq Q7
sqlcc7 = """
SELECT title, COUNT(DISTINCT actor)
FROM movies
INNER JOIN actors on movies.imdb = actors.imdb
WHERE title LIKE 'Frozen%'
AND production_company LIKE 'Walt Disney Animation Studios%'
"""
cc7 = runsql( sqlcc7, db_conn)

#
# S12ccq Q8
sqlcc8 = """
SELECT COUNT(title)
FROM movies
WHERE title LIKE '%Spider%'
"""
cc8 = runsql( sqlcc8, db_conn)

#
# S12ccq Q9
sqlcc9 = """
SELECT COUNT ( DISTINCT production_company)
FROM movies
WHERE title LIKE 'Spider%'
"""
cc9 = runsql( sqlcc9, db_conn)

#
# S12ccq Q10
sqlcc10 = """
SELECT movies.title, genre
FROM movies
INNER JOIN genre
ON movies.title = genre.title
WHERE movies.title = 'Black Panther'
"""
cc10 = runsql( sqlcc10, db_conn)

#
# S12ccq Q11
sqlcc11 = """
SELECT DISTINCT genre
FROM movies
INNER JOIN genre
ON movies.title = genre.title
WHERE production_company = 'Marvel Studios'
"""
cc11 = runsql( sqlcc11, db_conn)

#
# S12ccq Q12
sqlcc12 = """
SELECT title, duration
FROM movies
INNER JOIN actors
ON movies.imdb = actors.imdb
WHERE actor LIKE '%Jamie Foxx%'
ORDER BY duration
"""
cc12 = runsql( sqlcc12, db_conn)

#
# S12ccq Q13
sqlcc13 = """
SELECT title, director, duration
FROM movies
INNER JOIN actors
ON movies.imdb = actors.imdb
WHERE actor LIKE '%Jamie Foxx%'
ORDER BY duration
"""
cc13 = runsql( sqlcc13, db_conn)


#Collaboration Challenge End
###########################################################
# Individual Challenge
#
# S12icq Q2
sqlic2 = """
SELECT year, title, director
FROM movies
INNER JOIN actors
ON movies.imdb = actors.imdb
WHERE actor LIKE '%Whoopi Goldberg%'
ORDER BY year
"""
ic2 = runsql( sqlic2, db_conn)

#
# S12icq Q3
sqlic3 = """
SELECT year, title, duration, avg_vote
FROM movies
INNER JOIN actors
ON movies.imdb = actors.imdb
WHERE actor LIKE '%Whoopi Goldberg%'
ORDER BY duration

"""
ic3 = runsql( sqlic3, db_conn)

#
# S12icq Q4
sqlic4 = """
SELECT title, duration, avg_vote, budget
FROM movies
WHERE writer LIKE '%Linda Woolverton%'
ORDER BY budget
"""
ic4 = runsql( sqlic4, db_conn)

#
# S12icq Q5
sqlic5 = """
SELECT year, title
FROM movies
WHERE title = 'Ghostbusters'
"""
ic5 = runsql( sqlic5, db_conn)

#
# S12icq Q6
sqlic6 = """
SELECT DISTINCT genre
FROM movies
INNER JOIN genre
ON movies.title = genre.title
WHERE director LIKE '%Greta Gerwig%'
"""
ic6 = runsql( sqlic6, db_conn)

#
# S12icq Q7
sqlic7 = """
SELECT COUNT(actor)
FROM movies
INNER JOIN actors
ON movies.imdb = actors.imdb
WHERE movies.title = 'Closer'
"""
ic7 = runsql( sqlic7, db_conn)


###########################################################
#
#Individual Challenge: End
db_conn.close()
EndHere(globals())
#exit();
############################################################Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$*,ROTJ%XYZIJSY}N=OP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
#Atr`$-5DXFRFSYMF%XHTYYOP4R$/6Vo30z@[QL{lSZf\iF|$J}Kb$5a6$Q9S1_U]:eKH0
