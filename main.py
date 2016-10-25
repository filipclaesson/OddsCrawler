
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
#import db_handler as db




def loadPage(url):
	page = QWebPage()
	loop = QEventLoop() # Create event loop
	page.mainFrame().loadFinished.connect(loop.quit) # Connect loadFinished to loop quit
	page.mainFrame().load(QUrl(url))
	loop.exec_() # Run event loop, it will end on loadFinished
	return page.mainFrame().toHtml()

app = QApplication(sys.argv)
url = 'http://www.oddsportal.com/basketball/sweden/ligan-2015-2016/results/'
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


save_next_games = True
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
			month = strptime(date[3:6],'%b').tm_mon 
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
				print(str(timestamp) + ", " + str(home_name) + " - " + str(away_name) + ", " + "odds: " + i[3].text_content() + "/" + i[4].text_content())
			a = a+1

		b = 1
else:
	print("odds in wrong mode: " + odds_test)

		# for j in i:
		# 	print(str(b) + ": " + str(len(j)))

			# if (len(j) == 4):
			# 	print("date: " + j[0].text_content())
			# if (len(j) == 6):
			# 	print("time: " + j[0].text_content())
			# 	print("teams: " + j[1].text_content())
			# 	#print("odds: " + j[3].text_content() + "/" + j[4].text_content())


			#print(str(b) + ": " + str(len(j)))
			#print(j.text_content())
			#b = b+1
		



app.exit()