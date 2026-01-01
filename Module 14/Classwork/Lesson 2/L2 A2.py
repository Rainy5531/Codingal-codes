# Import necessary library
import sqlite3
import pandas as pd

# Name of SQLite database file
database = 'database.sqlite'

# Connect to the database
conn = sqlite3.connect(database)
print("Opened database successfully")

# Get list of all tables
tables = pd.read_sql(""" SELECT name 
                         FROM sqlite_master 
                         WHERE type='table'; """, conn)
print("All Tables in the Database:")
print(tables)

# Load the 'Team' table
teams = pd.read_sql(""" SELECT * FROM Team; """, conn)

print("\nTeam Table (first 5 rows):")
print(teams.head()) # head() to display first rows (default is 5)   tail() for last rows (default is 5)

# Load the 'Match table
matches = pd.read_sql(""" SELECT * FROM Match; """, conn)

print("\nMatch Table (first 5 rows):")
print(matches.head())

# Check details of all matches won by Mumbai Indians
#   (Assuming Mumbai Indians has Team_ID = 7)
MI_wins = pd.read_sql(""" SELECT *
                      FROM Match
                      WHERE Match_Winner == 7; """, conn)

print("\n--- All MI Wins ---")
print(MI_wins)

# Matches won by MI in last two seasons
#   (Assuming seasons 8 and 9)
MI_S8_S9 = pd.read_sql(""" SELECT *
                        FROM Match
                        WHERE Match_Winner == 7 AND Season_Id IN (8, 9); """, conn)

print("\n--- MI Wins in Seasons 8 and 9 ---")
print(MI_S8_S9)

# Find new teams (team names starting with 'De')
new_teams = pd.read_sql(""" SELECT *
                            FROM Team
                            WHERE Team_Name LIKE 'De%'; """, conn)

print("\n--- New Teams (Name starts with 'De') ---")
print(new_teams)

# Minimum and Maximum winning margins
win_max_margin = pd.read_sql(""" SELECT MIN(Win_Margin) AS Min_Margin,
                             MAX(Win_Margin) AS Max_Margin
                             FROM Match; """, conn)

print("\n--- Minimum & Maximum Winning Margins ---")
print(win_max_margin)