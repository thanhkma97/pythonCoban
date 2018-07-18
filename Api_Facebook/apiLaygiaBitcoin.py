
#lay gia tien dong bitcoint bip
import requests
import json


def getTienbitCoint():
	r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/CNY.jsons')
	if r.status_code == 200:
		data = r.json()
		#lay thong tin 
		print "thoi gian cap nhat: "
		print "",data['time']
		print "gia tien:"
		print data['bpi']['USD']['rate']


	else:
		print "trang khong tra loi"	


if __name__ == '__main__':
	getTienbitCoint()
