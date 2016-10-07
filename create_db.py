# Create a database here. 
# Reference this article: http://stackoverflow.com/questions/19426448/creating-a-postgresql-db-using-psycopg2
# Reference this tutorial: https://wiki.postgresql.org/wiki/Psycopg2_Tutorial
# Consider refactoring later to do this: http://stackoverflow.com/questions/35153483/create-db-and-tables-from-setup-py
from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = None
newdb = "grays_almanac"
cur = None

# Create the database grays_almanac
try:
    # Attempt to connect to the database
    con = connect(user='postgres', port = '5432', database = newdb)
except:
    # If the database cannot be connected to, make it
    print "I didn't find the database " + newdb + " so I'm going to create it."
    con = connect(user='postgres', port = '5432')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute('CREATE DATABASE ' + newdb)

con = connect(user='postgres', port = '5432', database = newdb)
cur = con.cursor()

new_schema = "sport_schema"
try:
    cur.execute("CREATE SCHEMA IF NOT EXISTS " + new_schema + " AUTHORIZATION postgres;")
except:
    print "I encountered an exception trying to create the schema " + new_schema + ": ", sys.exc_info()[0]


new_table = "game"
try:
    cur.execute("CREATE TABLE IF NOT EXISTS sport_schema."+ new_table +" ("
            "league_abbrev          VARCHAR (5)         NOT NULL,"
            "season                 CHAR (8)            NOT NULL,"
            "sport                  VARCHAR (35)        NOT NULL,"
            "game_indoors           BOOLEAN             NOT NULL,"
            "home_score             INT,"
            "away_score             INT,"
            "home_penalties         INT,"
            "away_penalties         INT,"
            "start_time             TIME,"
            "game_length_minutes    INT,"
            "date                   DATE                NOT NULL,"
            "home_team              VARCHAR (100)        NOT NULL,"
            "away_team              VARCHAR (100)        NOT NULL,"
            "weather_report_id      UUID,"
            "regular_season_game    BOOLEAN             NOT NULL,"
            "post_season_game       BOOLEAN             NOT NULL,"
            "championship_game      BOOLEAN             NOT NULL"
            ");")
except:
    print "I encountered an exception trying to create the table " + new_table + ": ", sys.exc_info()[0]

new_table = "team"
try:
    cur.execute("CREATE TABLE IF NOT EXISTS sport_schema."+ new_table +" ("
            "league_abbrev                      VARCHAR (5)         NOT NULL,"
            "season                             CHAR (8)            NOT NULL,"
            "sport                              VARCHAR (35)        NOT NULL,"
            "team_name                          VARCHAR (100)       NOT NULL,"
            "season_wins                        INT,"
            "season_losses                      INT,"
            "season_ties                        INT,"
            "overtime_wins                      INT,"
            "overtime_losses                    INT,"
            "avg_game_penalties                 INT,"
            "avg_game_penalty_points_scored     INT,"
            "avg_game_penalty_points_allowed    INT,"
            "avg_game_points_scored             INT,"
            "avg_game_points_allowed            INT,"
            "days_since_last_game               INT,"
            "consecutive_home_games             INT                 NOT NULL,"
            "win_streak                         INT                 NOT NULL,"
            "home_venue_indoors                 BOOLEAN             NOT NULL,"
            "starters_out                       INT"
            ");")
except:
    print "I encountered an exception trying to create the table " + new_table + ": ", sys.exc_info()[0]

cur.close()
con.close()