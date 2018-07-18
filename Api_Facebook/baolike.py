import requests
import time
token = 'EAAAAUaZA8jlABAPSnN4ROHQffOvpV3ImW1se0a7sG9mk59bEjAh8wdKbnmSAFvqmPTVU7AFIxGTIGSlzJUBiLVjm29jiSRRIUGjKpKrF1wMQONZBh6SpTynX5vT9ZBFNR8xx90jKdYSxzuH2yjPZBkD39YDZAC5gB3HpYou0dTQZDZD'
id_cua_doi_tuong = '100009828489413'

a = requests.get('https://graph.facebook.com/v3.0/'+id_cua_doi_tuong+'/feed?limit=10&access_token='+token).json()
for i in a['data']:
	noidung = {'access_token': token, 'message': '<3'}
	b = requests.post('https://graph.facebook.com/v3.0/'+i['id'] +'/likes')
	print("ban da like thanh cong vao anh ID=", i['id'])
	print(b.status_code)
	time.sleep(3)#delay 3 giay