import basketball as basketball
import psycopg2

# Connect to an existing database
conn = psycopg2.connect("dbname=basketball user=Filip")

# Open a cursor to perform database operations
cur = conn.cursor()

def insertInDb(date, home_name, away_name, home_odds, away_odds):
	query = '''
	insert into odds (game_id, game_date, home_name, away_name, winning_team, home_odds, away_odds)
	values(
	(select game_id from games where game_date = %s and home_name = %s),
	%s,
	%s, 
	%s,
	(select winning_team from games where game_date = %s and home_name = %s),
	coalesce(nullif(%s,'-'),'1.0')::numeric,
	coalesce(nullif(%s,'-'),'1.0')::numeric)
	'''
	cur.execute(query, (date, home_name,date, home_name, away_name,date,home_name, home_odds, away_odds))


	
	# Make the changes to the database persistent
	conn.commit()
	
	# Close communication with the database
def closeDb():
	cur.close()
	conn.close()

