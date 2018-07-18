import requests

token = 'EAAAAUaZA8jlABAP1dzsK0xQkIes8ByfXURvAcrCwLYy8zDaN5ZC5dfTy4CZAtHZCZCAVTSYqPwGvkG85yFbMZBEP87XMPGJQIplwcXoakgdpoIe1mgWBgDCZCFU7ckyJTZAbDND4Sy4iWwOZAqcpE4m7SdAZAp2o1XBgew9bpMsBYZAEWJ1kgwiyv9a'
id_comment = "100004018229213/feed?limit=15"
url = 'https://graph.facebook.com/v3.0//'+id_comment+'&access_token='+token

a  = requests.get(url).json()


dulieu = a['data']

for i in dulieu:
	print(i['id'])
	url_request = 'https://graph.facebook.com/'+i['id']+'/reactions?type=LOVE'
	noidung = {'access_token':token}
	kq = requests.post(url_request, data=noidung)
	print(kq)