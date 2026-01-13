# Connect with sqlite database
# Import necessary libraries
import pandas as pd
import sqlite3

# Datebase file
database = 'database.sqlite'

# Connect to the database
conn = sqlite3.connect(database)
print("Opened database successfullt")

# --------------------------------------------------
# Display all the tables of the database
df = pd.read_sql("""
                 SELECT *
                 FROM sqlite_master
                 WHERE type = 'table'
""", conn)

# --------------------------------------------------
# Display the first five rows of the Player_match table
player_match = pd.read_sql("""
                            SELECT *
                           FROM Player_Match
""", conn)

print(player_match.head())

# -----------------------------------------------------
# Check the presence of NULL values in the Player_match table
null_player_match = pd.read_sql("""
                            SELECT *
                           FROM Player_Match
                           WHERE Team_Id IS NULL
""", conn)

print(null_player_match)

# ---------------------------------------------------------
# Display the first five rows of the Match table
toss_dec = pd.read_sql("""
                        SELECT *
                        FROM Match
""", conn)

print(toss_dec.head())

# -------------------------------------------------------------
# Check the presence of NULL values in the Match table
null_match = pd.read_sql("""
                         SELECT *
                         FROM Match
                         WHERE Match_Winner IS NULL
""", conn)

print(null_match)

team_sum = pd.read_sql("""
                         SELECT Team_1, Team_2, Team_1 + Team_2 AS Sum_of_Team_1_and_2
                         FROM Match
                         WHERE Match_Winner IS NULL
""", conn)

print(team_sum)

team_largest = pd.read_sql("""
                         SELECT Team_1, Team_2, MAX(Team_1, Team_2) AS Largest_of_Team_1_and_2
                         FROM Match
                         WHERE Match_Winner IS NULL
""", conn)

print(team_largest)