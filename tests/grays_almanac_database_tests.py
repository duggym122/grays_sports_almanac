from grays_sports_almanac import grays_almanac_database
from psycopg2 import connect
from nose import with_setup
from nose.tools import assert_equal, assert_not_equal, assert_raises, assert_true, assert_false

import sys

con = None

def setup_module(module):
    print ("\nSetup database tests by connecting to the database") # this is to get a newline after the dots
    module.con = connect(user='postgres', port = '5432', database = "grays_almanac")
 
def teardown_module(module):
    print ("Tear down database tests by disconnecting from the database")
    module.con.close()

class basic_database_tests:
    cur = None
    @classmethod
    def setup_class(cls):
        print ("Start basic database tests")
        cls.cur = con.cursor()
    
    def test_team_table_existence(self):
        raised = False
        
        try:
            self.cur.execute("SELECT * FROM team;")
        except:
            raised = True
        
        assert_false(raised)
    
    def test_game_table_existence(self):
        raised = False
        
        try:
            self.cur.execute("SELECT * FROM game;")
        except:
            raised = True
        
        assert_false(raised)
    
    def test_weather_table_existence(self):
        raised = False
        
        try:
            self.cur.execute("SELECT * FROM weather;")
        except:
            raised = True
        
        assert_false(raised)
        
 
    @classmethod
    def teardown_class(cls):
        print ("End basic database tests")
        cls.cur.close()

#This test must be re-adapted to cover Teams, Games, and Weather Reports
'''
class championship_table_tests:
    cur = None
    @classmethod
    def setup_class(cls):
        print ("Start championship table tests")
        cls.cur = con.cursor()
    
    def test_league_abbrev_column_existence(self):
        assert_true(self.cur.execute(
            "select exists (select 1 from sport_schema.columns where "
            "table_name ='championship' and column_name='league_abbrev');"))
            
    def test_season_column_existence(self):
        assert_true(self.cur.execute(
            "select exists (select 1 from sport_schema.columns where "
            "table_name ='championship' and column_name='season');"))
            
    def test_sport_column_existence(self):
        assert_true(self.cur.execute(
            "select exists (select 1 from sport_schema.columns where "
            "table_name ='championship' and column_name='sport');"))
    
    def test_bracket_column_existence(self):
        assert_true(self.cur.execute(
            "select exists (select 1 from sport_schema.columns where "
            "table_name ='championship' and column_name='bracket');"))
    
    def test_champion_column_existence(self):
        assert_true(self.cur.execute(
            "select exists (select 1 from sport_schema.columns where "
            "table_name ='championship' and column_name='champion');"))
 
    @classmethod
    def teardown_class(cls):
        print ("End championship table tests")
        cls.cur.close()
'''