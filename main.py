
import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import * 
from lxml import html 
#import gameScraper as gs
import time 
import datetime
from time import strptime
import basketball as basketball
import db_handler as db

def getMonthNbr(month_name):
	months = [["Jan","1"],
	["Feb","2"],["Mar","3"],["Apr","4"],["May","5"],["Jun","6"],["Jul","7"],["Aug","8"],["Sep","19"],["Oct","10"],["Nov","11"],["Dec","12"]]
	for i in months:
		if (i[0] == month_name):
			return int(i[1])




def loadPage(url):
	page = QWebPage()
	loop = QEventLoop() # Create event loop
	page.mainFrame().loadFinished.connect(loop.quit) # Connect loadFinished to loop quit
	page.mainFrame().load(QUrl(url))
	loop.exec_() # Run event loop, it will end on loadFinished
	return page.mainFrame().toHtml()

app = QApplication(sys.argv)
urls = [
#'http://www.oddsportal.com/basketball/sweden/ligan-2015-2016/results/',
#'http://www.oddsportal.com/basketball/sweden/ligan-2015-2016/results/#/page/2/',
#'http://www.oddsportal.com/basketball/sweden/ligan-2015-2016/results/#/page/3/',
#'http://www.oddsportal.com/basketball/sweden/ligan-2015-2016/results/#/page/4/'
]
for url in urls:

	result = loadPage(url)
	#print(result)
	page = html.fromstring(result)
	odds = page.get_element_by_id('tournamentTable')
	#odds.find_class('mbt-table')
	print(len(odds[0][1]))
	table = odds[0][1]
	a = 0
	b = 1
	timestamp = ""

	# check if odds are in correct mode
	for i in range(0,len(table)):
		if (len(table[i]) == 6):
			odds_test = float(table[i][3].text_content())
			break


	save_next_games = False
	if (odds_test < 30.0):
		for i in table:
			if (len(i) == 4):
				#print(i[0].text_content())
				#print("date: " + i[0].text_content())
				date = i[0].text_content().strip()
				yay = date
				#print(yay.find("Play"))
				if (yay.find("Play")>-1):
					#print("hej")
					save_next_games = False
				else:
					save_next_games = True
				#print(date)
				day = int(date[0:2])
				month = getMonthNbr(date[3:6]) 
				year =  int(date[7:11])
				timestamp = datetime.datetime(year=year, month=month, day=day)

			if (len(i) == 6):
				#check if regular season game
				clock = i[0].text_content()
				hour = int(clock[0:2])
				minute = int(clock[3:5])
				timestamp = timestamp.replace(hour=hour+2, minute=minute)
				teams = i[1].text_content()
				end = int(teams.index('-'))
				home_name = teams[0:end]
				home_name = home_name.rstrip()
				home_name = basketball.getGameName(home_name)
				away_name = teams[end+2:]
				away_name = basketball.getGameName(away_name)
				home_odds = i[3].text_content()
				away_odds = i[4].text_content()
				
				if(save_next_games):
					print("--------------------")
					print(timestamp)
					print(home_name)
					print(away_name)
					print(home_odds)
					print(away_odds)
					db.insertInDb(timestamp, home_name, away_name, home_odds, away_odds)
					print(str(timestamp) + ", " + str(home_name) + " - " + str(away_name) + ", " + "odds: " + i[3].text_content() + "/" + i[4].text_content())
	else:
		print("odds in wrong mode: " + str(odds_test))


db.closeDb()
app.exit()






