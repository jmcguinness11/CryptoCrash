import smtplib
from exchanges.bitfinex import Bitfinex
import time
import variables as var

#access initial bitcoin price
btc_price = Bitfinex().get_current_price()

#connect to gmail smtp server and login
gmail_server = smtplib.SMTP( "smtp.gmail.com", 587 )
gmail_server.starttls()
gmail_server.login(var.ACCOUNT, var.PWD)

while(1):
	#access bitcoin price
	btc_price = Bitfinex().get_current_price()

	MSG = 'The current price of Bitcoin is ${:.2f}'.format(btc_price)
	MSG = str(MSG)

	#send sms message
	gmail_server.sendmail('{}@gmail.com'.format(var.ACCOUNT), 
		'{}@vtext.com'.format(var.NUMBER), MSG)
	time.sleep(60)
