import requests
import time

#token giong nhu mot cai khoa de minh truy cap vao du lieu
token = "EAAAAUaZA8jlABAAXGIvXbAe4AZBBqTJJ6OM52HuYiLLaeFtsHHQ73EofcjNrpOHDnHJBChKyPoeUXx5iaNn04LTFb5PMkmhx2ZBSHcvOXaNJLntHGZCrYEjHldolo8h89egfqPfBTlgCjPZAoqqOvLYCueez5PWLM4OEW1CdI5Uq1pQW18Ji8"
id_face = "220927758545788"
#noi dung commet
noidung = {'message': 'Có ngay đây ạ! :D', "access_token": token}
count = 0
while (count < 4):
	a =  requests.post('https://graph.facebook.com/'+ id_face +'/comments', data = noidung)
	print(a)
	count = count + 1
	time.sleep(5)


#comment tận 100k lần trên s luôn :)